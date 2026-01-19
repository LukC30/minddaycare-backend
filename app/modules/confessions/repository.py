from .interface import BaseConfessionRepository
from .schemas import ConfessionRequestDTO

class ConfessionRepository(BaseConfessionRepository):
    def __init__(self, db):
        super().__init__(db)

    def create(self, confession_create: ConfessionRequestDTO):
        pass
