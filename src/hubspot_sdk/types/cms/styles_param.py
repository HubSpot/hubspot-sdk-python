# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .gradient_param import GradientParam
from .rgba_color_param import RgbaColorParam
from .background_image_param import BackgroundImageParam
from .breakpoint_styles_param import BreakpointStylesParam

__all__ = ["StylesParam"]


class StylesParam(TypedDict, total=False):
    background_color: Required[Annotated[RgbaColorParam, PropertyInfo(alias="backgroundColor")]]
    """A color defined by RGB values."""

    background_gradient: Required[Annotated[GradientParam, PropertyInfo(alias="backgroundGradient")]]

    background_image: Required[Annotated[BackgroundImageParam, PropertyInfo(alias="backgroundImage")]]

    flexbox_positioning: Required[Annotated[str, PropertyInfo(alias="flexboxPositioning")]]

    force_full_width_section: Required[Annotated[bool, PropertyInfo(alias="forceFullWidthSection")]]

    max_width_section_centering: Required[Annotated[int, PropertyInfo(alias="maxWidthSectionCentering")]]

    vertical_alignment: Required[Annotated[str, PropertyInfo(alias="verticalAlignment")]]

    breakpoint_styles: Annotated[Dict[str, BreakpointStylesParam], PropertyInfo(alias="breakpointStyles")]
