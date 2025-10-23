# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .gradient import Gradient
from ..._models import BaseModel
from .rgba_color import RgbaColor
from .background_image import BackgroundImage
from .blogs.breakpoint_styles import BreakpointStyles

__all__ = ["Styles"]


class Styles(BaseModel):
    background_color: RgbaColor = FieldInfo(alias="backgroundColor")
    """A color defined by RGB values."""

    background_gradient: Gradient = FieldInfo(alias="backgroundGradient")

    background_image: BackgroundImage = FieldInfo(alias="backgroundImage")

    flexbox_positioning: str = FieldInfo(alias="flexboxPositioning")

    force_full_width_section: bool = FieldInfo(alias="forceFullWidthSection")

    max_width_section_centering: int = FieldInfo(alias="maxWidthSectionCentering")

    vertical_alignment: str = FieldInfo(alias="verticalAlignment")

    breakpoint_styles: Optional[Dict[str, BreakpointStyles]] = FieldInfo(alias="breakpointStyles", default=None)
