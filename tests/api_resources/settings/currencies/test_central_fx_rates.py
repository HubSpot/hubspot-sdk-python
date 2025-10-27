# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.settings import (
    ExchangeRate,
    CentralExchangeRatesInformation,
    CollectionResponseCurrencyCodeInfoNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCentralFxRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_currency(self, client: HubSpot) -> None:
        central_fx_rate = client.settings.currencies.central_fx_rates.create_currency(
            currency_code="AED",
        )
        assert_matches_type(ExchangeRate, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_currency(self, client: HubSpot) -> None:
        response = client.settings.currencies.central_fx_rates.with_raw_response.create_currency(
            currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        central_fx_rate = response.parse()
        assert_matches_type(ExchangeRate, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_currency(self, client: HubSpot) -> None:
        with client.settings.currencies.central_fx_rates.with_streaming_response.create_currency(
            currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            central_fx_rate = response.parse()
            assert_matches_type(ExchangeRate, central_fx_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_information(self, client: HubSpot) -> None:
        central_fx_rate = client.settings.currencies.central_fx_rates.get_information()
        assert_matches_type(CentralExchangeRatesInformation, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_information(self, client: HubSpot) -> None:
        response = client.settings.currencies.central_fx_rates.with_raw_response.get_information()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        central_fx_rate = response.parse()
        assert_matches_type(CentralExchangeRatesInformation, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_information(self, client: HubSpot) -> None:
        with client.settings.currencies.central_fx_rates.with_streaming_response.get_information() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            central_fx_rate = response.parse()
            assert_matches_type(CentralExchangeRatesInformation, central_fx_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_unsupported_currencies(self, client: HubSpot) -> None:
        central_fx_rate = client.settings.currencies.central_fx_rates.get_unsupported_currencies()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_unsupported_currencies(self, client: HubSpot) -> None:
        response = client.settings.currencies.central_fx_rates.with_raw_response.get_unsupported_currencies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        central_fx_rate = response.parse()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_unsupported_currencies(self, client: HubSpot) -> None:
        with (
            client.settings.currencies.central_fx_rates.with_streaming_response.get_unsupported_currencies()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            central_fx_rate = response.parse()
            assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, central_fx_rate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCentralFxRates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_currency(self, async_client: AsyncHubSpot) -> None:
        central_fx_rate = await async_client.settings.currencies.central_fx_rates.create_currency(
            currency_code="AED",
        )
        assert_matches_type(ExchangeRate, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_currency(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.central_fx_rates.with_raw_response.create_currency(
            currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        central_fx_rate = await response.parse()
        assert_matches_type(ExchangeRate, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_currency(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.central_fx_rates.with_streaming_response.create_currency(
            currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            central_fx_rate = await response.parse()
            assert_matches_type(ExchangeRate, central_fx_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_information(self, async_client: AsyncHubSpot) -> None:
        central_fx_rate = await async_client.settings.currencies.central_fx_rates.get_information()
        assert_matches_type(CentralExchangeRatesInformation, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_information(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.central_fx_rates.with_raw_response.get_information()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        central_fx_rate = await response.parse()
        assert_matches_type(CentralExchangeRatesInformation, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_information(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.settings.currencies.central_fx_rates.with_streaming_response.get_information()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            central_fx_rate = await response.parse()
            assert_matches_type(CentralExchangeRatesInformation, central_fx_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_unsupported_currencies(self, async_client: AsyncHubSpot) -> None:
        central_fx_rate = await async_client.settings.currencies.central_fx_rates.get_unsupported_currencies()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_unsupported_currencies(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.settings.currencies.central_fx_rates.with_raw_response.get_unsupported_currencies()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        central_fx_rate = await response.parse()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, central_fx_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_unsupported_currencies(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.settings.currencies.central_fx_rates.with_streaming_response.get_unsupported_currencies()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            central_fx_rate = await response.parse()
            assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, central_fx_rate, path=["response"])

        assert cast(Any, response.is_closed) is True
