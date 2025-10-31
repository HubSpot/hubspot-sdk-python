# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_delay_param import APITimeDelayParam

__all__ = ["APIRelativeDateTimeValueParam"]


class APIRelativeDateTimeValueParam(TypedDict, total=False):
    time_delay: Required[Annotated[APITimeDelayParam, PropertyInfo(alias="timeDelay")]]

    type: Required[Literal["RELATIVE_DATETIME"]]
