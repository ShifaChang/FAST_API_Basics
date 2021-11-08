from fastapi import FastAPI
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

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Edeka"
    }
}

@app.post("/create-item")
def create_item(item: Item):   # this is for the request body from the class this isn't a query parameter
    return {}