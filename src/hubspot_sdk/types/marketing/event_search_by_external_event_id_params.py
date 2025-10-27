# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EventSearchByExternalEventIDParams"]


class EventSearchByExternalEventIDParams(TypedDict, total=False):
    q: Required[str]
    """
    The id of the marketing event in the external event application
    (externalEventId)
    """
