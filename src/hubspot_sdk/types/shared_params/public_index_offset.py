# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PublicIndexOffset"]


class PublicIndexOffset(TypedDict, total=False):
    days: int

    hours: int

    milliseconds: int

    minutes: int

    months: int

    quarters: int

    seconds: int

    weeks: int

    years: int
