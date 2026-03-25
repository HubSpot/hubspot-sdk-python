# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .gradient_param import GradientParam
from .rgba_color_param import RgbaColorParam
from .background_image_param import BackgroundImageParam
from .breakpoint_styles_param import BreakpointStylesParam

__all__ = ["StylesParam"]


class StylesParam(TypedDict, total=False):
    background_color: Required[Annotated[RgbaColorParam, PropertyInfo(alias="backgroundColor")]]

    background_gradient: Required[Annotated[GradientParam, PropertyInfo(alias="backgroundGradient")]]

    background_image: Required[Annotated[BackgroundImageParam, PropertyInfo(alias="backgroundImage")]]

    flexbox_positioning: Required[
        Annotated[
            Literal[
                "BOTTOM_CENTER",
                "BOTTOM_LEFT",
                "BOTTOM_RIGHT",
                "MIDDLE_CENTER",
                "MIDDLE_LEFT",
                "MIDDLE_RIGHT",
                "TOP_CENTER",
                "TOP_LEFT",
                "TOP_RIGHT",
            ],
            PropertyInfo(alias="flexboxPositioning"),
        ]
    ]
    """Indicates whether flexbox positioning is enabled for the section."""

    force_full_width_section: Required[Annotated[bool, PropertyInfo(alias="forceFullWidthSection")]]
    """Determines if the section should be forced to full width."""

    max_width_section_centering: Required[Annotated[int, PropertyInfo(alias="maxWidthSectionCentering")]]
    """Defines the maximum width for centering the section."""

    vertical_alignment: Required[Annotated[Literal["BOTTOM", "MIDDLE", "TOP"], PropertyInfo(alias="verticalAlignment")]]
    """Specifies the vertical alignment of elements within the section."""

    breakpoint_styles: Annotated[Dict[str, BreakpointStylesParam], PropertyInfo(alias="breakpointStyles")]
    """Breakpoint CSS styles for margin, padding, etc..."""
