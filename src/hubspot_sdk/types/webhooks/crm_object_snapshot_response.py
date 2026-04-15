# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrmObjectSnapshotResponse"]


class CrmObjectSnapshotResponse(BaseModel):
    object_id: int = FieldInfo(alias="objectId")
    """An integer representing the unique identifier for the CRM object."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """A string representing the type identifier of the CRM object."""

    portal_id: int = FieldInfo(alias="portalId")
    """An integer representing the unique identifier for the HubSpot portal."""

    snapshot_status_id: str = FieldInfo(alias="snapshotStatusId")
    """A UUID string representing the status identifier of the snapshot."""
