# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .crm_object_snapshot_request import CrmObjectSnapshotRequest

__all__ = ["CrmObjectSnapshotBatchRequest"]


class CrmObjectSnapshotBatchRequest(BaseModel):
    snapshot_requests: List[CrmObjectSnapshotRequest] = FieldInfo(alias="snapshotRequests")
    """
    An array of CrmObjectSnapshotRequest objects, each representing a request to
    create a snapshot for a specific CRM object. This property is required.
    """
