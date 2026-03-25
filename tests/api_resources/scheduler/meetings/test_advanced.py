# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.scheduler import (
    ExternalMeetingBookingResponse,
    ExternalCalenderMeetingEventResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvanced:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        advanced = client.scheduler.meetings.advanced.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        advanced = client.scheduler.meetings.advanced.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
                "hs_activity_type": "hs_activity_type",
                "hs_attachment_ids": ["string"],
                "hs_attendee_owner_ids": ["string"],
                "hs_internal_meeting_notes": "hs_internal_meeting_notes",
                "hs_meeting_body": "hs_meeting_body",
                "hs_meeting_location": "hs_meeting_location",
                "hs_meeting_location_type": "ADDRESS",
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.scheduler.meetings.advanced.with_raw_response.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advanced = response.parse()
        assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.scheduler.meetings.advanced.with_streaming_response.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advanced = response.parse()
            assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_book(self, client: Hubspot) -> None:
        advanced = client.scheduler.meetings.advanced.book(
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
        assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_book_with_all_params(self, client: Hubspot) -> None:
        advanced = client.scheduler.meetings.advanced.book(
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
        assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_book(self, client: Hubspot) -> None:
        response = client.scheduler.meetings.advanced.with_raw_response.book(
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
        advanced = response.parse()
        assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_book(self, client: Hubspot) -> None:
        with client.scheduler.meetings.advanced.with_streaming_response.book(
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

            advanced = response.parse()
            assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdvanced:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        advanced = await async_client.scheduler.meetings.advanced.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        advanced = await async_client.scheduler.meetings.advanced.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
                "hs_activity_type": "hs_activity_type",
                "hs_attachment_ids": ["string"],
                "hs_attendee_owner_ids": ["string"],
                "hs_internal_meeting_notes": "hs_internal_meeting_notes",
                "hs_meeting_body": "hs_meeting_body",
                "hs_meeting_location": "hs_meeting_location",
                "hs_meeting_location_type": "ADDRESS",
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.scheduler.meetings.advanced.with_raw_response.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advanced = await response.parse()
        assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.scheduler.meetings.advanced.with_streaming_response.create(
            organizer_user_id="organizerUserId",
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
            email_reminder_schedule={
                "reminders": [
                    {
                        "number_of_time_units": 0,
                        "time_unit": "DAYS",
                    }
                ],
                "should_include_invite_description": True,
            },
            properties={
                "hs_meeting_end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_outcome": "hs_meeting_outcome",
                "hs_meeting_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hs_meeting_title": "hs_meeting_title",
                "hs_timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advanced = await response.parse()
            assert_matches_type(ExternalCalenderMeetingEventResponse, advanced, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_book(self, async_client: AsyncHubspot) -> None:
        advanced = await async_client.scheduler.meetings.advanced.book(
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
        assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_book_with_all_params(self, async_client: AsyncHubspot) -> None:
        advanced = await async_client.scheduler.meetings.advanced.book(
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
        assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_book(self, async_client: AsyncHubspot) -> None:
        response = await async_client.scheduler.meetings.advanced.with_raw_response.book(
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
        advanced = await response.parse()
        assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_book(self, async_client: AsyncHubspot) -> None:
        async with async_client.scheduler.meetings.advanced.with_streaming_response.book(
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

            advanced = await response.parse()
            assert_matches_type(ExternalMeetingBookingResponse, advanced, path=["response"])

        assert cast(Any, response.is_closed) is True
