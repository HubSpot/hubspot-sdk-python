# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .meetings.meetings import (
    MeetingsResource,
    AsyncMeetingsResource,
    MeetingsResourceWithRawResponse,
    AsyncMeetingsResourceWithRawResponse,
    MeetingsResourceWithStreamingResponse,
    AsyncMeetingsResourceWithStreamingResponse,
)

__all__ = ["SchedulerResource", "AsyncSchedulerResource"]


class SchedulerResource(SyncAPIResource):
    @cached_property
    def meetings(self) -> MeetingsResource:
        return MeetingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SchedulerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SchedulerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SchedulerResourceWithStreamingResponse(self)


class AsyncSchedulerResource(AsyncAPIResource):
    @cached_property
    def meetings(self) -> AsyncMeetingsResource:
        return AsyncMeetingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSchedulerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSchedulerResourceWithStreamingResponse(self)


class SchedulerResourceWithRawResponse:
    def __init__(self, scheduler: SchedulerResource) -> None:
        self._scheduler = scheduler

    @cached_property
    def meetings(self) -> MeetingsResourceWithRawResponse:
        return MeetingsResourceWithRawResponse(self._scheduler.meetings)


class AsyncSchedulerResourceWithRawResponse:
    def __init__(self, scheduler: AsyncSchedulerResource) -> None:
        self._scheduler = scheduler

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithRawResponse:
        return AsyncMeetingsResourceWithRawResponse(self._scheduler.meetings)


class SchedulerResourceWithStreamingResponse:
    def __init__(self, scheduler: SchedulerResource) -> None:
        self._scheduler = scheduler

    @cached_property
    def meetings(self) -> MeetingsResourceWithStreamingResponse:
        return MeetingsResourceWithStreamingResponse(self._scheduler.meetings)


class AsyncSchedulerResourceWithStreamingResponse:
    def __init__(self, scheduler: AsyncSchedulerResource) -> None:
        self._scheduler = scheduler

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithStreamingResponse:
        return AsyncMeetingsResourceWithStreamingResponse(self._scheduler.meetings)
