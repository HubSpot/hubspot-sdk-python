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

__all__ = ["VideoconferencingResource", "AsyncVideoconferencingResource"]


class VideoconferencingResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VideoconferencingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoconferencingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoconferencingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return VideoconferencingResourceWithStreamingResponse(self)


class AsyncVideoconferencingResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVideoconferencingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoconferencingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoconferencingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncVideoconferencingResourceWithStreamingResponse(self)


class VideoconferencingResourceWithRawResponse:
    def __init__(self, videoconferencing: VideoconferencingResource) -> None:
        self._videoconferencing = videoconferencing

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._videoconferencing.settings)


class AsyncVideoconferencingResourceWithRawResponse:
    def __init__(self, videoconferencing: AsyncVideoconferencingResource) -> None:
        self._videoconferencing = videoconferencing

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._videoconferencing.settings)


class VideoconferencingResourceWithStreamingResponse:
    def __init__(self, videoconferencing: VideoconferencingResource) -> None:
        self._videoconferencing = videoconferencing

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._videoconferencing.settings)


class AsyncVideoconferencingResourceWithStreamingResponse:
    def __init__(self, videoconferencing: AsyncVideoconferencingResource) -> None:
        self._videoconferencing = videoconferencing

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._videoconferencing.settings)
