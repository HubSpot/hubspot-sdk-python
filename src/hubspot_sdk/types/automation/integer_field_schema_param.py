# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IntegerFieldSchemaParam"]


class IntegerFieldSchemaParam(TypedDict, total=False):
    type: Required[Literal["INTEGER"]]
    """The type of the field, which is set to INTEGER."""

    maximum: int
    """The maximum value allowed for the integer field."""

    minimum: int
    """The minimum value allowed for the integer field."""
