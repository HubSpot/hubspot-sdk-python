# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .form_style import FormStyle

__all__ = ["FormDisplayOptions"]


class FormDisplayOptions(BaseModel):
    render_raw_html: bool = FieldInfo(alias="renderRawHtml")
    """Whether the form will render as raw HTML as opposed to inside an iFrame."""

    style: FormStyle
    """Styling options for the form"""

    submit_button_text: str = FieldInfo(alias="submitButtonText")
    """The text displayed on the form submit button."""

    theme: Literal["canvas", "default_style", "legacy", "linear", "round", "sharp"]
    """The theme used for styling the input fields.

    This will not apply if the form is added to a HubSpot CMS page.
    """

    css_class: Optional[str] = FieldInfo(alias="cssClass", default=None)
