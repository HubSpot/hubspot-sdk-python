# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.cms import (
    Page,
    PageVersion,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_page_folders(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_page_folders()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_page_folders_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_page_folders(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_landing_page_folders(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_landing_page_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_landing_page_folders(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_landing_page_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_page_folders_by_query(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_page_folders_by_query()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_page_folders_by_query_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_page_folders_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_landing_page_folders_by_query(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_landing_page_folders_by_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_landing_page_folders_by_query(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_landing_page_folders_by_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_page_revision(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_landing_page_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_landing_page_revision(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageVersion, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_landing_page_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.get_landing_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.with_raw_response.get_landing_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_pages(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_pages()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_pages_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_pages(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_landing_pages(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_landing_pages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_landing_pages(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_landing_pages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_pages_by_query(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_pages_by_query()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_landing_pages_by_query_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.get_landing_pages_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_landing_pages_by_query(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_landing_pages_by_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_landing_pages_by_query(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_landing_pages_by_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_site_page_revision(self, client: Hubspot) -> None:
        page = client.cms.pages.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_site_page_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_site_page_revision(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageVersion, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_site_page_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.get_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.with_raw_response.get_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_site_pages(self, client: Hubspot) -> None:
        page = client.cms.pages.get_site_pages()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_site_pages_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.get_site_pages(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_site_pages(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_site_pages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_site_pages(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_site_pages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_site_pages_by_query(self, client: Hubspot) -> None:
        page = client.cms.pages.get_site_pages_by_query()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_site_pages_by_query_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.get_site_pages_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_site_pages_by_query(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.get_site_pages_by_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_site_pages_by_query(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.get_site_pages_by_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_landing_page_revisions(self, client: Hubspot) -> None:
        page = client.cms.pages.list_landing_page_revisions(
            object_id="objectId",
        )
        assert_matches_type(SyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_landing_page_revisions_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.list_landing_page_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_landing_page_revisions(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.list_landing_page_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(SyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_landing_page_revisions(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.list_landing_page_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(SyncPage[PageVersion], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_landing_page_revisions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.list_landing_page_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_site_page_revisions(self, client: Hubspot) -> None:
        page = client.cms.pages.list_site_page_revisions(
            object_id="objectId",
        )
        assert_matches_type(SyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_site_page_revisions_with_all_params(self, client: Hubspot) -> None:
        page = client.cms.pages.list_site_page_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_site_page_revisions(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.list_site_page_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(SyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_site_page_revisions(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.list_site_page_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(SyncPage[PageVersion], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_site_page_revisions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.list_site_page_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_site_page_draft(self, client: Hubspot) -> None:
        page = client.cms.pages.reset_site_page_draft(
            "objectId",
        )
        assert page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset_site_page_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.reset_site_page_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset_site_page_draft(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.reset_site_page_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reset_site_page_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.reset_site_page_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_landing_page_revision(self, client: Hubspot) -> None:
        page = client.cms.pages.restore_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_landing_page_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.restore_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_landing_page_revision(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.restore_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_landing_page_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.restore_landing_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.with_raw_response.restore_landing_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_landing_page_revision_to_draft(self, client: Hubspot) -> None:
        page = client.cms.pages.restore_landing_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_landing_page_revision_to_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.restore_landing_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_landing_page_revision_to_draft(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.restore_landing_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_landing_page_revision_to_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.restore_landing_page_revision_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_site_page_revision(self, client: Hubspot) -> None:
        page = client.cms.pages.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_site_page_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_site_page_revision(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_site_page_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.restore_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.with_raw_response.restore_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_site_page_revision_to_draft(self, client: Hubspot) -> None:
        page = client.cms.pages.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_site_page_revision_to_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.with_raw_response.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_site_page_revision_to_draft(self, client: Hubspot) -> None:
        with client.cms.pages.with_streaming_response.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_site_page_revision_to_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.with_raw_response.restore_site_page_revision_to_draft(
                revision_id=0,
                object_id="",
            )


class TestAsyncPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_page_folders(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_page_folders()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_page_folders_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_page_folders(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_landing_page_folders(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_landing_page_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_landing_page_folders(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_landing_page_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_page_folders_by_query(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_page_folders_by_query()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_page_folders_by_query_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_page_folders_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_landing_page_folders_by_query(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_landing_page_folders_by_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_landing_page_folders_by_query(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_landing_page_folders_by_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageVersion, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.get_landing_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.with_raw_response.get_landing_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_pages(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_pages()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_pages_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_pages(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_landing_pages(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_landing_pages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_landing_pages(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_landing_pages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_pages_by_query(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_pages_by_query()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_landing_pages_by_query_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_landing_pages_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_landing_pages_by_query(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_landing_pages_by_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_landing_pages_by_query(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_landing_pages_by_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_site_page_revision(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_site_page_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageVersion, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_site_page_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageVersion, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_site_page_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.get_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.with_raw_response.get_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_site_pages(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_site_pages()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_site_pages_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_site_pages(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_site_pages(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_site_pages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_site_pages(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_site_pages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_site_pages_by_query(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_site_pages_by_query()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_site_pages_by_query_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.get_site_pages_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_site_pages_by_query(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.get_site_pages_by_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(object, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_site_pages_by_query(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.get_site_pages_by_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_landing_page_revisions(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.list_landing_page_revisions(
            object_id="objectId",
        )
        assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_landing_page_revisions_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.list_landing_page_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_landing_page_revisions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.list_landing_page_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_landing_page_revisions(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.list_landing_page_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_landing_page_revisions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.list_landing_page_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_site_page_revisions(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.list_site_page_revisions(
            object_id="objectId",
        )
        assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_site_page_revisions_with_all_params(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.list_site_page_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_site_page_revisions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.list_site_page_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_site_page_revisions(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.list_site_page_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(AsyncPage[PageVersion], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_site_page_revisions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.list_site_page_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_site_page_draft(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.reset_site_page_draft(
            "objectId",
        )
        assert page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset_site_page_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.reset_site_page_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset_site_page_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.reset_site_page_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reset_site_page_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.reset_site_page_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.restore_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.restore_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.restore_landing_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_landing_page_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.restore_landing_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.with_raw_response.restore_landing_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_landing_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.restore_landing_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_landing_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.restore_landing_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_landing_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.restore_landing_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_landing_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.restore_landing_page_revision_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_site_page_revision(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_site_page_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_site_page_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.restore_site_page_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_site_page_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.restore_site_page_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.with_raw_response.restore_site_page_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_site_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        page = await async_client.cms.pages.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_site_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.with_raw_response.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Page, page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_site_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.with_streaming_response.restore_site_page_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_site_page_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.with_raw_response.restore_site_page_revision_to_draft(
                revision_id=0,
                object_id="",
            )
