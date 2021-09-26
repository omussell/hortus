# Standard Library
from typing import List
from typing import Optional

# 3rd-party
import databases
from fastapi import APIRouter
from floras.models import *
from floras.service import *

router = APIRouter()


@router.get("/", tags=["floras"])
async def get_floras() -> List[FloraRead]:
    """Get a list of Flora's."""
    return await get_all()


@router.get("/{flora_id}", tags=["floras"])
async def get_flora(flora: FloraRead):
    """Get a specific flora."""
    return await get(flora)


@router.post("/", tags=["floras"])
async def create_flora(flora: FloraCreate):
    """Create a Flora."""
    return await create(flora)


@router.put("/{flora_id}", tags=["floras"])
async def update_flora(flora: FloraUpdate):
    """Update a Flora."""
    return await update(flora)


@router.delete("/{flora_id}", tags=["floras"])
async def delete_flora(flora_id: int):
    """Delete a Flora."""
    return await delete(flora_id)
