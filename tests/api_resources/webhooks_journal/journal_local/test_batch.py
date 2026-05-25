# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.shared import BatchResponseJournalFetchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        batch = client.webhooks_journal.journal_local.batch.get(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        batch = client.webhooks_journal.journal_local.batch.get(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.webhooks_journal.journal_local.batch.with_raw_response.get(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.webhooks_journal.journal_local.batch.with_streaming_response.get(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest(self, client: HubSpot) -> None:
        batch = client.webhooks_journal.journal_local.batch.get_earliest(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest_with_all_params(self, client: HubSpot) -> None:
        batch = client.webhooks_journal.journal_local.batch.get_earliest(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_earliest(self, client: HubSpot) -> None:
        response = client.webhooks_journal.journal_local.batch.with_raw_response.get_earliest(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_earliest(self, client: HubSpot) -> None:
        with client.webhooks_journal.journal_local.batch.with_streaming_response.get_earliest(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_from_offset(self, client: HubSpot) -> None:
        batch = client.webhooks_journal.journal_local.batch.get_from_offset(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_from_offset_with_all_params(self, client: HubSpot) -> None:
        batch = client.webhooks_journal.journal_local.batch.get_from_offset(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_from_offset(self, client: HubSpot) -> None:
        response = client.webhooks_journal.journal_local.batch.with_raw_response.get_from_offset(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_from_offset(self, client: HubSpot) -> None:
        with client.webhooks_journal.journal_local.batch.with_streaming_response.get_from_offset(
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
    def test_path_params_get_from_offset(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks_journal.journal_local.batch.with_raw_response.get_from_offset(
                count=1,
                offset="",
            )


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.webhooks_journal.journal_local.batch.get(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.webhooks_journal.journal_local.batch.get(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.journal_local.batch.with_raw_response.get(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.journal_local.batch.with_streaming_response.get(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.webhooks_journal.journal_local.batch.get_earliest(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest_with_all_params(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.webhooks_journal.journal_local.batch.get_earliest(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_earliest(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.journal_local.batch.with_raw_response.get_earliest(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_earliest(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.journal_local.batch.with_streaming_response.get_earliest(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_from_offset(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.webhooks_journal.journal_local.batch.get_from_offset(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_from_offset_with_all_params(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.webhooks_journal.journal_local.batch.get_from_offset(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_from_offset(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.journal_local.batch.with_raw_response.get_from_offset(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_from_offset(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.journal_local.batch.with_streaming_response.get_from_offset(
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
    async def test_path_params_get_from_offset(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks_journal.journal_local.batch.with_raw_response.get_from_offset(
                count=1,
                offset="",
            )
