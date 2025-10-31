# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import (
    PublicSubscriptionStatus,
    SubscriptionDefinitionsResponse,
    PublicSubscriptionStatusesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        subscription = client.marketing.subscriptions.list()
        assert_matches_type(SubscriptionDefinitionsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDefinitionsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDefinitionsResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_email_status(self, client: Hubspot) -> None:
        subscription = client.marketing.subscriptions.get_email_status(
            "emailAddress",
        )
        assert_matches_type(PublicSubscriptionStatusesResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_email_status(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.with_raw_response.get_email_status(
            "emailAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(PublicSubscriptionStatusesResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_email_status(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.with_streaming_response.get_email_status(
            "emailAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(PublicSubscriptionStatusesResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_email_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_address` but received ''"):
            client.marketing.subscriptions.with_raw_response.get_email_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_subscribe(self, client: Hubspot) -> None:
        subscription = client.marketing.subscriptions.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_subscribe_with_all_params(self, client: Hubspot) -> None:
        subscription = client.marketing.subscriptions.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
            legal_basis="LEGITIMATE_INTEREST_PQL",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_subscribe(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.with_raw_response.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_subscribe(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.with_streaming_response.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe(self, client: Hubspot) -> None:
        subscription = client.marketing.subscriptions.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_with_all_params(self, client: Hubspot) -> None:
        subscription = client.marketing.subscriptions.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
            legal_basis="LEGITIMATE_INTEREST_PQL",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.with_raw_response.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.with_streaming_response.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        subscription = await async_client.marketing.subscriptions.list()
        assert_matches_type(SubscriptionDefinitionsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDefinitionsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDefinitionsResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_email_status(self, async_client: AsyncHubspot) -> None:
        subscription = await async_client.marketing.subscriptions.get_email_status(
            "emailAddress",
        )
        assert_matches_type(PublicSubscriptionStatusesResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_email_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.with_raw_response.get_email_status(
            "emailAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(PublicSubscriptionStatusesResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_email_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.with_streaming_response.get_email_status(
            "emailAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(PublicSubscriptionStatusesResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_email_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_address` but received ''"):
            await async_client.marketing.subscriptions.with_raw_response.get_email_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_subscribe(self, async_client: AsyncHubspot) -> None:
        subscription = await async_client.marketing.subscriptions.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_subscribe_with_all_params(self, async_client: AsyncHubspot) -> None:
        subscription = await async_client.marketing.subscriptions.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
            legal_basis="LEGITIMATE_INTEREST_PQL",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_subscribe(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.with_raw_response.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_subscribe(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.with_streaming_response.subscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe(self, async_client: AsyncHubspot) -> None:
        subscription = await async_client.marketing.subscriptions.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_with_all_params(self, async_client: AsyncHubspot) -> None:
        subscription = await async_client.marketing.subscriptions.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
            legal_basis="LEGITIMATE_INTEREST_PQL",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.with_raw_response.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.with_streaming_response.unsubscribe(
            email_address="emailAddress",
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(PublicSubscriptionStatus, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True
