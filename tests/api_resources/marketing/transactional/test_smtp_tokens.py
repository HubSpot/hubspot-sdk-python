# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.marketing import SmtpAPITokenView

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSmtpTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        smtp_token = client.marketing.transactional.smtp_tokens.create(
            campaign_name="campaignName",
            create_contact=True,
        )
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.marketing.transactional.smtp_tokens.with_raw_response.create(
            campaign_name="campaignName",
            create_contact=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = response.parse()
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.marketing.transactional.smtp_tokens.with_streaming_response.create(
            campaign_name="campaignName",
            create_contact=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = response.parse()
            assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        smtp_token = client.marketing.transactional.smtp_tokens.list()
        assert_matches_type(SyncPage[SmtpAPITokenView], smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        smtp_token = client.marketing.transactional.smtp_tokens.list(
            after="after",
            campaign_name="campaignName",
            email_campaign_id="emailCampaignId",
            limit=0,
        )
        assert_matches_type(SyncPage[SmtpAPITokenView], smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.marketing.transactional.smtp_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = response.parse()
        assert_matches_type(SyncPage[SmtpAPITokenView], smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.marketing.transactional.smtp_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = response.parse()
            assert_matches_type(SyncPage[SmtpAPITokenView], smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        smtp_token = client.marketing.transactional.smtp_tokens.delete(
            "tokenId",
        )
        assert smtp_token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.marketing.transactional.smtp_tokens.with_raw_response.delete(
            "tokenId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = response.parse()
        assert smtp_token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.marketing.transactional.smtp_tokens.with_streaming_response.delete(
            "tokenId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = response.parse()
            assert smtp_token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.marketing.transactional.smtp_tokens.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        smtp_token = client.marketing.transactional.smtp_tokens.get(
            "tokenId",
        )
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.marketing.transactional.smtp_tokens.with_raw_response.get(
            "tokenId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = response.parse()
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.marketing.transactional.smtp_tokens.with_streaming_response.get(
            "tokenId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = response.parse()
            assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.marketing.transactional.smtp_tokens.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_password(self, client: HubSpot) -> None:
        smtp_token = client.marketing.transactional.smtp_tokens.reset_password(
            "tokenId",
        )
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_password(self, client: HubSpot) -> None:
        response = client.marketing.transactional.smtp_tokens.with_raw_response.reset_password(
            "tokenId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = response.parse()
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_password(self, client: HubSpot) -> None:
        with client.marketing.transactional.smtp_tokens.with_streaming_response.reset_password(
            "tokenId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = response.parse()
            assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_password(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.marketing.transactional.smtp_tokens.with_raw_response.reset_password(
                "",
            )


class TestAsyncSmtpTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        smtp_token = await async_client.marketing.transactional.smtp_tokens.create(
            campaign_name="campaignName",
            create_contact=True,
        )
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.transactional.smtp_tokens.with_raw_response.create(
            campaign_name="campaignName",
            create_contact=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = await response.parse()
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.transactional.smtp_tokens.with_streaming_response.create(
            campaign_name="campaignName",
            create_contact=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = await response.parse()
            assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        smtp_token = await async_client.marketing.transactional.smtp_tokens.list()
        assert_matches_type(AsyncPage[SmtpAPITokenView], smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        smtp_token = await async_client.marketing.transactional.smtp_tokens.list(
            after="after",
            campaign_name="campaignName",
            email_campaign_id="emailCampaignId",
            limit=0,
        )
        assert_matches_type(AsyncPage[SmtpAPITokenView], smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.transactional.smtp_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = await response.parse()
        assert_matches_type(AsyncPage[SmtpAPITokenView], smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.transactional.smtp_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = await response.parse()
            assert_matches_type(AsyncPage[SmtpAPITokenView], smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        smtp_token = await async_client.marketing.transactional.smtp_tokens.delete(
            "tokenId",
        )
        assert smtp_token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.transactional.smtp_tokens.with_raw_response.delete(
            "tokenId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = await response.parse()
        assert smtp_token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.transactional.smtp_tokens.with_streaming_response.delete(
            "tokenId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = await response.parse()
            assert smtp_token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.marketing.transactional.smtp_tokens.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        smtp_token = await async_client.marketing.transactional.smtp_tokens.get(
            "tokenId",
        )
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.transactional.smtp_tokens.with_raw_response.get(
            "tokenId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = await response.parse()
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.transactional.smtp_tokens.with_streaming_response.get(
            "tokenId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = await response.parse()
            assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.marketing.transactional.smtp_tokens.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_password(self, async_client: AsyncHubSpot) -> None:
        smtp_token = await async_client.marketing.transactional.smtp_tokens.reset_password(
            "tokenId",
        )
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_password(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.transactional.smtp_tokens.with_raw_response.reset_password(
            "tokenId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smtp_token = await response.parse()
        assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_password(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.transactional.smtp_tokens.with_streaming_response.reset_password(
            "tokenId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smtp_token = await response.parse()
            assert_matches_type(SmtpAPITokenView, smtp_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_password(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.marketing.transactional.smtp_tokens.with_raw_response.reset_password(
                "",
            )
