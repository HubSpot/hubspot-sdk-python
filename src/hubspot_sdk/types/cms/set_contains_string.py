# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SetContainsString"]


class SetContainsString(BaseModel):
    operator: Literal["SET_CONTAINS_STRING"]

    string_to_check: "Expression" = FieldInfo(alias="stringToCheck")

    inputs: Optional[List["Expression"]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


from .expression import Expression
