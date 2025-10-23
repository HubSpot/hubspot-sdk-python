# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import HubDBTableRowV3, UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.create(
                table_id_or_name="",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.list(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(SyncPage[object], row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.list(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(SyncPage[object], row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.list(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(SyncPage[object], row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.list(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(SyncPage[object], row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.list(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            name="name",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.clone_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.rows.with_raw_response.clone_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_draft(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert row is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert row is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert row is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.delete_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.rows.with_raw_response.delete_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.get(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.rows.with_raw_response.get(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.get_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.rows.with_raw_response.get_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_draft(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.list_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_draft_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.list_draft(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.list_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.list_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.list_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_draft(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_draft_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.replace_draft(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.rows.with_raw_response.replace_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_with_all_params(self, client: HubSpot) -> None:
        row = client.cms.hubdb.rows.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.with_raw_response.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.with_streaming_response.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.with_raw_response.update_draft(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.rows.with_raw_response.update_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )


class TestAsyncRows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.create(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.create(
                table_id_or_name="",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.list(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(AsyncPage[object], row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.list(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(AsyncPage[object], row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.list(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(AsyncPage[object], row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.list(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(AsyncPage[object], row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.list(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            name="name",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.clone_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.clone_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.clone_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_draft(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert row is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert row is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert row is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.delete_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.delete_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.get(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.get(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.get(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.get_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.get_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.get_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_draft(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.list_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.list_draft(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.list_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.list_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.list_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_draft(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.replace_draft(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.replace_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        row = await async_client.cms.hubdb.rows.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.with_raw_response.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        row = await response.parse()
        assert_matches_type(HubDBTableRowV3, row, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.with_streaming_response.update_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            row = await response.parse()
            assert_matches_type(HubDBTableRowV3, row, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.update_draft(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.rows.with_raw_response.update_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )
