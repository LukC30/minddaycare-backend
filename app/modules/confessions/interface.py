from abc import ABC, abstractmethod
from app.core.database.db import Database
from .models import ConfessionModel

class BaseConfessionRepository(ABC):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db

    @abstractmethod
    def create(self, confession_request: ConfessionModel):
        pass

    @abstractmethod
    def select_by_date(self, id_user, date):
        pass

    @abstractmethod
    def select_last_thirty_days(self, id_user):
        pass