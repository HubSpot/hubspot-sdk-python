# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrmObjectSnapshotResponse"]


class CrmObjectSnapshotResponse(BaseModel):
    object_id: int = FieldInfo(alias="objectId")

    object_type_id: str = FieldInfo(alias="objectTypeId")

    portal_id: int = FieldInfo(alias="portalId")

    snapshot_status_id: str = FieldInfo(alias="snapshotStatusId")
