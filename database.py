from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from decouple import config

SQLALCHEMY_DATABASE_URL = f"postgresql://{config('DATABASE_USER')}:{config('DATABASE_PASSWORD')}@172.23.1.3/{config('DATABASE_NAME')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

Base = declarative_base()
