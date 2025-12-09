# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DependentFieldFilter"]


class DependentFieldFilter(BaseModel):
    """A condition based on customer input"""

    operator: Literal[
        "between",
        "contains",
        "doesnt_contain",
        "eq",
        "gt",
        "gte",
        "is_not_empty",
        "lt",
        "lte",
        "neq",
        "not_between",
        "set_all",
        "set_any",
        "set_eq",
        "set_neq",
        "set_not_all",
        "set_not_any",
        "str_ends_with",
        "str_starts_with",
        "within_time",
        "within_time_reverse",
    ]

    range_end: str = FieldInfo(alias="rangeEnd")

    range_start: str = FieldInfo(alias="rangeStart")

    value: str

    values: List[str]
