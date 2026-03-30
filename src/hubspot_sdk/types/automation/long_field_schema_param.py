# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LongFieldSchemaParam"]


class LongFieldSchemaParam(TypedDict, total=False):
    type: Required[Literal["LONG"]]
    """The type of the field, which is LONG by default."""

    maximum: int
    """The maximum value allowed for the long field."""

    minimum: int
    """The minimum value allowed for the long field."""
