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
from ....types.crm.timeline import batch_create_params
from ....types.crm.app_event_occurrence_param import AppEventOccurrenceParam
from ....types.crm.batch_response_app_event_occurrence import BatchResponseAppEventOccurrence

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
        *,
        inputs: Iterable[AppEventOccurrenceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseAppEventOccurrence:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integrators/timeline/2026-03/events/batch",
            body=maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseAppEventOccurrence,
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
        *,
        inputs: Iterable[AppEventOccurrenceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseAppEventOccurrence:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integrators/timeline/2026-03/events/batch",
            body=await async_maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseAppEventOccurrence,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
