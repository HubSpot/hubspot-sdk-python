# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_delay import APITimeDelay

__all__ = ["APIRelativeDateTimeValue"]


class APIRelativeDateTimeValue(BaseModel):
    time_delay: APITimeDelay = FieldInfo(alias="timeDelay")

    type: Literal["RELATIVE_DATETIME"]
