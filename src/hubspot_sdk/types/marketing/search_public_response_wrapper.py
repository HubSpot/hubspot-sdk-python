# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SearchPublicResponseWrapper"]


class SearchPublicResponseWrapper(BaseModel):
    app_id: int = FieldInfo(alias="appId")
    """The ID of the source application of the marketing event"""

    external_account_id: str = FieldInfo(alias="externalAccountId")
    """The account ID associated with this marketing event in the external application"""

    external_event_id: str = FieldInfo(alias="externalEventId")
    """The ID of the marketing event in the external event application"""

    object_id: str = FieldInfo(alias="objectId")
    """The internal ID of the marketing event in HubSpot"""
