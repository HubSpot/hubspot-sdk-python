# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingUpdateChannelConnectionSettingsParams"]


class CallingUpdateChannelConnectionSettingsParams(TypedDict, total=False):
    is_ready: Annotated[bool, PropertyInfo(alias="isReady")]
    """Indicates whether the channel connection settings are ready."""

    url: str
    """The URL for the channel connection settings."""
