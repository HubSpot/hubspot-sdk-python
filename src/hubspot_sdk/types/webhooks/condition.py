# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Condition"]


class Condition(BaseModel):
    filter_type: Literal["CRM_OBJECT_PROPERTY"] = FieldInfo(alias="filterType")
    """A string representing the type of filter. Valid value is 'CRM_OBJECT_PROPERTY'."""

    operator: Literal[
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
    """A string indicating the operation to apply for filtering.

    Valid values include 'EQ', 'N_EQ', 'LT', 'GT', 'LTE', 'GTE', 'CONTAINS',
    'STARTS_WITH', 'ENDS_WITH', 'IN', 'NOT_IN', 'IS_EMPTY', and 'IS_NOT_EMPTY'.
    """

    property: str
    """A string specifying the property of the CRM object to be filtered."""

    value: Optional[str] = None
    """
    A string representing the value to compare against the specified property when
    filtering.
    """

    values: Optional[List[str]] = None
    """
    An array of strings, each representing a value to be used in the filtering
    operation.
    """
