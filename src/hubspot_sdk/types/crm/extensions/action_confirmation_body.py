# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActionConfirmationBody"]


class ActionConfirmationBody(BaseModel):
    cancel_button_label: str = FieldInfo(alias="cancelButtonLabel")

    confirm_button_label: str = FieldInfo(alias="confirmButtonLabel")

    prompt: str
