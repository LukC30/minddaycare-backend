from pydantic import BaseModel,  Field
from typing import Literal, Optional
import datetime

class UserModel(BaseModel):
    id: Optional[int] = Field(0)
    nome: str
    email: str
    senha: str
    telefone: str
    created_at: Optional[str] = Field("")

    def to_insert(self):
        insert_data = (self.nome, self.email, self.senha, self.telefone)
        return insert_data