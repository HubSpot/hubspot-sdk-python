# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["Condition"]


class Condition(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["CRM_OBJECT_PROPERTY"], PropertyInfo(alias="filterType")]]
    """A string indicating the type of filter being applied.

    Valid value is 'CRM_OBJECT_PROPERTY'.
    """

    operator: Required[
        Literal[
            "CONTAINS",
            "ENDS_WITH",
            "EQ",
            "GT",
            "GTE",
            "IN",
            "IS_EMPTY",
            "IS_NOT_EMPTY",
            "LT",
            "LTE",
            "N_EQ",
            "NOT_IN",
            "STARTS_WITH",
        ]
    ]
    """A string specifying the operation to be performed in the condition.

    Valid values include 'EQ', 'N_EQ', 'LT', 'GT', 'LTE', 'GTE', 'CONTAINS',
    'STARTS_WITH', 'ENDS_WITH', 'IN', 'NOT_IN', 'IS_EMPTY', and 'IS_NOT_EMPTY'.
    """

    property: Required[str]
    """
    A string representing the specific property of the CRM object that the condition
    applies to.
    """

    value: str
    """
    A string representing the value to be compared against the specified property
    when using single-value operators.
    """

    values: SequenceNotStr[str]
    """
    An array of strings used to specify multiple values for comparison when using
    operators that support multiple values, such as 'IN' or 'NOT_IN'.
    """
