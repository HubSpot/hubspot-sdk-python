# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .condition import Condition

__all__ = ["Filter"]


class Filter(BaseModel):
    """
    Defines a single condition for searching CRM objects, specifying the property to filter on, the operator to use (such as equals, greater than, or contains), and the value(s) to compare against.
    """

    conditions: List[Condition]
