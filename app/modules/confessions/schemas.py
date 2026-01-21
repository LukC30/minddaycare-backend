from pydantic import BaseModel
from typing import Literal
from ..users.schema import UserResponseDTO
import datetime

class ConfessionRequestDTO(BaseModel):
    id_user: int
    humor: Literal['calmaria',"tristeza","felicidade","alegria","ansiedade","irritação","desânimo","mudança de humor"," autocritica","apatia","confusão"]
    descricao: str
    date: datetime.date

class ConfessionResponseDTO(BaseModel):
    user: UserResponseDTO
    humor: Literal['calmaria',"tristeza","felicidade","alegria","ansiedade","irritação","desânimo","mudança de humor"," autocritica","apatia","confusão"]
    descricao: str
    date: datetime.date