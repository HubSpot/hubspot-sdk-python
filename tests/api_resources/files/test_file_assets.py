# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.files import (
    File,
    Folder,
    FileStat,
    SignedURL,
    FileActionResponse,
    ImportFromURLTaskLocator,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.create(
            name="name",
        )
        assert_matches_type(Folder, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.create(
            name="name",
            parent_folder_id="parentFolderId",
            parent_path="parentPath",
        )
        assert_matches_type(Folder, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(Folder, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(Folder, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.update(
            file_id="321669910225",
            clear_expires=True,
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.update(
            file_id="321669910225",
            clear_expires=True,
            access="HIDDEN_INDEXABLE",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_usable_in_content=True,
            name="name",
            parent_folder_id="parentFolderId",
            parent_folder_path="parentFolderPath",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.update(
            file_id="321669910225",
            clear_expires=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.update(
            file_id="321669910225",
            clear_expires=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.file_assets.with_raw_response.update(
                file_id="",
                clear_expires=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.delete(
            "321669910225",
        )
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.delete(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.delete(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert file_asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.file_assets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_gdpr_delete(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.gdpr_delete(
            "321669910225",
        )
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_gdpr_delete(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.gdpr_delete(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_gdpr_delete(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.gdpr_delete(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert file_asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_gdpr_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.file_assets.with_raw_response.gdpr_delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.get(
            file_id="321669910225",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.get(
            file_id="321669910225",
            properties=["string"],
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.get(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.get(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.file_assets.with_raw_response.get(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_path(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.get_by_path(
            path="path",
        )
        assert_matches_type(FileStat, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_path_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.get_by_path(
            path="path",
            properties=["string"],
        )
        assert_matches_type(FileStat, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_path(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.get_by_path(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(FileStat, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_path(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.get_by_path(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(FileStat, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_path(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.files.file_assets.with_raw_response.get_by_path(
                path="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_import_task_status(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.get_import_task_status(
            "taskId",
        )
        assert_matches_type(FileActionResponse, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_import_task_status(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.get_import_task_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(FileActionResponse, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_import_task_status(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.get_import_task_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(FileActionResponse, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_import_task_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.files.file_assets.with_raw_response.get_import_task_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_signed_url(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.get_signed_url(
            file_id="321669910225",
        )
        assert_matches_type(SignedURL, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_signed_url_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.get_signed_url(
            file_id="321669910225",
            expiration_seconds=0,
            size="icon",
            upscale=True,
        )
        assert_matches_type(SignedURL, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_signed_url(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.get_signed_url(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(SignedURL, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_signed_url(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.get_signed_url(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(SignedURL, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_signed_url(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.file_assets.with_raw_response.get_signed_url(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_url_async(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )
        assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_url_async_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            folder_id="folderId",
            folder_path="folderPath",
            name="name",
            ttl="ttl",
            url="url",
        )
        assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import_from_url_async(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import_from_url_async(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.replace(
            file_id="321669910225",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.replace(
            file_id="321669910225",
            charset_hunch="charsetHunch",
            file=b"Example data",
            options="options",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.replace(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.replace(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.file_assets.with_raw_response.replace(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.search()
        assert_matches_type(SyncPage[File], file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.search(
            after="after",
            allows_anonymous_access=True,
            before="before",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            encoding="encoding",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            extension="extension",
            file_md5="fileMd5",
            height=0,
            height_gte=0,
            height_lte=0,
            id_gte=0,
            id_lte=0,
            ids=[0],
            is_usable_in_content=True,
            limit=0,
            name="name",
            parent_folder_ids=[0],
            path="path",
            properties=["string"],
            size=0,
            size_gte=0,
            size_lte=0,
            sort=["string"],
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            width=0,
            width_gte=0,
            width_lte=0,
        )
        assert_matches_type(SyncPage[File], file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(SyncPage[File], file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(SyncPage[File], file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.upload()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Hubspot) -> None:
        file_asset = client.files.file_assets.upload(
            charset_hunch="charsetHunch",
            file=b"Example data",
            file_name="fileName",
            folder_id="folderId",
            folder_path="folderPath",
            options="options",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Hubspot) -> None:
        response = client.files.file_assets.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Hubspot) -> None:
        with client.files.file_assets.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFileAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.create(
            name="name",
        )
        assert_matches_type(Folder, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.create(
            name="name",
            parent_folder_id="parentFolderId",
            parent_path="parentPath",
        )
        assert_matches_type(Folder, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(Folder, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(Folder, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.update(
            file_id="321669910225",
            clear_expires=True,
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.update(
            file_id="321669910225",
            clear_expires=True,
            access="HIDDEN_INDEXABLE",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_usable_in_content=True,
            name="name",
            parent_folder_id="parentFolderId",
            parent_folder_path="parentFolderPath",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.update(
            file_id="321669910225",
            clear_expires=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.update(
            file_id="321669910225",
            clear_expires=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.file_assets.with_raw_response.update(
                file_id="",
                clear_expires=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.delete(
            "321669910225",
        )
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.delete(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.delete(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert file_asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.file_assets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_gdpr_delete(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.gdpr_delete(
            "321669910225",
        )
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_gdpr_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.gdpr_delete(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert file_asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_gdpr_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.gdpr_delete(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert file_asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_gdpr_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.file_assets.with_raw_response.gdpr_delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.get(
            file_id="321669910225",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.get(
            file_id="321669910225",
            properties=["string"],
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.get(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.get(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.file_assets.with_raw_response.get(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_path(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.get_by_path(
            path="path",
        )
        assert_matches_type(FileStat, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_path_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.get_by_path(
            path="path",
            properties=["string"],
        )
        assert_matches_type(FileStat, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_path(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.get_by_path(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(FileStat, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_path(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.get_by_path(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(FileStat, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_path(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.files.file_assets.with_raw_response.get_by_path(
                path="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.get_import_task_status(
            "taskId",
        )
        assert_matches_type(FileActionResponse, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.get_import_task_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(FileActionResponse, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.get_import_task_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(FileActionResponse, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.files.file_assets.with_raw_response.get_import_task_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_signed_url(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.get_signed_url(
            file_id="321669910225",
        )
        assert_matches_type(SignedURL, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_signed_url_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.get_signed_url(
            file_id="321669910225",
            expiration_seconds=0,
            size="icon",
            upscale=True,
        )
        assert_matches_type(SignedURL, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_signed_url(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.get_signed_url(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(SignedURL, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_signed_url(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.get_signed_url(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(SignedURL, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_signed_url(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.file_assets.with_raw_response.get_signed_url(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_url_async(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )
        assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_url_async_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            folder_id="folderId",
            folder_path="folderPath",
            name="name",
            ttl="ttl",
            url="url",
        )
        assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import_from_url_async(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import_from_url_async(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(ImportFromURLTaskLocator, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.replace(
            file_id="321669910225",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.replace(
            file_id="321669910225",
            charset_hunch="charsetHunch",
            file=b"Example data",
            options="options",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.replace(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.replace(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.file_assets.with_raw_response.replace(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.search()
        assert_matches_type(AsyncPage[File], file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.search(
            after="after",
            allows_anonymous_access=True,
            before="before",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            encoding="encoding",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            extension="extension",
            file_md5="fileMd5",
            height=0,
            height_gte=0,
            height_lte=0,
            id_gte=0,
            id_lte=0,
            ids=[0],
            is_usable_in_content=True,
            limit=0,
            name="name",
            parent_folder_ids=[0],
            path="path",
            properties=["string"],
            size=0,
            size_gte=0,
            size_lte=0,
            sort=["string"],
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            width=0,
            width_gte=0,
            width_lte=0,
        )
        assert_matches_type(AsyncPage[File], file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(AsyncPage[File], file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(AsyncPage[File], file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.upload()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncHubspot) -> None:
        file_asset = await async_client.files.file_assets.upload(
            charset_hunch="charsetHunch",
            file=b"Example data",
            file_name="fileName",
            folder_id="folderId",
            folder_path="folderPath",
            options="options",
        )
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.file_assets.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_asset = await response.parse()
        assert_matches_type(File, file_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.file_assets.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_asset = await response.parse()
            assert_matches_type(File, file_asset, path=["response"])

        assert cast(Any, response.is_closed) is True
