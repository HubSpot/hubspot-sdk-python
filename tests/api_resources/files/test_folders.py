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
    Folder,
    FolderActionResponse,
    FolderUpdateTaskLocator,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_id(self, client: Hubspot) -> None:
        folder = client.files.folders.delete_by_id(
            "321669910225",
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_by_id(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.delete_by_id(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_id(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.delete_by_id(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_by_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.files.folders.with_raw_response.delete_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_path(self, client: Hubspot) -> None:
        folder = client.files.folders.delete_by_path(
            "folderPath",
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_by_path(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.delete_by_path(
            "folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_path(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.delete_by_path(
            "folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_by_path(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            client.files.folders.with_raw_response.delete_by_path(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_id(self, client: Hubspot) -> None:
        folder = client.files.folders.get_by_id(
            folder_id="321669910225",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_id_with_all_params(self, client: Hubspot) -> None:
        folder = client.files.folders.get_by_id(
            folder_id="321669910225",
            properties=["string"],
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_id(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.get_by_id(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_id(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.get_by_id(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.files.folders.with_raw_response.get_by_id(
                folder_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_path(self, client: Hubspot) -> None:
        folder = client.files.folders.get_by_path(
            folder_path="folderPath",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_path_with_all_params(self, client: Hubspot) -> None:
        folder = client.files.folders.get_by_path(
            folder_path="folderPath",
            properties=["string"],
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_path(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.get_by_path(
            folder_path="folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_path(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.get_by_path(
            folder_path="folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_path(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            client.files.folders.with_raw_response.get_by_path(
                folder_path="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_update_async_status(self, client: Hubspot) -> None:
        folder = client.files.folders.get_update_async_status(
            "taskId",
        )
        assert_matches_type(FolderActionResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_update_async_status(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.get_update_async_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderActionResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_update_async_status(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.get_update_async_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderActionResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_update_async_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.files.folders.with_raw_response.get_update_async_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        folder = client.files.folders.search()
        assert_matches_type(SyncPage[Folder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        folder = client.files.folders.search(
            after="after",
            before="before",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_gte=0,
            id_lte=0,
            ids=[0],
            limit=0,
            name="name",
            parent_folder_ids=[0],
            path="path",
            properties=["string"],
            sort=["string"],
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[Folder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(SyncPage[Folder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(SyncPage[Folder], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_async_by_id(self, client: Hubspot) -> None:
        folder = client.files.folders.update_async_by_id(
            id="id",
        )
        assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_async_by_id_with_all_params(self, client: Hubspot) -> None:
        folder = client.files.folders.update_async_by_id(
            id="id",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_async_by_id(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.update_async_by_id(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_async_by_id(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.update_async_by_id(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_id(self, client: Hubspot) -> None:
        folder = client.files.folders.update_by_id(
            folder_id="321669910225",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_id_with_all_params(self, client: Hubspot) -> None:
        folder = client.files.folders.update_by_id(
            folder_id="321669910225",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_by_id(self, client: Hubspot) -> None:
        response = client.files.folders.with_raw_response.update_by_id(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_by_id(self, client: Hubspot) -> None:
        with client.files.folders.with_streaming_response.update_by_id(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_by_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.files.folders.with_raw_response.update_by_id(
                folder_id="",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.delete_by_id(
            "321669910225",
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.delete_by_id(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.delete_by_id(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.files.folders.with_raw_response.delete_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_path(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.delete_by_path(
            "folderPath",
        )
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_path(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.delete_by_path(
            "folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_path(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.delete_by_path(
            "folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_by_path(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            await async_client.files.folders.with_raw_response.delete_by_path(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.get_by_id(
            folder_id="321669910225",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_id_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.get_by_id(
            folder_id="321669910225",
            properties=["string"],
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.get_by_id(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.get_by_id(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.files.folders.with_raw_response.get_by_id(
                folder_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_path(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.get_by_path(
            folder_path="folderPath",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_path_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.get_by_path(
            folder_path="folderPath",
            properties=["string"],
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_path(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.get_by_path(
            folder_path="folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_path(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.get_by_path(
            folder_path="folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_path(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            await async_client.files.folders.with_raw_response.get_by_path(
                folder_path="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_update_async_status(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.get_update_async_status(
            "taskId",
        )
        assert_matches_type(FolderActionResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_update_async_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.get_update_async_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderActionResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_update_async_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.get_update_async_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderActionResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_update_async_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.files.folders.with_raw_response.get_update_async_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.search()
        assert_matches_type(AsyncPage[Folder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.search(
            after="after",
            before="before",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_gte=0,
            id_lte=0,
            ids=[0],
            limit=0,
            name="name",
            parent_folder_ids=[0],
            path="path",
            properties=["string"],
            sort=["string"],
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[Folder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(AsyncPage[Folder], folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(AsyncPage[Folder], folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_async_by_id(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.update_async_by_id(
            id="id",
        )
        assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_async_by_id_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.update_async_by_id(
            id="id",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_async_by_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.update_async_by_id(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_async_by_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.update_async_by_id(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderUpdateTaskLocator, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_id(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.update_by_id(
            folder_id="321669910225",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_id_with_all_params(self, async_client: AsyncHubspot) -> None:
        folder = await async_client.files.folders.update_by_id(
            folder_id="321669910225",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_by_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.files.folders.with_raw_response.update_by_id(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(Folder, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_by_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.files.folders.with_streaming_response.update_by_id(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(Folder, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_by_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.files.folders.with_raw_response.update_by_id(
                folder_id="",
            )
