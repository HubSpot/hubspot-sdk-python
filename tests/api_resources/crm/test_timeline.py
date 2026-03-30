# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.crm import (
    AppEventResolutionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeline:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event(self, client: Hubspot) -> None:
        timeline = client.crm.timeline.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
        )
        assert timeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event_with_all_params(self, client: Hubspot) -> None:
        timeline = client.crm.timeline.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
            domain="domain",
            email="email",
            extra_data={},
            object_id="objectId",
            object_type_fully_qualified_name="objectTypeFullyQualifiedName",
            timeline_i_frame={
                "header_label": "headerLabel",
                "height": 0,
                "link_label": "linkLabel",
                "url": "url",
                "width": 0,
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            utk="utk",
        )
        assert timeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_event(self, client: Hubspot) -> None:
        response = client.crm.timeline.with_raw_response.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeline = response.parse()
        assert timeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_event(self, client: Hubspot) -> None:
        with client.crm.timeline.with_streaming_response.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeline = response.parse()
            assert timeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_project_type(self, client: Hubspot) -> None:
        timeline = client.crm.timeline.create_project_type(
            developer_symbol="developerSymbol",
            project_name="projectName",
        )
        assert_matches_type(AppEventResolutionResponse, timeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_project_type(self, client: Hubspot) -> None:
        response = client.crm.timeline.with_raw_response.create_project_type(
            developer_symbol="developerSymbol",
            project_name="projectName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeline = response.parse()
        assert_matches_type(AppEventResolutionResponse, timeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_project_type(self, client: Hubspot) -> None:
        with client.crm.timeline.with_streaming_response.create_project_type(
            developer_symbol="developerSymbol",
            project_name="projectName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeline = response.parse()
            assert_matches_type(AppEventResolutionResponse, timeline, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeline:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event(self, async_client: AsyncHubspot) -> None:
        timeline = await async_client.crm.timeline.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
        )
        assert timeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event_with_all_params(self, async_client: AsyncHubspot) -> None:
        timeline = await async_client.crm.timeline.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
            domain="domain",
            email="email",
            extra_data={},
            object_id="objectId",
            object_type_fully_qualified_name="objectTypeFullyQualifiedName",
            timeline_i_frame={
                "header_label": "headerLabel",
                "height": 0,
                "link_label": "linkLabel",
                "url": "url",
                "width": 0,
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            utk="utk",
        )
        assert timeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_event(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.timeline.with_raw_response.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeline = await response.parse()
        assert timeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_event(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.timeline.with_streaming_response.create_event(
            id="id",
            event_type_name="eventTypeName",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeline = await response.parse()
            assert timeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_project_type(self, async_client: AsyncHubspot) -> None:
        timeline = await async_client.crm.timeline.create_project_type(
            developer_symbol="developerSymbol",
            project_name="projectName",
        )
        assert_matches_type(AppEventResolutionResponse, timeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_project_type(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.timeline.with_raw_response.create_project_type(
            developer_symbol="developerSymbol",
            project_name="projectName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeline = await response.parse()
        assert_matches_type(AppEventResolutionResponse, timeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_project_type(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.timeline.with_streaming_response.create_project_type(
            developer_symbol="developerSymbol",
            project_name="projectName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeline = await response.parse()
            assert_matches_type(AppEventResolutionResponse, timeline, path=["response"])

        assert cast(Any, response.is_closed) is True
