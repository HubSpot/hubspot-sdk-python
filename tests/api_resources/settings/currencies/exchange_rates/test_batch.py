# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.settings import BatchResponseExchangeRate

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        batch = client.settings.currencies.exchange_rates.batch.create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.batch.with_raw_response.create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.batch.with_streaming_response.create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        batch = client.settings.currencies.exchange_rates.batch.update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.batch.with_raw_response.update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.batch.with_streaming_response.update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        batch = client.settings.currencies.exchange_rates.batch.get(
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.settings.currencies.exchange_rates.batch.with_raw_response.get(
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.settings.currencies.exchange_rates.batch.with_streaming_response.get(
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.settings.currencies.exchange_rates.batch.create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.batch.with_raw_response.create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.exchange_rates.batch.with_streaming_response.create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.settings.currencies.exchange_rates.batch.update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.batch.with_raw_response.update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.exchange_rates.batch.with_streaming_response.update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.settings.currencies.exchange_rates.batch.get(
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.currencies.exchange_rates.batch.with_raw_response.get(
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.currencies.exchange_rates.batch.with_streaming_response.get(
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseExchangeRate, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
