# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIFlowListing"]


class APIFlowListing(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    flow_type: str = FieldInfo(alias="flowType")

    is_enabled: bool = FieldInfo(alias="isEnabled")

    object_type_id: str = FieldInfo(alias="objectTypeId")

    revision_id: str = FieldInfo(alias="revisionId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    name: Optional[str] = None

    uuid: Optional[str] = None
