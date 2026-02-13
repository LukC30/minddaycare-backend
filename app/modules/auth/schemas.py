from pydantic import BaseModel
from datetime import datetime

class AuthRequest(BaseModel):
    email: str
    senha: str

class RefreshTokenRequest(BaseModel):
    access_token: str
    refresh_token: str

class AccessTokenDTO(BaseModel):
    id: str
    sub: str
    exp: datetime
    iat: datetime
    is_valid: bool
