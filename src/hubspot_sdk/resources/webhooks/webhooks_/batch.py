# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ....types.webhooks.webhooks_ import (
    batch_read_params,
    batch_create_params,
    batch_get_next_params,
    batch_get_latest_params,
    batch_get_earliest_params,
)
from ....types.webhooks.batch_response_subscription_response import BatchResponseSubscriptionResponse
from ....types.webhooks.batch_response_journal_fetch_response import BatchResponseJournalFetchResponse
from ....types.webhooks.subscription_batch_update_request_param import SubscriptionBatchUpdateRequestParam

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        inputs: Iterable[SubscriptionBatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriptionResponse:
        """
        Batch create event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
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
        Args:
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
        Args:
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

    def get_next(
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
        Args:
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
                    {"install_portal_id": install_portal_id}, batch_get_next_params.BatchGetNextParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def read(
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
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_read_params.BatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"install_portal_id": install_portal_id}, batch_read_params.BatchReadParams),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        inputs: Iterable[SubscriptionBatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriptionResponse:
        """
        Batch create event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=await async_maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
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
        Args:
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
        Args:
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

    async def get_next(
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
        Args:
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
                    {"install_portal_id": install_portal_id}, batch_get_next_params.BatchGetNextParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def read(
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
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_read_params.BatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id}, batch_read_params.BatchReadParams
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )
        self.get_earliest = to_raw_response_wrapper(
            batch.get_earliest,
        )
        self.get_latest = to_raw_response_wrapper(
            batch.get_latest,
        )
        self.get_next = to_raw_response_wrapper(
            batch.get_next,
        )
        self.read = to_raw_response_wrapper(
            batch.read,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )
        self.get_earliest = async_to_raw_response_wrapper(
            batch.get_earliest,
        )
        self.get_latest = async_to_raw_response_wrapper(
            batch.get_latest,
        )
        self.get_next = async_to_raw_response_wrapper(
            batch.get_next,
        )
        self.read = async_to_raw_response_wrapper(
            batch.read,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )
        self.get_earliest = to_streamed_response_wrapper(
            batch.get_earliest,
        )
        self.get_latest = to_streamed_response_wrapper(
            batch.get_latest,
        )
        self.get_next = to_streamed_response_wrapper(
            batch.get_next,
        )
        self.read = to_streamed_response_wrapper(
            batch.read,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
        self.get_earliest = async_to_streamed_response_wrapper(
            batch.get_earliest,
        )
        self.get_latest = async_to_streamed_response_wrapper(
            batch.get_latest,
        )
        self.get_next = async_to_streamed_response_wrapper(
            batch.get_next,
        )
        self.read = async_to_streamed_response_wrapper(
            batch.read,
        )
