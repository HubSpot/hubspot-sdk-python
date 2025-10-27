# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_font_style import PublicFontStyle

__all__ = ["PublicButtonStyleSettings"]


class PublicButtonStyleSettings(BaseModel):
    background_color: Optional[object] = FieldInfo(alias="backgroundColor", default=None)

    corner_radius: Optional[int] = FieldInfo(alias="cornerRadius", default=None)

    font_style: Optional[PublicFontStyle] = FieldInfo(alias="fontStyle", default=None)
