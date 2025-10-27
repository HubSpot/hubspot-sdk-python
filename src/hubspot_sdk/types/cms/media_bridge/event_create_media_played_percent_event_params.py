# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EventCreateMediaPlayedPercentEventParams"]


class EventCreateMediaPlayedPercentEventParams(TypedDict, total=False):
    media_type: Required[
        Annotated[Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"], PropertyInfo(alias="mediaType")]
    ]

    occurred_timestamp: Required[Annotated[int, PropertyInfo(alias="occurredTimestamp")]]

    played_percent: Required[Annotated[int, PropertyInfo(alias="playedPercent")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    _hsenc: str

    contact_id: Annotated[int, PropertyInfo(alias="contactId")]

    contact_utk: Annotated[str, PropertyInfo(alias="contactUtk")]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    media_bridge_id: Annotated[int, PropertyInfo(alias="mediaBridgeId")]

    media_name: Annotated[str, PropertyInfo(alias="mediaName")]

    media_url: Annotated[str, PropertyInfo(alias="mediaUrl")]

    page_id: Annotated[int, PropertyInfo(alias="pageId")]

    page_name: Annotated[str, PropertyInfo(alias="pageName")]

    page_url: Annotated[str, PropertyInfo(alias="pageUrl")]
