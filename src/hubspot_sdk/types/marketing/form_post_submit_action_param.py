# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FormPostSubmitActionParam"]


class FormPostSubmitActionParam(TypedDict, total=False):
    """What should happen after the customer submits the form."""

    type: Required[Literal["redirect_url", "thank_you"]]
    """The action to take after submit.

    The default action is displaying a thank you message.
    """

    value: Required[str]
    """The thank you text or the page to redirect to."""
