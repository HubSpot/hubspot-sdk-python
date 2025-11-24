# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DependentFieldFilterParam"]


class DependentFieldFilterParam(TypedDict, total=False):
    operator: Required[
        Literal[
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
    ]

    range_end: Required[Annotated[str, PropertyInfo(alias="rangeEnd")]]

    range_start: Required[Annotated[str, PropertyInfo(alias="rangeStart")]]

    value: Required[str]

    values: Required[SequenceNotStr[str]]
