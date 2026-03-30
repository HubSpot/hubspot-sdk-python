# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SizeParam"]


class SizeParam(TypedDict, total=False):
    units: Required[
        Literal["%", "ch", "cm", "em", "ex", "in", "lh", "mm", "pc", "pt", "px", "Q", "rem", "vh", "vmax", "vmin", "vw"]
    ]

    value: Required[float]
