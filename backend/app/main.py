"""This is the main file for the FastAPI application. This is where we will
create all the routes for the application. We will also create a function
to initialize the database connection.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.auth import auth_router
from .api.portfolio_api import portfolio_router
from .api.ping import ping_router


app = FastAPI()

# Invoke the routes
app.include_router(auth_router)
app.include_router(portfolio_router)
app.include_router(ping_router)


origins = ["http://localhost", "http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home_message():
    '''This is the home route for the application. It will return a simple
    message.'''
    return {"message": "Hi, Welcome to my portfolio api"}
