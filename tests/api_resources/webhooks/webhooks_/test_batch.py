# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.webhooks import BatchResponseJournalFetchResponse, BatchResponseSubscriptionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.create(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriptionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.webhooks.webhooks.batch.with_raw_response.create(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseSubscriptionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.webhooks.webhooks.batch.with_streaming_response.create(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseSubscriptionResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.get_earliest(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest_with_all_params(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.get_earliest(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_earliest(self, client: Hubspot) -> None:
        response = client.webhooks.webhooks.batch.with_raw_response.get_earliest(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_earliest(self, client: Hubspot) -> None:
        with client.webhooks.webhooks.batch.with_streaming_response.get_earliest(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_latest(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.get_latest(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_latest_with_all_params(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.get_latest(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_latest(self, client: Hubspot) -> None:
        response = client.webhooks.webhooks.batch.with_raw_response.get_latest(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_latest(self, client: Hubspot) -> None:
        with client.webhooks.webhooks.batch.with_streaming_response.get_latest(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_next(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.get_next(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_next_with_all_params(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.get_next(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_next(self, client: Hubspot) -> None:
        response = client.webhooks.webhooks.batch.with_raw_response.get_next(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_next(self, client: Hubspot) -> None:
        with client.webhooks.webhooks.batch.with_streaming_response.get_next(
            count=1,
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_next(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks.webhooks.batch.with_raw_response.get_next(
                count=1,
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_read(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.read(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: Hubspot) -> None:
        batch = client.webhooks.webhooks.batch.read(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: Hubspot) -> None:
        response = client.webhooks.webhooks.batch.with_raw_response.read(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: Hubspot) -> None:
        with client.webhooks.webhooks.batch.with_streaming_response.read(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.create(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriptionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhooks.batch.with_raw_response.create(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseSubscriptionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhooks.batch.with_streaming_response.create(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseSubscriptionResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.get_earliest(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.get_earliest(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_earliest(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhooks.batch.with_raw_response.get_earliest(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_earliest(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhooks.batch.with_streaming_response.get_earliest(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_latest(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.get_latest(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_latest_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.get_latest(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_latest(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhooks.batch.with_raw_response.get_latest(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_latest(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhooks.batch.with_streaming_response.get_latest(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_next(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.get_next(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_next_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.get_next(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_next(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhooks.batch.with_raw_response.get_next(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_next(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhooks.batch.with_streaming_response.get_next(
            count=1,
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_next(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks.webhooks.batch.with_raw_response.get_next(
                count=1,
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.read(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.webhooks.webhooks.batch.read(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhooks.batch.with_raw_response.read(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhooks.batch.with_streaming_response.read(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
