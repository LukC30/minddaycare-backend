from app.core.database.db import Database
from app.modules.users.repository import UserRepository
from app.modules.users.service import UserService

class DependencyContainer():
    def __init__(self):
        self.db = Database()
        self.user_repository = UserRepository(self.db)
        self.user_service = UserService(self.user_repository)

#wrapper com tudo bonitinho
def get_container() -> DependencyContainer:
    return DependencyContainer()

def get_db() -> Database:
    return Database()

def get_user_repository() -> UserRepository:
    db = get_db()
    return UserRepository(db)

def get_user_service() -> UserService:
    user_repo = get_user_repository()
    return UserService(user_repo)