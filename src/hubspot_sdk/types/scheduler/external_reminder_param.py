# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExternalReminderParam"]


class ExternalReminderParam(TypedDict, total=False):
    number_of_time_units: Required[Annotated[int, PropertyInfo(alias="numberOfTimeUnits")]]
    """
    The number of timeUnits prior to the meeting start when the reminder will be
    sent.
    """

    time_unit: Required[Annotated[Literal["DAYS", "HOURS", "MINUTES", "WEEKS"], PropertyInfo(alias="timeUnit")]]
    """Accepted values are: WEEKS, DAYS, HOURS, MINUTES."""
