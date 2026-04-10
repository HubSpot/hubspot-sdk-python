# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cards_dev import (
    CardsDevResource,
    AsyncCardsDevResource,
    CardsDevResourceWithRawResponse,
    AsyncCardsDevResourceWithRawResponse,
    CardsDevResourceWithStreamingResponse,
    AsyncCardsDevResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .calling.calling import (
    CallingResource,
    AsyncCallingResource,
    CallingResourceWithRawResponse,
    AsyncCallingResourceWithRawResponse,
    CallingResourceWithStreamingResponse,
    AsyncCallingResourceWithStreamingResponse,
)
from .video_conferencing import (
    VideoConferencingResource,
    AsyncVideoConferencingResource,
    VideoConferencingResourceWithRawResponse,
    AsyncVideoConferencingResourceWithRawResponse,
    VideoConferencingResourceWithStreamingResponse,
    AsyncVideoConferencingResourceWithStreamingResponse,
)

__all__ = ["ExtensionsResource", "AsyncExtensionsResource"]


class ExtensionsResource(SyncAPIResource):
    @cached_property
    def calling(self) -> CallingResource:
        return CallingResource(self._client)

    @cached_property
    def cards_dev(self) -> CardsDevResource:
        return CardsDevResource(self._client)

    @cached_property
    def video_conferencing(self) -> VideoConferencingResource:
        return VideoConferencingResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return ExtensionsResourceWithStreamingResponse(self)


class AsyncExtensionsResource(AsyncAPIResource):
    @cached_property
    def calling(self) -> AsyncCallingResource:
        return AsyncCallingResource(self._client)

    @cached_property
    def cards_dev(self) -> AsyncCardsDevResource:
        return AsyncCardsDevResource(self._client)

    @cached_property
    def video_conferencing(self) -> AsyncVideoConferencingResource:
        return AsyncVideoConferencingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncExtensionsResourceWithStreamingResponse(self)


class ExtensionsResourceWithRawResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> CallingResourceWithRawResponse:
        return CallingResourceWithRawResponse(self._extensions.calling)

    @cached_property
    def cards_dev(self) -> CardsDevResourceWithRawResponse:
        return CardsDevResourceWithRawResponse(self._extensions.cards_dev)

    @cached_property
    def video_conferencing(self) -> VideoConferencingResourceWithRawResponse:
        return VideoConferencingResourceWithRawResponse(self._extensions.video_conferencing)


class AsyncExtensionsResourceWithRawResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> AsyncCallingResourceWithRawResponse:
        return AsyncCallingResourceWithRawResponse(self._extensions.calling)

    @cached_property
    def cards_dev(self) -> AsyncCardsDevResourceWithRawResponse:
        return AsyncCardsDevResourceWithRawResponse(self._extensions.cards_dev)

    @cached_property
    def video_conferencing(self) -> AsyncVideoConferencingResourceWithRawResponse:
        return AsyncVideoConferencingResourceWithRawResponse(self._extensions.video_conferencing)


class ExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> CallingResourceWithStreamingResponse:
        return CallingResourceWithStreamingResponse(self._extensions.calling)

    @cached_property
    def cards_dev(self) -> CardsDevResourceWithStreamingResponse:
        return CardsDevResourceWithStreamingResponse(self._extensions.cards_dev)

    @cached_property
    def video_conferencing(self) -> VideoConferencingResourceWithStreamingResponse:
        return VideoConferencingResourceWithStreamingResponse(self._extensions.video_conferencing)


class AsyncExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> AsyncCallingResourceWithStreamingResponse:
        return AsyncCallingResourceWithStreamingResponse(self._extensions.calling)

    @cached_property
    def cards_dev(self) -> AsyncCardsDevResourceWithStreamingResponse:
        return AsyncCardsDevResourceWithStreamingResponse(self._extensions.cards_dev)

    @cached_property
    def video_conferencing(self) -> AsyncVideoConferencingResourceWithStreamingResponse:
        return AsyncVideoConferencingResourceWithStreamingResponse(self._extensions.video_conferencing)
