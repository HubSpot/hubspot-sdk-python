# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import BatchResponseSimplePublicObject, BatchResponseSimplePublicUpsertObject

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        batch = client.crm.objects.quotes.batch.create(
            inputs=[
                {
                    "associations": [
                        {
                            "to": {"id": "id"},
                            "types": [
                                {
                                    "association_category": "HUBSPOT_DEFINED",
                                    "association_type_id": 0,
                                }
                            ],
                        }
                    ],
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.objects.quotes.batch.with_raw_response.create(
            inputs=[
                {
                    "associations": [
                        {
                            "to": {"id": "id"},
                            "types": [
                                {
                                    "association_category": "HUBSPOT_DEFINED",
                                    "association_type_id": 0,
                                }
                            ],
                        }
                    ],
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.objects.quotes.batch.with_streaming_response.create(
            inputs=[
                {
                    "associations": [
                        {
                            "to": {"id": "id"},
                            "types": [
                                {
                                    "association_category": "HUBSPOT_DEFINED",
                                    "association_type_id": 0,
                                }
                            ],
                        }
                    ],
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        batch = client.crm.objects.quotes.batch.update(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.objects.quotes.batch.with_raw_response.update(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.objects.quotes.batch.with_streaming_response.update(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        batch = client.crm.objects.quotes.batch.delete(
            inputs=[{"id": "430001"}],
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.objects.quotes.batch.with_raw_response.delete(
            inputs=[{"id": "430001"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.objects.quotes.batch.with_streaming_response.delete(
            inputs=[{"id": "430001"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        batch = client.crm.objects.quotes.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        batch = client.crm.objects.quotes.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
            archived=True,
            id_property="idProperty",
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.objects.quotes.batch.with_raw_response.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.objects.quotes.batch.with_streaming_response.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: HubSpot) -> None:
        batch = client.crm.objects.quotes.batch.upsert(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicUpsertObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: HubSpot) -> None:
        response = client.crm.objects.quotes.batch.with_raw_response.upsert(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseSimplePublicUpsertObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: HubSpot) -> None:
        with client.crm.objects.quotes.batch.with_streaming_response.upsert(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseSimplePublicUpsertObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.objects.quotes.batch.create(
            inputs=[
                {
                    "associations": [
                        {
                            "to": {"id": "id"},
                            "types": [
                                {
                                    "association_category": "HUBSPOT_DEFINED",
                                    "association_type_id": 0,
                                }
                            ],
                        }
                    ],
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.quotes.batch.with_raw_response.create(
            inputs=[
                {
                    "associations": [
                        {
                            "to": {"id": "id"},
                            "types": [
                                {
                                    "association_category": "HUBSPOT_DEFINED",
                                    "association_type_id": 0,
                                }
                            ],
                        }
                    ],
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.quotes.batch.with_streaming_response.create(
            inputs=[
                {
                    "associations": [
                        {
                            "to": {"id": "id"},
                            "types": [
                                {
                                    "association_category": "HUBSPOT_DEFINED",
                                    "association_type_id": 0,
                                }
                            ],
                        }
                    ],
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.objects.quotes.batch.update(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.quotes.batch.with_raw_response.update(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.quotes.batch.with_streaming_response.update(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.objects.quotes.batch.delete(
            inputs=[{"id": "430001"}],
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.quotes.batch.with_raw_response.delete(
            inputs=[{"id": "430001"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.quotes.batch.with_streaming_response.delete(
            inputs=[{"id": "430001"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.objects.quotes.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.objects.quotes.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
            archived=True,
            id_property="idProperty",
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.quotes.batch.with_raw_response.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.quotes.batch.with_streaming_response.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.objects.quotes.batch.upsert(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicUpsertObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.quotes.batch.with_raw_response.upsert(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseSimplePublicUpsertObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.quotes.batch.with_streaming_response.upsert(
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseSimplePublicUpsertObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
