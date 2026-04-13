# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["StatusesResource", "AsyncStatusesResource"]


class StatusesResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> StatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return StatusesResourceWithStreamingResponse(self)


class AsyncStatusesResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncStatusesResourceWithStreamingResponse(self)


class StatusesResourceWithRawResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._statuses.batch)


class AsyncStatusesResourceWithRawResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._statuses.batch)


class StatusesResourceWithStreamingResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._statuses.batch)


class AsyncStatusesResourceWithStreamingResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._statuses.batch)
