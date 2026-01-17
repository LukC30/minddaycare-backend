from pydantic import BaseModel
from typing import Literal, Optional
import datetime

class ConfessionRequestDTO(BaseModel):
    email: str
    humor: Literal['calmaria',"tristeza","felicidade","alegria","ansiedade","irritação","desânimo","mudança de humor"," autocritica","apatia","confusão"]
    descricao: str
    date: datetime.date

class ConfessionResponseDTO(BaseModel):
    humor: Literal['calmaria',"tristeza","felicidade","alegria","ansiedade","irritação","desânimo","mudança de humor"," autocritica","apatia","confusão"]
    descricao: str
    date: datetime.date