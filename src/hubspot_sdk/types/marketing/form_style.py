# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FormStyle"]


class FormStyle(BaseModel):
    background_width: str = FieldInfo(alias="backgroundWidth")

    font_family: str = FieldInfo(alias="fontFamily")

    help_text_color: str = FieldInfo(alias="helpTextColor")

    help_text_size: str = FieldInfo(alias="helpTextSize")

    label_text_color: str = FieldInfo(alias="labelTextColor")

    label_text_size: str = FieldInfo(alias="labelTextSize")

    legal_consent_text_color: str = FieldInfo(alias="legalConsentTextColor")

    legal_consent_text_size: str = FieldInfo(alias="legalConsentTextSize")

    submit_alignment: Literal["center", "left", "right"] = FieldInfo(alias="submitAlignment")

    submit_color: str = FieldInfo(alias="submitColor")

    submit_font_color: str = FieldInfo(alias="submitFontColor")

    submit_size: str = FieldInfo(alias="submitSize")
