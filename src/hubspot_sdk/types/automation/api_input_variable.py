# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .api_static_value import APIStaticValue
from .api_increment_value import APIIncrementValue
from .api_timestamp_value import APITimestampValue
from .api_action_data_value import APIActionDataValue
from .api_static_append_value import APIStaticAppendValue
from .api_object_property_value import APIObjectPropertyValue
from .api_relative_date_time_value import APIRelativeDateTimeValue
from .api_append_object_property_value import APIAppendObjectPropertyValue
from .api_fetched_object_property_value import APIFetchedObjectPropertyValue
from .api_enrollment_event_property_value import APIEnrollmentEventPropertyValue

__all__ = ["APIInputVariable", "Value"]

Value: TypeAlias = Union[
    APIActionDataValue,
    APIObjectPropertyValue,
    APIStaticValue,
    APIRelativeDateTimeValue,
    APITimestampValue,
    APIIncrementValue,
    APIFetchedObjectPropertyValue,
    APIAppendObjectPropertyValue,
    APIStaticAppendValue,
    APIEnrollmentEventPropertyValue,
]


class APIInputVariable(BaseModel):
    name: str

    value: Value
