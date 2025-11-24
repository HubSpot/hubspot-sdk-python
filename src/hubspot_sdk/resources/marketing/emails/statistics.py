# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

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
from ...._base_client import make_request_options
from ....types.marketing.emails import statistic_get_params, statistic_get_histogram_params
from ....types.marketing.aggregate_email_statistics import AggregateEmailStatistics
from ....types.marketing.collection_response_with_total_email_statistic_interval_no_paging import (
    CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
)

__all__ = ["StatisticsResource", "AsyncStatisticsResource"]


class StatisticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return StatisticsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        property: str | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateEmailStatistics:
        """
        Use this endpoint to get aggregated statistics of emails sent in a specified
        time span. It also returns the list of emails that were sent during the time
        span.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          property: Specifies which email properties should be returned. All properties will be
              returned by default.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/marketing/v3/emails/statistics/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "property": property,
                        "start_timestamp": start_timestamp,
                    },
                    statistic_get_params.StatisticGetParams,
                ),
            ),
            cast_to=AggregateEmailStatistics,
        )

    def get_histogram(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        interval: Literal["DAY", "HOUR", "MINUTE", "MONTH", "QUARTER", "QUARTER_HOUR", "SECOND", "WEEK", "YEAR"]
        | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalEmailStatisticIntervalNoPaging:
        """Get aggregated statistics in intervals for a specified time span.

        Each interval
        contains aggregated statistics of the emails that were sent in that time.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          interval: The interval to aggregate statistics for.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/marketing/v3/emails/statistics/histogram",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "interval": interval,
                        "start_timestamp": start_timestamp,
                    },
                    statistic_get_histogram_params.StatisticGetHistogramParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
        )


class AsyncStatisticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncStatisticsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        property: str | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateEmailStatistics:
        """
        Use this endpoint to get aggregated statistics of emails sent in a specified
        time span. It also returns the list of emails that were sent during the time
        span.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          property: Specifies which email properties should be returned. All properties will be
              returned by default.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/marketing/v3/emails/statistics/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "property": property,
                        "start_timestamp": start_timestamp,
                    },
                    statistic_get_params.StatisticGetParams,
                ),
            ),
            cast_to=AggregateEmailStatistics,
        )

    async def get_histogram(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        interval: Literal["DAY", "HOUR", "MINUTE", "MONTH", "QUARTER", "QUARTER_HOUR", "SECOND", "WEEK", "YEAR"]
        | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalEmailStatisticIntervalNoPaging:
        """Get aggregated statistics in intervals for a specified time span.

        Each interval
        contains aggregated statistics of the emails that were sent in that time.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          interval: The interval to aggregate statistics for.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/marketing/v3/emails/statistics/histogram",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "interval": interval,
                        "start_timestamp": start_timestamp,
                    },
                    statistic_get_histogram_params.StatisticGetHistogramParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get = to_raw_response_wrapper(
            statistics.get,
        )
        self.get_histogram = to_raw_response_wrapper(
            statistics.get_histogram,
        )


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get = async_to_raw_response_wrapper(
            statistics.get,
        )
        self.get_histogram = async_to_raw_response_wrapper(
            statistics.get_histogram,
        )


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get = to_streamed_response_wrapper(
            statistics.get,
        )
        self.get_histogram = to_streamed_response_wrapper(
            statistics.get_histogram,
        )


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get = async_to_streamed_response_wrapper(
            statistics.get,
        )
        self.get_histogram = async_to_streamed_response_wrapper(
            statistics.get_histogram,
        )
