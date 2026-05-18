# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Size"]


class Size(BaseModel):
    units: Literal[
        "CH", "CM", "EM", "EX", "IN", "LH", "MM", "PC", "PERCENTAGE", "PT", "PX", "Q", "REM", "VH", "VMAX", "VMIN", "VW"
    ]

    value: float
