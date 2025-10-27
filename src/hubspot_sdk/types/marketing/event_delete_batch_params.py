# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .marketing_event_public_object_id_delete_request_param import MarketingEventPublicObjectIDDeleteRequestParam

__all__ = ["EventDeleteBatchParams"]


class EventDeleteBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[MarketingEventPublicObjectIDDeleteRequestParam]]
