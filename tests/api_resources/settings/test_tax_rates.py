# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.settings import PublicTaxRateGroup

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaxRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        tax_rate = client.settings.tax_rates.list()
        assert_matches_type(SyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        tax_rate = client.settings.tax_rates.list(
            active=True,
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.settings.tax_rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = response.parse()
        assert_matches_type(SyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.settings.tax_rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_rate = response.parse()
            assert_matches_type(SyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        tax_rate = client.settings.tax_rates.get(
            "taxRateGroupId",
        )
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.settings.tax_rates.with_raw_response.get(
            "taxRateGroupId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = response.parse()
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.settings.tax_rates.with_streaming_response.get(
            "taxRateGroupId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_rate = response.parse()
            assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tax_rate_group_id` but received ''"):
            client.settings.tax_rates.with_raw_response.get(
                "",
            )


class TestAsyncTaxRates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        tax_rate = await async_client.settings.tax_rates.list()
        assert_matches_type(AsyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        tax_rate = await async_client.settings.tax_rates.list(
            active=True,
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.tax_rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = await response.parse()
        assert_matches_type(AsyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.tax_rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_rate = await response.parse()
            assert_matches_type(AsyncPage[PublicTaxRateGroup], tax_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        tax_rate = await async_client.settings.tax_rates.get(
            "taxRateGroupId",
        )
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.tax_rates.with_raw_response.get(
            "taxRateGroupId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = await response.parse()
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.tax_rates.with_streaming_response.get(
            "taxRateGroupId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_rate = await response.parse()
            assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tax_rate_group_id` but received ''"):
            await async_client.settings.tax_rates.with_raw_response.get(
                "",
            )
