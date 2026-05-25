# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ArrayFieldSchema"]


class ArrayFieldSchema(BaseModel):
    items: object

    type: Literal["ARRAY"]
    """Specifies that the field is of type 'ARRAY'."""
