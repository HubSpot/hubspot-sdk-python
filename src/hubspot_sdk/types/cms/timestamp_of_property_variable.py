# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TimestampOfPropertyVariable"]


class TimestampOfPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_PROPERTY_VARIABLE"]

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None
