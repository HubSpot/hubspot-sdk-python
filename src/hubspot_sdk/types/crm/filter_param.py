# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["FilterParam"]


class FilterParam(TypedDict, total=False):
    operator: Required[
        Literal[
            "BETWEEN",
            "CONTAINS_TOKEN",
            "EQ",
            "GT",
            "GTE",
            "HAS_PROPERTY",
            "IN",
            "LT",
            "LTE",
            "NEQ",
            "NOT_CONTAINS_TOKEN",
            "NOT_HAS_PROPERTY",
            "NOT_IN",
        ]
    ]
    """The comparison operator used in the filter, such as "EQ" or "GT"."""

    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]
    """The name of the property to apply the filter to."""

    high_value: Annotated[str, PropertyInfo(alias="highValue")]
    """The upper boundary value when using ranged-based filters."""

    value: str
    """The value to match against the property."""

    values: SequenceNotStr[str]
    """The values to match against the property."""
