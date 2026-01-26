from .security import verify_password, _generate_token, verify_token
from ..users.schema import UserRequestDTO
from ..users.interfaces import BaseUserRepository
from .interface import BaseAuthRepository
import os

class AuthService():
    def __init__(self, user_repo: BaseUserRepository, auth_repo: BaseAuthRepository):
        self._auth_key = os.getenv("AUTHENTICATION_KEY")
        self.user_repo = user_repo
        self.auth_repo = auth_repo
        
    def authorize_user(self, user_request: UserRequestDTO):
        user_model = self.user_repo.get_by_email(user_request.email)
        is_user = verify_password(user_model.senha, user_request.senha)
        
        if not is_user:
            return None
        
        user_data = user_request.model_dump()
        token = _generate_token(user_data, self._auth_key, 1)
        refresh_token = _generate_token(user_data, self._auth_key, 10080)

        tokens = {
            "token" : token,
            "refresh_token" : refresh_token,
            "type" : "Bearer"
        }
        return tokens
    
    def verify_user(token: str):
        payload = verify_token(token)

        

        if payload is None:
            return None
        
        return payload
    

    

    
