# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import PublicMigrationMapping, PublicBatchMigrationMapping

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMapping:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_create_id_mapping(self, client: Hubspot) -> None:
        mapping = client.crm.lists.mapping.batch_create_id_mapping(
            body=["string"],
        )
        assert_matches_type(PublicBatchMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_create_id_mapping(self, client: Hubspot) -> None:
        response = client.crm.lists.mapping.with_raw_response.batch_create_id_mapping(
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = response.parse()
        assert_matches_type(PublicBatchMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_create_id_mapping(self, client: Hubspot) -> None:
        with client.crm.lists.mapping.with_streaming_response.batch_create_id_mapping(
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = response.parse()
            assert_matches_type(PublicBatchMigrationMapping, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_id_mapping(self, client: Hubspot) -> None:
        mapping = client.crm.lists.mapping.get_id_mapping()
        assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_id_mapping_with_all_params(self, client: Hubspot) -> None:
        mapping = client.crm.lists.mapping.get_id_mapping(
            legacy_list_id="legacyListId",
        )
        assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_id_mapping(self, client: Hubspot) -> None:
        response = client.crm.lists.mapping.with_raw_response.get_id_mapping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = response.parse()
        assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_id_mapping(self, client: Hubspot) -> None:
        with client.crm.lists.mapping.with_streaming_response.get_id_mapping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = response.parse()
            assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMapping:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_create_id_mapping(self, async_client: AsyncHubspot) -> None:
        mapping = await async_client.crm.lists.mapping.batch_create_id_mapping(
            body=["string"],
        )
        assert_matches_type(PublicBatchMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_create_id_mapping(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.mapping.with_raw_response.batch_create_id_mapping(
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = await response.parse()
        assert_matches_type(PublicBatchMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_create_id_mapping(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.mapping.with_streaming_response.batch_create_id_mapping(
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = await response.parse()
            assert_matches_type(PublicBatchMigrationMapping, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_id_mapping(self, async_client: AsyncHubspot) -> None:
        mapping = await async_client.crm.lists.mapping.get_id_mapping()
        assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_id_mapping_with_all_params(self, async_client: AsyncHubspot) -> None:
        mapping = await async_client.crm.lists.mapping.get_id_mapping(
            legacy_list_id="legacyListId",
        )
        assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_id_mapping(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.mapping.with_raw_response.get_id_mapping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = await response.parse()
        assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_id_mapping(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.mapping.with_streaming_response.get_id_mapping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = await response.parse()
            assert_matches_type(PublicMigrationMapping, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True
