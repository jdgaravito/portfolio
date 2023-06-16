from fastapi import FastAPI
from .api.auth import auth_router
from .api.portfolio_api import portfolio_router
from .api.ping import ping_router
from .db import init_db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Invoke the routes
app.include_router(auth_router)
app.include_router(portfolio_router)
app.include_router(ping_router)



origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://jdgaravito.dev"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home_message():
    return {
        "message":"Hi, Welcome to my portfolio api"
    }


# @app.on_event("startup")
# def on_startup():
#     init_db()
