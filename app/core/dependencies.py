from app.core.database.db import Database
from app.modules.users.repository import UserRepository
from app.modules.users.service import UserService

db_instance = Database()

def get_user_repository() -> UserRepository:
    db = db_instance
    return UserRepository(db)

def get_user_service() -> UserService:
    user_repo = get_user_repository()
    return UserService(user_repo)