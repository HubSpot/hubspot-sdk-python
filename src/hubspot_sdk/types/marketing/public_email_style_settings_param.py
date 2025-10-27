# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_font_style_param import PublicFontStyleParam
from .public_button_style_settings_param import PublicButtonStyleSettingsParam
from .public_divider_style_settings_param import PublicDividerStyleSettingsParam

__all__ = ["PublicEmailStyleSettingsParam"]


class PublicEmailStyleSettingsParam(TypedDict, total=False):
    background_color: Annotated[str, PropertyInfo(alias="backgroundColor")]

    background_image: Annotated[str, PropertyInfo(alias="backgroundImage")]

    background_image_type: Annotated[str, PropertyInfo(alias="backgroundImageType")]

    body_border_color: Annotated[str, PropertyInfo(alias="bodyBorderColor")]

    body_border_color_choice: Annotated[str, PropertyInfo(alias="bodyBorderColorChoice")]

    body_border_width: Annotated[float, PropertyInfo(alias="bodyBorderWidth")]

    body_color: Annotated[str, PropertyInfo(alias="bodyColor")]

    button_style_settings: Annotated[PublicButtonStyleSettingsParam, PropertyInfo(alias="buttonStyleSettings")]

    color_picker_favorite1: Annotated[str, PropertyInfo(alias="colorPickerFavorite1")]

    color_picker_favorite2: Annotated[str, PropertyInfo(alias="colorPickerFavorite2")]

    color_picker_favorite3: Annotated[str, PropertyInfo(alias="colorPickerFavorite3")]

    color_picker_favorite4: Annotated[str, PropertyInfo(alias="colorPickerFavorite4")]

    color_picker_favorite5: Annotated[str, PropertyInfo(alias="colorPickerFavorite5")]

    color_picker_favorite6: Annotated[str, PropertyInfo(alias="colorPickerFavorite6")]

    divider_style_settings: Annotated[PublicDividerStyleSettingsParam, PropertyInfo(alias="dividerStyleSettings")]

    email_body_padding: Annotated[str, PropertyInfo(alias="emailBodyPadding")]

    email_body_width: Annotated[str, PropertyInfo(alias="emailBodyWidth")]

    heading_one_font: Annotated[PublicFontStyleParam, PropertyInfo(alias="headingOneFont")]

    heading_two_font: Annotated[PublicFontStyleParam, PropertyInfo(alias="headingTwoFont")]

    links_font: Annotated[PublicFontStyleParam, PropertyInfo(alias="linksFont")]

    primary_accent_color: Annotated[str, PropertyInfo(alias="primaryAccentColor")]

    primary_font: Annotated[str, PropertyInfo(alias="primaryFont")]

    primary_font_color: Annotated[str, PropertyInfo(alias="primaryFontColor")]

    primary_font_line_height: Annotated[str, PropertyInfo(alias="primaryFontLineHeight")]

    primary_font_size: Annotated[float, PropertyInfo(alias="primaryFontSize")]

    secondary_accent_color: Annotated[str, PropertyInfo(alias="secondaryAccentColor")]

    secondary_font: Annotated[str, PropertyInfo(alias="secondaryFont")]

    secondary_font_color: Annotated[str, PropertyInfo(alias="secondaryFontColor")]

    secondary_font_line_height: Annotated[str, PropertyInfo(alias="secondaryFontLineHeight")]

    secondary_font_size: Annotated[float, PropertyInfo(alias="secondaryFontSize")]
