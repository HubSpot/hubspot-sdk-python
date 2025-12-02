# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubtractNumbers"]


class SubtractNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["SUBTRACT_NUMBERS"]

    inputs: Optional[List["Expression"]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


from .expression import Expression
