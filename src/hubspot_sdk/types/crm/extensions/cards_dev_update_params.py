# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .card_actions_param import CardActionsParam
from .card_display_body_param import CardDisplayBodyParam
from .card_fetch_body_patch_param import CardFetchBodyPatchParam

__all__ = ["CardsDevUpdateParams"]


class CardsDevUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    actions: CardActionsParam

    display: CardDisplayBodyParam

    fetch: CardFetchBodyPatchParam

    title: str
    """The top-level title for this card. Displayed to users in the CRM UI."""
