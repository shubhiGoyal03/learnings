from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None
class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None
inventory={
    1:{
        "name":"Milk",
        "price":3.99,
        "brand":"Saras"
    }
}
@app.get("/")
def home():
    return {"result": "home"}

@app.get("/about")
def about():
    return {"result": "about"}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(None, description="The id of the item", gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_by_name(*,item_id:int, name :Optional[str]=None,test:int):
    for item_id in inventory:
        if inventory[item_id]["name"]==name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int,item:Item):
    if item_id in inventory:
        return {"Error":"Item id already exists"}
    else:
        inventory[item_id]=item
    return inventory

@app.put("/update-item/{item_id}")
def update_item(item_id: int,item:UpdateItem):
    if item_id not in inventory:
        return {"Error":"Item id does not exists"}
    else:
        if item.name!=None:
            inventory[item_id].update(item)
    return inventory