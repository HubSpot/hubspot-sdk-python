# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.crm import EventDetail, TimelineEventResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        event = client.crm.timeline.events.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
        )
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        event = client.crm.timeline.events.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
            id="id",
            domain="domain",
            email="art3mis-pup@petspot.com",
            extra_data={
                "questions": [
                    {
                        "answer": "Bark!",
                        "question": "Who's a good girl?",
                    },
                    {
                        "answer": "Woof!",
                        "question": "Do you wanna go on a walk?",
                    },
                ]
            },
            object_id="objectId",
            timeline_i_frame={
                "header_label": "Art3mis dog",
                "height": 400,
                "link_label": "View Art3mis",
                "url": "https://my.petspot.com/pets/Art3mis",
                "width": 600,
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            utk="utk",
        )
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.timeline.events.with_raw_response.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.timeline.events.with_streaming_response.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(TimelineEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_create(self, client: HubSpot) -> None:
        event = client.crm.timeline.events.batch_create(
            inputs=[
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "black",
                        "petName": "Art3mis",
                    },
                },
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "yellow",
                        "petName": "Pocket",
                    },
                },
            ],
        )
        assert event is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_create(self, client: HubSpot) -> None:
        response = client.crm.timeline.events.with_raw_response.batch_create(
            inputs=[
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "black",
                        "petName": "Art3mis",
                    },
                },
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "yellow",
                        "petName": "Pocket",
                    },
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert event is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_create(self, client: HubSpot) -> None:
        with client.crm.timeline.events.with_streaming_response.batch_create(
            inputs=[
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "black",
                        "petName": "Art3mis",
                    },
                },
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "yellow",
                        "petName": "Pocket",
                    },
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert event is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        event = client.crm.timeline.events.get(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.timeline.events.with_raw_response.get(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.timeline.events.with_streaming_response.get(
            event_id="eventId",
            event_template_id="eventTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(TimelineEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.events.with_raw_response.get(
                event_id="eventId",
                event_template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.crm.timeline.events.with_raw_response.get(
                event_id="",
                event_template_id="eventTemplateId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_detail(self, client: HubSpot) -> None:
        event = client.crm.timeline.events.get_detail(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )
        assert_matches_type(EventDetail, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_detail(self, client: HubSpot) -> None:
        response = client.crm.timeline.events.with_raw_response.get_detail(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventDetail, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_detail(self, client: HubSpot) -> None:
        with client.crm.timeline.events.with_streaming_response.get_detail(
            event_id="eventId",
            event_template_id="eventTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventDetail, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_detail(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.events.with_raw_response.get_detail(
                event_id="eventId",
                event_template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.crm.timeline.events.with_raw_response.get_detail(
                event_id="",
                event_template_id="eventTemplateId",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        event = await async_client.crm.timeline.events.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
        )
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        event = await async_client.crm.timeline.events.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
            id="id",
            domain="domain",
            email="art3mis-pup@petspot.com",
            extra_data={
                "questions": [
                    {
                        "answer": "Bark!",
                        "question": "Who's a good girl?",
                    },
                    {
                        "answer": "Woof!",
                        "question": "Do you wanna go on a walk?",
                    },
                ]
            },
            object_id="objectId",
            timeline_i_frame={
                "header_label": "Art3mis dog",
                "height": 400,
                "link_label": "View Art3mis",
                "url": "https://my.petspot.com/pets/Art3mis",
                "width": 600,
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            utk="utk",
        )
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.events.with_raw_response.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.events.with_streaming_response.create(
            event_template_id="1001298",
            tokens={
                "petAge": "string",
                "petColor": "black",
                "petName": "Art3mis",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(TimelineEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_create(self, async_client: AsyncHubSpot) -> None:
        event = await async_client.crm.timeline.events.batch_create(
            inputs=[
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "black",
                        "petName": "Art3mis",
                    },
                },
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "yellow",
                        "petName": "Pocket",
                    },
                },
            ],
        )
        assert event is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.events.with_raw_response.batch_create(
            inputs=[
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "black",
                        "petName": "Art3mis",
                    },
                },
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "yellow",
                        "petName": "Pocket",
                    },
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert event is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.events.with_streaming_response.batch_create(
            inputs=[
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "black",
                        "petName": "Art3mis",
                    },
                },
                {
                    "event_template_id": "1001298",
                    "tokens": {
                        "petAge": "string",
                        "petColor": "yellow",
                        "petName": "Pocket",
                    },
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert event is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        event = await async_client.crm.timeline.events.get(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.events.with_raw_response.get(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(TimelineEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.events.with_streaming_response.get(
            event_id="eventId",
            event_template_id="eventTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(TimelineEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.events.with_raw_response.get(
                event_id="eventId",
                event_template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.crm.timeline.events.with_raw_response.get(
                event_id="",
                event_template_id="eventTemplateId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_detail(self, async_client: AsyncHubSpot) -> None:
        event = await async_client.crm.timeline.events.get_detail(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )
        assert_matches_type(EventDetail, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_detail(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.events.with_raw_response.get_detail(
            event_id="eventId",
            event_template_id="eventTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventDetail, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_detail(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.events.with_streaming_response.get_detail(
            event_id="eventId",
            event_template_id="eventTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventDetail, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_detail(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.events.with_raw_response.get_detail(
                event_id="eventId",
                event_template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.crm.timeline.events.with_raw_response.get_detail(
                event_id="",
                event_template_id="eventTemplateId",
            )
