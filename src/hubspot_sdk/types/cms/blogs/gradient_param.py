# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .angle_param import AngleParam
from .color_stop_param import ColorStopParam
from .side_or_corner_param import SideOrCornerParam

__all__ = ["GradientParam"]


class GradientParam(TypedDict, total=False):
    angle: Required[AngleParam]

    colors: Required[Iterable[ColorStopParam]]

    side_or_corner: Required[Annotated[SideOrCornerParam, PropertyInfo(alias="sideOrCorner")]]
