# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import BatchResponseHubDBTableRowV3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_batch(self, client: Hubspot) -> None:
        batch = client.cms.hubdb.rows.batch.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_batch(self, client: Hubspot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_batch(self, client: Hubspot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.clone_batch(
                table_id_or_name="",
                inputs=[{"id": "id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: Hubspot) -> None:
        batch = client.cms.hubdb.rows.batch.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: Hubspot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: Hubspot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.create_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "child_table_id": 0,
                        "display_index": 0,
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch(self, client: Hubspot) -> None:
        batch = client.cms.hubdb.rows.batch.get_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_batch(self, client: Hubspot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.get_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_batch(self, client: Hubspot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.get_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.get_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_batch(self, client: Hubspot) -> None:
        batch = client.cms.hubdb.rows.batch.get_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft_batch(self, client: Hubspot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.get_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft_batch(self, client: Hubspot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.get_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.get_draft_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge_batch(self, client: Hubspot) -> None:
        batch = client.cms.hubdb.rows.batch.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purge_batch(self, client: Hubspot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purge_batch(self, client: Hubspot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_purge_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.purge_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_batch(self, client: Hubspot) -> None:
        batch = client.cms.hubdb.rows.batch.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace_batch(self, client: Hubspot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace_batch(self, client: Hubspot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.replace_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "child_table_id": 0,
                        "display_index": 0,
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: Hubspot) -> None:
        batch = client.cms.hubdb.rows.batch.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: Hubspot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: Hubspot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.update_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "child_table_id": 0,
                        "display_index": 0,
                        "values": {"foo": {}},
                    }
                ],
            )


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_batch(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.clone_batch(
                table_id_or_name="",
                inputs=[{"id": "id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.create_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "child_table_id": 0,
                        "display_index": 0,
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.get_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.get_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.get_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.get_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_batch(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.get_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.get_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.get_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.get_draft_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge_batch(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purge_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purge_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_purge_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.purge_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_batch(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.replace_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "child_table_id": 0,
                        "display_index": 0,
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "child_table_id": 0,
                    "display_index": 0,
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.update_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "child_table_id": 0,
                        "display_index": 0,
                        "values": {"foo": {}},
                    }
                ],
            )
