# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from .central_fx_rates import (
    CentralFxRatesResource,
    AsyncCentralFxRatesResource,
    CentralFxRatesResourceWithRawResponse,
    AsyncCentralFxRatesResourceWithRawResponse,
    CentralFxRatesResourceWithStreamingResponse,
    AsyncCentralFxRatesResourceWithStreamingResponse,
)
from ....types.settings import currency_update_company_currency_params
from .exchange_rates.exchange_rates import (
    ExchangeRatesResource,
    AsyncExchangeRatesResource,
    ExchangeRatesResourceWithRawResponse,
    AsyncExchangeRatesResourceWithRawResponse,
    ExchangeRatesResourceWithStreamingResponse,
    AsyncExchangeRatesResourceWithStreamingResponse,
)
from ....types.settings.company_currency import CompanyCurrency
from ....types.settings.collection_response_currency_code_info_no_paging import (
    CollectionResponseCurrencyCodeInfoNoPaging,
)

__all__ = ["CurrenciesResource", "AsyncCurrenciesResource"]


class CurrenciesResource(SyncAPIResource):
    @cached_property
    def central_fx_rates(self) -> CentralFxRatesResource:
        return CentralFxRatesResource(self._client)

    @cached_property
    def exchange_rates(self) -> ExchangeRatesResource:
        return ExchangeRatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return CurrenciesResourceWithStreamingResponse(self)

    def get_company_currency(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyCurrency:
        """Get the details for the company currency.

        The company currency is used in deal
        totals, reports, and the default currency for new deals.
        """
        return self._get(
            "/settings/currencies/2026-03/company-currency",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCurrency,
        )

    def list_codes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseCurrencyCodeInfoNoPaging:
        """Retrieve a list of all available currency codes and their names."""
        return self._get(
            "/settings/currencies/2026-03/codes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseCurrencyCodeInfoNoPaging,
        )

    def update_company_currency(
        self,
        *,
        currency_code: Literal[
            "AED",
            "AFN",
            "ALL",
            "AMD",
            "ANG",
            "AOA",
            "ARS",
            "AUD",
            "AWG",
            "AZN",
            "BAM",
            "BBD",
            "BDT",
            "BGN",
            "BHD",
            "BIF",
            "BMD",
            "BND",
            "BOB",
            "BOV",
            "BRL",
            "BSD",
            "BTN",
            "BWP",
            "BYN",
            "BZD",
            "CAD",
            "CDF",
            "CHE",
            "CHF",
            "CHW",
            "CLF",
            "CLP",
            "CNY",
            "COP",
            "COU",
            "CRC",
            "CUC",
            "CUP",
            "CVE",
            "CZK",
            "DJF",
            "DKK",
            "DOP",
            "DZD",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GEL",
            "GHS",
            "GIP",
            "GMD",
            "GNF",
            "GTQ",
            "GYD",
            "HKD",
            "HNL",
            "HRK",
            "HTG",
            "HUF",
            "IDR",
            "ILS",
            "INR",
            "IQD",
            "IRR",
            "ISK",
            "JMD",
            "JOD",
            "JPY",
            "KES",
            "KGS",
            "KHR",
            "KMF",
            "KPW",
            "KRW",
            "KWD",
            "KYD",
            "KZT",
            "LAK",
            "LBP",
            "LKR",
            "LRD",
            "LSL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRU",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MXV",
            "MYR",
            "MZN",
            "NAD",
            "NGN",
            "NIO",
            "NOK",
            "NPR",
            "NZD",
            "OMR",
            "PAB",
            "PEN",
            "PGK",
            "PHP",
            "PKR",
            "PLN",
            "PYG",
            "QAR",
            "RON",
            "RSD",
            "RUB",
            "RWF",
            "SAR",
            "SBD",
            "SCR",
            "SDG",
            "SEK",
            "SGD",
            "SHP",
            "SLL",
            "SOS",
            "SRD",
            "SSP",
            "STN",
            "SVC",
            "SYP",
            "SZL",
            "THB",
            "TJS",
            "TMT",
            "TND",
            "TOP",
            "TRY",
            "TTD",
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "USN",
            "UYI",
            "UYU",
            "UZS",
            "VEF",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XAG",
            "XAU",
            "XBA",
            "XBB",
            "XBC",
            "XBD",
            "XCD",
            "XDR",
            "XOF",
            "XPD",
            "XPF",
            "XPT",
            "XSU",
            "XUA",
            "YER",
            "ZAR",
            "ZMW",
            "ZWL",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyCurrency:
        """
        Set or update the primary company currency.

        Args:
          currency_code: The three-letter code representing a specific currency (ex. USD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/settings/currencies/2026-03/company-currency",
            body=maybe_transform(
                {"currency_code": currency_code},
                currency_update_company_currency_params.CurrencyUpdateCompanyCurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCurrency,
        )


class AsyncCurrenciesResource(AsyncAPIResource):
    @cached_property
    def central_fx_rates(self) -> AsyncCentralFxRatesResource:
        return AsyncCentralFxRatesResource(self._client)

    @cached_property
    def exchange_rates(self) -> AsyncExchangeRatesResource:
        return AsyncExchangeRatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCurrenciesResourceWithStreamingResponse(self)

    async def get_company_currency(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyCurrency:
        """Get the details for the company currency.

        The company currency is used in deal
        totals, reports, and the default currency for new deals.
        """
        return await self._get(
            "/settings/currencies/2026-03/company-currency",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCurrency,
        )

    async def list_codes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseCurrencyCodeInfoNoPaging:
        """Retrieve a list of all available currency codes and their names."""
        return await self._get(
            "/settings/currencies/2026-03/codes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseCurrencyCodeInfoNoPaging,
        )

    async def update_company_currency(
        self,
        *,
        currency_code: Literal[
            "AED",
            "AFN",
            "ALL",
            "AMD",
            "ANG",
            "AOA",
            "ARS",
            "AUD",
            "AWG",
            "AZN",
            "BAM",
            "BBD",
            "BDT",
            "BGN",
            "BHD",
            "BIF",
            "BMD",
            "BND",
            "BOB",
            "BOV",
            "BRL",
            "BSD",
            "BTN",
            "BWP",
            "BYN",
            "BZD",
            "CAD",
            "CDF",
            "CHE",
            "CHF",
            "CHW",
            "CLF",
            "CLP",
            "CNY",
            "COP",
            "COU",
            "CRC",
            "CUC",
            "CUP",
            "CVE",
            "CZK",
            "DJF",
            "DKK",
            "DOP",
            "DZD",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GEL",
            "GHS",
            "GIP",
            "GMD",
            "GNF",
            "GTQ",
            "GYD",
            "HKD",
            "HNL",
            "HRK",
            "HTG",
            "HUF",
            "IDR",
            "ILS",
            "INR",
            "IQD",
            "IRR",
            "ISK",
            "JMD",
            "JOD",
            "JPY",
            "KES",
            "KGS",
            "KHR",
            "KMF",
            "KPW",
            "KRW",
            "KWD",
            "KYD",
            "KZT",
            "LAK",
            "LBP",
            "LKR",
            "LRD",
            "LSL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRU",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MXV",
            "MYR",
            "MZN",
            "NAD",
            "NGN",
            "NIO",
            "NOK",
            "NPR",
            "NZD",
            "OMR",
            "PAB",
            "PEN",
            "PGK",
            "PHP",
            "PKR",
            "PLN",
            "PYG",
            "QAR",
            "RON",
            "RSD",
            "RUB",
            "RWF",
            "SAR",
            "SBD",
            "SCR",
            "SDG",
            "SEK",
            "SGD",
            "SHP",
            "SLL",
            "SOS",
            "SRD",
            "SSP",
            "STN",
            "SVC",
            "SYP",
            "SZL",
            "THB",
            "TJS",
            "TMT",
            "TND",
            "TOP",
            "TRY",
            "TTD",
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "USN",
            "UYI",
            "UYU",
            "UZS",
            "VEF",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XAG",
            "XAU",
            "XBA",
            "XBB",
            "XBC",
            "XBD",
            "XCD",
            "XDR",
            "XOF",
            "XPD",
            "XPF",
            "XPT",
            "XSU",
            "XUA",
            "YER",
            "ZAR",
            "ZMW",
            "ZWL",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyCurrency:
        """
        Set or update the primary company currency.

        Args:
          currency_code: The three-letter code representing a specific currency (ex. USD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/settings/currencies/2026-03/company-currency",
            body=await async_maybe_transform(
                {"currency_code": currency_code},
                currency_update_company_currency_params.CurrencyUpdateCompanyCurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCurrency,
        )


class CurrenciesResourceWithRawResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.get_company_currency = to_raw_response_wrapper(
            currencies.get_company_currency,
        )
        self.list_codes = to_raw_response_wrapper(
            currencies.list_codes,
        )
        self.update_company_currency = to_raw_response_wrapper(
            currencies.update_company_currency,
        )

    @cached_property
    def central_fx_rates(self) -> CentralFxRatesResourceWithRawResponse:
        return CentralFxRatesResourceWithRawResponse(self._currencies.central_fx_rates)

    @cached_property
    def exchange_rates(self) -> ExchangeRatesResourceWithRawResponse:
        return ExchangeRatesResourceWithRawResponse(self._currencies.exchange_rates)


class AsyncCurrenciesResourceWithRawResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.get_company_currency = async_to_raw_response_wrapper(
            currencies.get_company_currency,
        )
        self.list_codes = async_to_raw_response_wrapper(
            currencies.list_codes,
        )
        self.update_company_currency = async_to_raw_response_wrapper(
            currencies.update_company_currency,
        )

    @cached_property
    def central_fx_rates(self) -> AsyncCentralFxRatesResourceWithRawResponse:
        return AsyncCentralFxRatesResourceWithRawResponse(self._currencies.central_fx_rates)

    @cached_property
    def exchange_rates(self) -> AsyncExchangeRatesResourceWithRawResponse:
        return AsyncExchangeRatesResourceWithRawResponse(self._currencies.exchange_rates)


class CurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.get_company_currency = to_streamed_response_wrapper(
            currencies.get_company_currency,
        )
        self.list_codes = to_streamed_response_wrapper(
            currencies.list_codes,
        )
        self.update_company_currency = to_streamed_response_wrapper(
            currencies.update_company_currency,
        )

    @cached_property
    def central_fx_rates(self) -> CentralFxRatesResourceWithStreamingResponse:
        return CentralFxRatesResourceWithStreamingResponse(self._currencies.central_fx_rates)

    @cached_property
    def exchange_rates(self) -> ExchangeRatesResourceWithStreamingResponse:
        return ExchangeRatesResourceWithStreamingResponse(self._currencies.exchange_rates)


class AsyncCurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.get_company_currency = async_to_streamed_response_wrapper(
            currencies.get_company_currency,
        )
        self.list_codes = async_to_streamed_response_wrapper(
            currencies.list_codes,
        )
        self.update_company_currency = async_to_streamed_response_wrapper(
            currencies.update_company_currency,
        )

    @cached_property
    def central_fx_rates(self) -> AsyncCentralFxRatesResourceWithStreamingResponse:
        return AsyncCentralFxRatesResourceWithStreamingResponse(self._currencies.central_fx_rates)

    @cached_property
    def exchange_rates(self) -> AsyncExchangeRatesResourceWithStreamingResponse:
        return AsyncExchangeRatesResourceWithStreamingResponse(self._currencies.exchange_rates)
