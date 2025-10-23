# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .app_info import AppInfo
from ..._models import BaseModel

__all__ = ["MarketingEventIdentifiersResponse"]


class MarketingEventIdentifiersResponse(BaseModel):
    external_event_id: str = FieldInfo(alias="externalEventId")

    marketing_event_name: str = FieldInfo(alias="marketingEventName")

    object_id: str = FieldInfo(alias="objectId")

    app_info: Optional[AppInfo] = FieldInfo(alias="appInfo", default=None)

    external_account_id: Optional[str] = FieldInfo(alias="externalAccountId", default=None)
