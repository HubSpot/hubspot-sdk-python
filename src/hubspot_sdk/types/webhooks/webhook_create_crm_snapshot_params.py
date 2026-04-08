# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .crm_object_snapshot_request_param import CrmObjectSnapshotRequestParam

__all__ = ["WebhookCreateCrmSnapshotParams"]


class WebhookCreateCrmSnapshotParams(TypedDict, total=False):
    snapshot_requests: Required[
        Annotated[Iterable[CrmObjectSnapshotRequestParam], PropertyInfo(alias="snapshotRequests")]
    ]
