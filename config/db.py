from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import DB_USER, DB_PASSWORD, DB_HOST,DB_PORT,DB_DATABASE


SQLALCHEMY_DATABASE_URL2 = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'

engine = create_engine(SQLALCHEMY_DATABASE_URL2) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

