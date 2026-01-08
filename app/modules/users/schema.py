from pydantic import BaseModel
from typing import Literal, Optional

class UserRequestDTO(BaseModel):
    nome: str
    email: str
    senha: Optional[str]
    telefone: Optional[str]

class UserResponseDTO(BaseModel):
    nome: str
    email: str