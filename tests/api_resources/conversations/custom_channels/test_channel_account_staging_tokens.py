# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.conversations import PublicChannelAccountStagingToken

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelAccountStagingTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        channel_account_staging_token = client.conversations.custom_channels.channel_account_staging_tokens.update(
            account_token="accountToken",
            channel_id="channelId",
            account_name="accountName",
            delivery_identifier={
                "type": "type",
                "value": "value",
            },
        )
        assert_matches_type(PublicChannelAccountStagingToken, channel_account_staging_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.conversations.custom_channels.channel_account_staging_tokens.with_raw_response.update(
            account_token="accountToken",
            channel_id="channelId",
            account_name="accountName",
            delivery_identifier={
                "type": "type",
                "value": "value",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account_staging_token = response.parse()
        assert_matches_type(PublicChannelAccountStagingToken, channel_account_staging_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.conversations.custom_channels.channel_account_staging_tokens.with_streaming_response.update(
            account_token="accountToken",
            channel_id="channelId",
            account_name="accountName",
            delivery_identifier={
                "type": "type",
                "value": "value",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account_staging_token = response.parse()
            assert_matches_type(PublicChannelAccountStagingToken, channel_account_staging_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.conversations.custom_channels.channel_account_staging_tokens.with_raw_response.update(
                account_token="accountToken",
                channel_id="",
                account_name="accountName",
                delivery_identifier={
                    "type": "type",
                    "value": "value",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            client.conversations.custom_channels.channel_account_staging_tokens.with_raw_response.update(
                account_token="",
                channel_id="channelId",
                account_name="accountName",
                delivery_identifier={
                    "type": "type",
                    "value": "value",
                },
            )


class TestAsyncChannelAccountStagingTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        channel_account_staging_token = (
            await async_client.conversations.custom_channels.channel_account_staging_tokens.update(
                account_token="accountToken",
                channel_id="channelId",
                account_name="accountName",
                delivery_identifier={
                    "type": "type",
                    "value": "value",
                },
            )
        )
        assert_matches_type(PublicChannelAccountStagingToken, channel_account_staging_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.conversations.custom_channels.channel_account_staging_tokens.with_raw_response.update(
                account_token="accountToken",
                channel_id="channelId",
                account_name="accountName",
                delivery_identifier={
                    "type": "type",
                    "value": "value",
                },
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_account_staging_token = await response.parse()
        assert_matches_type(PublicChannelAccountStagingToken, channel_account_staging_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.conversations.custom_channels.channel_account_staging_tokens.with_streaming_response.update(
                account_token="accountToken",
                channel_id="channelId",
                account_name="accountName",
                delivery_identifier={
                    "type": "type",
                    "value": "value",
                },
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_account_staging_token = await response.parse()
            assert_matches_type(PublicChannelAccountStagingToken, channel_account_staging_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.conversations.custom_channels.channel_account_staging_tokens.with_raw_response.update(
                account_token="accountToken",
                channel_id="",
                account_name="accountName",
                delivery_identifier={
                    "type": "type",
                    "value": "value",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            await async_client.conversations.custom_channels.channel_account_staging_tokens.with_raw_response.update(
                account_token="",
                channel_id="channelId",
                account_name="accountName",
                delivery_identifier={
                    "type": "type",
                    "value": "value",
                },
            )
