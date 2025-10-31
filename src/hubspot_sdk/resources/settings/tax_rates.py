# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.settings.tax_rate_get_response import TaxRateGetResponse
from ...types.settings.tax_rate_list_response import TaxRateListResponse

__all__ = ["TaxRatesResource", "AsyncTaxRatesResource"]


class TaxRatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaxRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TaxRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaxRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return TaxRatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxRateListResponse:
        """
        Retrieve a paginated list of all tax rates set up in the account tax rate
        library
        """
        return self._get(
            "/tax-rates/v1/tax-rates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxRateListResponse,
        )

    def get(
        self,
        tax_rate_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxRateGetResponse:
        """
        Retrieve a specific tax rate by its `taxRateGroupId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tax_rate_group_id:
            raise ValueError(f"Expected a non-empty value for `tax_rate_group_id` but received {tax_rate_group_id!r}")
        return self._get(
            f"/tax-rates/v1/tax-rates/{tax_rate_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxRateGetResponse,
        )


class AsyncTaxRatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaxRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaxRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaxRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTaxRatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxRateListResponse:
        """
        Retrieve a paginated list of all tax rates set up in the account tax rate
        library
        """
        return await self._get(
            "/tax-rates/v1/tax-rates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxRateListResponse,
        )

    async def get(
        self,
        tax_rate_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxRateGetResponse:
        """
        Retrieve a specific tax rate by its `taxRateGroupId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tax_rate_group_id:
            raise ValueError(f"Expected a non-empty value for `tax_rate_group_id` but received {tax_rate_group_id!r}")
        return await self._get(
            f"/tax-rates/v1/tax-rates/{tax_rate_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxRateGetResponse,
        )


class TaxRatesResourceWithRawResponse:
    def __init__(self, tax_rates: TaxRatesResource) -> None:
        self._tax_rates = tax_rates

        self.list = to_raw_response_wrapper(
            tax_rates.list,
        )
        self.get = to_raw_response_wrapper(
            tax_rates.get,
        )


class AsyncTaxRatesResourceWithRawResponse:
    def __init__(self, tax_rates: AsyncTaxRatesResource) -> None:
        self._tax_rates = tax_rates

        self.list = async_to_raw_response_wrapper(
            tax_rates.list,
        )
        self.get = async_to_raw_response_wrapper(
            tax_rates.get,
        )


class TaxRatesResourceWithStreamingResponse:
    def __init__(self, tax_rates: TaxRatesResource) -> None:
        self._tax_rates = tax_rates

        self.list = to_streamed_response_wrapper(
            tax_rates.list,
        )
        self.get = to_streamed_response_wrapper(
            tax_rates.get,
        )


class AsyncTaxRatesResourceWithStreamingResponse:
    def __init__(self, tax_rates: AsyncTaxRatesResource) -> None:
        self._tax_rates = tax_rates

        self.list = async_to_streamed_response_wrapper(
            tax_rates.list,
        )
        self.get = async_to_streamed_response_wrapper(
            tax_rates.get,
        )
