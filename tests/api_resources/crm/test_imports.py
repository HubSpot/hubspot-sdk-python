# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    PublicImportResponse,
    CollectionResponsePublicImportErrorForwardPaging,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.shared import ActionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        import_ = client.crm.imports.create()
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        import_ = client.crm.imports.create(
            files=b"raw file contents",
            import_request="importRequest",
        )
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.imports.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.imports.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(PublicImportResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        import_ = client.crm.imports.list()
        assert_matches_type(SyncPage[PublicImportResponse], import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        import_ = client.crm.imports.list(
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[PublicImportResponse], import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.imports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(SyncPage[PublicImportResponse], import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.imports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(SyncPage[PublicImportResponse], import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Hubspot) -> None:
        import_ = client.crm.imports.cancel(
            0,
        )
        assert_matches_type(ActionResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Hubspot) -> None:
        response = client.crm.imports.with_raw_response.cancel(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(ActionResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Hubspot) -> None:
        with client.crm.imports.with_streaming_response.cancel(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(ActionResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        import_ = client.crm.imports.get(
            0,
        )
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.imports.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.imports.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(PublicImportResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_errors(self, client: Hubspot) -> None:
        import_ = client.crm.imports.list_errors(
            import_id=0,
        )
        assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_errors_with_all_params(self, client: Hubspot) -> None:
        import_ = client.crm.imports.list_errors(
            import_id=0,
            after="after",
            include_error_message=True,
            include_row_data=True,
            limit=0,
        )
        assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_errors(self, client: Hubspot) -> None:
        response = client.crm.imports.with_raw_response.list_errors(
            import_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_errors(self, client: Hubspot) -> None:
        with client.crm.imports.with_streaming_response.list_errors(
            import_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.create()
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.create(
            files=b"raw file contents",
            import_request="importRequest",
        )
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.imports.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.imports.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(PublicImportResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.list()
        assert_matches_type(AsyncPage[PublicImportResponse], import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.list(
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[PublicImportResponse], import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.imports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(AsyncPage[PublicImportResponse], import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.imports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(AsyncPage[PublicImportResponse], import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.cancel(
            0,
        )
        assert_matches_type(ActionResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.imports.with_raw_response.cancel(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(ActionResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.imports.with_streaming_response.cancel(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(ActionResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.get(
            0,
        )
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.imports.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(PublicImportResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.imports.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(PublicImportResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_errors(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.list_errors(
            import_id=0,
        )
        assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_errors_with_all_params(self, async_client: AsyncHubspot) -> None:
        import_ = await async_client.crm.imports.list_errors(
            import_id=0,
            after="after",
            include_error_message=True,
            include_row_data=True,
            limit=0,
        )
        assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_errors(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.imports.with_raw_response.list_errors(
            import_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_errors(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.imports.with_streaming_response.list_errors(
            import_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(CollectionResponsePublicImportErrorForwardPaging, import_, path=["response"])

        assert cast(Any, response.is_closed) is True
