# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicExportResponse"]


class PublicExportResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    export_state: Literal[
        "ENQUEUED", "PROCESSING", "DONE", "FAILED", "CANCELED", "CONFLICT", "DELETED", "DEFERRED", "PENDING_APPROVAL"
    ] = FieldInfo(alias="exportState")

    export_type: Literal["VIEW", "LIST"] = FieldInfo(alias="exportType")

    object_properties: List[str] = FieldInfo(alias="objectProperties")

    object_type: str = FieldInfo(alias="objectType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    export_name: Optional[str] = FieldInfo(alias="exportName", default=None)

    record_count: Optional[int] = FieldInfo(alias="recordCount", default=None)
