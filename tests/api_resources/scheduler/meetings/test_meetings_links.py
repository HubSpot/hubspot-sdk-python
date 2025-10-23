# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.scheduler import (
    ExternalBookingInfo,
    ExternalMeetingBookingResponse,
    ExternalLinkAvailabilityAndBusyTimes,
    CollectionResponseWithTotalExternalLinkMetadataForwardPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeetingsLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        meetings_link = client.scheduler.meetings.meetings_links.list()
        assert_matches_type(
            CollectionResponseWithTotalExternalLinkMetadataForwardPaging, meetings_link, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.scheduler.meetings.meetings_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = response.parse()
        assert_matches_type(
            CollectionResponseWithTotalExternalLinkMetadataForwardPaging, meetings_link, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.scheduler.meetings.meetings_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = response.parse()
            assert_matches_type(
                CollectionResponseWithTotalExternalLinkMetadataForwardPaging, meetings_link, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_book(self, client: HubSpot) -> None:
        meetings_link = client.scheduler.meetings.meetings_links.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_book_with_all_params(self, client: HubSpot) -> None:
        meetings_link = client.scheduler.meetings.meetings_links.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            locale="locale",
            timezone="timezone",
        )
        assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_book(self, client: HubSpot) -> None:
        response = client.scheduler.meetings.meetings_links.with_raw_response.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = response.parse()
        assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_book(self, client: HubSpot) -> None:
        with client.scheduler.meetings.meetings_links.with_streaming_response.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = response.parse()
            assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_availability_by_slug(self, client: HubSpot) -> None:
        meetings_link = client.scheduler.meetings.meetings_links.get_availability_by_slug(
            "slug",
        )
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_availability_by_slug(self, client: HubSpot) -> None:
        response = client.scheduler.meetings.meetings_links.with_raw_response.get_availability_by_slug(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = response.parse()
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_availability_by_slug(self, client: HubSpot) -> None:
        with client.scheduler.meetings.meetings_links.with_streaming_response.get_availability_by_slug(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = response.parse()
            assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, meetings_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_availability_by_slug(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.scheduler.meetings.meetings_links.with_raw_response.get_availability_by_slug(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_booking_info_by_slug(self, client: HubSpot) -> None:
        meetings_link = client.scheduler.meetings.meetings_links.get_booking_info_by_slug(
            "slug",
        )
        assert_matches_type(ExternalBookingInfo, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_booking_info_by_slug(self, client: HubSpot) -> None:
        response = client.scheduler.meetings.meetings_links.with_raw_response.get_booking_info_by_slug(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = response.parse()
        assert_matches_type(ExternalBookingInfo, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_booking_info_by_slug(self, client: HubSpot) -> None:
        with client.scheduler.meetings.meetings_links.with_streaming_response.get_booking_info_by_slug(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = response.parse()
            assert_matches_type(ExternalBookingInfo, meetings_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_booking_info_by_slug(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.scheduler.meetings.meetings_links.with_raw_response.get_booking_info_by_slug(
                "",
            )


class TestAsyncMeetingsLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        meetings_link = await async_client.scheduler.meetings.meetings_links.list()
        assert_matches_type(
            CollectionResponseWithTotalExternalLinkMetadataForwardPaging, meetings_link, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.scheduler.meetings.meetings_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = await response.parse()
        assert_matches_type(
            CollectionResponseWithTotalExternalLinkMetadataForwardPaging, meetings_link, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.scheduler.meetings.meetings_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = await response.parse()
            assert_matches_type(
                CollectionResponseWithTotalExternalLinkMetadataForwardPaging, meetings_link, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_book(self, async_client: AsyncHubSpot) -> None:
        meetings_link = await async_client.scheduler.meetings.meetings_links.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_book_with_all_params(self, async_client: AsyncHubSpot) -> None:
        meetings_link = await async_client.scheduler.meetings.meetings_links.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            locale="locale",
            timezone="timezone",
        )
        assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_book(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.scheduler.meetings.meetings_links.with_raw_response.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = await response.parse()
        assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_book(self, async_client: AsyncHubSpot) -> None:
        async with async_client.scheduler.meetings.meetings_links.with_streaming_response.book(
            duration=0,
            email="email",
            first_name="firstName",
            form_fields=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            last_name="lastName",
            legal_consent_responses=[
                {
                    "communication_type_id": "communicationTypeId",
                    "consented": True,
                }
            ],
            likely_available_user_ids=["string"],
            slug="slug",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = await response.parse()
            assert_matches_type(ExternalMeetingBookingResponse, meetings_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_availability_by_slug(self, async_client: AsyncHubSpot) -> None:
        meetings_link = await async_client.scheduler.meetings.meetings_links.get_availability_by_slug(
            "slug",
        )
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_availability_by_slug(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.scheduler.meetings.meetings_links.with_raw_response.get_availability_by_slug(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = await response.parse()
        assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_availability_by_slug(self, async_client: AsyncHubSpot) -> None:
        async with async_client.scheduler.meetings.meetings_links.with_streaming_response.get_availability_by_slug(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = await response.parse()
            assert_matches_type(ExternalLinkAvailabilityAndBusyTimes, meetings_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_availability_by_slug(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.scheduler.meetings.meetings_links.with_raw_response.get_availability_by_slug(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_booking_info_by_slug(self, async_client: AsyncHubSpot) -> None:
        meetings_link = await async_client.scheduler.meetings.meetings_links.get_booking_info_by_slug(
            "slug",
        )
        assert_matches_type(ExternalBookingInfo, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_booking_info_by_slug(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.scheduler.meetings.meetings_links.with_raw_response.get_booking_info_by_slug(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meetings_link = await response.parse()
        assert_matches_type(ExternalBookingInfo, meetings_link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_booking_info_by_slug(self, async_client: AsyncHubSpot) -> None:
        async with async_client.scheduler.meetings.meetings_links.with_streaming_response.get_booking_info_by_slug(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meetings_link = await response.parse()
            assert_matches_type(ExternalBookingInfo, meetings_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_booking_info_by_slug(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.scheduler.meetings.meetings_links.with_raw_response.get_booking_info_by_slug(
                "",
            )
