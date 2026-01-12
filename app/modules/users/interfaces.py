from app.core.database.db import Database
from app.modules.users.schema import UserRequestDTO
from abc import ABC, abstractmethod

class BaseUserRepository(ABC):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db

    @abstractmethod
    def create(self, user_request: UserRequestDTO):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_email(self):
        pass

    @abstractmethod
    def update(self, user_request: UserRequestDTO):
        pass




