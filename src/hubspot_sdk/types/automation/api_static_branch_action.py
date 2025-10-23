# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection
from .api_static_value import APIStaticValue
from .api_static_branch import APIStaticBranch
from .api_increment_value import APIIncrementValue
from .api_timestamp_value import APITimestampValue
from .api_action_data_value import APIActionDataValue
from .api_static_append_value import APIStaticAppendValue
from .api_object_property_value import APIObjectPropertyValue
from .api_relative_date_time_value import APIRelativeDateTimeValue
from .api_append_object_property_value import APIAppendObjectPropertyValue
from .api_fetched_object_property_value import APIFetchedObjectPropertyValue
from .api_enrollment_event_property_value import APIEnrollmentEventPropertyValue

__all__ = ["APIStaticBranchAction", "InputValue"]

InputValue: TypeAlias = Union[
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


class APIStaticBranchAction(BaseModel):
    action_id: str = FieldInfo(alias="actionId")
    """The ID for this action."""

    input_value: InputValue = FieldInfo(alias="inputValue")
    """The input value to branch off of."""

    static_branches: List[APIStaticBranch] = FieldInfo(alias="staticBranches")

    type: Literal["STATIC_BRANCH"]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """

    default_branch: Optional[APIConnection] = FieldInfo(alias="defaultBranch", default=None)

    default_branch_name: Optional[str] = FieldInfo(alias="defaultBranchName", default=None)
    """
    The name of the default branch, the branch that gets executed if `inputValue`
    does not match any of the `staticBranches`.
    """
