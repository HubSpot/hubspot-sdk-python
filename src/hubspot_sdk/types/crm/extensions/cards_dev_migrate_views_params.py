# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CardsDevMigrateViewsParams"]


class CardsDevMigrateViewsParams(TypedDict, total=False):
    allow_duplicate_app_card_ids: Required[Annotated[bool, PropertyInfo(alias="allowDuplicateAppCardIds")]]

    app_card_id: Required[Annotated[int, PropertyInfo(alias="appCardId")]]

    legacy_crm_card_id: Required[Annotated[int, PropertyInfo(alias="legacyCrmCardId")]]

    helpdesk_app_card_id: Annotated[int, PropertyInfo(alias="helpdeskAppCardId")]
