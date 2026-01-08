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