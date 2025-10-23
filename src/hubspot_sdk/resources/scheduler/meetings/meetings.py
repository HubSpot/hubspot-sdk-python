# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .calendar import (
    CalendarResource,
    AsyncCalendarResource,
    CalendarResourceWithRawResponse,
    AsyncCalendarResourceWithRawResponse,
    CalendarResourceWithStreamingResponse,
    AsyncCalendarResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .meetings_links import (
    MeetingsLinksResource,
    AsyncMeetingsLinksResource,
    MeetingsLinksResourceWithRawResponse,
    AsyncMeetingsLinksResourceWithRawResponse,
    MeetingsLinksResourceWithStreamingResponse,
    AsyncMeetingsLinksResourceWithStreamingResponse,
)

__all__ = ["MeetingsResource", "AsyncMeetingsResource"]


class MeetingsResource(SyncAPIResource):
    @cached_property
    def calendar(self) -> CalendarResource:
        return CalendarResource(self._client)

    @cached_property
    def meetings_links(self) -> MeetingsLinksResource:
        return MeetingsLinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeetingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MeetingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeetingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MeetingsResourceWithStreamingResponse(self)


class AsyncMeetingsResource(AsyncAPIResource):
    @cached_property
    def calendar(self) -> AsyncCalendarResource:
        return AsyncCalendarResource(self._client)

    @cached_property
    def meetings_links(self) -> AsyncMeetingsLinksResource:
        return AsyncMeetingsLinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeetingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeetingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeetingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMeetingsResourceWithStreamingResponse(self)


class MeetingsResourceWithRawResponse:
    def __init__(self, meetings: MeetingsResource) -> None:
        self._meetings = meetings

    @cached_property
    def calendar(self) -> CalendarResourceWithRawResponse:
        return CalendarResourceWithRawResponse(self._meetings.calendar)

    @cached_property
    def meetings_links(self) -> MeetingsLinksResourceWithRawResponse:
        return MeetingsLinksResourceWithRawResponse(self._meetings.meetings_links)


class AsyncMeetingsResourceWithRawResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

    @cached_property
    def calendar(self) -> AsyncCalendarResourceWithRawResponse:
        return AsyncCalendarResourceWithRawResponse(self._meetings.calendar)

    @cached_property
    def meetings_links(self) -> AsyncMeetingsLinksResourceWithRawResponse:
        return AsyncMeetingsLinksResourceWithRawResponse(self._meetings.meetings_links)


class MeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: MeetingsResource) -> None:
        self._meetings = meetings

    @cached_property
    def calendar(self) -> CalendarResourceWithStreamingResponse:
        return CalendarResourceWithStreamingResponse(self._meetings.calendar)

    @cached_property
    def meetings_links(self) -> MeetingsLinksResourceWithStreamingResponse:
        return MeetingsLinksResourceWithStreamingResponse(self._meetings.meetings_links)


class AsyncMeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

    @cached_property
    def calendar(self) -> AsyncCalendarResourceWithStreamingResponse:
        return AsyncCalendarResourceWithStreamingResponse(self._meetings.calendar)

    @cached_property
    def meetings_links(self) -> AsyncMeetingsLinksResourceWithStreamingResponse:
        return AsyncMeetingsLinksResourceWithStreamingResponse(self._meetings.meetings_links)
