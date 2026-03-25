# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TimeOffset"]


class TimeOffset(BaseModel):
    amount: int

    offset_direction: Literal["FUTURE", "PAST"] = FieldInfo(alias="offsetDirection")

    time_unit: Literal["DAYS", "HOURS", "MINUTES", "WEEKS"] = FieldInfo(alias="timeUnit")
