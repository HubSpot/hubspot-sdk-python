# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Size"]


class Size(BaseModel):
    units: Literal[
        "%", "ch", "cm", "em", "ex", "in", "lh", "mm", "pc", "pt", "px", "Q", "rem", "vh", "vmax", "vmin", "vw"
    ]

    value: float
