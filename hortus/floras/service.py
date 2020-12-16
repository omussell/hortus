# Standard Library
from typing import List
from typing import Optional

# 3rd-party
from floras.models import *


async def get_all() -> List[Optional[Flora]]:
    """Returns all Flora's."""
    flora = await Flora.objects.all()
    return flora


async def get(flora: FloraRead) -> Optional[Flora]:
    """Get a Flora."""
    flora = await Flora.objects.get(id=flora.id)
    return flora


async def create(flora_create: FloraCreate) -> Flora:
    """Create a Flora."""
    related_classification = await Classification.objects.get(
        name=flora_create.classification
    )
    flora = await Flora.objects.create(
        classification=related_classification,
        text=flora_create.text,
        completed=flora_create.completed,
    )
    return flora


async def update(flora_update: FloraUpdate) -> Flora:
    """Update a Flora."""
    flora = await Flora.objects.get(id=flora_update.id)
    related_classification = await Classification.objects.get(name=flora.classification)
    await flora.update(
        classification=related_classification,
        text=flora_update.text,
        completed=flora_update.completed,
    )
    return flora


async def delete(flora_id: int) -> bool:
    """Delete a Flora."""
    flora = await Flora.objects.get(id=flora_id)
    await flora.delete()
    return True
