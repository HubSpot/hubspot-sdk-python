# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Angle"]


class Angle(BaseModel):
    units: Literal["DEGREES", "GRADIANS", "RADIANS", "TURNS"]
    """The unit of measurement for the angle."""

    value: float
    """The numerical representation of the angle."""
