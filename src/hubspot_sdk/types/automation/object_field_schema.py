# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ObjectFieldSchema"]


class ObjectFieldSchema(BaseModel):
    properties: object
    """Contains the properties of the object."""

    type: Literal["OBJECT"]
    """Specifies the type of the field, which is 'OBJECT' by default."""
