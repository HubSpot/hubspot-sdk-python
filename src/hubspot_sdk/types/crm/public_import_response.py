# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .import_template import ImportTemplate
from .public_import_metadata import PublicImportMetadata

__all__ = ["PublicImportResponse"]


class PublicImportResponse(BaseModel):
    id: str
    """The unique identifier for this import."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp when the object was created, in ISO 8601 format."""

    mapped_object_type_ids: List[str] = FieldInfo(alias="mappedObjectTypeIds")

    metadata: PublicImportMetadata

    opt_out_import: bool = FieldInfo(alias="optOutImport")
    """
    Whether or not the import is a list of people disqualified from receiving
    emails.
    """

    state: Literal["CANCELED", "DEFERRED", "DONE", "FAILED", "PROCESSING", "REVERTED", "STARTED"]
    """The status of the import."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """
    The timestamp when the import record was last updated, formatted as an ISO 8601
    instant.
    """

    import_name: Optional[str] = FieldInfo(alias="importName", default=None)
    """The user-provided name for this import."""

    import_request_json: Optional[object] = FieldInfo(alias="importRequestJson", default=None)
    """The complete import request configuration as a JSON object."""

    import_source: Optional[Literal["API", "CRM_UI", "IMPORT", "MOBILE_ANDROID", "MOBILE_IOS", "SALESFORCE"]] = (
        FieldInfo(alias="importSource", default=None)
    )
    """Indicates where/how the import was initiated."""

    import_template: Optional[ImportTemplate] = FieldInfo(alias="importTemplate", default=None)
