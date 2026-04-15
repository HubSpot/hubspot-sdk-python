# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ConditionParam"]


class ConditionParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["CRM_OBJECT_PROPERTY"], PropertyInfo(alias="filterType")]]
    """A string representing the type of filter. Valid value is 'CRM_OBJECT_PROPERTY'."""

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
    """A string indicating the operation to apply for filtering.

    Valid values include 'EQ', 'N_EQ', 'LT', 'GT', 'LTE', 'GTE', 'CONTAINS',
    'STARTS_WITH', 'ENDS_WITH', 'IN', 'NOT_IN', 'IS_EMPTY', and 'IS_NOT_EMPTY'.
    """

    property: Required[str]
    """A string specifying the property of the CRM object to be filtered."""

    value: str
    """
    A string representing the value to compare against the specified property when
    filtering.
    """

    values: SequenceNotStr[str]
    """
    An array of strings, each representing a value to be used in the filtering
    operation.
    """
