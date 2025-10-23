# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.property import Property

__all__ = ["CreatedResponseProperty"]


class CreatedResponseProperty(BaseModel):
    created_resource_id: str = FieldInfo(alias="createdResourceId")

    entity: Property
    """Defines a property"""

    location: Optional[str] = None
