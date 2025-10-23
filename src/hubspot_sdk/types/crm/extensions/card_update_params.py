# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .card_actions_param import CardActionsParam
from .card_display_body_param import CardDisplayBodyParam
from .card_fetch_body_patch_param import CardFetchBodyPatchParam

__all__ = ["CardUpdateParams"]


class CardUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    actions: CardActionsParam
    """Configuration for custom user actions on cards."""

    display: CardDisplayBodyParam
    """Configuration for displayed info on a card"""

    fetch: CardFetchBodyPatchParam
    """Variant of CardFetchBody with fields as optional for patches"""

    title: str
    """The top-level title for this card. Displayed to users in the CRM UI."""
