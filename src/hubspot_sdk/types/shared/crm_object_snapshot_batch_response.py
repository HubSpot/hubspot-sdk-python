# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .crm_object_snapshot_response import CrmObjectSnapshotResponse

__all__ = ["CrmObjectSnapshotBatchResponse"]


class CrmObjectSnapshotBatchResponse(BaseModel):
    snapshot_responses: List[CrmObjectSnapshotResponse] = FieldInfo(alias="snapshotResponses")
    """
    An array of CrmObjectSnapshotResponse objects, each representing the result of a
    snapshot operation for a specific CRM object. This property is required.
    """
