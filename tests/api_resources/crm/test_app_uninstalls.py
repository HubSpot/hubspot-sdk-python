# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAppUninstalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_uninstall(self, client: HubSpot) -> None:
        app_uninstall = client.crm.app_uninstalls.uninstall()
        assert app_uninstall is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_uninstall(self, client: HubSpot) -> None:
        response = client.crm.app_uninstalls.with_raw_response.uninstall()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_uninstall = response.parse()
        assert app_uninstall is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_uninstall(self, client: HubSpot) -> None:
        with client.crm.app_uninstalls.with_streaming_response.uninstall() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_uninstall = response.parse()
            assert app_uninstall is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAppUninstalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_uninstall(self, async_client: AsyncHubSpot) -> None:
        app_uninstall = await async_client.crm.app_uninstalls.uninstall()
        assert app_uninstall is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_uninstall(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.app_uninstalls.with_raw_response.uninstall()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_uninstall = await response.parse()
        assert app_uninstall is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_uninstall(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.app_uninstalls.with_streaming_response.uninstall() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_uninstall = await response.parse()
            assert app_uninstall is None

        assert cast(Any, response.is_closed) is True
