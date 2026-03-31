# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingCreateChannelConnectionSettingsParams"]


class CallingCreateChannelConnectionSettingsParams(TypedDict, total=False):
    is_ready: Required[Annotated[bool, PropertyInfo(alias="isReady")]]
    """Indicates whether the channel connection settings are ready."""

    url: Required[str]
    """The URL associated with the channel connection settings."""
