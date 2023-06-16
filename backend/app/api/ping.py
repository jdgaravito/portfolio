'''This module will contain the ping route.'''
from fastapi import APIRouter, Depends
from app.config import get_settings, Settings


ping_router = APIRouter()


@ping_router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    '''This function will return a pong! message.'''
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
