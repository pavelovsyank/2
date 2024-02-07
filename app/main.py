from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/")
async def root():
    return {"message": "Hello World"}