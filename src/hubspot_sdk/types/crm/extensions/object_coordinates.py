# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ObjectCoordinates"]


class ObjectCoordinates(BaseModel):
    object_id: int = FieldInfo(alias="objectId")

    object_type_id: str = FieldInfo(alias="objectTypeId")

    portal_id: int = FieldInfo(alias="portalId")
