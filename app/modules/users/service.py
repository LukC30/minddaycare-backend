from app.core.database.db import Database
from .interfaces import BaseUserRepository
from .schema import UserRequestDTO
from .mapper import UserMapper
from ..auth.security import password_encript
import logging

logger = logging.getLogger(__name__)

class UserService():
    def __init__(self, user_repo: BaseUserRepository):
        self.user_repo = user_repo
    
    def create_user(self, user: UserRequestDTO):
        user.senha = password_encript(user.senha)
        result = self.user_repo.create(user)
        return result
    
    def get_all_users(self):
        users_model = self.user_repo.get_all()
        users_list = UserMapper.to_user_response_schema_list(users_model)

        if not users_list:
            logger.error("Hot get users")
            
        return users_list
    
    def get_user(self, id):
        user_dict = {}
    
        user_model = self.user_repo.get_by_id(id)
        if not user_model:
            return None
        
        user_dict = UserMapper.to_user_response_schema(user_model)
        return user_dict
    
    def get_user_by_email(self, email):
        user_dict = {}
        user_model = self.user_repo.get_by_email(email)
        
        if not user_model:
            return None
        
        user_dict = UserMapper.to_user_response_schema(user_model)
        return user_dict
    
    def update_user(self, user_updated: UserRequestDTO):
        user_model = UserMapper.to_model(user_updated)
        user_updated = self.user_repo.update(user_model)
        return True
    
    def delete(self, user_deleted: UserRequestDTO):
        user_model = UserMapper.to_model(user_deleted)
        self.user_repo.delete(user_model)
        return True
        
        