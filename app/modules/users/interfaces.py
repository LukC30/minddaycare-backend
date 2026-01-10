from app.core.database.db import Database
from app.modules.users.schema import UserRequestDTO
from abc import ABC, abstractmethod

class BaseUserRepository(ABC):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db

    @abstractmethod
    async def create(self, user_request: UserRequestDTO):
        pass
    
    @abstractmethod
    async def delete(self, id):
        pass

    @abstractmethod
    async def get_by_id(self, id):
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def update(self, user_request: UserRequestDTO):
        pass




