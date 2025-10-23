# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingEventAssociation"]


class MarketingEventAssociation(BaseModel):
    marketing_event_id: str = FieldInfo(alias="marketingEventId")

    name: str

    external_account_id: Optional[str] = FieldInfo(alias="externalAccountId", default=None)

    external_event_id: Optional[str] = FieldInfo(alias="externalEventId", default=None)
