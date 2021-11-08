from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
app = FastAPI()  #Creates an API object, initializes the API
## API methods:
## GET(returning information), POST(sending info to the endpoint/ creating something new), PUT(update somthing that is already existing), DELETE
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    #this class inherits from baseModel
    #define in this class the structure of the data that I am looking to accept as a item parameter

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
inventory = {}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):   # this is for the request body from the class this isn't a query parameter
    if item_id in inventory:
        return {"error": "item ID already exists"}
    ##inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}  # to access fields from the class
    inventory[item_id] = item # this item is an object
    return inventory[item_id]  # return inventory at item id

##PUT Method put is to update
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item = Item):
    if item_id not in inventory:
        return {"error": "item ID does not exists"}
    if item.name != None:
        inventory[item_id].name = item.name  # if the item exists overwrite the item with the new item
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
            inventory[item_id].brand = item.brand

    return inventory[item_id]  # return inventory at item id

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description= "The ID of the item to delete", ge=0,)):
    if item_id not in inventory:
        #return {"Error": "ID does not exits"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    del inventory[item_id]
    return {"success": "item deleted!"}