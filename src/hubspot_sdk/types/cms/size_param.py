# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SizeParam"]


class SizeParam(TypedDict, total=False):
    units: Required[
        Literal[
            "CH",
            "CM",
            "EM",
            "EX",
            "IN",
            "LH",
            "MM",
            "PC",
            "PERCENTAGE",
            "PT",
            "PX",
            "Q",
            "REM",
            "VH",
            "VMAX",
            "VMIN",
            "VW",
        ]
    ]

    value: Required[float]
