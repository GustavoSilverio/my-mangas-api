from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import environ
from fastapi import HTTPException, Security

load_dotenv()

security = HTTPBearer()

TOKEN_SECRET = environ.get("TOKEN_SECRET")
ACCESS_KEY = environ.get("ACCESS_KEY")
TOKEN_EXPIRATION_HOURS = int(environ.get("TOKEN_EXPIRATION_HOURS"))

def createToken() -> str:
    current_timestamp = datetime.now()
    
    return jwt.encode(
        {
            "exp": (current_timestamp + timedelta(hours=TOKEN_EXPIRATION_HOURS)).timestamp(),
            "nbf": current_timestamp,
            "iat": current_timestamp,
            "key": ACCESS_KEY,
        },
        key=TOKEN_SECRET,
    )
    
def validateToken(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials

    try:
        jwt.decode(
            token,
            key=TOKEN_SECRET,
            algorithms=["HS256"]
        )
    except Exception:
        raise HTTPException(
            status_code=401,
            detail={
                "message": "Token expired",
                "type": "token.expired"
            },
            headers={
                "token-expired": "true"
            }
        )
    return token