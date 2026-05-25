# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .condition import Condition

__all__ = ["Filter"]


class Filter(TypedDict, total=False):
    """
    Defines a single condition for searching CRM objects, specifying the property to filter on, the operator to use (such as equals, greater than, or contains), and the value(s) to compare against.
    """

    conditions: Required[Iterable[Condition]]
    """An array of conditions that define the criteria for the filter.

    Each condition specifies a property, an operator, and optionally a value or
    values.
    """
