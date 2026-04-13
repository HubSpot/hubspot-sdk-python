# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ....types.meta.origins import ip_range_list_params, ip_range_list_simple_params
from ....types.meta.collection_response_ip_range_no_paging import CollectionResponseIPRangeNoPaging

__all__ = ["IPRangesResource", "AsyncIPRangesResource"]


class IPRangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPRangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return IPRangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPRangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return IPRangesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        direction: List[Literal["INGRESS", "EGRESS"]] | Omit = omit,
        service: List[Literal["EMAIL", "API", "DNS", "WEB_SCRAPING", "TEST_SERVICE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseIPRangeNoPaging:
        """
        Retrieve a collection of IP ranges associated with specific services and
        directions, such as `EMAIL`, `API`, `DNS`, or `WEB_SCRAPING`. The response
        includes details like CIDR notation, description, and the direction of IP
        traffic.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/meta/network-origins/2026-03/ip-ranges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "service": service,
                    },
                    ip_range_list_params.IPRangeListParams,
                ),
            ),
            cast_to=CollectionResponseIPRangeNoPaging,
        )

    def list_simple(
        self,
        *,
        direction: List[Literal["INGRESS", "EGRESS"]] | Omit = omit,
        service: List[Literal["EMAIL", "API", "DNS", "WEB_SCRAPING", "TEST_SERVICE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Retrieve a simplified list of IP ranges for specified services and directions in
        plain text format. This endpoint provides a straightforward representation of IP
        ranges without additional metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/meta/network-origins/2026-03/ip-ranges/simple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "service": service,
                    },
                    ip_range_list_simple_params.IPRangeListSimpleParams,
                ),
            ),
            cast_to=str,
        )


class AsyncIPRangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPRangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPRangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPRangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncIPRangesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        direction: List[Literal["INGRESS", "EGRESS"]] | Omit = omit,
        service: List[Literal["EMAIL", "API", "DNS", "WEB_SCRAPING", "TEST_SERVICE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseIPRangeNoPaging:
        """
        Retrieve a collection of IP ranges associated with specific services and
        directions, such as `EMAIL`, `API`, `DNS`, or `WEB_SCRAPING`. The response
        includes details like CIDR notation, description, and the direction of IP
        traffic.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/meta/network-origins/2026-03/ip-ranges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "service": service,
                    },
                    ip_range_list_params.IPRangeListParams,
                ),
            ),
            cast_to=CollectionResponseIPRangeNoPaging,
        )

    async def list_simple(
        self,
        *,
        direction: List[Literal["INGRESS", "EGRESS"]] | Omit = omit,
        service: List[Literal["EMAIL", "API", "DNS", "WEB_SCRAPING", "TEST_SERVICE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Retrieve a simplified list of IP ranges for specified services and directions in
        plain text format. This endpoint provides a straightforward representation of IP
        ranges without additional metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/meta/network-origins/2026-03/ip-ranges/simple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "service": service,
                    },
                    ip_range_list_simple_params.IPRangeListSimpleParams,
                ),
            ),
            cast_to=str,
        )


class IPRangesResourceWithRawResponse:
    def __init__(self, ip_ranges: IPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = to_raw_response_wrapper(
            ip_ranges.list,
        )
        self.list_simple = to_raw_response_wrapper(
            ip_ranges.list_simple,
        )


class AsyncIPRangesResourceWithRawResponse:
    def __init__(self, ip_ranges: AsyncIPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = async_to_raw_response_wrapper(
            ip_ranges.list,
        )
        self.list_simple = async_to_raw_response_wrapper(
            ip_ranges.list_simple,
        )


class IPRangesResourceWithStreamingResponse:
    def __init__(self, ip_ranges: IPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = to_streamed_response_wrapper(
            ip_ranges.list,
        )
        self.list_simple = to_streamed_response_wrapper(
            ip_ranges.list_simple,
        )


class AsyncIPRangesResourceWithStreamingResponse:
    def __init__(self, ip_ranges: AsyncIPRangesResource) -> None:
        self._ip_ranges = ip_ranges

        self.list = async_to_streamed_response_wrapper(
            ip_ranges.list,
        )
        self.list_simple = async_to_streamed_response_wrapper(
            ip_ranges.list_simple,
        )
