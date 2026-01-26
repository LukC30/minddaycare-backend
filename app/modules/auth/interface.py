from abc import ABC, abstractmethod
from app.core.database.db import Database


class BaseAuthRepository(ABC):
    def __init__(self, db: Database):
        self.db = db

    @abstractmethod
    def create(self, token):
        pass

