from app.core.database.db import Database
from .repository import UserRepository
from .schema import UserRequestDTO
import logging 

logger = logging.getLogger(__name__)

class UserService():
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    def create_user(self, user: UserRequestDTO):
        try:
            self.user_repo.create_user(user)
        except Exception as e:
            logger.error("Error: %s", str(e))
        return
        
