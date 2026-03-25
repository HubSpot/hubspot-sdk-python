# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .card_actions_param import CardActionsParam
from .card_fetch_body_param import CardFetchBodyParam
from .card_display_body_param import CardDisplayBodyParam

__all__ = ["CardsDevCreateParams"]


class CardsDevCreateParams(TypedDict, total=False):
    actions: Required[CardActionsParam]

    display: Required[CardDisplayBodyParam]

    fetch: Required[CardFetchBodyParam]

    title: Required[str]
    """The top-level title for this card. Displayed to users in the CRM UI."""
