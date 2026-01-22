from app.modules.auth.service import AuthService
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from app.core.dependencies import get_auth_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

router = APIRouter(
    prefix='/v1/auth',
    tags=['auth', 'login', '']
)

def get_current_user(token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends(get_auth_service)):
    user_data = auth_service.verify_user(token)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_data

