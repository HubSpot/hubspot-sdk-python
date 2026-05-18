# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ArrayFieldSchemaParam"]


class ArrayFieldSchemaParam(TypedDict, total=False):
    items: Required[object]

    type: Required[Literal["ARRAY", "BOOLEAN", "DOUBLE", "INTEGER", "LONG", "OBJECT", "STRING"]]
    """Specifies that the field is of type 'ARRAY'."""
