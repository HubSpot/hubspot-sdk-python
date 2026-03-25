# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.communication_preferences import (
    BatchResponsePublicStatus,
    BatchResponsePublicStatusBulkResponse,
    BatchResponsePublicWideStatusBulkResponse,
    BatchResponsePublicBulkOptOutFromAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_statuses(self, client: Hubspot) -> None:
        batch = client.communication_preferences.statuses.batch.get_unsubscribe_all_statuses(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_statuses_with_all_params(self, client: Hubspot) -> None:
        batch = client.communication_preferences.statuses.batch.get_unsubscribe_all_statuses(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_unsubscribe_all_statuses(self, client: Hubspot) -> None:
        response = client.communication_preferences.statuses.batch.with_raw_response.get_unsubscribe_all_statuses(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_unsubscribe_all_statuses(self, client: Hubspot) -> None:
        with client.communication_preferences.statuses.batch.with_streaming_response.get_unsubscribe_all_statuses(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_read(self, client: Hubspot) -> None:
        batch = client.communication_preferences.statuses.batch.read(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: Hubspot) -> None:
        batch = client.communication_preferences.statuses.batch.read(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: Hubspot) -> None:
        response = client.communication_preferences.statuses.batch.with_raw_response.read(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: Hubspot) -> None:
        with client.communication_preferences.statuses.batch.with_streaming_response.read(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unsubscribe_all(self, client: Hubspot) -> None:
        batch = client.communication_preferences.statuses.batch.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unsubscribe_all_with_all_params(self, client: Hubspot) -> None:
        batch = client.communication_preferences.statuses.batch.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe_all(self, client: Hubspot) -> None:
        response = client.communication_preferences.statuses.batch.with_raw_response.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe_all(self, client: Hubspot) -> None:
        with client.communication_preferences.statuses.batch.with_streaming_response.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_statuses(self, client: Hubspot) -> None:
        batch = client.communication_preferences.statuses.batch.update_statuses(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicStatus, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_statuses(self, client: Hubspot) -> None:
        response = client.communication_preferences.statuses.batch.with_raw_response.update_statuses(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicStatus, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_statuses(self, client: Hubspot) -> None:
        with client.communication_preferences.statuses.batch.with_streaming_response.update_statuses(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicStatus, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_statuses(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.communication_preferences.statuses.batch.get_unsubscribe_all_statuses(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_statuses_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.communication_preferences.statuses.batch.get_unsubscribe_all_statuses(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_unsubscribe_all_statuses(self, async_client: AsyncHubspot) -> None:
        response = (
            await async_client.communication_preferences.statuses.batch.with_raw_response.get_unsubscribe_all_statuses(
                channel="EMAIL",
                inputs=["string"],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_unsubscribe_all_statuses(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.communication_preferences.statuses.batch.with_streaming_response.get_unsubscribe_all_statuses(
                channel="EMAIL",
                inputs=["string"],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicWideStatusBulkResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.communication_preferences.statuses.batch.read(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.communication_preferences.statuses.batch.read(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.statuses.batch.with_raw_response.read(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.statuses.batch.with_streaming_response.read(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicStatusBulkResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.communication_preferences.statuses.batch.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.communication_preferences.statuses.batch.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.statuses.batch.with_raw_response.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.statuses.batch.with_streaming_response.unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_statuses(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.communication_preferences.statuses.batch.update_statuses(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicStatus, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_statuses(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.statuses.batch.with_raw_response.update_statuses(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicStatus, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_statuses(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.statuses.batch.with_streaming_response.update_statuses(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicStatus, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
