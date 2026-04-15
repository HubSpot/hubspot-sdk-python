# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .condition_param import ConditionParam

__all__ = ["FilterParam"]


class FilterParam(TypedDict, total=False):
    """
    Defines a single condition for searching CRM objects, specifying the property to filter on, the operator to use (such as equals, greater than, or contains), and the value(s) to compare against.
    """

    conditions: Required[Iterable[ConditionParam]]
    """An array of conditions that define the filter criteria.

    Each condition specifies a property, operator, and value to determine if a data
    item meets the filter requirements.
    """
