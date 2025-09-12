from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from passlib.context import CryptContext
from src.models import User, Resume
from src.schema import UserCreate, UserLogin, Token
from depencies import get_db
import bcrypt

SQLALCHEMY_DATABASE_URL = f"postgresql://{config('DATABASE_USER')}:{config('DATABASE_PASSWORD')}@172.23.1.3/{config('DATABASE_NAME')}"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autoflush=False, bind=engine)
# db = SessionLocal()

# Base = declarative_base()

# login = "valeron@gmail.com"

# users = db.query(User).all()
# print(users)


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pwd_context.verify(password, pwd_context.hash(password))  # True


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzU3Mjc3NTA4fQ.Ww7PvXmavn_rW-ozU2bVOu06iGbtqEIBodrjXWFfdi0

import os
from os.path import join


# base_dir = os.path.dirname(os.path.abspath(__file__))

# env_config = config(RepositoryEnv(join(base_dir, '.env')))

# user = env_config.get('DATABASE_USER')

user = config('DATABASE_USER')

print(SQLALCHEMY_DATABASE_URL)



