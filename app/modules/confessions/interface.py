from abc import ABC, abstractmethod
from app.core.database.db import Database
from .models import ConfessionModel

class BaseConfessionRepository(ABC):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db

    def create(self, confession_request: ConfessionModel):
        pass