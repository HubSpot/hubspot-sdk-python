# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MeetingsLinkGetBookingInfoBySlugParams"]


class MeetingsLinkGetBookingInfoBySlugParams(TypedDict, total=False):
    timezone: Required[str]
    """Return times in response based on specified time zone."""
