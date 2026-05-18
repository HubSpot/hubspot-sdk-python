# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LongFieldSchema"]


class LongFieldSchema(BaseModel):
    type: Literal["ARRAY", "BOOLEAN", "DOUBLE", "INTEGER", "LONG", "OBJECT", "STRING"]
    """The type of the field, which is LONG by default."""

    maximum: Optional[int] = None
    """The maximum value allowed for the long field."""

    minimum: Optional[int] = None
    """The minimum value allowed for the long field."""
