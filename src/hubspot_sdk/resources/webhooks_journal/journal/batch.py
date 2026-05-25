# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.webhooks_journal.journal import (
    batch_get_params,
    batch_get_latest_params,
    batch_get_earliest_params,
    batch_get_from_offset_params,
)
from ....types.shared.batch_response_journal_fetch_response import BatchResponseJournalFetchResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        inputs: SequenceNotStr[str],
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Execute a batch read operation on the webhooks journal for the specified date,
        2026-03. This endpoint allows you to retrieve multiple entries from the webhooks
        journal in a single request, which can be useful for processing large amounts of
        data efficiently. Ensure that the request body is provided in the required
        format.

        Args:
          inputs: Strings to input.

          install_portal_id: An integer representing the ID of the portal installation for which the webhooks
              journal data should be retrieved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"install_portal_id": install_portal_id}, batch_get_params.BatchGetParams),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_earliest(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Retrieve the earliest batch of webhook journal entries for a specified count.
        This endpoint is useful for accessing historical webhook data in batches,
        allowing you to process or analyze older entries. The number of entries
        retrieved is determined by the count parameter.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value that specifies which
              portal's data to access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/earliest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_get_earliest_params.BatchGetEarliestParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_from_offset(
        self,
        count: int,
        *,
        offset: str,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Retrieve a batch of webhook journal entries starting from a specified offset.
        This endpoint allows you to fetch a defined number of entries, which can be
        useful for processing large datasets in manageable chunks.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/{offset}/next/{count}", offset=offset, count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_get_from_offset_params.BatchGetFromOffsetParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_latest(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Retrieve the latest batch of webhook journal entries up to the specified count.
        This endpoint is useful for fetching recent webhook data for analysis or
        processing. The count parameter determines the maximum number of entries to
        return.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to specify the
              portal context for the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/latest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_get_latest_params.BatchGetLatestParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        inputs: SequenceNotStr[str],
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Execute a batch read operation on the webhooks journal for the specified date,
        2026-03. This endpoint allows you to retrieve multiple entries from the webhooks
        journal in a single request, which can be useful for processing large amounts of
        data efficiently. Ensure that the request body is provided in the required
        format.

        Args:
          inputs: Strings to input.

          install_portal_id: An integer representing the ID of the portal installation for which the webhooks
              journal data should be retrieved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_get_params.BatchGetParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_earliest(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Retrieve the earliest batch of webhook journal entries for a specified count.
        This endpoint is useful for accessing historical webhook data in batches,
        allowing you to process or analyze older entries. The number of entries
        retrieved is determined by the count parameter.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value that specifies which
              portal's data to access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/earliest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_get_earliest_params.BatchGetEarliestParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_from_offset(
        self,
        count: int,
        *,
        offset: str,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Retrieve a batch of webhook journal entries starting from a specified offset.
        This endpoint allows you to fetch a defined number of entries, which can be
        useful for processing large datasets in manageable chunks.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/{offset}/next/{count}", offset=offset, count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_get_from_offset_params.BatchGetFromOffsetParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_latest(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Retrieve the latest batch of webhook journal entries up to the specified count.
        This endpoint is useful for fetching recent webhook data for analysis or
        processing. The count parameter determines the maximum number of entries to
        return.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to specify the
              portal context for the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/latest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_get_latest_params.BatchGetLatestParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.get = to_raw_response_wrapper(
            batch.get,
        )
        self.get_earliest = to_raw_response_wrapper(
            batch.get_earliest,
        )
        self.get_from_offset = to_raw_response_wrapper(
            batch.get_from_offset,
        )
        self.get_latest = to_raw_response_wrapper(
            batch.get_latest,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.get = async_to_raw_response_wrapper(
            batch.get,
        )
        self.get_earliest = async_to_raw_response_wrapper(
            batch.get_earliest,
        )
        self.get_from_offset = async_to_raw_response_wrapper(
            batch.get_from_offset,
        )
        self.get_latest = async_to_raw_response_wrapper(
            batch.get_latest,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.get = to_streamed_response_wrapper(
            batch.get,
        )
        self.get_earliest = to_streamed_response_wrapper(
            batch.get_earliest,
        )
        self.get_from_offset = to_streamed_response_wrapper(
            batch.get_from_offset,
        )
        self.get_latest = to_streamed_response_wrapper(
            batch.get_latest,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.get = async_to_streamed_response_wrapper(
            batch.get,
        )
        self.get_earliest = async_to_streamed_response_wrapper(
            batch.get_earliest,
        )
        self.get_from_offset = async_to_streamed_response_wrapper(
            batch.get_from_offset,
        )
        self.get_latest = async_to_streamed_response_wrapper(
            batch.get_latest,
        )
