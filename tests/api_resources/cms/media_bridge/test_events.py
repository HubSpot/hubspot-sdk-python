# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms.media_bridge import (
    EventCreateMediaPlayedEventResponse,
    EventCreateAttentionSpanEventResponse,
    EventCreateMediaPlayedPercentEventResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_attention_span_event(self, client: Hubspot) -> None:
        event = client.cms.media_bridge.events.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )
        assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_attention_span_event_with_all_params(self, client: Hubspot) -> None:
        event = client.cms.media_bridge.events.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            derived_values={
                "total_percent_played": 0,
                "total_seconds_played": 0,
            },
            external_id="externalId",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
            raw_data_string="rawDataString",
        )
        assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_attention_span_event(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.events.with_raw_response.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_attention_span_event(self, client: Hubspot) -> None:
        with client.cms.media_bridge.events.with_streaming_response.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_media_played_event(self, client: Hubspot) -> None:
        event = client.cms.media_bridge.events.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )
        assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_media_played_event_with_all_params(self, client: Hubspot) -> None:
        event = client.cms.media_bridge.events.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            iframe_url="iframeUrl",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_media_played_event(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.events.with_raw_response.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_media_played_event(self, client: Hubspot) -> None:
        with client.cms.media_bridge.events.with_streaming_response.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_media_played_percent_event(self, client: Hubspot) -> None:
        event = client.cms.media_bridge.events.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )
        assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_media_played_percent_event_with_all_params(self, client: Hubspot) -> None:
        event = client.cms.media_bridge.events.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_media_played_percent_event(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.events.with_raw_response.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_media_played_percent_event(self, client: Hubspot) -> None:
        with client.cms.media_bridge.events.with_streaming_response.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_attention_span_event(self, async_client: AsyncHubspot) -> None:
        event = await async_client.cms.media_bridge.events.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )
        assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_attention_span_event_with_all_params(self, async_client: AsyncHubspot) -> None:
        event = await async_client.cms.media_bridge.events.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            derived_values={
                "total_percent_played": 0,
                "total_seconds_played": 0,
            },
            external_id="externalId",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
            raw_data_string="rawDataString",
        )
        assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_attention_span_event(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.events.with_raw_response.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_attention_span_event(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.events.with_streaming_response.create_attention_span_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventCreateAttentionSpanEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_media_played_event(self, async_client: AsyncHubspot) -> None:
        event = await async_client.cms.media_bridge.events.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )
        assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_media_played_event_with_all_params(self, async_client: AsyncHubspot) -> None:
        event = await async_client.cms.media_bridge.events.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            iframe_url="iframeUrl",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_media_played_event(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.events.with_raw_response.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_media_played_event(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.events.with_streaming_response.create_media_played_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventCreateMediaPlayedEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_media_played_percent_event(self, async_client: AsyncHubspot) -> None:
        event = await async_client.cms.media_bridge.events.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )
        assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_media_played_percent_event_with_all_params(self, async_client: AsyncHubspot) -> None:
        event = await async_client.cms.media_bridge.events.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_media_played_percent_event(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.events.with_raw_response.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_media_played_percent_event(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.events.with_streaming_response.create_media_played_percent_event(
            media_type="VIDEO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventCreateMediaPlayedPercentEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
