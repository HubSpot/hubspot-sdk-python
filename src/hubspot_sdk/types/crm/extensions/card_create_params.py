# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .card_actions_param import CardActionsParam
from .card_fetch_body_param import CardFetchBodyParam
from .card_display_body_param import CardDisplayBodyParam

__all__ = ["CardCreateParams"]


class CardCreateParams(TypedDict, total=False):
    actions: Required[CardActionsParam]
    """Configuration for custom user actions on cards."""

    display: Required[CardDisplayBodyParam]
    """Configuration for displayed info on a card"""

    fetch: Required[CardFetchBodyParam]
    """Configuration for this card's data fetch request."""

    title: Required[str]
    """The top-level title for this card. Displayed to users in the CRM UI."""
