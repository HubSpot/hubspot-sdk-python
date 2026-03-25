# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PublicFontStyleParam"]


class PublicFontStyleParam(TypedDict, total=False):
    bold: bool

    color: str

    font: str

    italic: bool

    size: int

    underline: bool
