# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .marketing_event_public_update_request_full_v2_param import MarketingEventPublicUpdateRequestFullV2Param

__all__ = ["EventUpdateBatchParams"]


class EventUpdateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[MarketingEventPublicUpdateRequestFullV2Param]]
