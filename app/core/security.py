from datetime import datetime, timedelta
from jose.exceptions import JOSEError
from jose import jwt

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer

from app.schemas.token import TokenRespose
from app.core.settings import TOKEN_EXPIRE, ALGORITHM, SECRET
 
security = HTTPBearer()


def verify_token(credentials: HTTPBasicCredentials = Depends(security)):
    token = credentials.credentials
    print("Entrooooo")
    try:
        payload = jwt.decode(token, key=SECRET, algorithms=ALGORITHM)
        return payload
    except JOSEError as e:
        raise HTTPException(status_code=401, detail=str(e))

async def post_token_service(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=int(TOKEN_EXPIRE))
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET, algorithm=ALGORITHM)
    return TokenRespose(token=encoded_jwt, message="Generated token")