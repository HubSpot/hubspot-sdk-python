# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrmObjectSnapshotResponse"]


class CrmObjectSnapshotResponse(BaseModel):
    object_id: int = FieldInfo(alias="objectId")
    """
    An integer representing the unique identifier of the CRM object for which the
    snapshot is taken.
    """

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """
    A string indicating the type of the CRM object, such as contact, company, or
    deal.
    """

    portal_id: int = FieldInfo(alias="portalId")
    """
    An integer representing the unique identifier of the HubSpot portal associated
    with the CRM object.
    """

    snapshot_status_id: str = FieldInfo(alias="snapshotStatusId")
    """
    A UUID string representing the status identifier of the snapshot request,
    indicating the current state of the snapshot process.
    """
