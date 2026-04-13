# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.communication_preferences.statuses import (
    batch_read_params,
    batch_unsubscribe_all_params,
    batch_update_statuses_params,
    batch_get_unsubscribe_all_statuses_params,
)
from ....types.communication_preferences.public_status_request_param import PublicStatusRequestParam
from ....types.communication_preferences.batch_response_public_status import BatchResponsePublicStatus
from ....types.communication_preferences.batch_response_public_status_bulk_response import (
    BatchResponsePublicStatusBulkResponse,
)
from ....types.communication_preferences.batch_response_public_wide_status_bulk_response import (
    BatchResponsePublicWideStatusBulkResponse,
)
from ....types.communication_preferences.batch_response_public_bulk_opt_out_from_all_response import (
    BatchResponsePublicBulkOptOutFromAllResponse,
)

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

    def get_unsubscribe_all_statuses(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicWideStatusBulkResponse:
        """
        Checks whether a set of contacts have opted out of all communications.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/2026-03/statuses/batch/unsubscribe-all/read",
            body=maybe_transform(
                {"inputs": inputs}, batch_get_unsubscribe_all_statuses_params.BatchGetUnsubscribeAllStatusesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    batch_get_unsubscribe_all_statuses_params.BatchGetUnsubscribeAllStatusesParams,
                ),
            ),
            cast_to=BatchResponsePublicWideStatusBulkResponse,
        )

    def read(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatusBulkResponse:
        """
        Batch retrieve subscription statuses for a set of contacts.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/2026-03/statuses/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_read_params.BatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    batch_read_params.BatchReadParams,
                ),
            ),
            cast_to=BatchResponsePublicStatusBulkResponse,
        )

    def unsubscribe_all(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicBulkOptOutFromAllResponse:
        """
        Unsubscribe a set of contacts from all email subscriptions.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/2026-03/statuses/batch/unsubscribe-all",
            body=maybe_transform({"inputs": inputs}, batch_unsubscribe_all_params.BatchUnsubscribeAllParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    batch_unsubscribe_all_params.BatchUnsubscribeAllParams,
                ),
            ),
            cast_to=BatchResponsePublicBulkOptOutFromAllResponse,
        )

    def update_statuses(
        self,
        *,
        inputs: Iterable[PublicStatusRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatus:
        """
        Update the subscription status for a set of contacts.

        Args:
          inputs: An array of PublicStatusRequest objects, each representing a subscription status
              update request. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/2026-03/statuses/batch/write",
            body=maybe_transform({"inputs": inputs}, batch_update_statuses_params.BatchUpdateStatusesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicStatus,
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

    async def get_unsubscribe_all_statuses(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicWideStatusBulkResponse:
        """
        Checks whether a set of contacts have opted out of all communications.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/2026-03/statuses/batch/unsubscribe-all/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_get_unsubscribe_all_statuses_params.BatchGetUnsubscribeAllStatusesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    batch_get_unsubscribe_all_statuses_params.BatchGetUnsubscribeAllStatusesParams,
                ),
            ),
            cast_to=BatchResponsePublicWideStatusBulkResponse,
        )

    async def read(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatusBulkResponse:
        """
        Batch retrieve subscription statuses for a set of contacts.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/2026-03/statuses/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_read_params.BatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    batch_read_params.BatchReadParams,
                ),
            ),
            cast_to=BatchResponsePublicStatusBulkResponse,
        )

    async def unsubscribe_all(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicBulkOptOutFromAllResponse:
        """
        Unsubscribe a set of contacts from all email subscriptions.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/2026-03/statuses/batch/unsubscribe-all",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_unsubscribe_all_params.BatchUnsubscribeAllParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    batch_unsubscribe_all_params.BatchUnsubscribeAllParams,
                ),
            ),
            cast_to=BatchResponsePublicBulkOptOutFromAllResponse,
        )

    async def update_statuses(
        self,
        *,
        inputs: Iterable[PublicStatusRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatus:
        """
        Update the subscription status for a set of contacts.

        Args:
          inputs: An array of PublicStatusRequest objects, each representing a subscription status
              update request. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/2026-03/statuses/batch/write",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_update_statuses_params.BatchUpdateStatusesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicStatus,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.get_unsubscribe_all_statuses = to_raw_response_wrapper(
            batch.get_unsubscribe_all_statuses,
        )
        self.read = to_raw_response_wrapper(
            batch.read,
        )
        self.unsubscribe_all = to_raw_response_wrapper(
            batch.unsubscribe_all,
        )
        self.update_statuses = to_raw_response_wrapper(
            batch.update_statuses,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.get_unsubscribe_all_statuses = async_to_raw_response_wrapper(
            batch.get_unsubscribe_all_statuses,
        )
        self.read = async_to_raw_response_wrapper(
            batch.read,
        )
        self.unsubscribe_all = async_to_raw_response_wrapper(
            batch.unsubscribe_all,
        )
        self.update_statuses = async_to_raw_response_wrapper(
            batch.update_statuses,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.get_unsubscribe_all_statuses = to_streamed_response_wrapper(
            batch.get_unsubscribe_all_statuses,
        )
        self.read = to_streamed_response_wrapper(
            batch.read,
        )
        self.unsubscribe_all = to_streamed_response_wrapper(
            batch.unsubscribe_all,
        )
        self.update_statuses = to_streamed_response_wrapper(
            batch.update_statuses,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.get_unsubscribe_all_statuses = async_to_streamed_response_wrapper(
            batch.get_unsubscribe_all_statuses,
        )
        self.read = async_to_streamed_response_wrapper(
            batch.read,
        )
        self.unsubscribe_all = async_to_streamed_response_wrapper(
            batch.unsubscribe_all,
        )
        self.update_statuses = async_to_streamed_response_wrapper(
            batch.update_statuses,
        )
