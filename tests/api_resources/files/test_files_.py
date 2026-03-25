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
    FileActionResponse,
    ImportFromURLTaskLocator,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_import_task_status(self, client: Hubspot) -> None:
        file = client.files.files.get_import_task_status(
            "taskId",
        )
        assert_matches_type(FileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_import_task_status(self, client: Hubspot) -> None:
        response = client.files.files.with_raw_response.get_import_task_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_import_task_status(self, client: Hubspot) -> None:
        with client.files.files.with_streaming_response.get_import_task_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileActionResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_import_task_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.files.files.with_raw_response.get_import_task_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_url_async(self, client: Hubspot) -> None:
        file = client.files.files.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )
        assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_url_async_with_all_params(self, client: Hubspot) -> None:
        file = client.files.files.import_from_url_async(
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
        assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import_from_url_async(self, client: Hubspot) -> None:
        response = client.files.files.with_raw_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import_from_url_async(self, client: Hubspot) -> None:
        with client.files.files.with_streaming_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        file = client.files.files.search()
        assert_matches_type(SyncPage[File], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        file = client.files.files.search(
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
        assert_matches_type(SyncPage[File], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.files.files.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncPage[File], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.files.files.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncPage[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        file = await async_client.files.files.get_import_task_status(
            "taskId",
        )
        assert_matches_type(FileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.files.with_raw_response.get_import_task_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.files.with_streaming_response.get_import_task_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileActionResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_import_task_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.files.files.with_raw_response.get_import_task_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_url_async(self, async_client: AsyncHubspot) -> None:
        file = await async_client.files.files.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )
        assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_url_async_with_all_params(self, async_client: AsyncHubspot) -> None:
        file = await async_client.files.files.import_from_url_async(
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
        assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import_from_url_async(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.files.with_raw_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import_from_url_async(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.files.with_streaming_response.import_from_url_async(
            access="HIDDEN_INDEXABLE",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            overwrite=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(ImportFromURLTaskLocator, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        file = await async_client.files.files.search()
        assert_matches_type(AsyncPage[File], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        file = await async_client.files.files.search(
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
        assert_matches_type(AsyncPage[File], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.files.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncPage[File], file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.files.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncPage[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True
