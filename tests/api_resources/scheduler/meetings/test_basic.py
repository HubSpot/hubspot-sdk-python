# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.scheduler import ExternalBookingInfo, ExternalLinkMetadata, ExternalLinkAvailabilityAndBusyTimes

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBasic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        basic = client.scheduler.meetings.basic.list()
        assert_matches_type(SyncPage[ExternalLinkMetadata], basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        basic = client.scheduler.meetings.basic.list(
            after="after",
            limit=0,
            name="name",
            organizer_user_id="organizerUserId",
            type="GROUP_CALENDAR",
        )
        assert_matches_type(SyncPage[ExternalLinkMetadata], basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.scheduler.meetings.basic.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic = response.parse()
        assert_matches_type(SyncPage[ExternalLinkMetadata], basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.scheduler.meetings.basic.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic = response.parse()
            assert_matches_type(SyncPage[ExternalLinkMetadata], basic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_availability_by_slug(self, client: Hubspot) -> None:
        basic = client.scheduler.meetings.basic.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
        )
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_availability_by_slug_with_all_params(self, client: Hubspot) -> None:
        basic = client.scheduler.meetings.basic.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
            month_offset=0,
        )
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_availability_by_slug(self, client: Hubspot) -> None:
        response = client.scheduler.meetings.basic.with_raw_response.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic = response.parse()
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_availability_by_slug(self, client: Hubspot) -> None:
        with client.scheduler.meetings.basic.with_streaming_response.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic = response.parse()
            assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_availability_by_slug(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.scheduler.meetings.basic.with_raw_response.get_availability_by_slug(
                slug="",
                timezone="timezone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_booking_info_by_slug(self, client: Hubspot) -> None:
        basic = client.scheduler.meetings.basic.get_booking_info_by_slug(
            slug="slug",
            timezone="timezone",
        )
        assert_matches_type(ExternalBookingInfo, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_booking_info_by_slug(self, client: Hubspot) -> None:
        response = client.scheduler.meetings.basic.with_raw_response.get_booking_info_by_slug(
            slug="slug",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic = response.parse()
        assert_matches_type(ExternalBookingInfo, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_booking_info_by_slug(self, client: Hubspot) -> None:
        with client.scheduler.meetings.basic.with_streaming_response.get_booking_info_by_slug(
            slug="slug",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic = response.parse()
            assert_matches_type(ExternalBookingInfo, basic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_booking_info_by_slug(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.scheduler.meetings.basic.with_raw_response.get_booking_info_by_slug(
                slug="",
                timezone="timezone",
            )


class TestAsyncBasic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        basic = await async_client.scheduler.meetings.basic.list()
        assert_matches_type(AsyncPage[ExternalLinkMetadata], basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        basic = await async_client.scheduler.meetings.basic.list(
            after="after",
            limit=0,
            name="name",
            organizer_user_id="organizerUserId",
            type="GROUP_CALENDAR",
        )
        assert_matches_type(AsyncPage[ExternalLinkMetadata], basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.scheduler.meetings.basic.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic = await response.parse()
        assert_matches_type(AsyncPage[ExternalLinkMetadata], basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.scheduler.meetings.basic.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic = await response.parse()
            assert_matches_type(AsyncPage[ExternalLinkMetadata], basic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_availability_by_slug(self, async_client: AsyncHubspot) -> None:
        basic = await async_client.scheduler.meetings.basic.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
        )
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_availability_by_slug_with_all_params(self, async_client: AsyncHubspot) -> None:
        basic = await async_client.scheduler.meetings.basic.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
            month_offset=0,
        )
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_availability_by_slug(self, async_client: AsyncHubspot) -> None:
        response = await async_client.scheduler.meetings.basic.with_raw_response.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic = await response.parse()
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_availability_by_slug(self, async_client: AsyncHubspot) -> None:
        async with async_client.scheduler.meetings.basic.with_streaming_response.get_availability_by_slug(
            slug="slug",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic = await response.parse()
            assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, basic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_availability_by_slug(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.scheduler.meetings.basic.with_raw_response.get_availability_by_slug(
                slug="",
                timezone="timezone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_booking_info_by_slug(self, async_client: AsyncHubspot) -> None:
        basic = await async_client.scheduler.meetings.basic.get_booking_info_by_slug(
            slug="slug",
            timezone="timezone",
        )
        assert_matches_type(ExternalBookingInfo, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_booking_info_by_slug(self, async_client: AsyncHubspot) -> None:
        response = await async_client.scheduler.meetings.basic.with_raw_response.get_booking_info_by_slug(
            slug="slug",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic = await response.parse()
        assert_matches_type(ExternalBookingInfo, basic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_booking_info_by_slug(self, async_client: AsyncHubspot) -> None:
        async with async_client.scheduler.meetings.basic.with_streaming_response.get_booking_info_by_slug(
            slug="slug",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic = await response.parse()
            assert_matches_type(ExternalBookingInfo, basic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_booking_info_by_slug(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.scheduler.meetings.basic.with_raw_response.get_booking_info_by_slug(
                slug="",
                timezone="timezone",
            )
