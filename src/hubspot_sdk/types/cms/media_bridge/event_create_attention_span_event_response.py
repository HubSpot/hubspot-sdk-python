# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EventCreateAttentionSpanEventResponse"]


class EventCreateAttentionSpanEventResponse(BaseModel):
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

    media_type: Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"] = FieldInfo(alias="mediaType")

    occurred_timestamp: int = FieldInfo(alias="occurredTimestamp")
    """The timestamp at which this event occurred, in milliseconds since the epoch."""

    percent_range: str = FieldInfo(alias="percentRange")

    portal_id: int = FieldInfo(alias="portalId")
    """The ID of the HubSpot account."""

    provider_id: int = FieldInfo(alias="providerId")

    session_id: str = FieldInfo(alias="sessionId")

    total_percent_played: float = FieldInfo(alias="totalPercentPlayed")
    """The percent of the media that the user consumed.

    Providers may calculate this differently depending on how they consider repeated
    views of the same portion of media. For this reason, the API will not attempt to
    validate totalPercentWatched against the attention span information for the
    event. If it is missing, HubSpot will calculate this from the attention span map
    as follows: (number of spans with a value of 1 or more)/(Total number of spans).
    """

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)

    page_id: Optional[int] = FieldInfo(alias="pageId", default=None)
    """The ID of the page, if hosted on HubSpot. Required for HubSpot pages."""

    page_name: Optional[str] = FieldInfo(alias="pageName", default=None)
    """The name of the page. Required if the page is not hosted on HubSpot."""

    page_object_coordinates: Optional[str] = FieldInfo(alias="pageObjectCoordinates", default=None)

    page_url: Optional[str] = FieldInfo(alias="pageUrl", default=None)
    """The URL of the page that an event happened on.

    Required if the page is not hosted on HubSpot.
    """

    raw_data: Optional[str] = FieldInfo(alias="rawData", default=None)
    """
    This is the raw data which provides the most granular data about spans of the
    media, and how many times each span was consumed by the user. For example, for a
    10 second video where each second is a span, if a visitor watches the first 5
    seconds of the video, then restarts the video and watches the first 2 seconds
    again, the resulting `rawDataString` would be
    `“0=2;1=2;2=1;3=1;4=1;5=0;6=0;7=0;8=0;9=0;”`.
    """

    total_seconds_played: Optional[int] = FieldInfo(alias="totalSecondsPlayed", default=None)
    """The seconds that a user spent consuming the media.

    The media bridge calculates this as `totalPercentPlayed`\\**`mediaDuration`. If a
    provider would like this to be calculated differently, they can provide the
    pre-calculated value when they create the event.
    """
