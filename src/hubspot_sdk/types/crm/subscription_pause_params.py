# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionPauseParams"]


class SubscriptionPauseParams(TypedDict, total=False):
    pause_reason: Annotated[str, PropertyInfo(alias="pauseReason")]
