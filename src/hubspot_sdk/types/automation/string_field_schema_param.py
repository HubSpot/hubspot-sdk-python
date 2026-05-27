# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StringFieldSchemaParam"]


class StringFieldSchemaParam(TypedDict, total=False):
    type: Required[Literal["STRING"]]
    """Indicates that the type is a string, with the default value being STRING."""

    format: Literal["DATE", "DATE_TIME", "OBJECT_COORDINATE", "TIME", "URI"]
    """
    Specifies the format of the string, with accepted values: DATE, DATE_TIME,
    OBJECT_COORDINATE, TIME, URI.
    """
