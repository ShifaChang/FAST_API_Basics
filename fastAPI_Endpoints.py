from fastapi import FastAPI
app = FastAPI()  #Creates an API object, initializes the API
## API methods:
## GET(returning information), POST(sending info to the endpoint/ creating something new), PUT(update somthing that is already existing), DELETE

@app.get("/")
def home():      #home endpoint
    return {"Data": "Test"}


#in command prompt:
#uvicorn python_file_name:app -- reload

@app.get("/about")
def about():
    return {"Data": "About"}