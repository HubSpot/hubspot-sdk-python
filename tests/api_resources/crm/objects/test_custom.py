# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    SimplePublicObject,
    BatchResponseSimplePublicObject,
    SimplePublicObjectWithAssociations,
    BatchResponseSimplePublicUpsertObject,
    CollectionResponseWithTotalSimplePublicObject,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.create(
            object_type="objectType",
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
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.create(
            object_type="objectType",
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
        custom = response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.create(
            object_type="objectType",
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

            custom = response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.create(
                object_type="",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.update(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.update(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.update(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.update(
                object_type="",
                inputs=[
                    {
                        "id": "id",
                        "properties": {"foo": "string"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.list(
            object_type="objectType",
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.list(
            object_type="objectType",
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.list(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.delete(
            object_type="objectType",
            inputs=[{"id": "430001"}],
        )
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.delete(
            object_type="objectType",
            inputs=[{"id": "430001"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.delete(
            object_type="objectType",
            inputs=[{"id": "430001"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert custom is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.delete(
                object_type="",
                inputs=[{"id": "430001"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
            archived=True,
            id_property="idProperty",
        )
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.get(
                object_type="",
                inputs=[{"id": "430001"}],
                properties=["string"],
                properties_with_history=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merge(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merge(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_merge(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(SimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_merge(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.merge(
                object_type="",
                object_id_to_merge="objectIdToMerge",
                primary_object_id="primaryObjectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                            "high_value": "highValue",
                            "value": "value",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
            query="query",
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.search(
                object_type="",
                after="after",
                filter_groups=[
                    {
                        "filters": [
                            {
                                "operator": "BETWEEN",
                                "property_name": "propertyName",
                            }
                        ]
                    }
                ],
                limit=0,
                properties=["string"],
                sorts=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Hubspot) -> None:
        custom = client.crm.objects.custom.upsert(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicUpsertObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Hubspot) -> None:
        response = client.crm.objects.custom.with_raw_response.upsert(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(BatchResponseSimplePublicUpsertObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Hubspot) -> None:
        with client.crm.objects.custom.with_streaming_response.upsert(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(BatchResponseSimplePublicUpsertObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.upsert(
                object_type="",
                inputs=[
                    {
                        "id": "id",
                        "properties": {"foo": "string"},
                    }
                ],
            )


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.create(
            object_type="objectType",
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
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.create(
            object_type="objectType",
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
        custom = await response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.create(
            object_type="objectType",
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

            custom = await response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.create(
                object_type="",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.update(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.update(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.update(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.update(
                object_type="",
                inputs=[
                    {
                        "id": "id",
                        "properties": {"foo": "string"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.list(
            object_type="objectType",
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.list(
            object_type="objectType",
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.list(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.delete(
            object_type="objectType",
            inputs=[{"id": "430001"}],
        )
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.delete(
            object_type="objectType",
            inputs=[{"id": "430001"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.delete(
            object_type="objectType",
            inputs=[{"id": "430001"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert custom is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.delete(
                object_type="",
                inputs=[{"id": "430001"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
            archived=True,
            id_property="idProperty",
        )
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.get(
            object_type="objectType",
            inputs=[{"id": "430001"}],
            properties=["string"],
            properties_with_history=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(BatchResponseSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.get(
                object_type="",
                inputs=[{"id": "430001"}],
                properties=["string"],
                properties_with_history=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merge(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(SimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_merge(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.merge(
                object_type="",
                object_id_to_merge="objectIdToMerge",
                primary_object_id="primaryObjectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                            "high_value": "highValue",
                            "value": "value",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
            query="query",
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.search(
            object_type="objectType",
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.search(
                object_type="",
                after="after",
                filter_groups=[
                    {
                        "filters": [
                            {
                                "operator": "BETWEEN",
                                "property_name": "propertyName",
                            }
                        ]
                    }
                ],
                limit=0,
                properties=["string"],
                sorts=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncHubspot) -> None:
        custom = await async_client.crm.objects.custom.upsert(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(BatchResponseSimplePublicUpsertObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.upsert(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(BatchResponseSimplePublicUpsertObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.upsert(
            object_type="objectType",
            inputs=[
                {
                    "id": "id",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(BatchResponseSimplePublicUpsertObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.upsert(
                object_type="",
                inputs=[
                    {
                        "id": "id",
                        "properties": {"foo": "string"},
                    }
                ],
            )
