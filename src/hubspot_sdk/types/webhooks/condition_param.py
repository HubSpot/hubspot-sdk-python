# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ConditionParam"]


class ConditionParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["CRM_OBJECT_PROPERTY"], PropertyInfo(alias="filterType")]]

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

    property: Required[str]

    value: str

    values: SequenceNotStr[str]
