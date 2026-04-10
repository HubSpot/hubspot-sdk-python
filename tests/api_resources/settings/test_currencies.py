# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.settings import (
    CompanyCurrency,
    CollectionResponseCurrencyCodeInfoNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrencies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_company_currency(self, client: HubSpot) -> None:
        currency = client.settings.currencies.get_company_currency()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_company_currency(self, client: HubSpot) -> None:
        response = client.settings.currencies.with_raw_response.get_company_currency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_company_currency(self, client: HubSpot) -> None:
        with client.settings.currencies.with_streaming_response.get_company_currency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_codes(self, client: HubSpot) -> None:
        currency = client.settings.currencies.list_codes()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_codes(self, client: HubSpot) -> None:
        response = client.settings.currencies.with_raw_response.list_codes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_codes(self, client: HubSpot) -> None:
        with client.settings.currencies.with_streaming_response.list_codes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_company_currency(self, client: HubSpot) -> None:
        currency = client.settings.currencies.update_company_currency(
            currency_code="AED",
        )
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_company_currency(self, client: HubSpot) -> None:
        response = client.settings.currencies.with_raw_response.update_company_currency(
            currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_company_currency(self, client: HubSpot) -> None:
        with client.settings.currencies.with_streaming_response.update_company_currency(
            currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrencies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_company_currency(self, async_client: AsyncHubSpot) -> None:
        currency = await async_client.settings.currencies.get_company_currency()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_company_currency(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.with_raw_response.get_company_currency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_company_currency(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.with_streaming_response.get_company_currency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_codes(self, async_client: AsyncHubSpot) -> None:
        currency = await async_client.settings.currencies.list_codes()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_codes(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.with_raw_response.list_codes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_codes(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.with_streaming_response.list_codes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_company_currency(self, async_client: AsyncHubSpot) -> None:
        currency = await async_client.settings.currencies.update_company_currency(
            currency_code="AED",
        )
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_company_currency(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.with_raw_response.update_company_currency(
            currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_company_currency(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.with_streaming_response.update_company_currency(
            currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True
