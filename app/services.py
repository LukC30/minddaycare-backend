from app.database.db import Database
from app.repository import UserRepository
from app.schemas import UserDTO
import logging 

logger = logging.getLogger(__name__)

class UserService():
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    async def create_user(self, user: UserDTO):
        try:
            await self.user_repo.create_user(user)
        except Exception as e:
            logger.error("Error: %s", str(e))
        return
        
