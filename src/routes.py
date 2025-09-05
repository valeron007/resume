from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
from src.models import User
from src.schema import UserCreate, UserLogin, Token
from depencies import get_db

user_router = APIRouter()

@user_router.post('/signup')
def signup(user_data: UserCreate, db:Session = Depends(get_db)):
    user = User(email=user_data.email)
    user.hashed_password(user_data.password)
    db.add(user)
    db.commit()

    return {
        "message": "User create"
    }

@user_router.post('/login')
def login(user_data: UserCreate, db:Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == user_data.email).first()
    
    if user is None or not user.check_password(user_data.password):
        raise HTTPException(status_code=401, default="Invalid Credentials")

    token = user.generate_token()
    return Token(access_token=token, token_type='bearer')

