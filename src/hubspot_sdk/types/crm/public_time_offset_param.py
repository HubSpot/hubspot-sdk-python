# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicTimeOffsetParam"]


class PublicTimeOffsetParam(TypedDict, total=False):
    amount: Required[int]
    """The numerical value representing the quantity of the time offset."""

    offset_direction: Required[Annotated[str, PropertyInfo(alias="offsetDirection")]]
    """Indicates the direction of the time offset, such as forward or backward."""

    time_unit: Required[Annotated[str, PropertyInfo(alias="timeUnit")]]
    """Specifies the unit of time for the offset, such as days, hours, or minutes."""
