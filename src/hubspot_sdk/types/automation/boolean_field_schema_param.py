# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BooleanFieldSchemaParam"]


class BooleanFieldSchemaParam(TypedDict, total=False):
    type: Required[Literal["ARRAY", "BOOLEAN", "DOUBLE", "INTEGER", "LONG", "OBJECT", "STRING"]]
    """
    Specifies the field type as BOOLEAN, indicating that the field can hold a true
    or false value.
    """
