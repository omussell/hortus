# Standard Library
from typing import List
from typing import Optional

# 3rd-party
from classifications.models import *


async def get_all() -> List[Optional[Classification]]:
    """Returns all Classification's."""
    classifications = await Classification.objects.all()
    return classifications


async def get(classification: ClassificationRead) -> Optional[Classification]:
    """Get a Classification."""
    classification = await Classification.objects.get(id=classification.id)
    return classification


async def create(classification_create: ClassificationCreate) -> Classification:
    """Create a Classification."""
    classification = await Classification.objects.create(
        name=classification_create.name
    )
    return classification


async def update(classification_update: ClassificationUpdate) -> Classification:
    """Update a Classification."""
    classification = await Classification.objects.get(id=classification_update.id)
    await classification.update(name=classification_update.name)
    return classification


async def delete(classification_id: int) -> bool:
    """Delete a Classification."""
    classification = await Classification.objects.get(id=classification_id)
    await classification.delete()
    return True
