# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import (
    IndexedData,
    PublicSearchResults,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSiteSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_indexed_data(self, client: HubSpot) -> None:
        site_search = client.cms.site_search.get_indexed_data(
            content_id="contentId",
        )
        assert_matches_type(IndexedData, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_indexed_data_with_all_params(self, client: HubSpot) -> None:
        site_search = client.cms.site_search.get_indexed_data(
            content_id="contentId",
            type="type",
        )
        assert_matches_type(IndexedData, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_indexed_data(self, client: HubSpot) -> None:
        response = client.cms.site_search.with_raw_response.get_indexed_data(
            content_id="contentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_search = response.parse()
        assert_matches_type(IndexedData, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_indexed_data(self, client: HubSpot) -> None:
        with client.cms.site_search.with_streaming_response.get_indexed_data(
            content_id="contentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_search = response.parse()
            assert_matches_type(IndexedData, site_search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_indexed_data(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `content_id` but received ''"):
            client.cms.site_search.with_raw_response.get_indexed_data(
                content_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: HubSpot) -> None:
        site_search = client.cms.site_search.search()
        assert_matches_type(PublicSearchResults, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HubSpot) -> None:
        site_search = client.cms.site_search.search(
            analytics=True,
            autocomplete=True,
            boost_limit=0,
            boost_recent="boostRecent",
            domain=["string"],
            group_id=[0],
            hubdb_query="hubdbQuery",
            language="aa",
            length="LONG",
            limit=0,
            match_prefix=True,
            offset=0,
            path_prefix=["string"],
            popularity_boost=0,
            property=["string"],
            q="q",
            table_id=0,
            type=["string"],
            types=["LANDING_PAGE"],
        )
        assert_matches_type(PublicSearchResults, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HubSpot) -> None:
        response = client.cms.site_search.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_search = response.parse()
        assert_matches_type(PublicSearchResults, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HubSpot) -> None:
        with client.cms.site_search.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_search = response.parse()
            assert_matches_type(PublicSearchResults, site_search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSiteSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_indexed_data(self, async_client: AsyncHubSpot) -> None:
        site_search = await async_client.cms.site_search.get_indexed_data(
            content_id="contentId",
        )
        assert_matches_type(IndexedData, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_indexed_data_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_search = await async_client.cms.site_search.get_indexed_data(
            content_id="contentId",
            type="type",
        )
        assert_matches_type(IndexedData, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_indexed_data(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.site_search.with_raw_response.get_indexed_data(
            content_id="contentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_search = await response.parse()
        assert_matches_type(IndexedData, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_indexed_data(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.site_search.with_streaming_response.get_indexed_data(
            content_id="contentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_search = await response.parse()
            assert_matches_type(IndexedData, site_search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_indexed_data(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `content_id` but received ''"):
            await async_client.cms.site_search.with_raw_response.get_indexed_data(
                content_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubSpot) -> None:
        site_search = await async_client.cms.site_search.search()
        assert_matches_type(PublicSearchResults, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_search = await async_client.cms.site_search.search(
            analytics=True,
            autocomplete=True,
            boost_limit=0,
            boost_recent="boostRecent",
            domain=["string"],
            group_id=[0],
            hubdb_query="hubdbQuery",
            language="aa",
            length="LONG",
            limit=0,
            match_prefix=True,
            offset=0,
            path_prefix=["string"],
            popularity_boost=0,
            property=["string"],
            q="q",
            table_id=0,
            type=["string"],
            types=["LANDING_PAGE"],
        )
        assert_matches_type(PublicSearchResults, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.site_search.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_search = await response.parse()
        assert_matches_type(PublicSearchResults, site_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.site_search.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_search = await response.parse()
            assert_matches_type(PublicSearchResults, site_search, path=["response"])

        assert cast(Any, response.is_closed) is True
