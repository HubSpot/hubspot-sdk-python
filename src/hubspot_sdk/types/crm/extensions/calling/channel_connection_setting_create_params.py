# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ChannelConnectionSettingCreateParams"]


class ChannelConnectionSettingCreateParams(TypedDict, total=False):
    is_ready: Required[Annotated[bool, PropertyInfo(alias="isReady")]]
    """If true, this app will be considered to support channel connection"""

    url: Required[str]
    """The URL to fetch phone numbers available for channel connection"""
