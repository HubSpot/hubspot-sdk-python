# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.shared import TaskLocator, ActionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSourceCode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_async(self, client: HubSpot) -> None:
        source_code = client.cms.source_code.extract_async(
            path="path",
        )
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_async(self, client: HubSpot) -> None:
        response = client.cms.source_code.with_raw_response.extract_async(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_async(self, client: HubSpot) -> None:
        with client.cms.source_code.with_streaming_response.extract_async(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = response.parse()
            assert_matches_type(TaskLocator, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_extraction_status(self, client: HubSpot) -> None:
        source_code = client.cms.source_code.get_extraction_status(
            0,
        )
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_extraction_status(self, client: HubSpot) -> None:
        response = client.cms.source_code.with_raw_response.get_extraction_status(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_extraction_status(self, client: HubSpot) -> None:
        with client.cms.source_code.with_streaming_response.get_extraction_status(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = response.parse()
            assert_matches_type(ActionResponse, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSourceCode:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_async(self, async_client: AsyncHubSpot) -> None:
        source_code = await async_client.cms.source_code.extract_async(
            path="path",
        )
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_async(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.source_code.with_raw_response.extract_async(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_async(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.source_code.with_streaming_response.extract_async(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = await response.parse()
            assert_matches_type(TaskLocator, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_extraction_status(self, async_client: AsyncHubSpot) -> None:
        source_code = await async_client.cms.source_code.get_extraction_status(
            0,
        )
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_extraction_status(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.source_code.with_raw_response.get_extraction_status(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_extraction_status(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.source_code.with_streaming_response.get_extraction_status(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = await response.parse()
            assert_matches_type(ActionResponse, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True
