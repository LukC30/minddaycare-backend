from pydantic import BaseModel
from datetime import datetime

class AuthModel(BaseModel):
    id_user: int
    token: str
    expires_at: datetime
    created_at: datetime