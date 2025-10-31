# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.extensions import ChannelConnectionSettingsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelConnectionSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        channel_connection_setting = client.crm.extensions.calling.channel_connection_settings.create(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.channel_connection_settings.with_raw_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.channel_connection_settings.with_streaming_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        channel_connection_setting = client.crm.extensions.calling.channel_connection_settings.update(
            app_id=0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        channel_connection_setting = client.crm.extensions.calling.channel_connection_settings.update(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.channel_connection_settings.with_raw_response.update(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.channel_connection_settings.with_streaming_response.update(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        channel_connection_setting = client.crm.extensions.calling.channel_connection_settings.delete(
            0,
        )
        assert channel_connection_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.channel_connection_settings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = response.parse()
        assert channel_connection_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.channel_connection_settings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = response.parse()
            assert channel_connection_setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        channel_connection_setting = client.crm.extensions.calling.channel_connection_settings.get(
            0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.channel_connection_settings.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.channel_connection_settings.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChannelConnectionSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        channel_connection_setting = await async_client.crm.extensions.calling.channel_connection_settings.create(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.channel_connection_settings.with_raw_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = await response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.channel_connection_settings.with_streaming_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = await response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        channel_connection_setting = await async_client.crm.extensions.calling.channel_connection_settings.update(
            app_id=0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        channel_connection_setting = await async_client.crm.extensions.calling.channel_connection_settings.update(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.channel_connection_settings.with_raw_response.update(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = await response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.channel_connection_settings.with_streaming_response.update(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = await response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        channel_connection_setting = await async_client.crm.extensions.calling.channel_connection_settings.delete(
            0,
        )
        assert channel_connection_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.channel_connection_settings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = await response.parse()
        assert channel_connection_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.channel_connection_settings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = await response.parse()
            assert channel_connection_setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        channel_connection_setting = await async_client.crm.extensions.calling.channel_connection_settings.get(
            0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.channel_connection_settings.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_connection_setting = await response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.channel_connection_settings.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_connection_setting = await response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, channel_connection_setting, path=["response"])

        assert cast(Any, response.is_closed) is True
