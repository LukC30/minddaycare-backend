from abc import ABC, abstractmethod

from .model import AuthModel
from app.core.database.db import Database


class BaseAuthRepository(ABC):
    def __init__(self, db: Database):
        self.db = db

    @abstractmethod
    def create(self, auth_model: AuthModel):
        pass

    
    def select_by_date(self, date, id_user):
        pass