from app.core.database.db import Database
from app.modules.auth.repository import AuthRepository
from app.modules.auth.service import AuthService
from app.modules.users.repository import UserRepository
from app.modules.users.service import UserService

db_instance = Database()

def get_user_repository() -> UserRepository:
    db = db_instance
    return UserRepository(db)

def get_auth_repository() -> AuthRepository:
    db = db_instance
    return AuthRepository(db)

def get_user_service() -> UserService:
    user_repo = get_user_repository()
    return UserService(user_repo)

def get_auth_service() -> AuthService:
    user_repo = get_user_repository()
    auth_repo = get_auth_repository()
    return AuthService(user_repo, auth_repo)