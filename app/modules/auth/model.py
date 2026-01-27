from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class AuthModel(BaseModel):
    id_user: int
    token: str
    created_at: datetime = Field(datetime.now())
    expires_at: datetime = Field(datetime.now() + timedelta(days=7))