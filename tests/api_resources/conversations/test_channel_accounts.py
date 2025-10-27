# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.conversations import (
    PublicChannelAccount,
    CollectionResponseWithTotalPublicChannelAccountForwardPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        channel_account = client.conversations.channel_accounts.list()
        assert_matches_type(
            CollectionResponseWithTotalPublicChannelAccountForwardPaging, channel_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.conversations.channel_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = response.parse()
        assert_matches_type(
            CollectionResponseWithTotalPublicChannelAccountForwardPaging, channel_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.conversations.channel_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = response.parse()
            assert_matches_type(
                CollectionResponseWithTotalPublicChannelAccountForwardPaging, channel_account, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        channel_account = client.conversations.channel_accounts.get(
            "channelAccountId",
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.conversations.channel_accounts.with_raw_response.get(
            "channelAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.conversations.channel_accounts.with_streaming_response.get(
            "channelAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_account_id` but received ''"):
            client.conversations.channel_accounts.with_raw_response.get(
                "",
            )


class TestAsyncChannelAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        channel_account = await async_client.conversations.channel_accounts.list()
        assert_matches_type(
            CollectionResponseWithTotalPublicChannelAccountForwardPaging, channel_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.conversations.channel_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = await response.parse()
        assert_matches_type(
            CollectionResponseWithTotalPublicChannelAccountForwardPaging, channel_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.conversations.channel_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = await response.parse()
            assert_matches_type(
                CollectionResponseWithTotalPublicChannelAccountForwardPaging, channel_account, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        channel_account = await async_client.conversations.channel_accounts.get(
            "channelAccountId",
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.conversations.channel_accounts.with_raw_response.get(
            "channelAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = await response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.conversations.channel_accounts.with_streaming_response.get(
            "channelAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = await response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_account_id` but received ''"):
            await async_client.conversations.channel_accounts.with_raw_response.get(
                "",
            )
