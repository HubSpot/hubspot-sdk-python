# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ObjectFieldSchemaParam"]


class ObjectFieldSchemaParam(TypedDict, total=False):
    properties: Required[object]
    """Contains the properties of the object."""

    type: Required[Literal["ARRAY", "BOOLEAN", "DOUBLE", "INTEGER", "LONG", "OBJECT", "STRING"]]
    """Specifies the type of the field, which is 'OBJECT' by default."""
