# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
    report_get_attribution_metrics_params,
    report_get_revenue_attribution_params,
    report_list_contact_ids_by_type_params,
)
from ....types.marketing.metrics_counters import MetricsCounters
from ....types.marketing.contact_reference import ContactReference
from ....types.marketing.revenue_attribution_aggregate import RevenueAttributionAggregate

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

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
          end_date: End date for the report data, formatted as YYYY-MM-DD. Default value: Current
              date

          start_date:
              The start date for the report data, formatted as YYYY-MM-DD. Default value:
              2006-01-01

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/reports/metrics",
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
                    report_get_attribution_metrics_params.ReportGetAttributionMetricsParams,
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
          attribution_model: Allowed values: LINEAR, FIRST_INTERACTION, LAST_INTERACTION, FULL_PATH,
              U_SHAPED, W_SHAPED, TIME_DECAY, J_SHAPED, INVERSE_J_SHAPED Default value: LINEAR

          end_date: End date for the report data, formatted as YYYY-MM-DD. Default value: Current
              date

          start_date:
              The start date for the report data, formatted as YYYY-MM-DD. Default value:
              2006-01-01

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/reports/revenue",
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
                    report_get_revenue_attribution_params.ReportGetRevenueAttributionParams,
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
          after: A cursor for pagination. If provided, the results will start after the given
              cursor. Example: NTI1Cg%3D%3D

          end_date: End date for the report data, formatted as YYYY-MM-DD. Default value: Current
              date

          limit: Limit for the number of contacts to fetch Default: 100

          start_date:
              The start date for the report data, formatted as YYYY-MM-DD. Default value:
              2006-01-01

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
            f"/marketing/v3/campaigns/{campaign_guid}/reports/contacts/{contact_type}",
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
                    report_list_contact_ids_by_type_params.ReportListContactIDsByTypeParams,
                ),
            ),
            model=ContactReference,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

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
          end_date: End date for the report data, formatted as YYYY-MM-DD. Default value: Current
              date

          start_date:
              The start date for the report data, formatted as YYYY-MM-DD. Default value:
              2006-01-01

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/reports/metrics",
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
                    report_get_attribution_metrics_params.ReportGetAttributionMetricsParams,
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
          attribution_model: Allowed values: LINEAR, FIRST_INTERACTION, LAST_INTERACTION, FULL_PATH,
              U_SHAPED, W_SHAPED, TIME_DECAY, J_SHAPED, INVERSE_J_SHAPED Default value: LINEAR

          end_date: End date for the report data, formatted as YYYY-MM-DD. Default value: Current
              date

          start_date:
              The start date for the report data, formatted as YYYY-MM-DD. Default value:
              2006-01-01

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/reports/revenue",
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
                    report_get_revenue_attribution_params.ReportGetRevenueAttributionParams,
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
          after: A cursor for pagination. If provided, the results will start after the given
              cursor. Example: NTI1Cg%3D%3D

          end_date: End date for the report data, formatted as YYYY-MM-DD. Default value: Current
              date

          limit: Limit for the number of contacts to fetch Default: 100

          start_date:
              The start date for the report data, formatted as YYYY-MM-DD. Default value:
              2006-01-01

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
            f"/marketing/v3/campaigns/{campaign_guid}/reports/contacts/{contact_type}",
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
                    report_list_contact_ids_by_type_params.ReportListContactIDsByTypeParams,
                ),
            ),
            model=ContactReference,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.get_attribution_metrics = to_raw_response_wrapper(
            reports.get_attribution_metrics,
        )
        self.get_revenue_attribution = to_raw_response_wrapper(
            reports.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = to_raw_response_wrapper(
            reports.list_contact_ids_by_type,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.get_attribution_metrics = async_to_raw_response_wrapper(
            reports.get_attribution_metrics,
        )
        self.get_revenue_attribution = async_to_raw_response_wrapper(
            reports.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = async_to_raw_response_wrapper(
            reports.list_contact_ids_by_type,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.get_attribution_metrics = to_streamed_response_wrapper(
            reports.get_attribution_metrics,
        )
        self.get_revenue_attribution = to_streamed_response_wrapper(
            reports.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = to_streamed_response_wrapper(
            reports.list_contact_ids_by_type,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.get_attribution_metrics = async_to_streamed_response_wrapper(
            reports.get_attribution_metrics,
        )
        self.get_revenue_attribution = async_to_streamed_response_wrapper(
            reports.get_revenue_attribution,
        )
        self.list_contact_ids_by_type = async_to_streamed_response_wrapper(
            reports.list_contact_ids_by_type,
        )
