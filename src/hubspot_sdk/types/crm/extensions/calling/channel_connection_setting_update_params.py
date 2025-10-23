# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ChannelConnectionSettingUpdateParams"]


class ChannelConnectionSettingUpdateParams(TypedDict, total=False):
    is_ready: Annotated[bool, PropertyInfo(alias="isReady")]
    """If true, this app will be considered to support channel connection"""

    url: str
    """The URL to fetch phone numbers available for channel connection"""
