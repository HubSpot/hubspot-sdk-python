# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.conversations import PublicChannel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        channel = client.conversations.channels.list()
        assert_matches_type(SyncPage[PublicChannel], channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        channel = client.conversations.channels.list(
            after="after",
            default_page_length=0,
            limit=0,
            sort=["string"],
        )
        assert_matches_type(SyncPage[PublicChannel], channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.conversations.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(SyncPage[PublicChannel], channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.conversations.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(SyncPage[PublicChannel], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        channel = client.conversations.channels.get(
            0,
        )
        assert_matches_type(PublicChannel, channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.conversations.channels.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(PublicChannel, channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.conversations.channels.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(PublicChannel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChannels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        channel = await async_client.conversations.channels.list()
        assert_matches_type(AsyncPage[PublicChannel], channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        channel = await async_client.conversations.channels.list(
            after="after",
            default_page_length=0,
            limit=0,
            sort=["string"],
        )
        assert_matches_type(AsyncPage[PublicChannel], channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(AsyncPage[PublicChannel], channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(AsyncPage[PublicChannel], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        channel = await async_client.conversations.channels.get(
            0,
        )
        assert_matches_type(PublicChannel, channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.channels.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(PublicChannel, channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.channels.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(PublicChannel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True
