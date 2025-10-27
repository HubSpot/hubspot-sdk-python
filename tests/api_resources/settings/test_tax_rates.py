# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.settings import PublicTaxRateGroup, CollectionResponsePublicTaxRateGroupForwardPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaxRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        tax_rate = client.settings.tax_rates.list()
        assert_matches_type(CollectionResponsePublicTaxRateGroupForwardPaging, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.settings.tax_rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = response.parse()
        assert_matches_type(CollectionResponsePublicTaxRateGroupForwardPaging, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.settings.tax_rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_rate = response.parse()
            assert_matches_type(CollectionResponsePublicTaxRateGroupForwardPaging, tax_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        tax_rate = client.settings.tax_rates.get(
            "taxRateGroupId",
        )
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.settings.tax_rates.with_raw_response.get(
            "taxRateGroupId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = response.parse()
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
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
    def test_path_params_get(self, client: HubSpot) -> None:
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
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        tax_rate = await async_client.settings.tax_rates.list()
        assert_matches_type(CollectionResponsePublicTaxRateGroupForwardPaging, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.tax_rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = await response.parse()
        assert_matches_type(CollectionResponsePublicTaxRateGroupForwardPaging, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.settings.tax_rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_rate = await response.parse()
            assert_matches_type(CollectionResponsePublicTaxRateGroupForwardPaging, tax_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        tax_rate = await async_client.settings.tax_rates.get(
            "taxRateGroupId",
        )
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.settings.tax_rates.with_raw_response.get(
            "taxRateGroupId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_rate = await response.parse()
        assert_matches_type(PublicTaxRateGroup, tax_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
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
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tax_rate_group_id` but received ''"):
            await async_client.settings.tax_rates.with_raw_response.get(
                "",
            )
