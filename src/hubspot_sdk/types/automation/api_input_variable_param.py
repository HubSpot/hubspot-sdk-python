# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .api_static_value_param import APIStaticValueParam
from .api_increment_value_param import APIIncrementValueParam
from .api_timestamp_value_param import APITimestampValueParam
from .api_action_data_value_param import APIActionDataValueParam
from .api_static_append_value_param import APIStaticAppendValueParam
from .api_object_property_value_param import APIObjectPropertyValueParam
from .api_relative_date_time_value_param import APIRelativeDateTimeValueParam
from .api_append_object_property_value_param import APIAppendObjectPropertyValueParam
from .api_fetched_object_property_value_param import APIFetchedObjectPropertyValueParam
from .api_enrollment_event_property_value_param import APIEnrollmentEventPropertyValueParam

__all__ = ["APIInputVariableParam", "Value"]

Value: TypeAlias = Union[
    APIActionDataValueParam,
    APIObjectPropertyValueParam,
    APIStaticValueParam,
    APIRelativeDateTimeValueParam,
    APITimestampValueParam,
    APIIncrementValueParam,
    APIFetchedObjectPropertyValueParam,
    APIAppendObjectPropertyValueParam,
    APIStaticAppendValueParam,
    APIEnrollmentEventPropertyValueParam,
]


class APIInputVariableParam(TypedDict, total=False):
    name: Required[str]

    value: Required[Value]
