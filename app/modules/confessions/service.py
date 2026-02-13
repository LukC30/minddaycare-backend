from ..users.interfaces import BaseUserRepository
from ..users.mapper import UserMapper

from .interface import BaseConfessionRepository
from .mapper import ConfessionMapper
from .schemas import ConfessionResponseDTO, ConfessionRequestDTO
from .models import ConfessionModel
from ..auth.schemas import AccessTokenDTO
from datetime import date

class ConfessionService():
    def __init__(self, user_repo: BaseUserRepository, confession_repo: BaseConfessionRepository):
        self.user_repo = user_repo
        self.confession_repo = confession_repo

    def create(self, confession_request: ConfessionRequestDTO, access_token: AccessTokenDTO):
        id_user = access_token.id
        user_data = self.user_repo.get_by_id(id_user)
        if user_data is None:
            return None
        
        confession_today = self.confession_repo.select_by_date(id_user, date=date.today())
        if confession_today:
            return {"Message" : "Do you forget that make your confession today? Pathetic."}
        
        confession_model = ConfessionMapper.to_confession_model(id_user, confession_request)
        confession = self.confession_repo.create(confession_model)
        if confession is None:
            return None
        
        user_response = UserMapper.to_user_response_schema(user_data)
        confession_response = ConfessionMapper.to_response(confession_model, user_response)

        return confession_response
    
    def select_last_month(self, id_user):
        user_data = self.user_repo.get_by_id(id_user)
        if not user_data:
            return None
        
        user_response = UserMapper.to_user_response_schema(user_data)
        confessions = self.confession_repo.select_last_thirty_days(id_user)

        confessions_list = ConfessionMapper.to_confession_model_list(confessions)
        confessions_response = [ConfessionMapper.to_response(confession, user_response) for confession in confessions_list]
        return confessions_response       