# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .tax_rates import (
    TaxRatesResource,
    AsyncTaxRatesResource,
    TaxRatesResourceWithRawResponse,
    AsyncTaxRatesResourceWithRawResponse,
    TaxRatesResourceWithStreamingResponse,
    AsyncTaxRatesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .currencies.currencies import (
    CurrenciesResource,
    AsyncCurrenciesResource,
    CurrenciesResourceWithRawResponse,
    AsyncCurrenciesResourceWithRawResponse,
    CurrenciesResourceWithStreamingResponse,
    AsyncCurrenciesResourceWithStreamingResponse,
)

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def currencies(self) -> CurrenciesResource:
        return CurrenciesResource(self._client)

    @cached_property
    def tax_rates(self) -> TaxRatesResource:
        return TaxRatesResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def currencies(self) -> AsyncCurrenciesResource:
        return AsyncCurrenciesResource(self._client)

    @cached_property
    def tax_rates(self) -> AsyncTaxRatesResource:
        return AsyncTaxRatesResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def currencies(self) -> CurrenciesResourceWithRawResponse:
        return CurrenciesResourceWithRawResponse(self._settings.currencies)

    @cached_property
    def tax_rates(self) -> TaxRatesResourceWithRawResponse:
        return TaxRatesResourceWithRawResponse(self._settings.tax_rates)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._settings.users)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def currencies(self) -> AsyncCurrenciesResourceWithRawResponse:
        return AsyncCurrenciesResourceWithRawResponse(self._settings.currencies)

    @cached_property
    def tax_rates(self) -> AsyncTaxRatesResourceWithRawResponse:
        return AsyncTaxRatesResourceWithRawResponse(self._settings.tax_rates)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._settings.users)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def currencies(self) -> CurrenciesResourceWithStreamingResponse:
        return CurrenciesResourceWithStreamingResponse(self._settings.currencies)

    @cached_property
    def tax_rates(self) -> TaxRatesResourceWithStreamingResponse:
        return TaxRatesResourceWithStreamingResponse(self._settings.tax_rates)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._settings.users)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def currencies(self) -> AsyncCurrenciesResourceWithStreamingResponse:
        return AsyncCurrenciesResourceWithStreamingResponse(self._settings.currencies)

    @cached_property
    def tax_rates(self) -> AsyncTaxRatesResourceWithStreamingResponse:
        return AsyncTaxRatesResourceWithStreamingResponse(self._settings.tax_rates)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._settings.users)
