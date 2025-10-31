# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam
from .api_static_value_param import APIStaticValueParam
from .api_static_branch_param import APIStaticBranchParam
from .api_increment_value_param import APIIncrementValueParam
from .api_timestamp_value_param import APITimestampValueParam
from .api_action_data_value_param import APIActionDataValueParam
from .api_static_append_value_param import APIStaticAppendValueParam
from .api_object_property_value_param import APIObjectPropertyValueParam
from .api_relative_date_time_value_param import APIRelativeDateTimeValueParam
from .api_append_object_property_value_param import APIAppendObjectPropertyValueParam
from .api_fetched_object_property_value_param import APIFetchedObjectPropertyValueParam
from .api_enrollment_event_property_value_param import APIEnrollmentEventPropertyValueParam

__all__ = ["APIStaticBranchActionParam", "InputValue"]

InputValue: TypeAlias = Union[
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


class APIStaticBranchActionParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    input_value: Required[Annotated[InputValue, PropertyInfo(alias="inputValue")]]

    static_branches: Required[Annotated[Iterable[APIStaticBranchParam], PropertyInfo(alias="staticBranches")]]

    type: Required[Literal["STATIC_BRANCH"]]

    default_branch: Annotated[APIConnectionParam, PropertyInfo(alias="defaultBranch")]

    default_branch_name: Annotated[str, PropertyInfo(alias="defaultBranchName")]
