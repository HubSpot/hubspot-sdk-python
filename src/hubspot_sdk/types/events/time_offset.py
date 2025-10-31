# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TimeOffset"]


class TimeOffset(BaseModel):
    amount: int

    offset_direction: Literal["PAST", "FUTURE"] = FieldInfo(alias="offsetDirection")

    time_unit: Literal["WEEKS", "DAYS", "HOURS", "MINUTES"] = FieldInfo(alias="timeUnit")
