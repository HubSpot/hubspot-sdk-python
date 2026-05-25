# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DoubleFieldSchemaParam"]


class DoubleFieldSchemaParam(TypedDict, total=False):
    type: Required[Literal["DOUBLE"]]
    """Indicates the field type as DOUBLE."""

    maximum: float
    """The maximum allowable value for the double field."""

    minimum: float
    """The minimum allowable value for the double field."""
