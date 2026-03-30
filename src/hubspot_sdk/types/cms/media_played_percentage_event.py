# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MediaPlayedPercentageEvent"]


class MediaPlayedPercentageEvent(BaseModel):
    contact_id: int = FieldInfo(alias="contactId")
    """The ID of the contact in HubSpot’s system that consumed the media.

    This can be fetched using HubSpot's Get contact by usertoken (utk) API. The API
    also supports supplying a usertoken, and will handle converting this into a
    contact ID automatically.
    """

    media_bridge_id: int = FieldInfo(alias="mediaBridgeId")

    media_bridge_object_coordinates: str = FieldInfo(alias="mediaBridgeObjectCoordinates")

    media_bridge_object_type_id: str = FieldInfo(alias="mediaBridgeObjectTypeId")

    media_name: str = FieldInfo(alias="mediaName")

    media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"] = FieldInfo(alias="mediaType")

    occurred_timestamp: int = FieldInfo(alias="occurredTimestamp")

    played_percent: int = FieldInfo(alias="playedPercent")

    portal_id: int = FieldInfo(alias="portalId")
    """The ID of the HubSpot account."""

    provider_id: int = FieldInfo(alias="providerId")

    session_id: str = FieldInfo(alias="sessionId")

    external_play_context: Optional[Literal["EMAIL", "EXTERNAL_PAGE"]] = FieldInfo(
        alias="externalPlayContext", default=None
    )

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)

    page_id: Optional[int] = FieldInfo(alias="pageId", default=None)
    """The content ID of the page that an event happened on, for HubSpot pages.

    Required if the page is a HubSpot page.
    """

    page_name: Optional[str] = FieldInfo(alias="pageName", default=None)
    """The name or title of the page that an event happened on.

    Required for non-HubSpot pages.
    """

    page_object_coordinates: Optional[str] = FieldInfo(alias="pageObjectCoordinates", default=None)

    page_url: Optional[str] = FieldInfo(alias="pageUrl", default=None)
    """The URL of the page that an event happened on. Required for non-HubSpot pages."""
