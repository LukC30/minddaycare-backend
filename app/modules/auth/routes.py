from app.modules.auth.schemas import AuthRequest, RefreshTokenRequest
from app.modules.auth.service import AuthService

from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from app.core.dependencies import get_auth_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

auth_router = APIRouter(
    prefix='/v1/auth',
    tags=['auth']
)

# Isso aqui vai virar o middleware de autenticação

def get_current_user(token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends(get_auth_service)):
    user_data = auth_service.verify_user(token)    
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return


@auth_router.post('/login')
def login(user_data: AuthRequest, auth_service: AuthService = Depends(get_auth_service)):
    tokens = auth_service.authorize_user(user_data)
    if not tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return tokens

@auth_router.post('/refresh')
def refresh_token(token_request: RefreshTokenRequest, user_data: AuthRequest, auth_service: AuthService = Depends(get_auth_service)):
    token = auth_service.refresh_token(token_request, user_data)
    return token