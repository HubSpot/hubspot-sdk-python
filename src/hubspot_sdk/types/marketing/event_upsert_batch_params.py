# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .marketing_event_create_request_params import MarketingEventCreateRequestParams

__all__ = ["EventUpsertBatchParams"]


class EventUpsertBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[MarketingEventCreateRequestParams]]
