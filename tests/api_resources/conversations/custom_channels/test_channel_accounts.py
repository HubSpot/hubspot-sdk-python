# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.conversations import PublicChannelAccount

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
            delivery_identifier={
                "type": "type",
                "value": "value",
            },
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.channel_accounts.with_raw_response.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.channel_accounts.with_streaming_response.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.update(
            channel_account_id=0,
            channel_id=0,
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.update(
            channel_account_id=0,
            channel_id=0,
            authorized=True,
            name="name",
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.channel_accounts.with_raw_response.update(
            channel_account_id=0,
            channel_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.channel_accounts.with_streaming_response.update(
            channel_account_id=0,
            channel_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.list(
            channel_id=0,
        )
        assert_matches_type(SyncPage[PublicChannelAccount], channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.list(
            channel_id=0,
            after="after",
            archived=True,
            default_page_length=0,
            delivery_identifier_type=["string"],
            delivery_identifier_value=["string"],
            limit=0,
            sort=["string"],
        )
        assert_matches_type(SyncPage[PublicChannelAccount], channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.channel_accounts.with_raw_response.list(
            channel_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = response.parse()
        assert_matches_type(SyncPage[PublicChannelAccount], channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.channel_accounts.with_streaming_response.list(
            channel_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = response.parse()
            assert_matches_type(SyncPage[PublicChannelAccount], channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.get(
            channel_account_id=0,
            channel_id=0,
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        channel_account = client.conversations.custom_channels.channel_accounts.get(
            channel_account_id=0,
            channel_id=0,
            archived=True,
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.channel_accounts.with_raw_response.get(
            channel_account_id=0,
            channel_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.channel_accounts.with_streaming_response.get(
            channel_account_id=0,
            channel_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChannelAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
            delivery_identifier={
                "type": "type",
                "value": "value",
            },
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.channel_accounts.with_raw_response.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = await response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.channel_accounts.with_streaming_response.create(
            channel_id=0,
            authorized=True,
            inbox_id="inboxId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = await response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.update(
            channel_account_id=0,
            channel_id=0,
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.update(
            channel_account_id=0,
            channel_id=0,
            authorized=True,
            name="name",
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.channel_accounts.with_raw_response.update(
            channel_account_id=0,
            channel_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = await response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.channel_accounts.with_streaming_response.update(
            channel_account_id=0,
            channel_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = await response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.list(
            channel_id=0,
        )
        assert_matches_type(AsyncPage[PublicChannelAccount], channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.list(
            channel_id=0,
            after="after",
            archived=True,
            default_page_length=0,
            delivery_identifier_type=["string"],
            delivery_identifier_value=["string"],
            limit=0,
            sort=["string"],
        )
        assert_matches_type(AsyncPage[PublicChannelAccount], channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.channel_accounts.with_raw_response.list(
            channel_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = await response.parse()
        assert_matches_type(AsyncPage[PublicChannelAccount], channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.channel_accounts.with_streaming_response.list(
            channel_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = await response.parse()
            assert_matches_type(AsyncPage[PublicChannelAccount], channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.get(
            channel_account_id=0,
            channel_id=0,
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        channel_account = await async_client.conversations.custom_channels.channel_accounts.get(
            channel_account_id=0,
            channel_id=0,
            archived=True,
        )
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.channel_accounts.with_raw_response.get(
            channel_account_id=0,
            channel_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account = await response.parse()
        assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.channel_accounts.with_streaming_response.get(
            channel_account_id=0,
            channel_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account = await response.parse()
            assert_matches_type(PublicChannelAccount, channel_account, path=["response"])

        assert cast(Any, response.is_closed) is True
