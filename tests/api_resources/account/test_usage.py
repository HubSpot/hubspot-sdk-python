# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.account import CollectionResponseAPIUsage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_daily_private_apps_usage(self, client: Hubspot) -> None:
        usage = client.account.usage.get_daily_private_apps_usage()
        assert_matches_type(CollectionResponseAPIUsage, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_daily_private_apps_usage(self, client: Hubspot) -> None:
        response = client.account.usage.with_raw_response.get_daily_private_apps_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(CollectionResponseAPIUsage, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_private_apps_usage(self, client: Hubspot) -> None:
        with client.account.usage.with_streaming_response.get_daily_private_apps_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(CollectionResponseAPIUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_daily_private_apps_usage(self, async_client: AsyncHubspot) -> None:
        usage = await async_client.account.usage.get_daily_private_apps_usage()
        assert_matches_type(CollectionResponseAPIUsage, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_private_apps_usage(self, async_client: AsyncHubspot) -> None:
        response = await async_client.account.usage.with_raw_response.get_daily_private_apps_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(CollectionResponseAPIUsage, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_private_apps_usage(self, async_client: AsyncHubspot) -> None:
        async with async_client.account.usage.with_streaming_response.get_daily_private_apps_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(CollectionResponseAPIUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
