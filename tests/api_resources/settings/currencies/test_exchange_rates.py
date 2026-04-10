# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.settings import ExchangeRate, CollectionResponseExchangeRateNoPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExchangeRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_exchange_rate(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_exchange_rate_with_all_params(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_exchange_rate(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.with_raw_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_exchange_rate(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.with_streaming_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_exchange_rate_by_id(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.get_exchange_rate_by_id(
            "exchangeRateId",
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_exchange_rate_by_id(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.with_raw_response.get_exchange_rate_by_id(
            "exchangeRateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_exchange_rate_by_id(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.with_streaming_response.get_exchange_rate_by_id(
            "exchangeRateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_exchange_rate_by_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            client.settings.currencies.exchange_rates.with_raw_response.get_exchange_rate_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_current_exchange_rates(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.list_current_exchange_rates()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_current_exchange_rates(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.with_raw_response.list_current_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_current_exchange_rates(self, client: HubSpot) -> None:
        with (
            client.settings.currencies.exchange_rates.with_streaming_response.list_current_exchange_rates()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CollectionResponseExchangeRateNoPaging, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_exchange_rates(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.list_exchange_rates()
        assert_matches_type(SyncPage[ExchangeRate], exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_exchange_rates_with_all_params(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.list_exchange_rates(
            after="after",
            from_currency_code="AED",
            limit=0,
            to_currency_code="AED",
        )
        assert_matches_type(SyncPage[ExchangeRate], exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_exchange_rates(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.with_raw_response.list_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(SyncPage[ExchangeRate], exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_exchange_rates(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.with_streaming_response.list_exchange_rates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(SyncPage[ExchangeRate], exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_exchange_rate(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_exchange_rate_with_all_params(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_exchange_rate(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.with_raw_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_exchange_rate(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.with_streaming_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_exchange_rate(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            client.settings.currencies.exchange_rates.with_raw_response.update_exchange_rate(
                exchange_rate_id="",
                conversion_rate=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_visibility(self, client: HubSpot) -> None:
        exchange_rate = client.settings.currencies.exchange_rates.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_visibility(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.with_raw_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_visibility(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.with_streaming_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True


class TestAsyncExchangeRates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_exchange_rate(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_exchange_rate_with_all_params(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_exchange_rate(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.with_raw_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_exchange_rate(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.exchange_rates.with_streaming_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_exchange_rate_by_id(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.get_exchange_rate_by_id(
            "exchangeRateId",
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_exchange_rate_by_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.with_raw_response.get_exchange_rate_by_id(
            "exchangeRateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_exchange_rate_by_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.exchange_rates.with_streaming_response.get_exchange_rate_by_id(
            "exchangeRateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_exchange_rate_by_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            await async_client.settings.currencies.exchange_rates.with_raw_response.get_exchange_rate_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_current_exchange_rates(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.list_current_exchange_rates()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_current_exchange_rates(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.with_raw_response.list_current_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_current_exchange_rates(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.settings.currencies.exchange_rates.with_streaming_response.list_current_exchange_rates()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CollectionResponseExchangeRateNoPaging, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_exchange_rates(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.list_exchange_rates()
        assert_matches_type(AsyncPage[ExchangeRate], exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_exchange_rates_with_all_params(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.list_exchange_rates(
            after="after",
            from_currency_code="AED",
            limit=0,
            to_currency_code="AED",
        )
        assert_matches_type(AsyncPage[ExchangeRate], exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_exchange_rates(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.with_raw_response.list_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(AsyncPage[ExchangeRate], exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_exchange_rates(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.settings.currencies.exchange_rates.with_streaming_response.list_exchange_rates()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(AsyncPage[ExchangeRate], exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_exchange_rate(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_exchange_rate_with_all_params(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_exchange_rate(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.with_raw_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_exchange_rate(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.exchange_rates.with_streaming_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(ExchangeRate, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_exchange_rate(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            await async_client.settings.currencies.exchange_rates.with_raw_response.update_exchange_rate(
                exchange_rate_id="",
                conversion_rate=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_visibility(self, async_client: AsyncHubSpot) -> None:
        exchange_rate = await async_client.settings.currencies.exchange_rates.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_visibility(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.with_raw_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_visibility(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.exchange_rates.with_streaming_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True
