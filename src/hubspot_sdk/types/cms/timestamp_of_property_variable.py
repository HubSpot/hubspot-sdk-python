# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TimestampOfPropertyVariable"]


class TimestampOfPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_PROPERTY_VARIABLE"]

    inputs: Optional[List["Expression"]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


from .expression import Expression
