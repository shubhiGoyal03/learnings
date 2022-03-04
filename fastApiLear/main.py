from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app =FastAPI()

@app.get('/')
def index():
    return {"data":"Blog list"}

@app.get("/blog")
def blog(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else: return {"data":f"{limit} blogs from the db" }

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished blogs" }

@app.get("/blog/{id}")
def show(id:int):
    return {"data": id }

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post("/blog")
def create_blog(blog:Blog):
    #return blog
    return {"data" : f"Blog is created with a title as {blog.title}"}