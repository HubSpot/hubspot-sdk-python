# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Condition"]


class Condition(BaseModel):
    filter_type: Literal["CRM_OBJECT_PROPERTY"] = FieldInfo(alias="filterType")

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

    property: str

    value: Optional[str] = None

    values: Optional[List[str]] = None
