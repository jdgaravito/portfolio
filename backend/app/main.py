
from fastapi import FastAPI
from .router import blog_get, blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def home_message():
    return {"message": "Hi, Welcome to my portfolio website"}


   
