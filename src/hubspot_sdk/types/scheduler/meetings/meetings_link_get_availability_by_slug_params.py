# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MeetingsLinkGetAvailabilityBySlugParams"]


class MeetingsLinkGetAvailabilityBySlugParams(TypedDict, total=False):
    timezone: Required[str]
    """Return times in response based on specified time zone."""

    month_offset: Annotated[int, PropertyInfo(alias="monthOffset")]
    """Get times for a different month."""
