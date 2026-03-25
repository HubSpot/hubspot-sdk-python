# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.extensions import ExternalSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideoConferencing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        video_conferencing = client.crm.extensions.video_conferencing.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
        )
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        video_conferencing = client.crm.extensions.video_conferencing.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
            delete_meeting_url="deleteMeetingUrl",
            fetch_accounts_uri="fetchAccountsUri",
            update_meeting_url="updateMeetingUrl",
            user_verify_url="userVerifyUrl",
        )
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.extensions.video_conferencing.with_raw_response.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_conferencing = response.parse()
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.extensions.video_conferencing.with_streaming_response.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_conferencing = response.parse()
            assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        video_conferencing = client.crm.extensions.video_conferencing.delete(
            0,
        )
        assert video_conferencing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.extensions.video_conferencing.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_conferencing = response.parse()
        assert video_conferencing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.extensions.video_conferencing.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_conferencing = response.parse()
            assert video_conferencing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        video_conferencing = client.crm.extensions.video_conferencing.get(
            0,
        )
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.extensions.video_conferencing.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_conferencing = response.parse()
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.extensions.video_conferencing.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_conferencing = response.parse()
            assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideoConferencing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        video_conferencing = await async_client.crm.extensions.video_conferencing.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
        )
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        video_conferencing = await async_client.crm.extensions.video_conferencing.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
            delete_meeting_url="deleteMeetingUrl",
            fetch_accounts_uri="fetchAccountsUri",
            update_meeting_url="updateMeetingUrl",
            user_verify_url="userVerifyUrl",
        )
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.video_conferencing.with_raw_response.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_conferencing = await response.parse()
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.video_conferencing.with_streaming_response.update(
            app_id=0,
            create_meeting_url="createMeetingUrl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_conferencing = await response.parse()
            assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        video_conferencing = await async_client.crm.extensions.video_conferencing.delete(
            0,
        )
        assert video_conferencing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.video_conferencing.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_conferencing = await response.parse()
        assert video_conferencing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.video_conferencing.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_conferencing = await response.parse()
            assert video_conferencing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        video_conferencing = await async_client.crm.extensions.video_conferencing.get(
            0,
        )
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.video_conferencing.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_conferencing = await response.parse()
        assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.video_conferencing.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_conferencing = await response.parse()
            assert_matches_type(ExternalSettings, video_conferencing, path=["response"])

        assert cast(Any, response.is_closed) is True
