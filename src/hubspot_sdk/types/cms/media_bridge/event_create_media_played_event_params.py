# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EventCreateMediaPlayedEventParams"]


class EventCreateMediaPlayedEventParams(TypedDict, total=False):
    media_type: Required[
        Annotated[Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"], PropertyInfo(alias="mediaType")]
    ]

    occurred_timestamp: Required[Annotated[int, PropertyInfo(alias="occurredTimestamp")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    state: Required[Literal["STARTED", "VIEWED"]]

    _hsenc: str

    contact_id: Annotated[int, PropertyInfo(alias="contactId")]

    contact_utk: Annotated[str, PropertyInfo(alias="contactUtk")]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    iframe_url: Annotated[str, PropertyInfo(alias="iframeUrl")]

    media_bridge_id: Annotated[int, PropertyInfo(alias="mediaBridgeId")]

    media_name: Annotated[str, PropertyInfo(alias="mediaName")]

    media_url: Annotated[str, PropertyInfo(alias="mediaUrl")]

    page_id: Annotated[int, PropertyInfo(alias="pageId")]

    page_name: Annotated[str, PropertyInfo(alias="pageName")]

    page_url: Annotated[str, PropertyInfo(alias="pageUrl")]
