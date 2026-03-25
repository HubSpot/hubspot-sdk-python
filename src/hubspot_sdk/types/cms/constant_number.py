# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConstantNumber"]


class ConstantNumber(BaseModel):
    operator: Literal["CONSTANT_NUMBER"]

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None
