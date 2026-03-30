# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .rgba_color import RgbaColor

__all__ = ["ColorStop"]


class ColorStop(BaseModel):
    color: RgbaColor
