# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DoubleFieldSchema"]


class DoubleFieldSchema(BaseModel):
    type: Literal["DOUBLE"]
    """Indicates the field type as DOUBLE."""

    maximum: Optional[float] = None
    """The maximum allowable value for the double field."""

    minimum: Optional[float] = None
    """The minimum allowable value for the double field."""
