# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_font_style import PublicFontStyle
from .public_button_style_settings import PublicButtonStyleSettings
from .public_divider_style_settings import PublicDividerStyleSettings

__all__ = ["PublicEmailStyleSettings"]


class PublicEmailStyleSettings(BaseModel):
    background_color: Optional[str] = FieldInfo(alias="backgroundColor", default=None)

    background_image: Optional[str] = FieldInfo(alias="backgroundImage", default=None)

    background_image_type: Optional[str] = FieldInfo(alias="backgroundImageType", default=None)

    body_border_color: Optional[str] = FieldInfo(alias="bodyBorderColor", default=None)

    body_border_color_choice: Optional[str] = FieldInfo(alias="bodyBorderColorChoice", default=None)

    body_border_width: Optional[float] = FieldInfo(alias="bodyBorderWidth", default=None)

    body_color: Optional[str] = FieldInfo(alias="bodyColor", default=None)

    button_style_settings: Optional[PublicButtonStyleSettings] = FieldInfo(alias="buttonStyleSettings", default=None)

    color_picker_favorite1: Optional[str] = FieldInfo(alias="colorPickerFavorite1", default=None)

    color_picker_favorite2: Optional[str] = FieldInfo(alias="colorPickerFavorite2", default=None)

    color_picker_favorite3: Optional[str] = FieldInfo(alias="colorPickerFavorite3", default=None)

    color_picker_favorite4: Optional[str] = FieldInfo(alias="colorPickerFavorite4", default=None)

    color_picker_favorite5: Optional[str] = FieldInfo(alias="colorPickerFavorite5", default=None)

    color_picker_favorite6: Optional[str] = FieldInfo(alias="colorPickerFavorite6", default=None)

    divider_style_settings: Optional[PublicDividerStyleSettings] = FieldInfo(alias="dividerStyleSettings", default=None)

    email_body_padding: Optional[str] = FieldInfo(alias="emailBodyPadding", default=None)

    email_body_width: Optional[str] = FieldInfo(alias="emailBodyWidth", default=None)

    heading_one_font: Optional[PublicFontStyle] = FieldInfo(alias="headingOneFont", default=None)

    heading_two_font: Optional[PublicFontStyle] = FieldInfo(alias="headingTwoFont", default=None)

    links_font: Optional[PublicFontStyle] = FieldInfo(alias="linksFont", default=None)

    primary_accent_color: Optional[str] = FieldInfo(alias="primaryAccentColor", default=None)

    primary_font: Optional[str] = FieldInfo(alias="primaryFont", default=None)

    primary_font_color: Optional[str] = FieldInfo(alias="primaryFontColor", default=None)

    primary_font_line_height: Optional[str] = FieldInfo(alias="primaryFontLineHeight", default=None)

    primary_font_size: Optional[float] = FieldInfo(alias="primaryFontSize", default=None)

    secondary_accent_color: Optional[str] = FieldInfo(alias="secondaryAccentColor", default=None)

    secondary_font: Optional[str] = FieldInfo(alias="secondaryFont", default=None)

    secondary_font_color: Optional[str] = FieldInfo(alias="secondaryFontColor", default=None)

    secondary_font_line_height: Optional[str] = FieldInfo(alias="secondaryFontLineHeight", default=None)

    secondary_font_size: Optional[float] = FieldInfo(alias="secondaryFontSize", default=None)
