# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.cms import ContentFolder, ContentFolderVersion, BatchResponseContentFolder
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.create(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.create(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.create(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.folders.with_raw_response.update(
                object_id="",
                id="id",
                category=0,
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                name="name",
                parent_folder_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.list()
        assert_matches_type(SyncPage[ContentFolder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.list(
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
        assert_matches_type(SyncPage[ContentFolder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(SyncPage[ContentFolder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(SyncPage[ContentFolder], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.delete(
            object_id="objectId",
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.delete(
            object_id="objectId",
            archived=True,
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.folders.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_get(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.batch_get(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_get_with_all_params(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.batch_get(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_get(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.batch_get(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_get(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.batch_get(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.get(
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.folders.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_revision(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(ContentFolderVersion, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(ContentFolderVersion, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_revision(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(ContentFolderVersion, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.folders.with_raw_response.get_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.folders.with_raw_response.get_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_revisions(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.list_revisions(
            object_id="objectId",
        )
        assert_matches_type(SyncPage[ContentFolderVersion], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_revisions_with_all_params(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.list_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[ContentFolderVersion], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_revisions(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.list_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(SyncPage[ContentFolderVersion], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_revisions(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.list_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(SyncPage[ContentFolderVersion], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_revisions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.folders.with_raw_response.list_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_revision(self, client: Hubspot) -> None:
        folder = client.cms.pages.folders.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.folders.with_raw_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision(self, client: Hubspot) -> None:
        with client.cms.pages.folders.with_streaming_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.folders.with_raw_response.restore_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.folders.with_raw_response.restore_revision(
                revision_id="",
                object_id="objectId",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.create(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.create(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.create(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.update(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.update(
                object_id="",
                id="id",
                category=0,
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                name="name",
                parent_folder_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.list()
        assert_matches_type(AsyncPage[ContentFolder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.list(
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
        assert_matches_type(AsyncPage[ContentFolder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(AsyncPage[ContentFolder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(AsyncPage[ContentFolder], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.delete(
            object_id="objectId",
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.delete(
            object_id="objectId",
            archived=True,
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_get(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.batch_get(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.batch_get(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.batch_get(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.batch_get(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(BatchResponseContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.get(
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_revision(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(ContentFolderVersion, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(ContentFolderVersion, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(ContentFolderVersion, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.get_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.get_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_revisions(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.list_revisions(
            object_id="objectId",
        )
        assert_matches_type(AsyncPage[ContentFolderVersion], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_revisions_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.list_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[ContentFolderVersion], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.list_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(AsyncPage[ContentFolderVersion], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.list_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(AsyncPage[ContentFolderVersion], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_revisions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.list_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_revision(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.cms.pages.folders.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.folders.with_raw_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(ContentFolder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.folders.with_streaming_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(ContentFolder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.restore_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.folders.with_raw_response.restore_revision(
                revision_id="",
                object_id="objectId",
            )
