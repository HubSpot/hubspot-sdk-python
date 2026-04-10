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

__all__ = ["DealSplitsResource", "AsyncDealSplitsResource"]


class DealSplitsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> DealSplitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DealSplitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DealSplitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return DealSplitsResourceWithStreamingResponse(self)


class AsyncDealSplitsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDealSplitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDealSplitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDealSplitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDealSplitsResourceWithStreamingResponse(self)


class DealSplitsResourceWithRawResponse:
    def __init__(self, deal_splits: DealSplitsResource) -> None:
        self._deal_splits = deal_splits

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._deal_splits.batch)


class AsyncDealSplitsResourceWithRawResponse:
    def __init__(self, deal_splits: AsyncDealSplitsResource) -> None:
        self._deal_splits = deal_splits

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._deal_splits.batch)


class DealSplitsResourceWithStreamingResponse:
    def __init__(self, deal_splits: DealSplitsResource) -> None:
        self._deal_splits = deal_splits

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._deal_splits.batch)


class AsyncDealSplitsResourceWithStreamingResponse:
    def __init__(self, deal_splits: AsyncDealSplitsResource) -> None:
        self._deal_splits = deal_splits

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._deal_splits.batch)
