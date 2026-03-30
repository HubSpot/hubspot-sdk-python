# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .gradient import Gradient
from ..._models import BaseModel
from .rgba_color import RgbaColor
from .background_image import BackgroundImage
from .breakpoint_styles import BreakpointStyles

__all__ = ["Styles"]


class Styles(BaseModel):
    background_color: RgbaColor = FieldInfo(alias="backgroundColor")

    background_gradient: Gradient = FieldInfo(alias="backgroundGradient")

    background_image: BackgroundImage = FieldInfo(alias="backgroundImage")

    flexbox_positioning: Literal[
        "BOTTOM_CENTER",
        "BOTTOM_LEFT",
        "BOTTOM_RIGHT",
        "MIDDLE_CENTER",
        "MIDDLE_LEFT",
        "MIDDLE_RIGHT",
        "TOP_CENTER",
        "TOP_LEFT",
        "TOP_RIGHT",
    ] = FieldInfo(alias="flexboxPositioning")
    """Indicates whether flexbox positioning is enabled for the section."""

    force_full_width_section: bool = FieldInfo(alias="forceFullWidthSection")
    """Determines if the section should be forced to full width."""

    max_width_section_centering: int = FieldInfo(alias="maxWidthSectionCentering")
    """Defines the maximum width for centering the section."""

    vertical_alignment: Literal["BOTTOM", "MIDDLE", "TOP"] = FieldInfo(alias="verticalAlignment")
    """Specifies the vertical alignment of elements within the section."""

    breakpoint_styles: Optional[Dict[str, BreakpointStyles]] = FieldInfo(alias="breakpointStyles", default=None)
    """Breakpoint CSS styles for margin, padding, etc..."""
