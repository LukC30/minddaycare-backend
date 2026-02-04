from ..users.interfaces import BaseUserRepository
from ..users.mapper import UserMapper

from .interface import BaseConfessionRepository
from .mapper import ConfessionMapper
from .schemas import ConfessionResponseDTO, ConfessionRequestDTO

from .models import ConfessionModel

class ConfessionService():
    def __init__(self, user_repo: BaseUserRepository, confession_repo: BaseConfessionRepository):
        self.user_repo = user_repo
        self.confession_repo = confession_repo

    def create(self, confession_request: ConfessionRequestDTO):
        user_data = self.user_repo.get_by_email(confession_request.email)
        if user_data is None:
            return None
        
        confession_model = ConfessionMapper.to_confession_model(user_data.id, confession_request)

        confession = self.confession_repo.create(confession_model)
        if confession is None:
            return None
        
        return confession
    
    def select_by_month(self, date):
        pass
        



        