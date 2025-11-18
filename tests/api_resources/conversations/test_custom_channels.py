# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.conversations import (
    PublicChannelIntegrationChannel,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomChannels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        custom_channel = client.conversations.custom_channels.create(
            capabilities={"foo": {}},
            name="name",
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        custom_channel = client.conversations.custom_channels.create(
            capabilities={"foo": {}},
            name="name",
            channel_account_connection_redirect_url="channelAccountConnectionRedirectUrl",
            channel_description="channelDescription",
            channel_logo_url="channelLogoUrl",
            webhook_url="webhookUrl",
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.with_raw_response.create(
            capabilities={"foo": {}},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = response.parse()
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.with_streaming_response.create(
            capabilities={"foo": {}},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = response.parse()
            assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        custom_channel = client.conversations.custom_channels.update(
            channel_id=0,
            capabilities={"foo": {}},
            channel_account_connection_redirect_url={},
            channel_description={},
            channel_logo_url={},
            name={},
            webhook_url={},
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.with_raw_response.update(
            channel_id=0,
            capabilities={"foo": {}},
            channel_account_connection_redirect_url={},
            channel_description={},
            channel_logo_url={},
            name={},
            webhook_url={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = response.parse()
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.with_streaming_response.update(
            channel_id=0,
            capabilities={"foo": {}},
            channel_account_connection_redirect_url={},
            channel_description={},
            channel_logo_url={},
            name={},
            webhook_url={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = response.parse()
            assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        custom_channel = client.conversations.custom_channels.list()
        assert_matches_type(SyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        custom_channel = client.conversations.custom_channels.list(
            after="after",
            default_page_length=0,
            limit=0,
            sort=["string"],
        )
        assert_matches_type(SyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = response.parse()
        assert_matches_type(SyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = response.parse()
            assert_matches_type(SyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        custom_channel = client.conversations.custom_channels.delete(
            0,
        )
        assert custom_channel is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = response.parse()
        assert custom_channel is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = response.parse()
            assert custom_channel is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        custom_channel = client.conversations.custom_channels.get(
            0,
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.conversations.custom_channels.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = response.parse()
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.conversations.custom_channels.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = response.parse()
            assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomChannels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        custom_channel = await async_client.conversations.custom_channels.create(
            capabilities={"foo": {}},
            name="name",
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        custom_channel = await async_client.conversations.custom_channels.create(
            capabilities={"foo": {}},
            name="name",
            channel_account_connection_redirect_url="channelAccountConnectionRedirectUrl",
            channel_description="channelDescription",
            channel_logo_url="channelLogoUrl",
            webhook_url="webhookUrl",
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.with_raw_response.create(
            capabilities={"foo": {}},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = await response.parse()
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.with_streaming_response.create(
            capabilities={"foo": {}},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = await response.parse()
            assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        custom_channel = await async_client.conversations.custom_channels.update(
            channel_id=0,
            capabilities={"foo": {}},
            channel_account_connection_redirect_url={},
            channel_description={},
            channel_logo_url={},
            name={},
            webhook_url={},
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.with_raw_response.update(
            channel_id=0,
            capabilities={"foo": {}},
            channel_account_connection_redirect_url={},
            channel_description={},
            channel_logo_url={},
            name={},
            webhook_url={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = await response.parse()
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.with_streaming_response.update(
            channel_id=0,
            capabilities={"foo": {}},
            channel_account_connection_redirect_url={},
            channel_description={},
            channel_logo_url={},
            name={},
            webhook_url={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = await response.parse()
            assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        custom_channel = await async_client.conversations.custom_channels.list()
        assert_matches_type(AsyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        custom_channel = await async_client.conversations.custom_channels.list(
            after="after",
            default_page_length=0,
            limit=0,
            sort=["string"],
        )
        assert_matches_type(AsyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = await response.parse()
        assert_matches_type(AsyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = await response.parse()
            assert_matches_type(AsyncPage[PublicChannelIntegrationChannel], custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        custom_channel = await async_client.conversations.custom_channels.delete(
            0,
        )
        assert custom_channel is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = await response.parse()
        assert custom_channel is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = await response.parse()
            assert custom_channel is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        custom_channel = await async_client.conversations.custom_channels.get(
            0,
        )
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.custom_channels.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_channel = await response.parse()
        assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.custom_channels.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_channel = await response.parse()
            assert_matches_type(PublicChannelIntegrationChannel, custom_channel, path=["response"])

        assert cast(Any, response.is_closed) is True
