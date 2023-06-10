from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    description: str
    published: Optional[bool]

@router.post("/")
def create_blog(blog: BlogModel):
    return "Ok"

