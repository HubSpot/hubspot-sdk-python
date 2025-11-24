# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .display_option import DisplayOption

__all__ = ["CardDisplayProperty"]


class CardDisplayProperty(BaseModel):
    data_type: Literal["BOOLEAN", "CURRENCY", "DATE", "DATETIME", "EMAIL", "LINK", "NUMERIC", "STATUS", "STRING"] = (
        FieldInfo(alias="dataType")
    )
    """Type of data represented by this property."""

    label: str
    """The label for this property as you'd like it displayed to users."""

    name: str
    """An internal identifier for this property. This value must be unique TODO."""

    options: List[DisplayOption]
    """An array of available options that can be displayed.

    Only used in when `dataType` is `STATUS`.
    """
