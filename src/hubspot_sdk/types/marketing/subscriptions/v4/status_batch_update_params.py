# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..public_status_request_param import PublicStatusRequestParam

__all__ = ["StatusBatchUpdateParams"]


class StatusBatchUpdateParams(TypedDict, total=False):
    inputs: Required[Iterable[PublicStatusRequestParam]]
