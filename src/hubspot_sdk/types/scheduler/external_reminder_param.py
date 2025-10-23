# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExternalReminderParam"]


class ExternalReminderParam(TypedDict, total=False):
    number_of_time_units: Required[Annotated[int, PropertyInfo(alias="numberOfTimeUnits")]]

    time_unit: Required[Annotated[str, PropertyInfo(alias="timeUnit")]]
