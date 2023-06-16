'''This module will create a database session instance and
it will be used to query the database.'''

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from .config import Settings, get_settings

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, echo=True, connect_args={
    "options": "-c timezone=utc"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    '''This function will create all the tables in the database if they
    do not exist.'''
    Base.metadata.create_all(bind=engine)


def get_db():
    '''This function will return a database session instance.
    The session is created using the sessionmaker instance and
    it will be closed after the request is completed.
    '''
    try:
        data_base = SessionLocal()
        yield data_base
    finally:
        data_base.close()
