# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ObjectToken"]


class ObjectToken(BaseModel):
    value: str
    """The value of the property"""

    data_type: Optional[
        Literal["BOOLEAN", "CURRENCY", "DATE", "DATETIME", "EMAIL", "LINK", "NUMERIC", "STATUS", "STRING"]
    ] = FieldInfo(alias="dataType", default=None)
    """Type of data represented by this property."""

    label: Optional[str] = None
    """The label for this property as you'd like it displayed to users."""

    name: Optional[str] = None
    """An internal identifier for this property. This value must be unique TODO."""
