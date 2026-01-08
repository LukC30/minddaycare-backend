from app.core.database.db import Database
from .interfaces import BaseUserRepository
from .schema import UserRequestDTO
from .mapper import UserMapper
import logging 

logger = logging.getLogger(__name__)

class UserService():
    def __init__(self, user_repo: BaseUserRepository):
        self.user_repo = user_repo
    
    def create_user(self, user: UserRequestDTO):
        user_model = UserMapper.to_user_model(user)
        try:
            self.user_repo.create(user_model)
        except Exception as e:
            logger.error("Error: %s", str(e))
            raise
        return
    
    def get_all_users(self):
        users_dict = []
        try:
            users_model = self.user_repo.get_all()
            users_dict = UserMapper.to_user_response_schema_list(users_model)
        
        except Exception as e:
            logger.error("Error: %s", str(e))
            raise 
        return users_dict



            
        
