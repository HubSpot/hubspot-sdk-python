# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicList"]


class PublicList(BaseModel):
    list_id: str = FieldInfo(alias="listId")

    list_version: int = FieldInfo(alias="listVersion")

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    processing_status: str = FieldInfo(alias="processingStatus")

    processing_type: str = FieldInfo(alias="processingType")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by_id: Optional[str] = FieldInfo(alias="createdById", default=None)

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    filters_updated_at: Optional[datetime] = FieldInfo(alias="filtersUpdatedAt", default=None)

    size: Optional[int] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by_id: Optional[str] = FieldInfo(alias="updatedById", default=None)
