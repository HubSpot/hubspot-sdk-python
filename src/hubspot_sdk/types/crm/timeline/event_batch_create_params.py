# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..timeline_event_param import TimelineEventParam

__all__ = ["EventBatchCreateParams"]


class EventBatchCreateParams(TypedDict, total=False):
    inputs: Required[Iterable[TimelineEventParam]]
    """A collection of timeline events we want to create."""
