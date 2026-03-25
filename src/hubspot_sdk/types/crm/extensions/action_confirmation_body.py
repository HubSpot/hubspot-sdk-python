# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActionConfirmationBody"]


class ActionConfirmationBody(BaseModel):
    cancel_button_label: str = FieldInfo(alias="cancelButtonLabel")
    """The label for the button that cancels the action."""

    confirm_button_label: str = FieldInfo(alias="confirmButtonLabel")
    """The label for the button that confirms the action."""

    prompt: str
    """The message displayed to the user to confirm the action."""
