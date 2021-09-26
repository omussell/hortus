# Standard Library
from typing import List
from typing import Optional

# 3rd-party
import databases
from classifications.models import *
from classifications.service import *
from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["classifications"])
async def get_classifications() -> List[ClassificationRead]:
    """Get a list of Classification's."""
    return await get_all()


@router.get("/{classification_id}", tags=["classifications"])
async def get_classification(classification: ClassificationRead):
    """Get a specific classification."""
    return await get(classification)


@router.post("/", tags=["classifications"])
async def create_classification(classification: ClassificationCreate):
    """Create a Classification."""
    return await create(classification)


@router.put("/{classification_id}", tags=["classifications"])
async def update_classification(classification: ClassificationUpdate):
    """Update a Classification."""
    return await update(classification)


@router.delete("/{classification_id}", tags=["classifications"])
async def delete_classification(classification_id: int):
    """Delete a Classification."""
    return await delete(classification_id)
