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

__all__ = ["VideoConferencingResource", "AsyncVideoConferencingResource"]


class VideoConferencingResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VideoConferencingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoConferencingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoConferencingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return VideoConferencingResourceWithStreamingResponse(self)


class AsyncVideoConferencingResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVideoConferencingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoConferencingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoConferencingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncVideoConferencingResourceWithStreamingResponse(self)


class VideoConferencingResourceWithRawResponse:
    def __init__(self, video_conferencing: VideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._video_conferencing.settings)


class AsyncVideoConferencingResourceWithRawResponse:
    def __init__(self, video_conferencing: AsyncVideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._video_conferencing.settings)


class VideoConferencingResourceWithStreamingResponse:
    def __init__(self, video_conferencing: VideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._video_conferencing.settings)


class AsyncVideoConferencingResourceWithStreamingResponse:
    def __init__(self, video_conferencing: AsyncVideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._video_conferencing.settings)
