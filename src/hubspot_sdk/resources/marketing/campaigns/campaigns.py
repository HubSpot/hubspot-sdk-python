# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .spend import (
    SpendResource,
    AsyncSpendResource,
    SpendResourceWithRawResponse,
    AsyncSpendResourceWithRawResponse,
    SpendResourceWithStreamingResponse,
    AsyncSpendResourceWithStreamingResponse,
)
from .assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .budget import (
    BudgetResource,
    AsyncBudgetResource,
    BudgetResourceWithRawResponse,
    AsyncBudgetResourceWithRawResponse,
    BudgetResourceWithStreamingResponse,
    AsyncBudgetResourceWithStreamingResponse,
)
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.marketing import campaign_get_params, campaign_update_params
from ....types.marketing.public_campaign import PublicCampaign
from ....types.marketing.public_campaign_with_assets import PublicCampaignWithAssets

__all__ = ["CampaignsResource", "AsyncCampaignsResource"]


class CampaignsResource(SyncAPIResource):
    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def budget(self) -> BudgetResource:
        return BudgetResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def spend(self) -> SpendResource:
        return SpendResource(self._client)

    @cached_property
    def with_raw_response(self) -> CampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CampaignsResourceWithStreamingResponse(self)

    def update(
        self,
        campaign_guid: str,
        *,
        properties: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCampaign:
        """Perform a partial update of a campaign identified by the specified ID.

        Provided
        property values will be overwritten. Read-only and non-existent properties will
        be ignored. Properties values can be cleared by passing an empty string. Note:
        The 'hs_goal' property is deprecated and will be ignored if provided.

        Args:
          properties: A collection of key-value pairs representing the properties of the campaign.
              Each key is a property name, and the corresponding value is the property's
              value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._patch(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}", campaign_guid=campaign_guid),
            body=maybe_transform({"properties": properties}, campaign_update_params.CampaignUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCampaign,
        )

    def delete(
        self,
        campaign_guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a specified campaign from the system.

        This operation removes the campaign
        identified by the provided campaignGuid from your HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}", campaign_guid=campaign_guid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        campaign_guid: str,
        *,
        end_date: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCampaignWithAssets:
        """Read a campaign identified by a specified internal ID.

        This endpoint allows you
        to retrieve detailed information about a specific marketing campaign using its
        unique identifier. It supports filtering the response by specific properties and
        date ranges.

        Args:
          end_date: The end date for filtering campaign data, in YYYY-MM-DD format.

          properties: A comma-separated list of property names to include in the response.

          start_date: The start date for filtering campaign data, in YYYY-MM-DD format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}", campaign_guid=campaign_guid),
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
                    campaign_get_params.CampaignGetParams,
                ),
            ),
            cast_to=PublicCampaignWithAssets,
        )


class AsyncCampaignsResource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def budget(self) -> AsyncBudgetResource:
        return AsyncBudgetResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def spend(self) -> AsyncSpendResource:
        return AsyncSpendResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCampaignsResourceWithStreamingResponse(self)

    async def update(
        self,
        campaign_guid: str,
        *,
        properties: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCampaign:
        """Perform a partial update of a campaign identified by the specified ID.

        Provided
        property values will be overwritten. Read-only and non-existent properties will
        be ignored. Properties values can be cleared by passing an empty string. Note:
        The 'hs_goal' property is deprecated and will be ignored if provided.

        Args:
          properties: A collection of key-value pairs representing the properties of the campaign.
              Each key is a property name, and the corresponding value is the property's
              value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._patch(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}", campaign_guid=campaign_guid),
            body=await async_maybe_transform({"properties": properties}, campaign_update_params.CampaignUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCampaign,
        )

    async def delete(
        self,
        campaign_guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a specified campaign from the system.

        This operation removes the campaign
        identified by the provided campaignGuid from your HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}", campaign_guid=campaign_guid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        campaign_guid: str,
        *,
        end_date: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCampaignWithAssets:
        """Read a campaign identified by a specified internal ID.

        This endpoint allows you
        to retrieve detailed information about a specific marketing campaign using its
        unique identifier. It supports filtering the response by specific properties and
        date ranges.

        Args:
          end_date: The end date for filtering campaign data, in YYYY-MM-DD format.

          properties: A comma-separated list of property names to include in the response.

          start_date: The start date for filtering campaign data, in YYYY-MM-DD format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}", campaign_guid=campaign_guid),
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
                    campaign_get_params.CampaignGetParams,
                ),
            ),
            cast_to=PublicCampaignWithAssets,
        )


class CampaignsResourceWithRawResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.update = to_raw_response_wrapper(
            campaigns.update,
        )
        self.delete = to_raw_response_wrapper(
            campaigns.delete,
        )
        self.get = to_raw_response_wrapper(
            campaigns.get,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._campaigns.assets)

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._campaigns.batch)

    @cached_property
    def budget(self) -> BudgetResourceWithRawResponse:
        return BudgetResourceWithRawResponse(self._campaigns.budget)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._campaigns.metrics)

    @cached_property
    def spend(self) -> SpendResourceWithRawResponse:
        return SpendResourceWithRawResponse(self._campaigns.spend)


class AsyncCampaignsResourceWithRawResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.update = async_to_raw_response_wrapper(
            campaigns.update,
        )
        self.delete = async_to_raw_response_wrapper(
            campaigns.delete,
        )
        self.get = async_to_raw_response_wrapper(
            campaigns.get,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._campaigns.assets)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._campaigns.batch)

    @cached_property
    def budget(self) -> AsyncBudgetResourceWithRawResponse:
        return AsyncBudgetResourceWithRawResponse(self._campaigns.budget)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._campaigns.metrics)

    @cached_property
    def spend(self) -> AsyncSpendResourceWithRawResponse:
        return AsyncSpendResourceWithRawResponse(self._campaigns.spend)


class CampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.update = to_streamed_response_wrapper(
            campaigns.update,
        )
        self.delete = to_streamed_response_wrapper(
            campaigns.delete,
        )
        self.get = to_streamed_response_wrapper(
            campaigns.get,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._campaigns.assets)

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._campaigns.batch)

    @cached_property
    def budget(self) -> BudgetResourceWithStreamingResponse:
        return BudgetResourceWithStreamingResponse(self._campaigns.budget)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._campaigns.metrics)

    @cached_property
    def spend(self) -> SpendResourceWithStreamingResponse:
        return SpendResourceWithStreamingResponse(self._campaigns.spend)


class AsyncCampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.update = async_to_streamed_response_wrapper(
            campaigns.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            campaigns.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            campaigns.get,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._campaigns.assets)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._campaigns.batch)

    @cached_property
    def budget(self) -> AsyncBudgetResourceWithStreamingResponse:
        return AsyncBudgetResourceWithStreamingResponse(self._campaigns.budget)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._campaigns.metrics)

    @cached_property
    def spend(self) -> AsyncSpendResourceWithStreamingResponse:
        return AsyncSpendResourceWithStreamingResponse(self._campaigns.spend)
