# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .form_style_param import FormStyleParam

__all__ = ["FormDisplayOptionsParam"]


class FormDisplayOptionsParam(TypedDict, total=False):
    """Options for styling the form."""

    render_raw_html: Required[Annotated[bool, PropertyInfo(alias="renderRawHtml")]]
    """Whether the form will render as raw HTML as opposed to inside an iFrame."""

    style: Required[FormStyleParam]
    """Styling options for the form"""

    submit_button_text: Required[Annotated[str, PropertyInfo(alias="submitButtonText")]]
    """The text displayed on the form submit button."""

    theme: Required[Literal["canvas", "default_style", "legacy", "linear", "round", "sharp"]]
    """The theme used for styling the input fields.

    This will not apply if the form is added to a HubSpot CMS page.
    """

    css_class: Annotated[str, PropertyInfo(alias="cssClass")]
