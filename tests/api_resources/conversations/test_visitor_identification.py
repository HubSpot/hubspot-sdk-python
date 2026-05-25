# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.conversations import IdentificationTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVisitorIdentification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_token(self, client: HubSpot) -> None:
        visitor_identification = client.conversations.visitor_identification.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
        )
        assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_token_with_all_params(self, client: HubSpot) -> None:
        visitor_identification = client.conversations.visitor_identification.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
            first_name="firstName",
            last_name="lastName",
        )
        assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_token(self, client: HubSpot) -> None:
        response = client.conversations.visitor_identification.with_raw_response.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor_identification = response.parse()
        assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_token(self, client: HubSpot) -> None:
        with client.conversations.visitor_identification.with_streaming_response.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor_identification = response.parse()
            assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVisitorIdentification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_token(self, async_client: AsyncHubSpot) -> None:
        visitor_identification = await async_client.conversations.visitor_identification.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
        )
        assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_token_with_all_params(self, async_client: AsyncHubSpot) -> None:
        visitor_identification = await async_client.conversations.visitor_identification.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
            first_name="firstName",
            last_name="lastName",
        )
        assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_token(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.conversations.visitor_identification.with_raw_response.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        visitor_identification = await response.parse()
        assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_token(self, async_client: AsyncHubSpot) -> None:
        async with async_client.conversations.visitor_identification.with_streaming_response.generate_token(
            email="email",
            hs_customer_agent_context={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            visitor_identification = await response.parse()
            assert_matches_type(IdentificationTokenResponse, visitor_identification, path=["response"])

        assert cast(Any, response.is_closed) is True
