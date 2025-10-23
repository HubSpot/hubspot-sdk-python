# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.scheduler import (
    ExternalCalenderMeetingEventResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalendar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        calendar = client.scheduler.meetings.calendar.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        calendar = client.scheduler.meetings.calendar.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
                "hs_activity_type": "hs_activity_type",
                "hs_attachment_ids": ["string"],
                "hs_attendee_owner_ids": ["string"],
                "hs_internal_meeting_notes": "hs_internal_meeting_notes",
                "hs_meeting_body": "hs_meeting_body",
                "hs_meeting_location": "hs_meeting_location",
                "hs_meeting_location_type": "hs_meeting_location_type",
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.scheduler.meetings.calendar.with_raw_response.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
            },
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = response.parse()
        assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.scheduler.meetings.calendar.with_streaming_response.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
            },
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = response.parse()
            assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalendar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        calendar = await async_client.scheduler.meetings.calendar.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        calendar = await async_client.scheduler.meetings.calendar.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
                "hs_activity_type": "hs_activity_type",
                "hs_attachment_ids": ["string"],
                "hs_attendee_owner_ids": ["string"],
                "hs_internal_meeting_notes": "hs_internal_meeting_notes",
                "hs_meeting_body": "hs_meeting_body",
                "hs_meeting_location": "hs_meeting_location",
                "hs_meeting_location_type": "hs_meeting_location_type",
                "hubspot_owner_id": "hubspot_owner_id",
            },
            timezone="timezone",
        )
        assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.scheduler.meetings.calendar.with_raw_response.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
            },
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = await response.parse()
        assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.scheduler.meetings.calendar.with_streaming_response.create(
            associations=[
                {
                    "to": {"id": "37295"},
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
                        "time_unit": "timeUnit",
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
            },
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = await response.parse()
            assert_matches_type(ExternalCalenderMeetingEventResponse, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True
