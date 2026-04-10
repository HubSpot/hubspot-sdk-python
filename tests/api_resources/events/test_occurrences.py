# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.events import ExternalUnifiedEvent, VisibleExternalEventTypeNames

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOccurrences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        occurrence = client.events.occurrences.list()
        assert_matches_type(SyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        occurrence = client.events.occurrences.list(
            id=["string"],
            after="after",
            before="before",
            event_type="eventType",
            limit=0,
            object_id=0,
            object_property={"propname": {}},
            object_type="objectType",
            occurred_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            occurred_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            properties=["string"],
            property={"propname": {}},
            sort=["string"],
        )
        assert_matches_type(SyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.events.occurrences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        occurrence = response.parse()
        assert_matches_type(SyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.events.occurrences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            occurrence = response.parse()
            assert_matches_type(SyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_event_types(self, client: HubSpot) -> None:
        occurrence = client.events.occurrences.list_event_types()
        assert_matches_type(VisibleExternalEventTypeNames, occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_event_types(self, client: HubSpot) -> None:
        response = client.events.occurrences.with_raw_response.list_event_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        occurrence = response.parse()
        assert_matches_type(VisibleExternalEventTypeNames, occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_event_types(self, client: HubSpot) -> None:
        with client.events.occurrences.with_streaming_response.list_event_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            occurrence = response.parse()
            assert_matches_type(VisibleExternalEventTypeNames, occurrence, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOccurrences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        occurrence = await async_client.events.occurrences.list()
        assert_matches_type(AsyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        occurrence = await async_client.events.occurrences.list(
            id=["string"],
            after="after",
            before="before",
            event_type="eventType",
            limit=0,
            object_id=0,
            object_property={"propname": {}},
            object_type="objectType",
            occurred_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            occurred_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            properties=["string"],
            property={"propname": {}},
            sort=["string"],
        )
        assert_matches_type(AsyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.occurrences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        occurrence = await response.parse()
        assert_matches_type(AsyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.occurrences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            occurrence = await response.parse()
            assert_matches_type(AsyncPage[ExternalUnifiedEvent], occurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_event_types(self, async_client: AsyncHubSpot) -> None:
        occurrence = await async_client.events.occurrences.list_event_types()
        assert_matches_type(VisibleExternalEventTypeNames, occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_event_types(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.occurrences.with_raw_response.list_event_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        occurrence = await response.parse()
        assert_matches_type(VisibleExternalEventTypeNames, occurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_event_types(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.occurrences.with_streaming_response.list_event_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            occurrence = await response.parse()
            assert_matches_type(VisibleExternalEventTypeNames, occurrence, path=["response"])

        assert cast(Any, response.is_closed) is True
