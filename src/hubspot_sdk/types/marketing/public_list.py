# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicList"]


class PublicList(BaseModel):
    list_id: str = FieldInfo(alias="listId")
    """An internal ID of the list"""

    list_version: int = FieldInfo(alias="listVersion")
    """A number that represents a version of the list"""

    name: str
    """The name of the list"""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The internal ID of the object type of the list"""

    processing_status: str = FieldInfo(alias="processingStatus")
    """Represents the current processing status of the list"""

    processing_type: str = FieldInfo(alias="processingType")
    """Processing type of the list"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp of the creation of the list"""

    created_by_id: Optional[str] = FieldInfo(alias="createdById", default=None)
    """The ID of the user who created the list"""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """Timestamp of the deletion of the list"""

    filters_updated_at: Optional[datetime] = FieldInfo(alias="filtersUpdatedAt", default=None)
    """Timestamp of the last update of the list filters"""

    size: Optional[int] = None
    """The size of the result list"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp of the last update of the list"""

    updated_by_id: Optional[str] = FieldInfo(alias="updatedById", default=None)
    """The ID of the user who last updated the list"""
