# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import PublicBudgetItem, PublicBudgetTotals

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBudget:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        budget = client.marketing.campaigns.budget.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        budget = client.marketing.campaigns.budget.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.budget.with_raw_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.marketing.campaigns.budget.with_streaming_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(PublicBudgetItem, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.budget.with_raw_response.create(
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        budget = client.marketing.campaigns.budget.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        budget = client.marketing.campaigns.budget.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.budget.with_raw_response.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.marketing.campaigns.budget.with_streaming_response.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(PublicBudgetItem, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.budget.with_raw_response.update(
                budget_id=0,
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        budget = client.marketing.campaigns.budget.delete(
            budget_id=0,
            campaign_guid="campaignGuid",
        )
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.budget.with_raw_response.delete(
            budget_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.marketing.campaigns.budget.with_streaming_response.delete(
            budget_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert budget is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.budget.with_raw_response.delete(
                budget_id=0,
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        budget = client.marketing.campaigns.budget.get(
            budget_id=0,
            campaign_guid="campaignGuid",
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.budget.with_raw_response.get(
            budget_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.marketing.campaigns.budget.with_streaming_response.get(
            budget_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(PublicBudgetItem, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.budget.with_raw_response.get(
                budget_id=0,
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_totals(self, client: HubSpot) -> None:
        budget = client.marketing.campaigns.budget.get_totals(
            "campaignGuid",
        )
        assert_matches_type(PublicBudgetTotals, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_totals(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.budget.with_raw_response.get_totals(
            "campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(PublicBudgetTotals, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_totals(self, client: HubSpot) -> None:
        with client.marketing.campaigns.budget.with_streaming_response.get_totals(
            "campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(PublicBudgetTotals, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_totals(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.budget.with_raw_response.get_totals(
                "",
            )


class TestAsyncBudget:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        budget = await async_client.marketing.campaigns.budget.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        budget = await async_client.marketing.campaigns.budget.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.budget.with_raw_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.budget.with_streaming_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(PublicBudgetItem, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.budget.with_raw_response.create(
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        budget = await async_client.marketing.campaigns.budget.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        budget = await async_client.marketing.campaigns.budget.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.budget.with_raw_response.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.budget.with_streaming_response.update(
            budget_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(PublicBudgetItem, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.budget.with_raw_response.update(
                budget_id=0,
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        budget = await async_client.marketing.campaigns.budget.delete(
            budget_id=0,
            campaign_guid="campaignGuid",
        )
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.budget.with_raw_response.delete(
            budget_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.budget.with_streaming_response.delete(
            budget_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert budget is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.budget.with_raw_response.delete(
                budget_id=0,
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        budget = await async_client.marketing.campaigns.budget.get(
            budget_id=0,
            campaign_guid="campaignGuid",
        )
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.budget.with_raw_response.get(
            budget_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(PublicBudgetItem, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.budget.with_streaming_response.get(
            budget_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(PublicBudgetItem, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.budget.with_raw_response.get(
                budget_id=0,
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_totals(self, async_client: AsyncHubSpot) -> None:
        budget = await async_client.marketing.campaigns.budget.get_totals(
            "campaignGuid",
        )
        assert_matches_type(PublicBudgetTotals, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_totals(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.budget.with_raw_response.get_totals(
            "campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(PublicBudgetTotals, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_totals(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.budget.with_streaming_response.get_totals(
            "campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(PublicBudgetTotals, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_totals(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.budget.with_raw_response.get_totals(
                "",
            )
