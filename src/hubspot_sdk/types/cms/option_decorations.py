# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OptionDecorations"]


class OptionDecorations(BaseModel):
    color: Literal[
        "BLACK",
        "BLUE",
        "BLUE_LIGHT",
        "GRAY",
        "GREEN",
        "GREEN_LIGHT",
        "ORANGE",
        "ORANGE_LIGHT",
        "PINK",
        "PINK_LIGHT",
        "PURPLE",
        "PURPLE_LIGHT",
        "RED",
        "RED_LIGHT",
        "TEAL",
        "TEAL_LIGHT",
        "YELLOW",
        "YELLOW_LIGHT",
    ]
