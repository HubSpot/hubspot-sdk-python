# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import PublicSpendItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        spend = client.marketing.campaigns.spend.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        spend = client.marketing.campaigns.spend.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.marketing.campaigns.spend.with_raw_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = response.parse()
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.marketing.campaigns.spend.with_streaming_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = response.parse()
            assert_matches_type(PublicSpendItem, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.spend.with_raw_response.create(
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        spend = client.marketing.campaigns.spend.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        spend = client.marketing.campaigns.spend.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.marketing.campaigns.spend.with_raw_response.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = response.parse()
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.marketing.campaigns.spend.with_streaming_response.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = response.parse()
            assert_matches_type(PublicSpendItem, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.spend.with_raw_response.update(
                spend_id=0,
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        spend = client.marketing.campaigns.spend.delete(
            spend_id=0,
            campaign_guid="campaignGuid",
        )
        assert spend is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.marketing.campaigns.spend.with_raw_response.delete(
            spend_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = response.parse()
        assert spend is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.marketing.campaigns.spend.with_streaming_response.delete(
            spend_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = response.parse()
            assert spend is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.spend.with_raw_response.delete(
                spend_id=0,
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        spend = client.marketing.campaigns.spend.get(
            spend_id=0,
            campaign_guid="campaignGuid",
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.marketing.campaigns.spend.with_raw_response.get(
            spend_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = response.parse()
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.marketing.campaigns.spend.with_streaming_response.get(
            spend_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = response.parse()
            assert_matches_type(PublicSpendItem, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.spend.with_raw_response.get(
                spend_id=0,
                campaign_guid="",
            )


class TestAsyncSpend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        spend = await async_client.marketing.campaigns.spend.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        spend = await async_client.marketing.campaigns.spend.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.campaigns.spend.with_raw_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = await response.parse()
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.campaigns.spend.with_streaming_response.create(
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = await response.parse()
            assert_matches_type(PublicSpendItem, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.spend.with_raw_response.create(
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        spend = await async_client.marketing.campaigns.spend.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        spend = await async_client.marketing.campaigns.spend.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
            description="description",
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.campaigns.spend.with_raw_response.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = await response.parse()
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.campaigns.spend.with_streaming_response.update(
            spend_id=0,
            campaign_guid="campaignGuid",
            amount=0,
            name="name",
            order=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = await response.parse()
            assert_matches_type(PublicSpendItem, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.spend.with_raw_response.update(
                spend_id=0,
                campaign_guid="",
                amount=0,
                name="name",
                order=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        spend = await async_client.marketing.campaigns.spend.delete(
            spend_id=0,
            campaign_guid="campaignGuid",
        )
        assert spend is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.campaigns.spend.with_raw_response.delete(
            spend_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = await response.parse()
        assert spend is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.campaigns.spend.with_streaming_response.delete(
            spend_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = await response.parse()
            assert spend is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.spend.with_raw_response.delete(
                spend_id=0,
                campaign_guid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        spend = await async_client.marketing.campaigns.spend.get(
            spend_id=0,
            campaign_guid="campaignGuid",
        )
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.campaigns.spend.with_raw_response.get(
            spend_id=0,
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = await response.parse()
        assert_matches_type(PublicSpendItem, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.campaigns.spend.with_streaming_response.get(
            spend_id=0,
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = await response.parse()
            assert_matches_type(PublicSpendItem, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.spend.with_raw_response.get(
                spend_id=0,
                campaign_guid="",
            )
