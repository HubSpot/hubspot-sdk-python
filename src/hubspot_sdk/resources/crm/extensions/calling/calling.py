# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .recording_settings import (
    RecordingSettingsResource,
    AsyncRecordingSettingsResource,
    RecordingSettingsResourceWithRawResponse,
    AsyncRecordingSettingsResourceWithRawResponse,
    RecordingSettingsResourceWithStreamingResponse,
    AsyncRecordingSettingsResourceWithStreamingResponse,
)
from .channel_connection_settings import (
    ChannelConnectionSettingsResource,
    AsyncChannelConnectionSettingsResource,
    ChannelConnectionSettingsResourceWithRawResponse,
    AsyncChannelConnectionSettingsResourceWithRawResponse,
    ChannelConnectionSettingsResourceWithStreamingResponse,
    AsyncChannelConnectionSettingsResourceWithStreamingResponse,
)

__all__ = ["CallingResource", "AsyncCallingResource"]


class CallingResource(SyncAPIResource):
    @cached_property
    def channel_connection_settings(self) -> ChannelConnectionSettingsResource:
        return ChannelConnectionSettingsResource(self._client)

    @cached_property
    def recording_settings(self) -> RecordingSettingsResource:
        return RecordingSettingsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CallingResourceWithStreamingResponse(self)


class AsyncCallingResource(AsyncAPIResource):
    @cached_property
    def channel_connection_settings(self) -> AsyncChannelConnectionSettingsResource:
        return AsyncChannelConnectionSettingsResource(self._client)

    @cached_property
    def recording_settings(self) -> AsyncRecordingSettingsResource:
        return AsyncRecordingSettingsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCallingResourceWithStreamingResponse(self)


class CallingResourceWithRawResponse:
    def __init__(self, calling: CallingResource) -> None:
        self._calling = calling

    @cached_property
    def channel_connection_settings(self) -> ChannelConnectionSettingsResourceWithRawResponse:
        return ChannelConnectionSettingsResourceWithRawResponse(self._calling.channel_connection_settings)

    @cached_property
    def recording_settings(self) -> RecordingSettingsResourceWithRawResponse:
        return RecordingSettingsResourceWithRawResponse(self._calling.recording_settings)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._calling.settings)


class AsyncCallingResourceWithRawResponse:
    def __init__(self, calling: AsyncCallingResource) -> None:
        self._calling = calling

    @cached_property
    def channel_connection_settings(self) -> AsyncChannelConnectionSettingsResourceWithRawResponse:
        return AsyncChannelConnectionSettingsResourceWithRawResponse(self._calling.channel_connection_settings)

    @cached_property
    def recording_settings(self) -> AsyncRecordingSettingsResourceWithRawResponse:
        return AsyncRecordingSettingsResourceWithRawResponse(self._calling.recording_settings)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._calling.settings)


class CallingResourceWithStreamingResponse:
    def __init__(self, calling: CallingResource) -> None:
        self._calling = calling

    @cached_property
    def channel_connection_settings(self) -> ChannelConnectionSettingsResourceWithStreamingResponse:
        return ChannelConnectionSettingsResourceWithStreamingResponse(self._calling.channel_connection_settings)

    @cached_property
    def recording_settings(self) -> RecordingSettingsResourceWithStreamingResponse:
        return RecordingSettingsResourceWithStreamingResponse(self._calling.recording_settings)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._calling.settings)


class AsyncCallingResourceWithStreamingResponse:
    def __init__(self, calling: AsyncCallingResource) -> None:
        self._calling = calling

    @cached_property
    def channel_connection_settings(self) -> AsyncChannelConnectionSettingsResourceWithStreamingResponse:
        return AsyncChannelConnectionSettingsResourceWithStreamingResponse(self._calling.channel_connection_settings)

    @cached_property
    def recording_settings(self) -> AsyncRecordingSettingsResourceWithStreamingResponse:
        return AsyncRecordingSettingsResourceWithStreamingResponse(self._calling.recording_settings)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._calling.settings)
