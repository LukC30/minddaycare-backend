from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ConfessionModel(BaseModel):
    id: Optional[int]
    id_user: int
    humor: str
    descricao: str
    created_at: Optional[datetime]