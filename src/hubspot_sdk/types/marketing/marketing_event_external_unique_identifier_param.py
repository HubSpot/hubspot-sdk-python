# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketingEventExternalUniqueIdentifierParam"]


class MarketingEventExternalUniqueIdentifierParam(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]
    """The id of the application that created the marketing event in HubSpot."""

    external_account_id: Required[Annotated[str, PropertyInfo(alias="externalAccountId")]]
    """
    The accountId that is associated with this marketing event in the external event
    application.
    """

    external_event_id: Required[Annotated[str, PropertyInfo(alias="externalEventId")]]
    """The id of the marketing event in the external event application."""
