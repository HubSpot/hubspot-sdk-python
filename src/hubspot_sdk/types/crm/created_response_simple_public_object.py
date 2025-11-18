# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .simple_public_object import SimplePublicObject

__all__ = ["CreatedResponseSimplePublicObject"]


class CreatedResponseSimplePublicObject(BaseModel):
    created_resource_id: str = FieldInfo(alias="createdResourceId")
    """The unique identifier of the newly created resource."""

    entity: SimplePublicObject
    """A simple public object."""

    location: Optional[str] = None
    """The URL location of the newly created resource."""
