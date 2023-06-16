from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from ..db import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email= Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    projects = relationship("Project", back_populates="owner")