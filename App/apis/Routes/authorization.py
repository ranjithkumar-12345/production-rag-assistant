from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.core.auth import create_access_token, hash_password, verify_password


router = APIRouter(prefix="/auth", tags=["Authentication"])

user_db = {}


class UserRegister(BaseModel):
    username: str
    password: str



@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserRegister):
    
    if user.username in user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    
    user_db[user.username] = {
        "username": user.username,
        "hashed_password": hash_password(user.password),
    }
    return {"message": "User Created successfully"}


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_db.get(form_data.username)
    
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
        
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


if __name__ == "__main__":
    print("Auth router loaded successfully")