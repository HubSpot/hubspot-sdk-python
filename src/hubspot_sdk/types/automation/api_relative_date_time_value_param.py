# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_delay_param import APITimeDelayParam

__all__ = ["APIRelativeDateTimeValueParam"]


class APIRelativeDateTimeValueParam(TypedDict, total=False):
    time_delay: Required[Annotated[APITimeDelayParam, PropertyInfo(alias="timeDelay")]]

    type: Required[Literal["RELATIVE_DATETIME"]]
    """This is the type of input value.

    This can be one of: "FIELD_DATA", "OBJECT_PROPERTY", "STATIC_VALUE",
    "RELATIVE_DATETIME", "TIMESTAMP", "INCREMENT", "FETCHED_OBJECT_PROPERTY",
    "APPEND_OBJECT_PROPERTY", "STATIC_APPEND_VALUE", "ENROLLMENT_EVENT_PROPERTY"
    """
