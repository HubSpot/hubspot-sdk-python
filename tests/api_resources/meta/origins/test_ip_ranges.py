# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.meta import CollectionResponseIPRangeNoPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPRanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        ip_range = client.meta.origins.ip_ranges.list()
        assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        ip_range = client.meta.origins.ip_ranges.list(
            direction=["INGRESS"],
            service=["EMAIL"],
        )
        assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.meta.origins.ip_ranges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = response.parse()
        assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.meta.origins.ip_ranges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = response.parse()
            assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_simple(self, client: HubSpot) -> None:
        ip_range = client.meta.origins.ip_ranges.list_simple()
        assert_matches_type(str, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_simple_with_all_params(self, client: HubSpot) -> None:
        ip_range = client.meta.origins.ip_ranges.list_simple(
            direction=["INGRESS"],
            service=["EMAIL"],
        )
        assert_matches_type(str, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_simple(self, client: HubSpot) -> None:
        response = client.meta.origins.ip_ranges.with_raw_response.list_simple()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = response.parse()
        assert_matches_type(str, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_simple(self, client: HubSpot) -> None:
        with client.meta.origins.ip_ranges.with_streaming_response.list_simple() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = response.parse()
            assert_matches_type(str, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIPRanges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        ip_range = await async_client.meta.origins.ip_ranges.list()
        assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        ip_range = await async_client.meta.origins.ip_ranges.list(
            direction=["INGRESS"],
            service=["EMAIL"],
        )
        assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.meta.origins.ip_ranges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = await response.parse()
        assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.meta.origins.ip_ranges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = await response.parse()
            assert_matches_type(CollectionResponseIPRangeNoPaging, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_simple(self, async_client: AsyncHubSpot) -> None:
        ip_range = await async_client.meta.origins.ip_ranges.list_simple()
        assert_matches_type(str, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_simple_with_all_params(self, async_client: AsyncHubSpot) -> None:
        ip_range = await async_client.meta.origins.ip_ranges.list_simple(
            direction=["INGRESS"],
            service=["EMAIL"],
        )
        assert_matches_type(str, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_simple(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.meta.origins.ip_ranges.with_raw_response.list_simple()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_range = await response.parse()
        assert_matches_type(str, ip_range, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_simple(self, async_client: AsyncHubSpot) -> None:
        async with async_client.meta.origins.ip_ranges.with_streaming_response.list_simple() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_range = await response.parse()
            assert_matches_type(str, ip_range, path=["response"])

        assert cast(Any, response.is_closed) is True
