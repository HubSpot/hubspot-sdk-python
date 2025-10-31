# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing.subscriptions import LinkGenerationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        link = client.marketing.subscriptions.v4.links.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )
        assert_matches_type(LinkGenerationResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        link = client.marketing.subscriptions.v4.links.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
            business_unit_id=0,
            language="language",
            subscription_id=0,
        )
        assert_matches_type(LinkGenerationResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.links.with_raw_response.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkGenerationResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.links.with_streaming_response.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkGenerationResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        link = await async_client.marketing.subscriptions.v4.links.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )
        assert_matches_type(LinkGenerationResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        link = await async_client.marketing.subscriptions.v4.links.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
            business_unit_id=0,
            language="language",
            subscription_id=0,
        )
        assert_matches_type(LinkGenerationResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.links.with_raw_response.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkGenerationResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.links.with_streaming_response.create(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkGenerationResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True
