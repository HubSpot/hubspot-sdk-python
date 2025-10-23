# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .behavioral_event_http_completion_request_param import BehavioralEventHTTPCompletionRequestParam

__all__ = ["BatchSendParams"]


class BatchSendParams(TypedDict, total=False):
    inputs: Required[Iterable[BehavioralEventHTTPCompletionRequestParam]]
