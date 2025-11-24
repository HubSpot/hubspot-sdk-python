# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FormPostSubmitAction"]


class FormPostSubmitAction(BaseModel):
    type: Literal["redirect_url", "thank_you"]
    """The action to take after submit.

    The default action is displaying a thank you message.
    """

    value: str
    """The thank you text or the page to redirect to."""
