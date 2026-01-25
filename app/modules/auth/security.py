from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt


ENCRIPT_ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated="auto")

def password_encript(password: str):
    return pwd_context.hash(password)

def verify_password(hash: str, password: str):
    return pwd_context.verify(hash=hash, secret=password)

def verify_token(token: str, auth_key: str):
    payload = jwt.decode(token, auth_key, ENCRIPT_ALGORITHM)
    if not payload:
        return None
    
    exp_date = payload.get("exp")
    if datetime.now() >= exp_date:
        return None
    
    return payload

def _generate_token(user_data: dict, auth_key: str):
    payload = {
        "sub": f"{user_data.get("email")}",
        "exp": datetime.now() + timedelta(hours=1),
        "iat": datetime.now()
    }
    token = jwt.encode(payload, auth_key, ENCRIPT_ALGORITHM)
    return token
