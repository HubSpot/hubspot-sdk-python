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

    created_at: datetime = FieldInfo(alias="createdAt")

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

    import_name: Optional[str] = FieldInfo(alias="importName", default=None)

    import_request_json: Optional[object] = FieldInfo(alias="importRequestJson", default=None)

    import_source: Optional[Literal["API", "CRM_UI", "IMPORT", "MOBILE_ANDROID", "MOBILE_IOS", "SALESFORCE"]] = (
        FieldInfo(alias="importSource", default=None)
    )

    import_template: Optional[ImportTemplate] = FieldInfo(alias="importTemplate", default=None)
