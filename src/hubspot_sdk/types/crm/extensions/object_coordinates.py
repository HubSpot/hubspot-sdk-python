# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ObjectCoordinates"]


class ObjectCoordinates(BaseModel):
    object_id: int = FieldInfo(alias="objectId")
    """The unique identifier for the object."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The type identifier for the object."""

    portal_id: int = FieldInfo(alias="portalId")
    """The unique identifier for the portal."""
