# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import (
    AggregateEmailStatistics,
    CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        statistic = client.marketing.emails.statistics.get()
        assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        statistic = client.marketing.emails.statistics.get(
            email_ids=[0],
            end_timestamp="endTimestamp",
            property="property",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.marketing.emails.statistics.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.marketing.emails.statistics.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_histogram(self, client: HubSpot) -> None:
        statistic = client.marketing.emails.statistics.get_histogram()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_histogram_with_all_params(self, client: HubSpot) -> None:
        statistic = client.marketing.emails.statistics.get_histogram(
            email_ids=[0],
            end_timestamp="endTimestamp",
            interval="YEAR",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_histogram(self, client: HubSpot) -> None:
        response = client.marketing.emails.statistics.with_raw_response.get_histogram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_histogram(self, client: HubSpot) -> None:
        with client.marketing.emails.statistics.with_streaming_response.get_histogram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        statistic = await async_client.marketing.emails.statistics.get()
        assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        statistic = await async_client.marketing.emails.statistics.get(
            email_ids=[0],
            end_timestamp="endTimestamp",
            property="property",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.statistics.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.statistics.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(AggregateEmailStatistics, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_histogram(self, async_client: AsyncHubSpot) -> None:
        statistic = await async_client.marketing.emails.statistics.get_histogram()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_histogram_with_all_params(self, async_client: AsyncHubSpot) -> None:
        statistic = await async_client.marketing.emails.statistics.get_histogram(
            email_ids=[0],
            end_timestamp="endTimestamp",
            interval="YEAR",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_histogram(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.statistics.with_raw_response.get_histogram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_histogram(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.statistics.with_streaming_response.get_histogram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(CollectionResponseWithTotalEmailStatisticIntervalNoPaging, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True
