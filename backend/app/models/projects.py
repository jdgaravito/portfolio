import enum
from typing import Text
from sqlalchemy import Column, Boolean, Integer, Enum, String , DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .users import User
from ..db import Base

class ProjectCategory(enum.Enum):
    UX_UI = "UX_UI"
    DEV = "DEV"
    PRODUCT = "PRODUCT"
    VIDEO = "VIDEO"
    DATA_SCIENCE = "DATA_SCIENCE"


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    main_image_url = Column(String)
    description = Column(Text)
    is_public = Column(Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    time_published = Column(DateTime(timezone=True))
    category = Column(Enum(ProjectCategory))
    owner_id = Column(Integer, ForeignKey(User.id))

    owner = relationship("User", back_populates="projects")
