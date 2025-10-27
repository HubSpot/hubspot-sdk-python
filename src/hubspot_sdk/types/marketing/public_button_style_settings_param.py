# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_font_style_param import PublicFontStyleParam

__all__ = ["PublicButtonStyleSettingsParam"]


class PublicButtonStyleSettingsParam(TypedDict, total=False):
    background_color: Annotated[object, PropertyInfo(alias="backgroundColor")]

    corner_radius: Annotated[int, PropertyInfo(alias="cornerRadius")]

    font_style: Annotated[PublicFontStyleParam, PropertyInfo(alias="fontStyle")]
