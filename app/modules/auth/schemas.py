from pydantic import BaseModel

class AuthRequest(BaseModel):
    email: str
    senha: str

class RefreshTokenRequest(BaseModel):
    access_token: str
    refresh_token: str