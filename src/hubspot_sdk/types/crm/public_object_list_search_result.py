# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicObjectListSearchResult"]


class PublicObjectListSearchResult(BaseModel):
    additional_properties: Dict[str, str] = FieldInfo(alias="additionalProperties")
    """
    The name and value of any additional properties that exist for this list and
    that were included in the search request.
    """

    list_id: str = FieldInfo(alias="listId")
    """The **ILS ID** of the list."""

    list_version: int = FieldInfo(alias="listVersion")
    """The version of the list."""

    name: str
    """The name of the list."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The object type of the list."""

    processing_status: str = FieldInfo(alias="processingStatus")
    """The processing status of the list."""

    processing_type: str = FieldInfo(alias="processingType")
    """The processing type of the list."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The time when the list was created."""

    created_by_id: Optional[str] = FieldInfo(alias="createdById", default=None)
    """The ID of the user that created the list."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time when the list was deleted."""

    filters_updated_at: Optional[datetime] = FieldInfo(alias="filtersUpdatedAt", default=None)
    """The time when the filters for this list were last updated."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The time the list was last updated."""

    updated_by_id: Optional[str] = FieldInfo(alias="updatedById", default=None)
    """The ID of the user that last updated the list."""
