# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .public_deal_splits_create_request_param import PublicDealSplitsCreateRequestParam

__all__ = ["DealSplitBatchUpsertParams"]


class DealSplitBatchUpsertParams(TypedDict, total=False):
    inputs: Required[Iterable[PublicDealSplitsCreateRequestParam]]
