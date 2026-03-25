# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConstantString"]


class ConstantString(BaseModel):
    operator: Literal["CONSTANT_STRING"]

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None
