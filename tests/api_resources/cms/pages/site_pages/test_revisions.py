# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import PagesPage, PageVersion
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_site_page_revision(self, client: HubSpot) -> None:
        revision = client.cms.pages.site_pages.revisions.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PageVersion, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_site_page_revision(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.revisions.with_raw_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(PageVersion, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_site_page_revision(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.revisions.with_streaming_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(PageVersion, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_site_page_revision(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.revisions.with_raw_response.get_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.site_pages.revisions.with_raw_response.get_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_site_page_revisions(self, client: HubSpot) -> None:
        revision = client.cms.pages.site_pages.revisions.list_site_page_revisions(
            object_id="objectId",
        )
        assert_matches_type(SyncPage[PageVersion], revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_site_page_revisions_with_all_params(self, client: HubSpot) -> None:
        revision = client.cms.pages.site_pages.revisions.list_site_page_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[PageVersion], revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_site_page_revisions(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.revisions.with_raw_response.list_site_page_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(SyncPage[PageVersion], revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_site_page_revisions(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.revisions.with_streaming_response.list_site_page_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(SyncPage[PageVersion], revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_site_page_revisions(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.revisions.with_raw_response.list_site_page_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_site_page_revision(self, client: HubSpot) -> None:
        revision = client.cms.pages.site_pages.revisions.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_site_page_revision(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_site_page_revision(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.revisions.with_streaming_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(PagesPage, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_site_page_revision(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_site_page_revision_to_draft(self, client: HubSpot) -> None:
        revision = client.cms.pages.site_pages.revisions.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_site_page_revision_to_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_site_page_revision_to_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.revisions.with_streaming_response.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(PagesPage, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_site_page_revision_to_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision_to_draft(
                revision_id=0,
                object_id="",
            )


class TestAsyncRevisions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.cms.pages.site_pages.revisions.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PageVersion, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.revisions.with_raw_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(PageVersion, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.revisions.with_streaming_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(PageVersion, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.revisions.with_raw_response.get_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.site_pages.revisions.with_raw_response.get_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_site_page_revisions(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.cms.pages.site_pages.revisions.list_site_page_revisions(
            object_id="objectId",
        )
        assert_matches_type(AsyncPage[PageVersion], revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_site_page_revisions_with_all_params(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.cms.pages.site_pages.revisions.list_site_page_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[PageVersion], revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_site_page_revisions(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.revisions.with_raw_response.list_site_page_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(AsyncPage[PageVersion], revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_site_page_revisions(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.revisions.with_streaming_response.list_site_page_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(AsyncPage[PageVersion], revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_site_page_revisions(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.revisions.with_raw_response.list_site_page_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.cms.pages.site_pages.revisions.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.revisions.with_streaming_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(PagesPage, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_site_page_revision(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_site_page_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.cms.pages.site_pages.revisions.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_site_page_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision_to_draft(
                revision_id=0,
                object_id="objectId",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(PagesPage, revision, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_site_page_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.cms.pages.site_pages.revisions.with_streaming_response.restore_site_page_revision_to_draft(
                revision_id=0,
                object_id="objectId",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(PagesPage, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_site_page_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.revisions.with_raw_response.restore_site_page_revision_to_draft(
                revision_id=0,
                object_id="",
            )
