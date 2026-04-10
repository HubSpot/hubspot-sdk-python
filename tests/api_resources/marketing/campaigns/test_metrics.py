# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.marketing import MetricsCounters, ContactReference, RevenueAttributionAggregate

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_attribution_metrics(self, client: HubSpot) -> None:
        metric = client.marketing.campaigns.metrics.get_attribution_metrics(
            campaign_guid="campaignGuid",
        )
        assert_matches_type(MetricsCounters, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_attribution_metrics_with_all_params(self, client: HubSpot) -> None:
        metric = client.marketing.campaigns.metrics.get_attribution_metrics(
            campaign_guid="campaignGuid",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(MetricsCounters, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_attribution_metrics(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.metrics.with_raw_response.get_attribution_metrics(
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricsCounters, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_attribution_metrics(self, client: HubSpot) -> None:
        with client.marketing.campaigns.metrics.with_streaming_response.get_attribution_metrics(
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricsCounters, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_attribution_metrics(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.metrics.with_raw_response.get_attribution_metrics(
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_revenue_attribution(self, client: HubSpot) -> None:
        metric = client.marketing.campaigns.metrics.get_revenue_attribution(
            campaign_guid="campaignGuid",
        )
        assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_revenue_attribution_with_all_params(self, client: HubSpot) -> None:
        metric = client.marketing.campaigns.metrics.get_revenue_attribution(
            campaign_guid="campaignGuid",
            attribution_model="attributionModel",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_revenue_attribution(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.metrics.with_raw_response.get_revenue_attribution(
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_revenue_attribution(self, client: HubSpot) -> None:
        with client.marketing.campaigns.metrics.with_streaming_response.get_revenue_attribution(
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_revenue_attribution(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.metrics.with_raw_response.get_revenue_attribution(
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contact_ids_by_type(self, client: HubSpot) -> None:
        metric = client.marketing.campaigns.metrics.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
        )
        assert_matches_type(SyncPage[ContactReference], metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contact_ids_by_type_with_all_params(self, client: HubSpot) -> None:
        metric = client.marketing.campaigns.metrics.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
            after="after",
            end_date="endDate",
            limit=0,
            start_date="startDate",
        )
        assert_matches_type(SyncPage[ContactReference], metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_contact_ids_by_type(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.metrics.with_raw_response.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(SyncPage[ContactReference], metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_contact_ids_by_type(self, client: HubSpot) -> None:
        with client.marketing.campaigns.metrics.with_streaming_response.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(SyncPage[ContactReference], metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_contact_ids_by_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.metrics.with_raw_response.list_contact_ids_by_type(
                contact_type="contactType",
                campaign_guid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_type` but received ''"):
            client.marketing.campaigns.metrics.with_raw_response.list_contact_ids_by_type(
                contact_type="",
                campaign_guid="campaignGuid",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_attribution_metrics(self, async_client: AsyncHubSpot) -> None:
        metric = await async_client.marketing.campaigns.metrics.get_attribution_metrics(
            campaign_guid="campaignGuid",
        )
        assert_matches_type(MetricsCounters, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_attribution_metrics_with_all_params(self, async_client: AsyncHubSpot) -> None:
        metric = await async_client.marketing.campaigns.metrics.get_attribution_metrics(
            campaign_guid="campaignGuid",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(MetricsCounters, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_attribution_metrics(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.metrics.with_raw_response.get_attribution_metrics(
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricsCounters, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_attribution_metrics(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.metrics.with_streaming_response.get_attribution_metrics(
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricsCounters, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_attribution_metrics(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.metrics.with_raw_response.get_attribution_metrics(
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_revenue_attribution(self, async_client: AsyncHubSpot) -> None:
        metric = await async_client.marketing.campaigns.metrics.get_revenue_attribution(
            campaign_guid="campaignGuid",
        )
        assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_revenue_attribution_with_all_params(self, async_client: AsyncHubSpot) -> None:
        metric = await async_client.marketing.campaigns.metrics.get_revenue_attribution(
            campaign_guid="campaignGuid",
            attribution_model="attributionModel",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_revenue_attribution(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.metrics.with_raw_response.get_revenue_attribution(
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_revenue_attribution(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.metrics.with_streaming_response.get_revenue_attribution(
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(RevenueAttributionAggregate, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_revenue_attribution(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.metrics.with_raw_response.get_revenue_attribution(
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contact_ids_by_type(self, async_client: AsyncHubSpot) -> None:
        metric = await async_client.marketing.campaigns.metrics.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
        )
        assert_matches_type(AsyncPage[ContactReference], metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contact_ids_by_type_with_all_params(self, async_client: AsyncHubSpot) -> None:
        metric = await async_client.marketing.campaigns.metrics.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
            after="after",
            end_date="endDate",
            limit=0,
            start_date="startDate",
        )
        assert_matches_type(AsyncPage[ContactReference], metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_contact_ids_by_type(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.metrics.with_raw_response.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(AsyncPage[ContactReference], metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_contact_ids_by_type(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.metrics.with_streaming_response.list_contact_ids_by_type(
            contact_type="contactType",
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(AsyncPage[ContactReference], metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_contact_ids_by_type(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.metrics.with_raw_response.list_contact_ids_by_type(
                contact_type="contactType",
                campaign_guid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_type` but received ''"):
            await async_client.marketing.campaigns.metrics.with_raw_response.list_contact_ids_by_type(
                contact_type="",
                campaign_guid="campaignGuid",
            )
