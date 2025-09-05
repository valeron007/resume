import sqlalchemy.orm as orm
import uuid, bcrypt, jwt
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime, timedelta
from typing import List
from database import Base

class User(Base):
    __tablename__ = "user"
    id: orm.Mapped[int] = orm.mapped_column(Integer, primary_key=True)
    email:orm.Mapped[str] = orm.mapped_column(String(100), index=True, unique=True)
    password: orm.Mapped[str] = Column(String)
    resume: orm.Mapped[List["Resume"]] = orm.relationship(back_populates="user")

    def hashed_password(self, password:str):        
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf8')
        
    def check_password(self, password: str):
        return bcrypt.checkpw(password=password.encode('utf-8'), hashed_password=self.password.encode('utf-8'))

    def generate_token(self):
        expiration = datetime.utcnow() + timedelta(hours=24)
        payload = {
            "sub": str(self.id),
            "exp": expiration
        }
        return jwt.encode(payload, 'secret', algorithm="HS256")

class Resume(Base):
    __tablename__ = "resume"
    id: orm.Mapped[int] = orm.mapped_column(Integer, primary_key=True)
    title:orm.Mapped[str] = orm.mapped_column(String(100), index=True, unique=True)
    content: orm.Mapped[str] = Column(String)
    user_id: orm.Mapped[int] = orm.mapped_column(ForeignKey("user.id"))
    user: orm.Mapped["User"] = orm.relationship(back_populates="resume")



