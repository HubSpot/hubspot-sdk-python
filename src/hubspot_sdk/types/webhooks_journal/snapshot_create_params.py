# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.crm_object_snapshot_request import CrmObjectSnapshotRequest

__all__ = ["SnapshotCreateParams"]


class SnapshotCreateParams(TypedDict, total=False):
    snapshot_requests: Required[Annotated[Iterable[CrmObjectSnapshotRequest], PropertyInfo(alias="snapshotRequests")]]
    """
    An array of CrmObjectSnapshotRequest objects, each representing a request to
    create a snapshot for a specific CRM object. This property is required.
    """
