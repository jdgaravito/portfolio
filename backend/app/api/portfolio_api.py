'''This module will handle all the routes for the portfolio endpoints.'''

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models.projects import Project
from ..models.projects_schema import ProjectSchema
from .auth import get_current_user, get_user_exception

portfolio_router = APIRouter()


@portfolio_router.get("/portfolio")
async def get_all_projects(data_base: Session = Depends(get_db)):
    '''This function will return all the projects in the database.'''
    return data_base.query(Project).all()


@portfolio_router.get("/portfolio_by_user")
async def get_all_by_user(
    user: dict = Depends(get_current_user),
    data_base: Session = Depends(get_db)
):
    '''This function will return all the projects in the database by user.'''
    if user is None:
        raise get_user_exception()
    return data_base.query(Project).filter(
        Project.owner_id == user.get("id")).all()


@portfolio_router.get("/portfolio/{project_id}")
async def get_a_project(
    project_id: int,
    user: dict = Depends(get_current_user),
    data_base: Session = Depends(get_db),
):
    '''This function will return a project by id.'''
    if user is None:
        raise get_user_exception()
    project_model = (
        data_base.query(Project)
        .filter(Project.id == project_id)
        .filter(Project.owner_id == user.get("id"))
        .first()
    )

    if project_model is not None:
        return project_model
    raise http_exception()


@portfolio_router.post("/portfolio")
async def create_project(
    project: ProjectSchema,
    user: dict = Depends(get_current_user),
    data_base: Session = Depends(get_db),
):
    '''This function will create a new project in the database.'''
    if user is None:
        raise get_user_exception()
    project_model = Project()
    project_model.title = project.title
    project_model.description = project.description
    project_model.is_public = project.is_public
    project_model.main_image_url = project.main_image_url
    project_model.category = project.category
    project_model.owner_id = user.get("id")

    data_base.add(project_model)
    data_base.commit()

    return successfull_response(201)


@portfolio_router.put("/portfolio/{project_id}")
async def update_project(
    project_id: int,
    project: ProjectSchema,
    user: dict = Depends(get_current_user),
    data_base: Session = Depends(get_db),
):
    '''This function will update a project in the database.'''
    if user is None:
        raise get_user_exception()
    project_model = (
        data_base.query(Project)
        .filter(Project.id == project_id)
        .filter(Project.owner_id == user.get("id"))
        .first()
    )

    if project_model is None:
        raise http_exception()
    project_model.title = project.title
    project_model.description = project.description
    project_model.is_public = project.is_public
    project_model.main_image_url = project.main_image_url
    project_model.category = project.category

    data_base.add(project_model)
    data_base.commit()

    return successfull_response(200)


@portfolio_router.delete("/portfolio/{project_id}")
async def delete_project(
    project_id: int,
    user: dict = Depends(get_current_user),
    data_base: Session = Depends(get_db),
):
    '''This function will delete a project in the database.'''
    if user is None:
        raise get_user_exception()

    project_model = (
        data_base.query(Project)
        .filter(Project.id == project_id)
        .filter(Project.owner_id == user.get("id"))
        .first()
    )

    if project_model is None:
        raise http_exception()
    data_base.query(Project).filter(Project.id == project_id).delete()
    data_base.commit()

    return successfull_response(200)


def successfull_response(status_code: int):
    '''This function will return a successfull response.'''
    return {"status": status_code, "transaction": "Successful"}


def http_exception():
    '''This function will return a http exception.'''
    return HTTPException(status_code=404, detail="Project not found")
