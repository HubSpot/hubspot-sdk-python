# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["FileColumn"]


class FileColumn(BaseModel):
    name: str
    """The name of the column, represented as a string."""

    type: str
    """The data type of the column, represented as a string."""
