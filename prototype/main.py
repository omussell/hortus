from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()

class Plant(BaseModel):
    name: str
    radius: int
    height: int

class Tree(BaseModel):
    name: str
    trunk_radius: int
    trunk_height: int
    canopy_radius: int
    canopy_height: int
    # canopy starts X meters from the ground up the trunk
    canopy_offset: int

class GridLayer(BaseModel):
    horizontal: int
    vertical: int
    height: int
    area: int = horizontal * vertical

@app.get("/")
async def root():
    return {"message": "Hello World!"}




@app.get("/notes/{note_id}", tags=["notes"])
async def read_note(note_id: int):
    return {"note_id": note_id}


@app.post("/notes/",)
async def create_note(note: Note):
    return note
