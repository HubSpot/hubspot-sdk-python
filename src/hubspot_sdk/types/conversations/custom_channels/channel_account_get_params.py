# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChannelAccountGetParams"]


class ChannelAccountGetParams(TypedDict, total=False):
    channel_id: Required[Annotated[int, PropertyInfo(alias="channelId")]]

    archived: bool
    """Filter results to include only archived or non-archived channel accounts."""
