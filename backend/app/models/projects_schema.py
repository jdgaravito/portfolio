from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Category(str, Enum):
    '''Project category enum'''
    UX_UI = "UX_UI"
    DEV = "DEV"
    PRODUCT = "PRODUCT"
    VIDEO = "VIDEO"
    DATA_SCIENCE = "DATA_SCIENCE"


class ProjectBase(BaseModel):
    '''Project base schema'''
    title: str = Field(title="Title of the project",
                       min_length=2, max_length=250)
    description: str = Field(
        title="Description of the project", max_length=1000, min_length=25
    )
    is_public: bool = False
    main_image_url: str = Field(title="Main image URL", max_length=250)
    category: Category = Category.UX_UI

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "title": "An Excelent Project",
                "description": "lorem pisum sit dolor amet non sequa",
                "main_image_url": "https://myimage",
                "is_public": True,
                "category": "UX_UI",
            }
        }


class ProjectSchema(ProjectBase):
    '''Project schema child'''
    id: int = Field(default=None)
    time_created: datetime = Field(default_factory=datetime.utcnow)
    time_updated: datetime = Field(default_factory=datetime.utcnow)
