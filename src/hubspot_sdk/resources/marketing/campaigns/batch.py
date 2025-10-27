# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.marketing.campaigns import (
    batch_get_params,
    batch_create_params,
    batch_delete_params,
    batch_update_params,
)
from ....types.marketing.public_campaign_input_param import PublicCampaignInputParam
from ....types.marketing.batch_response_public_campaign import BatchResponsePublicCampaign
from ....types.marketing.public_campaign_read_input_param import PublicCampaignReadInputParam
from ....types.marketing.public_campaign_delete_input_param import PublicCampaignDeleteInputParam
from ....types.marketing.public_campaign_batch_update_item_param import PublicCampaignBatchUpdateItemParam
from ....types.marketing.batch_response_public_campaign_with_assets import BatchResponsePublicCampaignWithAssets

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
        inputs: Iterable[PublicCampaignInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicCampaign:
        """This endpoint creates a batch of campaigns.

        The maximum number of items in a
        batch request is 50. The campaigns in the response are not guaranteed to be in
        the same order as they were provided in the request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/v3/campaigns/batch/create",
            body=maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicCampaign,
        )

    def update(
        self,
        *,
        inputs: Iterable[PublicCampaignBatchUpdateItemParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicCampaign:
        """This endpoint updates a batch of campaigns based on the provided input data.

        The
        maximum number of items in a batch request is 50. If an empty string ("") is
        passed for any property in the Batch Update, it will reset that property's
        value.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/v3/campaigns/batch/update",
            body=maybe_transform({"inputs": inputs}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicCampaign,
        )

    def delete(
        self,
        *,
        inputs: Iterable[PublicCampaignDeleteInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint deletes a batch of campaigns.

        The maximum number of items in a
        batch request is 50. The response will always be 204 No Content, regardless of
        whether the campaigns exist or not, whether they were successfully deleted or
        not, or if only some of the campaigns in the batch were deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/marketing/v3/campaigns/batch/archive",
            body=maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        inputs: Iterable[PublicCampaignReadInputParam],
        end_date: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicCampaignWithAssets:
        """
        This endpoint reads a batch of campaigns based on the provided input data and
        returns the campaigns along with their associated assets. The maximum number of
        items in a batch request is 50. The campaigns in the response are not guaranteed
        to be in the same order as they were provided in the request. If duplicate
        campaign IDs are provided in the request, duplicates will be ignored. The
        response will include only unique IDs and will be returned without duplicates.

        Args:
          end_date: End date to fetch asset metrics, formatted as YYYY-MM-DD. This date is used to
              fetch the metrics associated with the assets for a specified period. If not
              provided, no asset metrics will be fetched.

          properties: A comma-separated list of the properties to be returned in the response. If any
              of the specified properties has empty value on the requested object(s), they
              will be ignored and not returned in response. If this parameter is empty, the
              response will include an empty properties map.

          start_date: Start date to fetch asset metrics, formatted as YYYY-MM-DD. This date is used to
              fetch the metrics associated with the assets for a specified period. If not
              provided, no asset metrics will be fetched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/v3/campaigns/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "properties": properties,
                        "start_date": start_date,
                    },
                    batch_get_params.BatchGetParams,
                ),
            ),
            cast_to=BatchResponsePublicCampaignWithAssets,
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
        inputs: Iterable[PublicCampaignInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicCampaign:
        """This endpoint creates a batch of campaigns.

        The maximum number of items in a
        batch request is 50. The campaigns in the response are not guaranteed to be in
        the same order as they were provided in the request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/v3/campaigns/batch/create",
            body=await async_maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicCampaign,
        )

    async def update(
        self,
        *,
        inputs: Iterable[PublicCampaignBatchUpdateItemParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicCampaign:
        """This endpoint updates a batch of campaigns based on the provided input data.

        The
        maximum number of items in a batch request is 50. If an empty string ("") is
        passed for any property in the Batch Update, it will reset that property's
        value.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/v3/campaigns/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicCampaign,
        )

    async def delete(
        self,
        *,
        inputs: Iterable[PublicCampaignDeleteInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint deletes a batch of campaigns.

        The maximum number of items in a
        batch request is 50. The response will always be 204 No Content, regardless of
        whether the campaigns exist or not, whether they were successfully deleted or
        not, or if only some of the campaigns in the batch were deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/marketing/v3/campaigns/batch/archive",
            body=await async_maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        inputs: Iterable[PublicCampaignReadInputParam],
        end_date: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicCampaignWithAssets:
        """
        This endpoint reads a batch of campaigns based on the provided input data and
        returns the campaigns along with their associated assets. The maximum number of
        items in a batch request is 50. The campaigns in the response are not guaranteed
        to be in the same order as they were provided in the request. If duplicate
        campaign IDs are provided in the request, duplicates will be ignored. The
        response will include only unique IDs and will be returned without duplicates.

        Args:
          end_date: End date to fetch asset metrics, formatted as YYYY-MM-DD. This date is used to
              fetch the metrics associated with the assets for a specified period. If not
              provided, no asset metrics will be fetched.

          properties: A comma-separated list of the properties to be returned in the response. If any
              of the specified properties has empty value on the requested object(s), they
              will be ignored and not returned in response. If this parameter is empty, the
              response will include an empty properties map.

          start_date: Start date to fetch asset metrics, formatted as YYYY-MM-DD. This date is used to
              fetch the metrics associated with the assets for a specified period. If not
              provided, no asset metrics will be fetched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/v3/campaigns/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "properties": properties,
                        "start_date": start_date,
                    },
                    batch_get_params.BatchGetParams,
                ),
            ),
            cast_to=BatchResponsePublicCampaignWithAssets,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )
        self.update = to_raw_response_wrapper(
            batch.update,
        )
        self.delete = to_raw_response_wrapper(
            batch.delete,
        )
        self.get = to_raw_response_wrapper(
            batch.get,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )
        self.update = async_to_raw_response_wrapper(
            batch.update,
        )
        self.delete = async_to_raw_response_wrapper(
            batch.delete,
        )
        self.get = async_to_raw_response_wrapper(
            batch.get,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )
        self.update = to_streamed_response_wrapper(
            batch.update,
        )
        self.delete = to_streamed_response_wrapper(
            batch.delete,
        )
        self.get = to_streamed_response_wrapper(
            batch.get,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
        self.update = async_to_streamed_response_wrapper(
            batch.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            batch.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            batch.get,
        )
