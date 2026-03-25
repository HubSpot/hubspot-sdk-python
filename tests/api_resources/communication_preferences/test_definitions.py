# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.communication_preferences import (
    ActionResponseWithResultsSubscriptionDefinition,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        definition = client.communication_preferences.definitions.list()
        assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        definition = client.communication_preferences.definitions.list(
            business_unit_id=0,
            include_translations=True,
        )
        assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.communication_preferences.definitions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.communication_preferences.definitions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDefinitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.communication_preferences.definitions.list()
        assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.communication_preferences.definitions.list(
            business_unit_id=0,
            include_translations=True,
        )
        assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.definitions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.definitions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(ActionResponseWithResultsSubscriptionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True
