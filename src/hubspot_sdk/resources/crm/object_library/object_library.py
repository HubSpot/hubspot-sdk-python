# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .enablement import (
    EnablementResource,
    AsyncEnablementResource,
    EnablementResourceWithRawResponse,
    AsyncEnablementResourceWithRawResponse,
    EnablementResourceWithStreamingResponse,
    AsyncEnablementResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ObjectLibraryResource", "AsyncObjectLibraryResource"]


class ObjectLibraryResource(SyncAPIResource):
    @cached_property
    def enablement(self) -> EnablementResource:
        return EnablementResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObjectLibraryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ObjectLibraryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectLibraryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return ObjectLibraryResourceWithStreamingResponse(self)


class AsyncObjectLibraryResource(AsyncAPIResource):
    @cached_property
    def enablement(self) -> AsyncEnablementResource:
        return AsyncEnablementResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObjectLibraryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectLibraryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectLibraryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncObjectLibraryResourceWithStreamingResponse(self)


class ObjectLibraryResourceWithRawResponse:
    def __init__(self, object_library: ObjectLibraryResource) -> None:
        self._object_library = object_library

    @cached_property
    def enablement(self) -> EnablementResourceWithRawResponse:
        return EnablementResourceWithRawResponse(self._object_library.enablement)


class AsyncObjectLibraryResourceWithRawResponse:
    def __init__(self, object_library: AsyncObjectLibraryResource) -> None:
        self._object_library = object_library

    @cached_property
    def enablement(self) -> AsyncEnablementResourceWithRawResponse:
        return AsyncEnablementResourceWithRawResponse(self._object_library.enablement)


class ObjectLibraryResourceWithStreamingResponse:
    def __init__(self, object_library: ObjectLibraryResource) -> None:
        self._object_library = object_library

    @cached_property
    def enablement(self) -> EnablementResourceWithStreamingResponse:
        return EnablementResourceWithStreamingResponse(self._object_library.enablement)


class AsyncObjectLibraryResourceWithStreamingResponse:
    def __init__(self, object_library: AsyncObjectLibraryResource) -> None:
        self._object_library = object_library

    @cached_property
    def enablement(self) -> AsyncEnablementResourceWithStreamingResponse:
        return AsyncEnablementResourceWithStreamingResponse(self._object_library.enablement)
