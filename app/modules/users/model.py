from pydantic import BaseModel,  Field
from typing import Optional
import datetime

class UserModel(BaseModel):
    id: Optional[int] = Field(0)
    nome: str = Field("")
    email: str = Field("")
    senha: str = Field("")
    telefone: str = Field("")
    created_at: datetime.datetime
    is_active: int = Field(1)

