from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import environ
from fastapi import HTTPException, Security

load_dotenv()

security = HTTPBearer()

TOKEN_SECRET = environ.get("TOKEN_SECRET") 

def createToken() -> str:
    current_timestamp = datetime.now()
    
    return jwt.encode(
        {
            "exp": (current_timestamp + timedelta(hours=5)).timestamp(),
            "nbf": current_timestamp,
            "iat": current_timestamp,
        },
        key=TOKEN_SECRET,
    )
    
def validateToken(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials

    try:
        jwt.decode(
            token,
            key=TOKEN_SECRET,
            algorithms=["HS256"],
            options={
                "verify_exp": "verify_signature"
            }
        )
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )
    return token