from app.modules.auth.schemas import AuthRequest
from .security import verify_password, _generate_token, verify_token
from ..users.schema import UserRequestDTO
from ..users.interfaces import BaseUserRepository
from .interface import BaseAuthRepository
from .model import AuthModel
from datetime import datetime
import os

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
            refresh_token = _generate_token(user_data, self._auth_key, days=7)
            auth_user = AuthModel(id_user=user_model.id, token=refresh_token)
            created = self.auth_repo.create(auth_user)

            if not created:
                raise Exception

        token = _generate_token(user_data, self._auth_key, 1)

        tokens = {
            "token" : token,
            "refresh_token" : refresh_token,
            "type" : "Bearer"
        }
        return tokens
        
    def verify_user(token: str):
        payload = verify_token(token)
        if payload:
            return payload
        
        