# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicExportResponse"]


class PublicExportResponse(BaseModel):
    id: str
    """The unique ID of the export."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp when the export was created, in ISO 8601 format."""

    export_state: Literal[
        "ENQUEUED", "PROCESSING", "DONE", "FAILED", "CANCELED", "CONFLICT", "DELETED", "DEFERRED", "PENDING_APPROVAL"
    ] = FieldInfo(alias="exportState")
    """The current state of the export process."""

    export_type: Literal["VIEW", "LIST"] = FieldInfo(alias="exportType")
    """The type of export, which can be either VIEW or LIST."""

    object_properties: List[str] = FieldInfo(alias="objectProperties")
    """The list of properties exported for the associated object."""

    object_type: str = FieldInfo(alias="objectType")
    """The associated CRM object being exported."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp when the export was last updated, in ISO 8601 format."""

    export_name: Optional[str] = FieldInfo(alias="exportName", default=None)
    """The name assigned to the export."""

    record_count: Optional[int] = FieldInfo(alias="recordCount", default=None)
    """The total number of records included in the export."""
