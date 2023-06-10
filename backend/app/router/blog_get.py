from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get(
    "/",
    summary="Retrieves all blogs",
    description="This api call simulates fetching all blogs",
    response_description="The list of avaliable blogs entries",
)
def get_all_blogs(page: int = 1, page_size: Optional[int] = None):
    return {"message": f"all blogs, showing  {page} blogs posts of {page_size}"}


@router.get(
    "/{id}/",
    summary="Retrieves a blog post",
    description="This api call simulates retrieving a post by its ID",
    response_description="A specific blog post",
)
class BlogType(str, Enum):
    review = "review"
    tutorial = "tutorial"
    story = "story"
    short = "short"


@router.get(
    "/type/{type}",
    summary="Retrieves all blogs by category",
    description="This api call simulates fetching all blogs whintin a category",
    response_description="The list of avaliable blogs entries within a category type",
)
def get_blog_by_category(type: BlogType):
    return {"message:": f"blogs with category {type.value}"}


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Retrieves a blog post",
    description="This api call simulates retrieving a post by its ID",
    response_description="A specific blog post",
)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog with id {id} was not found"}
    else:
        return {"message": f"blog with {id}"}
