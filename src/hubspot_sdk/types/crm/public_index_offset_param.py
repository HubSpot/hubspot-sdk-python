# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PublicIndexOffsetParam"]


class PublicIndexOffsetParam(TypedDict, total=False):
    days: int
    """The number of days to offset."""

    hours: int
    """The number of hours to offset."""

    milliseconds: int
    """The number of milliseconds to offset."""

    minutes: int
    """The number of minutes to offset."""

    months: int
    """The number of months to offset."""

    quarters: int
    """The number of quarters to offset."""

    seconds: int
    """The number of seconds to offset."""

    weeks: int
    """The number of weeks to offset."""

    years: int
    """The number of years to offset."""
