from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()
inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Edeka"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view")):  # colon represents type hint,tells this item id is supposed to be an integer. Path helps to add more details in out path parameters, none is default value for description.
    return inventory[item_id]

## QUERY PARAMETERS
# example: "facebook.com/home?key="
## How to accept query parameters for our endpoint?
## in the webpage: query-parameter-name?variable-name=value


@app.get("/get-by-name")   #this is a query parameter
def get_item(name: Optional[str] = None):    #this query parameter is no longer required bcz it has a default value None, this is an optional parameter now
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data": "Not Found"}

##Error: non default argument came after default argument when doing 2 querries means, put mandatory first and optional later, or simply add an * first then , optional parameters


## Combine Path & Querry parameters:
@app.get("/get-by-name/{item_id}")
def get_name(*, item_id: int, name: Optional[str] = None, test: int): #item_id as path paramater, name as optional query parameter and test as mandatory query parameter.
    if inventory[item_id]["name"] == name:
        return inventory[item_id]
    return {"Data": "Not Found"}