# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicListConversionInactivity"]


class PublicListConversionInactivity(BaseModel):
    conversion_type: Literal["INACTIVITY"] = FieldInfo(alias="conversionType")
    """Specifies the type of conversion (INACTIVITY)."""

    offset: int
    """The number of time units for the inactivity period."""

    time_unit: Literal["DAY", "MONTH", "WEEK"] = FieldInfo(alias="timeUnit")
    """The unit of time for the inactivity period, such as (DAY, MONTH, WEEK)."""
