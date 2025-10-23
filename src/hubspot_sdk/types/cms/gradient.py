# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .angle import Angle
from ..._models import BaseModel
from .color_stop import ColorStop
from .side_or_corner import SideOrCorner

__all__ = ["Gradient"]


class Gradient(BaseModel):
    angle: Angle

    colors: List[ColorStop]

    side_or_corner: SideOrCorner = FieldInfo(alias="sideOrCorner")
