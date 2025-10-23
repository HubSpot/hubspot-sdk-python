# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicObjectListRecord"]


class PublicObjectListRecord(BaseModel):
    list_id: str = FieldInfo(alias="listId")
    """The ID of the list containing the imported objects."""

    object_type: str = FieldInfo(alias="objectType")
    """The type of object contained in the list."""
