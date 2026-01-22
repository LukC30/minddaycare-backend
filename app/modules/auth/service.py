from .security import verify_password, password_encript, _generate_jwt
from ..users.schema import UserRequestDTO
from ..users.repository import UserRepository
import os

class AuthService():
    def __init__(self, user_repo: UserRepository):
        self.auth_key = os.getenv("AUTHENTICATION_KEY")
        self.user_repo = user_repo
        
    def authorize_user(self, user_request: UserRequestDTO):
        user_model = self.user_repo.get_by_email(user_request.email)
        is_user = verify_password(user_model.senha, user_request.senha)
        
        if not is_user:
            return None
        
        user_data = user_request.model_dump()
        token = _generate_jwt(user_data, self.auth_key)
        return token
    
    
    
