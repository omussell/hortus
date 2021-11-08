from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

from image.generation import generate_image

app = FastAPI()


@app.get("/")
def read_root():
    img = generate_image()
    #return FileResponse("my_image.png")
    return FileResponse("my_other_image.png")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}