# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingEventAssociation"]


class MarketingEventAssociation(BaseModel):
    marketing_event_id: str = FieldInfo(alias="marketingEventId")
    """The internal ID of the marketing event in HubSpot"""

    name: str
    """The name of the marketing event in HubSpot"""

    external_account_id: Optional[str] = FieldInfo(alias="externalAccountId", default=None)
    """
    The account ID that is associated with this marketing event in the external
    event application
    """

    external_event_id: Optional[str] = FieldInfo(alias="externalEventId", default=None)
    """
    The event ID that is associated with this marketing event in the external event
    application
    """
