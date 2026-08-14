from fastapi import Depends,HTTPException,status,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional
from pydantic import BaseModel
from app.core.auth import create_access_token,hash_password,verify_password

router = APIRouter(prefix="/auth",tags = ["Authentication"])

user_db = {}
class userRegister(BaseModel):
    user_name:str
    pass_word:str

@router.post("/register",status_code =status.HTTP_201_CREATED )
def register(user:userRegister):
    if user.user_name not in user_db:
        raise  HTTPException(
        status_code = status.HTTP_400_BAD_REQUEST,
        details = "invaild user_name"
        )

    user_db[user.user_name] ={
        "username" :user.user_name,
        "hashed_password" : hash_password(user.pass_word)
    }
    return {"message":"User Created successfully"}

@router.post("/login",status_code=status.HTTP_404_NOT_FOUND)
def login(from_data: OAuth2PasswordRequestForm = Depends()):
    user=user_db.get(from_data.user_name)
    if not user or not verify_password(from_data.pass_word,user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            details = "wrong user_name and password",
            headers  = {"WWW_Authenticate":"baarer"}
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
    
    

if __name__=="__main__":

    print("login successfully")
