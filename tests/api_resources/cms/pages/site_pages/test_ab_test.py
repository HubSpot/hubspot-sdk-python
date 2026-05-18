# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import PagesPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAbTest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_site_page_variation(self, client: HubSpot) -> None:
        ab_test = client.cms.pages.site_pages.ab_test.create_site_page_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(PagesPage, ab_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_site_page_variation(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.ab_test.with_raw_response.create_site_page_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ab_test = response.parse()
        assert_matches_type(PagesPage, ab_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_site_page_variation(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.ab_test.with_streaming_response.create_site_page_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ab_test = response.parse()
            assert_matches_type(PagesPage, ab_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_end_site_page_test(self, client: HubSpot) -> None:
        ab_test = client.cms.pages.site_pages.ab_test.end_site_page_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_end_site_page_test(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.ab_test.with_raw_response.end_site_page_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ab_test = response.parse()
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_end_site_page_test(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.ab_test.with_streaming_response.end_site_page_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ab_test = response.parse()
            assert ab_test is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rerun_site_page_test(self, client: HubSpot) -> None:
        ab_test = client.cms.pages.site_pages.ab_test.rerun_site_page_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rerun_site_page_test(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.ab_test.with_raw_response.rerun_site_page_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ab_test = response.parse()
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rerun_site_page_test(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.ab_test.with_streaming_response.rerun_site_page_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ab_test = response.parse()
            assert ab_test is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAbTest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_site_page_variation(self, async_client: AsyncHubSpot) -> None:
        ab_test = await async_client.cms.pages.site_pages.ab_test.create_site_page_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(PagesPage, ab_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_site_page_variation(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.ab_test.with_raw_response.create_site_page_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ab_test = await response.parse()
        assert_matches_type(PagesPage, ab_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_site_page_variation(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.ab_test.with_streaming_response.create_site_page_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ab_test = await response.parse()
            assert_matches_type(PagesPage, ab_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_end_site_page_test(self, async_client: AsyncHubSpot) -> None:
        ab_test = await async_client.cms.pages.site_pages.ab_test.end_site_page_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_end_site_page_test(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.ab_test.with_raw_response.end_site_page_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ab_test = await response.parse()
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_end_site_page_test(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.ab_test.with_streaming_response.end_site_page_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ab_test = await response.parse()
            assert ab_test is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rerun_site_page_test(self, async_client: AsyncHubSpot) -> None:
        ab_test = await async_client.cms.pages.site_pages.ab_test.rerun_site_page_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rerun_site_page_test(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.ab_test.with_raw_response.rerun_site_page_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ab_test = await response.parse()
        assert ab_test is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rerun_site_page_test(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.ab_test.with_streaming_response.rerun_site_page_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ab_test = await response.parse()
            assert ab_test is None

        assert cast(Any, response.is_closed) is True
