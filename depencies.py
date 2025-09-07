import jwt
from database import SessionLocal
from fastapi import Depends, HTTPException
from src.auth.auth_bearer import JWTBearer
from src.models import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token:str = Depends(JWTBearer())) -> User:
    try:
        payload = jwt.decode(token, 'secret', algorithms=["HS256"])                
        user_id = payload.get('sub')
        db = SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        db.expunge(user)
        return user
    except(jwt.PyJWTError, AttributeError):
        return HTTPException(status_code="Invalid token")



