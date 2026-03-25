# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ip_ranges import (
    IPRangesResource,
    AsyncIPRangesResource,
    IPRangesResourceWithRawResponse,
    AsyncIPRangesResourceWithRawResponse,
    IPRangesResourceWithStreamingResponse,
    AsyncIPRangesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OriginsResource", "AsyncOriginsResource"]


class OriginsResource(SyncAPIResource):
    @cached_property
    def ip_ranges(self) -> IPRangesResource:
        return IPRangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> OriginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OriginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return OriginsResourceWithStreamingResponse(self)


class AsyncOriginsResource(AsyncAPIResource):
    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResource:
        return AsyncIPRangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOriginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncOriginsResourceWithStreamingResponse(self)


class OriginsResourceWithRawResponse:
    def __init__(self, origins: OriginsResource) -> None:
        self._origins = origins

    @cached_property
    def ip_ranges(self) -> IPRangesResourceWithRawResponse:
        return IPRangesResourceWithRawResponse(self._origins.ip_ranges)


class AsyncOriginsResourceWithRawResponse:
    def __init__(self, origins: AsyncOriginsResource) -> None:
        self._origins = origins

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResourceWithRawResponse:
        return AsyncIPRangesResourceWithRawResponse(self._origins.ip_ranges)


class OriginsResourceWithStreamingResponse:
    def __init__(self, origins: OriginsResource) -> None:
        self._origins = origins

    @cached_property
    def ip_ranges(self) -> IPRangesResourceWithStreamingResponse:
        return IPRangesResourceWithStreamingResponse(self._origins.ip_ranges)


class AsyncOriginsResourceWithStreamingResponse:
    def __init__(self, origins: AsyncOriginsResource) -> None:
        self._origins = origins

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResourceWithStreamingResponse:
        return AsyncIPRangesResourceWithStreamingResponse(self._origins.ip_ranges)
