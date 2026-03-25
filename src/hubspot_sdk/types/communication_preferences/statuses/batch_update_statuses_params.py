# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..public_status_request_param import PublicStatusRequestParam

__all__ = ["BatchUpdateStatusesParams"]


class BatchUpdateStatusesParams(TypedDict, total=False):
    inputs: Required[Iterable[PublicStatusRequestParam]]
    """
    An array of PublicStatusRequest objects, each representing a subscription status
    update request. This property is required.
    """
