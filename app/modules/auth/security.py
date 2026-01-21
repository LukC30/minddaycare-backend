from passlib.context import CryptContext
from datetime import datetime, timedelta 
import jwt

SECRET_KEY = "nao tenho chave ainda kkkkkkkkkkkkkkkkkkkkkkkkkkkk" 
ENCRIPT_ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(schemes=['bycrypt'])

def password_encript(password: str):
    return pwd_context.hash(password)

def verify_password(hash: str, password: str):
    return pwd_context.verify(hash=hash, secret=password)

