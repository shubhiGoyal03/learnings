import json

from fastapi import FastAPI, Form, Body,File, UploadFile,Request

from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/combine/")
async def create_upload_file(file: UploadFile,request):
    #print(Item(**json.loads(request)))
    return {"value":Item(**json.loads(request)),
            "filename": file.filename}

@ app.post("/combine1/",response_model=Item)
async def create_upload_file(file: UploadFile,request):
    #print(Item(**json.loads(request)))
    return json.loads(request)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/item/")
async def create_upload_file(test:Item=Body(...)):
    return test