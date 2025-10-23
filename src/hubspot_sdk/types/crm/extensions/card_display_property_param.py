# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .display_option_param import DisplayOptionParam

__all__ = ["CardDisplayPropertyParam"]


class CardDisplayPropertyParam(TypedDict, total=False):
    data_type: Required[
        Annotated[
            Literal["BOOLEAN", "CURRENCY", "DATE", "DATETIME", "EMAIL", "LINK", "NUMERIC", "STRING", "STATUS"],
            PropertyInfo(alias="dataType"),
        ]
    ]
    """Type of data represented by this property."""

    label: Required[str]
    """The label for this property as you'd like it displayed to users."""

    name: Required[str]
    """An internal identifier for this property. This value must be unique TODO."""

    options: Required[Iterable[DisplayOptionParam]]
    """An array of available options that can be displayed.

    Only used in when `dataType` is `STATUS`.
    """
