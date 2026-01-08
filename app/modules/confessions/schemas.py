from pydantic import BaseModel
from typing import Literal, Optional
import datetime

class DesabafoRequestDTO(BaseModel):
    id_user: int
    humor: Literal['calmaria',"tristeza","felicidade","alegria","ansiedade","irritação","desânimo","mudança de humor"," autocritica","apatia","confusão"]
    descricao: str
    date: datetime.date

class DesabafoResponseDTO(BaseModel):
    humor: Literal['calmaria',"tristeza","felicidade","alegria","ansiedade","irritação","desânimo","mudança de humor"," autocritica","apatia","confusão"]
    descricao: str
    date: datetime.date