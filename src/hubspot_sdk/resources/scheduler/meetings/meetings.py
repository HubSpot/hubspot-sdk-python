# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .basic import (
    BasicResource,
    AsyncBasicResource,
    BasicResourceWithRawResponse,
    AsyncBasicResourceWithRawResponse,
    BasicResourceWithStreamingResponse,
    AsyncBasicResourceWithStreamingResponse,
)
from .advanced import (
    AdvancedResource,
    AsyncAdvancedResource,
    AdvancedResourceWithRawResponse,
    AsyncAdvancedResourceWithRawResponse,
    AdvancedResourceWithStreamingResponse,
    AsyncAdvancedResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MeetingsResource", "AsyncMeetingsResource"]


class MeetingsResource(SyncAPIResource):
    @cached_property
    def advanced(self) -> AdvancedResource:
        return AdvancedResource(self._client)

    @cached_property
    def basic(self) -> BasicResource:
        return BasicResource(self._client)

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
    def advanced(self) -> AsyncAdvancedResource:
        return AsyncAdvancedResource(self._client)

    @cached_property
    def basic(self) -> AsyncBasicResource:
        return AsyncBasicResource(self._client)

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
    def advanced(self) -> AdvancedResourceWithRawResponse:
        return AdvancedResourceWithRawResponse(self._meetings.advanced)

    @cached_property
    def basic(self) -> BasicResourceWithRawResponse:
        return BasicResourceWithRawResponse(self._meetings.basic)


class AsyncMeetingsResourceWithRawResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

    @cached_property
    def advanced(self) -> AsyncAdvancedResourceWithRawResponse:
        return AsyncAdvancedResourceWithRawResponse(self._meetings.advanced)

    @cached_property
    def basic(self) -> AsyncBasicResourceWithRawResponse:
        return AsyncBasicResourceWithRawResponse(self._meetings.basic)


class MeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: MeetingsResource) -> None:
        self._meetings = meetings

    @cached_property
    def advanced(self) -> AdvancedResourceWithStreamingResponse:
        return AdvancedResourceWithStreamingResponse(self._meetings.advanced)

    @cached_property
    def basic(self) -> BasicResourceWithStreamingResponse:
        return BasicResourceWithStreamingResponse(self._meetings.basic)


class AsyncMeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

    @cached_property
    def advanced(self) -> AsyncAdvancedResourceWithStreamingResponse:
        return AsyncAdvancedResourceWithStreamingResponse(self._meetings.advanced)

    @cached_property
    def basic(self) -> AsyncBasicResourceWithStreamingResponse:
        return AsyncBasicResourceWithStreamingResponse(self._meetings.basic)
