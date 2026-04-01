# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import BatchResponseSimplePublicObject, BatchResponsePublicDefaultAssociation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        batch = client.crm.objects.partner_clients.batch.update(
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
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.objects.partner_clients.batch.with_raw_response.update(
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
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.objects.partner_clients.batch.with_streaming_response.update(
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
    def test_method_create_default_association(self, client: Hubspot) -> None:
        batch = client.crm.objects.partner_clients.batch.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_default_association(self, client: Hubspot) -> None:
        response = client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_default_association(self, client: Hubspot) -> None:
        with client.crm.objects.partner_clients.batch.with_streaming_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_default_association(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_id` but received ''"):
            client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        batch = client.crm.objects.partner_clients.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        batch = client.crm.objects.partner_clients.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
            archived=True,
            id_property="idProperty",
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.partner_clients.batch.with_raw_response.get(
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
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.partner_clients.batch.with_streaming_response.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.objects.partner_clients.batch.update(
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
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.partner_clients.batch.with_raw_response.update(
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
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.partner_clients.batch.with_streaming_response.update(
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
    async def test_method_create_default_association(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.objects.partner_clients.batch.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_default_association(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_default_association(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.partner_clients.batch.with_streaming_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_default_association(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_id` but received ''"):
            await async_client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.objects.partner_clients.batch.with_raw_response.create_default_association(
                to_object_id="",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.objects.partner_clients.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.objects.partner_clients.batch.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
            archived=True,
            id_property="idProperty",
        )
        assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.partner_clients.batch.with_raw_response.get(
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
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.partner_clients.batch.with_streaming_response.get(
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
