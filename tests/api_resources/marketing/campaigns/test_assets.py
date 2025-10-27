# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import CollectionResponsePublicCampaignAssetForwardPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        asset = client.marketing.campaigns.assets.update(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.assets.with_raw_response.update(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.marketing.campaigns.assets.with_streaming_response.update(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.update(
                asset_id="assetId",
                campaign_guid="",
                asset_type="assetType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_type` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.update(
                asset_id="assetId",
                campaign_guid="campaignGuid",
                asset_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.update(
                asset_id="",
                campaign_guid="campaignGuid",
                asset_type="assetType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        asset = client.marketing.campaigns.assets.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
        )
        assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        asset = client.marketing.campaigns.assets.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
            after="after",
            end_date="endDate",
            limit="limit",
            start_date="startDate",
        )
        assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.assets.with_raw_response.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.marketing.campaigns.assets.with_streaming_response.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.list(
                asset_type="assetType",
                campaign_guid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_type` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.list(
                asset_type="",
                campaign_guid="campaignGuid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        asset = client.marketing.campaigns.assets.delete(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.marketing.campaigns.assets.with_raw_response.delete(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.marketing.campaigns.assets.with_streaming_response.delete(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.delete(
                asset_id="assetId",
                campaign_guid="",
                asset_type="assetType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_type` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.delete(
                asset_id="assetId",
                campaign_guid="campaignGuid",
                asset_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.marketing.campaigns.assets.with_raw_response.delete(
                asset_id="",
                campaign_guid="campaignGuid",
                asset_type="assetType",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        asset = await async_client.marketing.campaigns.assets.update(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.assets.with_raw_response.update(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.assets.with_streaming_response.update(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.update(
                asset_id="assetId",
                campaign_guid="",
                asset_type="assetType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_type` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.update(
                asset_id="assetId",
                campaign_guid="campaignGuid",
                asset_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.update(
                asset_id="",
                campaign_guid="campaignGuid",
                asset_type="assetType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        asset = await async_client.marketing.campaigns.assets.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
        )
        assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        asset = await async_client.marketing.campaigns.assets.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
            after="after",
            end_date="endDate",
            limit="limit",
            start_date="startDate",
        )
        assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.assets.with_raw_response.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.assets.with_streaming_response.list(
            asset_type="assetType",
            campaign_guid="campaignGuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(CollectionResponsePublicCampaignAssetForwardPaging, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.list(
                asset_type="assetType",
                campaign_guid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_type` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.list(
                asset_type="",
                campaign_guid="campaignGuid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        asset = await async_client.marketing.campaigns.assets.delete(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.campaigns.assets.with_raw_response.delete(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.campaigns.assets.with_streaming_response.delete(
            asset_id="assetId",
            campaign_guid="campaignGuid",
            asset_type="assetType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_guid` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.delete(
                asset_id="assetId",
                campaign_guid="",
                asset_type="assetType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_type` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.delete(
                asset_id="assetId",
                campaign_guid="campaignGuid",
                asset_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.marketing.campaigns.assets.with_raw_response.delete(
                asset_id="",
                campaign_guid="campaignGuid",
                asset_type="assetType",
            )
