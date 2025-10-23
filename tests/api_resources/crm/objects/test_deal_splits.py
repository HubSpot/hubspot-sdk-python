# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.objects import (
    BatchResponseDealToDealSplits,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDealSplits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_read(self, client: HubSpot) -> None:
        deal_split = client.crm.objects.deal_splits.batch_read(
            inputs=[{"id": "37295"}],
        )
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_read(self, client: HubSpot) -> None:
        response = client.crm.objects.deal_splits.with_raw_response.batch_read(
            inputs=[{"id": "37295"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal_split = response.parse()
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_read(self, client: HubSpot) -> None:
        with client.crm.objects.deal_splits.with_streaming_response.batch_read(
            inputs=[{"id": "37295"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal_split = response.parse()
            assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_upsert(self, client: HubSpot) -> None:
        deal_split = client.crm.objects.deal_splits.batch_upsert(
            inputs=[
                {
                    "id": 0,
                    "splits": [
                        {
                            "owner_id": 0,
                            "percentage": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_upsert(self, client: HubSpot) -> None:
        response = client.crm.objects.deal_splits.with_raw_response.batch_upsert(
            inputs=[
                {
                    "id": 0,
                    "splits": [
                        {
                            "owner_id": 0,
                            "percentage": 0,
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal_split = response.parse()
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_upsert(self, client: HubSpot) -> None:
        with client.crm.objects.deal_splits.with_streaming_response.batch_upsert(
            inputs=[
                {
                    "id": 0,
                    "splits": [
                        {
                            "owner_id": 0,
                            "percentage": 0,
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal_split = response.parse()
            assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDealSplits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_read(self, async_client: AsyncHubSpot) -> None:
        deal_split = await async_client.crm.objects.deal_splits.batch_read(
            inputs=[{"id": "37295"}],
        )
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deal_splits.with_raw_response.batch_read(
            inputs=[{"id": "37295"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal_split = await response.parse()
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deal_splits.with_streaming_response.batch_read(
            inputs=[{"id": "37295"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal_split = await response.parse()
            assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_upsert(self, async_client: AsyncHubSpot) -> None:
        deal_split = await async_client.crm.objects.deal_splits.batch_upsert(
            inputs=[
                {
                    "id": 0,
                    "splits": [
                        {
                            "owner_id": 0,
                            "percentage": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_upsert(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deal_splits.with_raw_response.batch_upsert(
            inputs=[
                {
                    "id": 0,
                    "splits": [
                        {
                            "owner_id": 0,
                            "percentage": 0,
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal_split = await response.parse()
        assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_upsert(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deal_splits.with_streaming_response.batch_upsert(
            inputs=[
                {
                    "id": 0,
                    "splits": [
                        {
                            "owner_id": 0,
                            "percentage": 0,
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal_split = await response.parse()
            assert_matches_type(BatchResponseDealToDealSplits, deal_split, path=["response"])

        assert cast(Any, response.is_closed) is True
