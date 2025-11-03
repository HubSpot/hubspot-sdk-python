# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DateTime"]


class DateTime(BaseModel):
    date_only: bool = FieldInfo(alias="dateOnly")

    time_zone_shift: int = FieldInfo(alias="timeZoneShift")

    value: int
