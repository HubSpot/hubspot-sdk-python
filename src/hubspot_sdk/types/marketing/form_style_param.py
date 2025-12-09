# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FormStyleParam"]


class FormStyleParam(TypedDict, total=False):
    """Styling options for the form"""

    background_width: Required[Annotated[str, PropertyInfo(alias="backgroundWidth")]]

    font_family: Required[Annotated[str, PropertyInfo(alias="fontFamily")]]

    help_text_color: Required[Annotated[str, PropertyInfo(alias="helpTextColor")]]

    help_text_size: Required[Annotated[str, PropertyInfo(alias="helpTextSize")]]

    label_text_color: Required[Annotated[str, PropertyInfo(alias="labelTextColor")]]

    label_text_size: Required[Annotated[str, PropertyInfo(alias="labelTextSize")]]

    legal_consent_text_color: Required[Annotated[str, PropertyInfo(alias="legalConsentTextColor")]]

    legal_consent_text_size: Required[Annotated[str, PropertyInfo(alias="legalConsentTextSize")]]

    submit_alignment: Required[Annotated[Literal["center", "left", "right"], PropertyInfo(alias="submitAlignment")]]

    submit_color: Required[Annotated[str, PropertyInfo(alias="submitColor")]]

    submit_font_color: Required[Annotated[str, PropertyInfo(alias="submitFontColor")]]

    submit_size: Required[Annotated[str, PropertyInfo(alias="submitSize")]]
