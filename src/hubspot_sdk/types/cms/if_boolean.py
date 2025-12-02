# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IfBoolean"]


class IfBoolean(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: "Expression" = FieldInfo(alias="ifExpression")

    operator: Literal["IF_BOOLEAN"]

    else_expression: Optional["Expression"] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List["Expression"]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


from .expression import Expression
