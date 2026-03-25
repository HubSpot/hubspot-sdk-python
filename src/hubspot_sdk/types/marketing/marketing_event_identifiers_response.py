# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .app_info import AppInfo
from ..._models import BaseModel

__all__ = ["MarketingEventIdentifiersResponse"]


class MarketingEventIdentifiersResponse(BaseModel):
    external_event_id: str = FieldInfo(alias="externalEventId")
    """
    The ID that is associated with this marketing event in the external event
    application
    """

    marketing_event_name: str = FieldInfo(alias="marketingEventName")
    """The name of the marketing event"""

    object_id: str = FieldInfo(alias="objectId")
    """The internal ID of the marketing event in HubSpot CRM"""

    app_info: Optional[AppInfo] = FieldInfo(alias="appInfo", default=None)

    external_account_id: Optional[str] = FieldInfo(alias="externalAccountId", default=None)
    """
    The accountId that is associated with this marketing event in the external event
    application
    """
