# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IntegerFieldSchema"]


class IntegerFieldSchema(BaseModel):
    type: Literal["INTEGER"]
    """The type of the field, which is set to INTEGER."""

    maximum: Optional[int] = None
    """The maximum value allowed for the integer field."""

    minimum: Optional[int] = None
    """The minimum value allowed for the integer field."""
