# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MediaPlayedEvent"]


class MediaPlayedEvent(BaseModel):
    contact_id: int = FieldInfo(alias="contactId")

    media_bridge_id: int = FieldInfo(alias="mediaBridgeId")

    media_bridge_object_coordinates: str = FieldInfo(alias="mediaBridgeObjectCoordinates")

    media_bridge_object_type_id: str = FieldInfo(alias="mediaBridgeObjectTypeId")

    media_name: str = FieldInfo(alias="mediaName")

    media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"] = FieldInfo(alias="mediaType")

    occurred_timestamp: int = FieldInfo(alias="occurredTimestamp")

    portal_id: int = FieldInfo(alias="portalId")

    provider_id: int = FieldInfo(alias="providerId")

    session_id: str = FieldInfo(alias="sessionId")

    state: Literal["STARTED", "VIEWED"]

    iframe_url: Optional[str] = FieldInfo(alias="iframeUrl", default=None)

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)

    page_id: Optional[int] = FieldInfo(alias="pageId", default=None)

    page_name: Optional[str] = FieldInfo(alias="pageName", default=None)

    page_object_coordinates: Optional[str] = FieldInfo(alias="pageObjectCoordinates", default=None)

    page_url: Optional[str] = FieldInfo(alias="pageUrl", default=None)
