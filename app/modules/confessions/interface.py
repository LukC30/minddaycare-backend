from abc import ABC, abstractmethod
from app.core.database.db import Database
from .schemas import ConfessionRequestDTO

class BaseConfessionRepository(ABC):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db

    def create(self, confession_request: ConfessionRequestDTO):
        pass