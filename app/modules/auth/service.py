from app.modules.auth.schemas import AuthRequest, RefreshTokenRequest
from .security import verify_password, _generate_token, verify_token
from ..users.interfaces import BaseUserRepository
from .interface import BaseAuthRepository
from .model import AuthModel
from datetime import datetime, timedelta
import os

SEVEN_DAYS_IN_MINUTES = 10080

class AuthService():
    def __init__(self, user_repo: BaseUserRepository, auth_repo: BaseAuthRepository):
        self._auth_key = os.getenv("AUTHENTICATION_KEY")
        self.user_repo = user_repo
        self.auth_repo = auth_repo
        
    def authorize_user(self, auth_request: AuthRequest):
        user_model = self.user_repo.get_by_email(auth_request.email)
        is_user = verify_password(user_model.senha, auth_request.senha)
        
        if not is_user:
            return None
        
        user_data = auth_request.model_dump()

        refresh_token = self.auth_repo.select_by_date(datetime.now(), user_model.id)
        if not refresh_token:
            refresh_token = self.generate_token(user_data, is_refresh=True)
            auth_user = AuthModel(id_user=user_model.id, token=refresh_token)
            created = self.auth_repo.create(auth_user)

            if not created:
                raise Exception

        token = self.generate_token(user_data, is_refresh=False)

        tokens = {
            "token" : token,
            "refresh_token" : refresh_token,
            "type" : "Bearer"
        }
        return tokens
    
    def refresh_token(self, refresh_token_request: RefreshTokenRequest, user_data: AuthRequest):
        token = self.verify_user(refresh_token_request.access_token)
        if token is None:
            return None
        
        if token.get("is_valid"):
            return token
        
        refresh_token = self.verify_user(refresh_token_request.refresh_token)
        if refresh_token is None or not refresh_token.get('is_valid'):
            return None

        return self.generate_token(user_data)


    def generate_token(self, user_data, is_access: bool = True):
        if not is_access:
            return _generate_token(user_data, self._auth_key, SEVEN_DAYS_IN_MINUTES)
        return _generate_token(user_data, self._auth_key)

    def verify_user(self, token: str):
        payload = verify_token(token, self._auth_key)
        if payload is None:
            return None

        exp_date = payload.get("exp_date")
        if datetime.now() >= exp_date:
            payload['is_valid'] = False
            return payload
    
        return payload