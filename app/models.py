from pydantic import BaseModel, Field
from typing import Literal, Optional
import datetime

class UserModel(BaseModel):
    id: Optional[int] = Field(0)
    name: str
    email: str
    senha: str
    telefone: str
    created_at: Optional[str] = Field("")

    def to_insert(self):
        insert_data = self.model_dump().values()
        return insert_data

class ConfessionModel(BaseModel):
    id: int
    id_user: int
    humor: str
    descricao: str
    created_at: str

    def to_insert(self):
        insert_data = self.model_dump().values()
        return insert_data