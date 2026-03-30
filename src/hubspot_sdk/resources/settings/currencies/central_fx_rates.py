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
from ....types.settings.currencies import central_fx_rate_create_currency_params
from ....types.settings.exchange_rate import ExchangeRate
from ....types.settings.central_exchange_rates_information import CentralExchangeRatesInformation
from ....types.settings.collection_response_currency_code_info_no_paging import (
    CollectionResponseCurrencyCodeInfoNoPaging,
)

__all__ = ["CentralFxRatesResource", "AsyncCentralFxRatesResource"]


class CentralFxRatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CentralFxRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CentralFxRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CentralFxRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CentralFxRatesResourceWithStreamingResponse(self)

    def create_currency(
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
    ) -> ExchangeRate:
        """Create a new currency with central exchange rates in the portal.

        Unsupported
        currencies cannot be added here.

        Args:
          currency_code: The currency code being added to the HubSpot portal for use with central
              exchange rates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/settings/currencies/2026-03/central-fx-rates/add-currency",
            body=maybe_transform(
                {"currency_code": currency_code},
                central_fx_rate_create_currency_params.CentralFxRateCreateCurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRate,
        )

    def get_information(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CentralExchangeRatesInformation:
        """
        Retrieve details on whether the central exchange rates feature is enabled for
        the portal.
        """
        return self._get(
            "/settings/currencies/2026-03/central-fx-rates/information",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CentralExchangeRatesInformation,
        )

    def get_unsupported_currencies(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseCurrencyCodeInfoNoPaging:
        """
        Retrieve a list of currency codes that are not supported by the central exchange
        rates. Unsupported currencies will need to be manually updated.
        """
        return self._get(
            "/settings/currencies/2026-03/central-fx-rates/unsupported-currencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseCurrencyCodeInfoNoPaging,
        )


class AsyncCentralFxRatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCentralFxRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCentralFxRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCentralFxRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCentralFxRatesResourceWithStreamingResponse(self)

    async def create_currency(
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
    ) -> ExchangeRate:
        """Create a new currency with central exchange rates in the portal.

        Unsupported
        currencies cannot be added here.

        Args:
          currency_code: The currency code being added to the HubSpot portal for use with central
              exchange rates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/settings/currencies/2026-03/central-fx-rates/add-currency",
            body=await async_maybe_transform(
                {"currency_code": currency_code},
                central_fx_rate_create_currency_params.CentralFxRateCreateCurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRate,
        )

    async def get_information(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CentralExchangeRatesInformation:
        """
        Retrieve details on whether the central exchange rates feature is enabled for
        the portal.
        """
        return await self._get(
            "/settings/currencies/2026-03/central-fx-rates/information",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CentralExchangeRatesInformation,
        )

    async def get_unsupported_currencies(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseCurrencyCodeInfoNoPaging:
        """
        Retrieve a list of currency codes that are not supported by the central exchange
        rates. Unsupported currencies will need to be manually updated.
        """
        return await self._get(
            "/settings/currencies/2026-03/central-fx-rates/unsupported-currencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseCurrencyCodeInfoNoPaging,
        )


class CentralFxRatesResourceWithRawResponse:
    def __init__(self, central_fx_rates: CentralFxRatesResource) -> None:
        self._central_fx_rates = central_fx_rates

        self.create_currency = to_raw_response_wrapper(
            central_fx_rates.create_currency,
        )
        self.get_information = to_raw_response_wrapper(
            central_fx_rates.get_information,
        )
        self.get_unsupported_currencies = to_raw_response_wrapper(
            central_fx_rates.get_unsupported_currencies,
        )


class AsyncCentralFxRatesResourceWithRawResponse:
    def __init__(self, central_fx_rates: AsyncCentralFxRatesResource) -> None:
        self._central_fx_rates = central_fx_rates

        self.create_currency = async_to_raw_response_wrapper(
            central_fx_rates.create_currency,
        )
        self.get_information = async_to_raw_response_wrapper(
            central_fx_rates.get_information,
        )
        self.get_unsupported_currencies = async_to_raw_response_wrapper(
            central_fx_rates.get_unsupported_currencies,
        )


class CentralFxRatesResourceWithStreamingResponse:
    def __init__(self, central_fx_rates: CentralFxRatesResource) -> None:
        self._central_fx_rates = central_fx_rates

        self.create_currency = to_streamed_response_wrapper(
            central_fx_rates.create_currency,
        )
        self.get_information = to_streamed_response_wrapper(
            central_fx_rates.get_information,
        )
        self.get_unsupported_currencies = to_streamed_response_wrapper(
            central_fx_rates.get_unsupported_currencies,
        )


class AsyncCentralFxRatesResourceWithStreamingResponse:
    def __init__(self, central_fx_rates: AsyncCentralFxRatesResource) -> None:
        self._central_fx_rates = central_fx_rates

        self.create_currency = async_to_streamed_response_wrapper(
            central_fx_rates.create_currency,
        )
        self.get_information = async_to_streamed_response_wrapper(
            central_fx_rates.get_information,
        )
        self.get_unsupported_currencies = async_to_streamed_response_wrapper(
            central_fx_rates.get_unsupported_currencies,
        )
