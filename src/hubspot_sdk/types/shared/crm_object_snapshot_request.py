# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrmObjectSnapshotRequest"]


class CrmObjectSnapshotRequest(BaseModel):
    object_id: int = FieldInfo(alias="objectId")
    """
    An integer representing the unique identifier of the CRM object for which the
    snapshot is requested.
    """

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """
    A string representing the type identifier of the CRM object, specifying what
    kind of object it is within HubSpot.
    """

    portal_id: int = FieldInfo(alias="portalId")
    """
    An integer representing the unique identifier of the HubSpot account (portal)
    where the CRM object resides.
    """

    properties: List[str]
    """
    An array of strings, each representing a property of the CRM object that should
    be included in the snapshot.
    """
