# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["And"]


class And(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["AND"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None
