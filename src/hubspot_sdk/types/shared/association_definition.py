# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssociationDefinition"]


class AssociationDefinition(BaseModel):
    """The definition of an association"""

    id: str
    """The unique ID of the associated object (e.g., a contact ID)."""

    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")
    """The ID of the source object type (e.g., 0-1 for contacts)."""

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")
    """The ID of the destination object type (e.g., 0-3 for deals)."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The timestamp when the association was created, in ISO 8601 format."""

    name: Optional[str] = None
    """For labeled association types, the internal name of the association."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    The timestamp when the last update was made to an association, in ISO 8601
    format.
    """
