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
        """Create a batch of campaigns with specified properties.

        This endpoint allows for
        the creation of multiple campaigns in a single request. Note that the 'hs_goal'
        property is deprecated and will be ignored if provided.

        Args:
          inputs: An array of PublicCampaignInput objects, each representing the properties of a
              campaign to be created in the batch. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/campaigns/2026-03/batch/create",
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
        """Update a batch of marketing campaigns with specified properties.

        This endpoint
        allows you to modify multiple campaigns in one request. Note that the 'hs_goal'
        property is deprecated and will be ignored if provided.

        Args:
          inputs: An array of PublicCampaignBatchUpdateItem objects, each containing the ID and
              properties to update for a specific campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/campaigns/2026-03/batch/update",
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
        """Archive a batch of marketing campaigns in your HubSpot account.

        This operation
        permanently removes the specified campaigns, making them inaccessible. It is
        useful for cleaning up outdated or unnecessary campaigns in bulk.

        Args:
          inputs: An array of PublicCampaignDeleteInput objects, each specifying a campaign to be
              deleted. Each object must include the campaign's unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/marketing/campaigns/2026-03/batch/archive",
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
        """Retrieve a batch of campaigns with specified properties and date range.

        This
        endpoint allows you to filter campaigns by start and end dates and specify which
        properties to include in the response.

        Args:
          inputs: An array of PublicCampaignReadInput objects, each containing the ID of a
              campaign to be read. This property is required.

          end_date: The end date for filtering campaigns, in YYYY-MM-DD format.

          properties: A comma-separated list of property names to include in the response.

          start_date: The start date for filtering campaigns, in YYYY-MM-DD format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/campaigns/2026-03/batch/read",
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
        """Create a batch of campaigns with specified properties.

        This endpoint allows for
        the creation of multiple campaigns in a single request. Note that the 'hs_goal'
        property is deprecated and will be ignored if provided.

        Args:
          inputs: An array of PublicCampaignInput objects, each representing the properties of a
              campaign to be created in the batch. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/campaigns/2026-03/batch/create",
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
        """Update a batch of marketing campaigns with specified properties.

        This endpoint
        allows you to modify multiple campaigns in one request. Note that the 'hs_goal'
        property is deprecated and will be ignored if provided.

        Args:
          inputs: An array of PublicCampaignBatchUpdateItem objects, each containing the ID and
              properties to update for a specific campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/campaigns/2026-03/batch/update",
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
        """Archive a batch of marketing campaigns in your HubSpot account.

        This operation
        permanently removes the specified campaigns, making them inaccessible. It is
        useful for cleaning up outdated or unnecessary campaigns in bulk.

        Args:
          inputs: An array of PublicCampaignDeleteInput objects, each specifying a campaign to be
              deleted. Each object must include the campaign's unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/marketing/campaigns/2026-03/batch/archive",
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
        """Retrieve a batch of campaigns with specified properties and date range.

        This
        endpoint allows you to filter campaigns by start and end dates and specify which
        properties to include in the response.

        Args:
          inputs: An array of PublicCampaignReadInput objects, each containing the ID of a
              campaign to be read. This property is required.

          end_date: The end date for filtering campaigns, in YYYY-MM-DD format.

          properties: A comma-separated list of property names to include in the response.

          start_date: The start date for filtering campaigns, in YYYY-MM-DD format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/campaigns/2026-03/batch/read",
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
