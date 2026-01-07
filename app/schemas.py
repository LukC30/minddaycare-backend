from pydantic import BaseModel
from typing import Literal, Optional

class UserDTO(BaseModel):
    nome: str
    email: str
    senha: Optional[str]
    telefone: Optional[str]

class DesabafoDTO(BaseModel):
    id_user: int
    humor: Literal['calmaria',"tristeza","felicidade","alegria","ansiedade","irritação","desânimo","mudança de humor"," autocritica","apatia","confusão"]
    descricao: str