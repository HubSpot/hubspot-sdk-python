# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.objects import deal_split_batch_read_params, deal_split_batch_upsert_params
from ....types.shared_params.public_object_id import PublicObjectID
from ....types.crm.objects.batch_response_deal_to_deal_splits import BatchResponseDealToDealSplits
from ....types.crm.objects.public_deal_splits_create_request_param import PublicDealSplitsCreateRequestParam

__all__ = ["DealSplitsResource", "AsyncDealSplitsResource"]


class DealSplitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DealSplitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DealSplitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DealSplitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return DealSplitsResourceWithStreamingResponse(self)

    def batch_read(
        self,
        *,
        inputs: Iterable[PublicObjectID],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseDealToDealSplits:
        """
        Read a batch of deal split objects by their associated deal object internal ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/deals/splits/batch/read",
            body=maybe_transform({"inputs": inputs}, deal_split_batch_read_params.DealSplitBatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseDealToDealSplits,
        )

    def batch_upsert(
        self,
        *,
        inputs: Iterable[PublicDealSplitsCreateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseDealToDealSplits:
        """Create or replace deal splits for deals with the provided IDs.

        Deal split
        percentages for each deal must sum up to 1.0 (100%) and may have up to 8 decimal
        places

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/deals/splits/batch/upsert",
            body=maybe_transform({"inputs": inputs}, deal_split_batch_upsert_params.DealSplitBatchUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseDealToDealSplits,
        )


class AsyncDealSplitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDealSplitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDealSplitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDealSplitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDealSplitsResourceWithStreamingResponse(self)

    async def batch_read(
        self,
        *,
        inputs: Iterable[PublicObjectID],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseDealToDealSplits:
        """
        Read a batch of deal split objects by their associated deal object internal ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/deals/splits/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, deal_split_batch_read_params.DealSplitBatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseDealToDealSplits,
        )

    async def batch_upsert(
        self,
        *,
        inputs: Iterable[PublicDealSplitsCreateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseDealToDealSplits:
        """Create or replace deal splits for deals with the provided IDs.

        Deal split
        percentages for each deal must sum up to 1.0 (100%) and may have up to 8 decimal
        places

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/deals/splits/batch/upsert",
            body=await async_maybe_transform(
                {"inputs": inputs}, deal_split_batch_upsert_params.DealSplitBatchUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseDealToDealSplits,
        )


class DealSplitsResourceWithRawResponse:
    def __init__(self, deal_splits: DealSplitsResource) -> None:
        self._deal_splits = deal_splits

        self.batch_read = to_raw_response_wrapper(
            deal_splits.batch_read,
        )
        self.batch_upsert = to_raw_response_wrapper(
            deal_splits.batch_upsert,
        )


class AsyncDealSplitsResourceWithRawResponse:
    def __init__(self, deal_splits: AsyncDealSplitsResource) -> None:
        self._deal_splits = deal_splits

        self.batch_read = async_to_raw_response_wrapper(
            deal_splits.batch_read,
        )
        self.batch_upsert = async_to_raw_response_wrapper(
            deal_splits.batch_upsert,
        )


class DealSplitsResourceWithStreamingResponse:
    def __init__(self, deal_splits: DealSplitsResource) -> None:
        self._deal_splits = deal_splits

        self.batch_read = to_streamed_response_wrapper(
            deal_splits.batch_read,
        )
        self.batch_upsert = to_streamed_response_wrapper(
            deal_splits.batch_upsert,
        )


class AsyncDealSplitsResourceWithStreamingResponse:
    def __init__(self, deal_splits: AsyncDealSplitsResource) -> None:
        self._deal_splits = deal_splits

        self.batch_read = async_to_streamed_response_wrapper(
            deal_splits.batch_read,
        )
        self.batch_upsert = async_to_streamed_response_wrapper(
            deal_splits.batch_upsert,
        )
