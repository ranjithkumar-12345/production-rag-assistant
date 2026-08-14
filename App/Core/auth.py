import os
from datetime import datetime,timedelta,timezone
from fastapi import Depends, HTTPException,status
from jose import JWTError,jwt
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
oathschems = OAuth2PasswordBearer(tokenUrl = "/auth/login") 

SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-rag-assistant-key-12345")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict,expires_delta : Optional[timedelta]=None)->str:
    to_encode = data.copy()
    expires_datetime = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp".expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM)

def verify_token(token:str)->dict:
    try:
        pay_load=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return pay_load
    except JWTError:
        raise HTTPException(
            status_code =status.HTTP_401_UNAUTHORIZED,
            details = "INVAILD/EXPIRED TOKEN",
            headers={"WWW.Authenticate":"Barrer"}
        )
def get_current_user(token:str = Depends(oathschems))->dict:
    pay_load = verify_token(token)
    username:str = pay_load.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            details = "invaild credentials"
        )
    return pay_load



if __name__ =="__main__":

    print("created access token successfully")