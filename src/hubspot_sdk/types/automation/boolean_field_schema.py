# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BooleanFieldSchema"]


class BooleanFieldSchema(BaseModel):
    type: Literal["BOOLEAN"]
    """
    Specifies the field type as BOOLEAN, indicating that the field can hold a true
    or false value.
    """
