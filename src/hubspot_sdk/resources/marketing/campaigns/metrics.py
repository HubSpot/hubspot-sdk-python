# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.marketing.campaigns import (
    metric_get_attribution_metrics_params,
    metric_get_revenue_attribution_params,
    metric_list_contact_ids_by_type_params,
)
from ....types.marketing.metrics_counters import MetricsCounters
from ....types.marketing.contact_reference import ContactReference
from ....types.marketing.revenue_attribution_aggregate import RevenueAttributionAggregate

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    def get_attribution_metrics(
        self,
        campaign_guid: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsCounters:
        """
        This endpoint retrieves key attribution metrics for a specified campaign, such
        as sessions, new contacts, and influenced contacts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}/reports/metrics", campaign_guid=campaign_guid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    metric_get_attribution_metrics_params.MetricGetAttributionMetricsParams,
                ),
            ),
            cast_to=MetricsCounters,
        )

    def get_revenue_attribution(
        self,
        campaign_guid: str,
        *,
        attribution_model: str | Omit = omit,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueAttributionAggregate:
        """
        Fetch revenue attribution report data for a specified campaign

        Args:
          end_date: End date to fetch attribution data, YYYY-MM-DD

          start_date: Start date to fetch attribution data, YYYY-MM-DD

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}/reports/revenue", campaign_guid=campaign_guid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "attribution_model": attribution_model,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    metric_get_revenue_attribution_params.MetricGetRevenueAttributionParams,
                ),
            ),
            cast_to=RevenueAttributionAggregate,
        )

    def list_contact_ids_by_type(
        self,
        contact_type: str,
        *,
        campaign_guid: str,
        after: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ContactReference]:
        """
        Fetch the list of contact IDs for the specified campaign and contact type

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not contact_type:
            raise ValueError(f"Expected a non-empty value for `contact_type` but received {contact_type!r}")
        return self._get_api_list(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/reports/contacts/{contact_type}",
                campaign_guid=campaign_guid,
                contact_type=contact_type,
            ),
            page=SyncPage[ContactReference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "end_date": end_date,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    metric_list_contact_ids_by_type_params.MetricListContactIDsByTypeParams,
                ),
            ),
            model=ContactReference,
        )


class AsyncMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    async def get_attribution_metrics(
        self,
        campaign_guid: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsCounters:
        """
        This endpoint retrieves key attribution metrics for a specified campaign, such
        as sessions, new contacts, and influenced contacts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}/reports/metrics", campaign_guid=campaign_guid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    metric_get_attribution_metrics_params.MetricGetAttributionMetricsParams,
                ),
            ),
            cast_to=MetricsCounters,
        )

    async def get_revenue_attribution(
        self,
        campaign_guid: str,
        *,
        attribution_model: str | Omit = omit,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueAttributionAggregate:
        """
        Fetch revenue attribution report data for a specified campaign

        Args:
          end_date: End date to fetch attribution data, YYYY-MM-DD

          start_date: Start date to fetch attribution data, YYYY-MM-DD

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}/reports/revenue", campaign_guid=campaign_guid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "attribution_model": attribution_model,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    metric_get_revenue_attribution_params.MetricGetRevenueAttributionParams,
                ),
            ),
            cast_to=RevenueAttributionAggregate,
        )

    def list_contact_ids_by_type(
        self,
        contact_type: str,
        *,
        campaign_guid: str,
        after: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContactReference, AsyncPage[ContactReference]]:
        """
        Fetch the list of contact IDs for the specified campaign and contact type

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not contact_type:
            raise ValueError(f"Expected a non-empty value for `contact_type` but received {contact_type!r}")
        return self._get_api_list(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/reports/contacts/{contact_type}",
                campaign_guid=campaign_guid,
                contact_type=contact_type,
            ),
            page=AsyncPage[ContactReference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "end_date": end_date,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    metric_list_contact_ids_by_type_params.MetricListContactIDsByTypeParams,
                ),
            ),
            model=ContactReference,
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.get_attribution_metrics = to_raw_response_wrapper(
            metrics.get_attribution_metrics,
        )
        self.get_revenue_attribution = to_raw_response_wrapper(
            metrics.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = to_raw_response_wrapper(
            metrics.list_contact_ids_by_type,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.get_attribution_metrics = async_to_raw_response_wrapper(
            metrics.get_attribution_metrics,
        )
        self.get_revenue_attribution = async_to_raw_response_wrapper(
            metrics.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = async_to_raw_response_wrapper(
            metrics.list_contact_ids_by_type,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.get_attribution_metrics = to_streamed_response_wrapper(
            metrics.get_attribution_metrics,
        )
        self.get_revenue_attribution = to_streamed_response_wrapper(
            metrics.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = to_streamed_response_wrapper(
            metrics.list_contact_ids_by_type,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.get_attribution_metrics = async_to_streamed_response_wrapper(
            metrics.get_attribution_metrics,
        )
        self.get_revenue_attribution = async_to_streamed_response_wrapper(
            metrics.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = async_to_streamed_response_wrapper(
            metrics.list_contact_ids_by_type,
        )
