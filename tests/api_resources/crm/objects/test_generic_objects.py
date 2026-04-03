# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    SimplePublicObject,
    SimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenericObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.create(
            object_type="objectType",
            associations=[
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
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.objects.generic_objects.with_raw_response.create(
            object_type="objectType",
            associations=[
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
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = response.parse()
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.objects.generic_objects.with_streaming_response.create(
            object_type="objectType",
            associations=[
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
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = response.parse()
            assert_matches_type(SimplePublicObject, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.create(
                object_type="",
                associations=[
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
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.objects.generic_objects.with_raw_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = response.parse()
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.objects.generic_objects.with_streaming_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = response.parse()
            assert_matches_type(SimplePublicObject, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.update(
                object_id="objectId",
                object_type="",
                properties={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.update(
                object_id="",
                object_type="objectType",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.list(
            object_type="objectType",
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.list(
            object_type="objectType",
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.objects.generic_objects.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.objects.generic_objects.with_streaming_response.list(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = response.parse()
            assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.delete(
            object_id="objectId",
            object_type="objectType",
        )
        assert generic_object is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.objects.generic_objects.with_raw_response.delete(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = response.parse()
        assert generic_object is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.objects.generic_objects.with_streaming_response.delete(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = response.parse()
            assert generic_object is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.delete(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.delete(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.get(
            object_id="objectId",
            object_type="objectType",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.get(
            object_id="objectId",
            object_type="objectType",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.generic_objects.with_raw_response.get(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.generic_objects.with_streaming_response.get(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.get(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.get(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        generic_object = client.crm.objects.generic_objects.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.objects.generic_objects.with_raw_response.search(
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
        generic_object = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.objects.generic_objects.with_streaming_response.search(
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

            generic_object = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.generic_objects.with_raw_response.search(
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


class TestAsyncGenericObjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.create(
            object_type="objectType",
            associations=[
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
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.generic_objects.with_raw_response.create(
            object_type="objectType",
            associations=[
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
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = await response.parse()
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.generic_objects.with_streaming_response.create(
            object_type="objectType",
            associations=[
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
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = await response.parse()
            assert_matches_type(SimplePublicObject, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.create(
                object_type="",
                associations=[
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
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.generic_objects.with_raw_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = await response.parse()
        assert_matches_type(SimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.generic_objects.with_streaming_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = await response.parse()
            assert_matches_type(SimplePublicObject, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.update(
                object_id="objectId",
                object_type="",
                properties={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.update(
                object_id="",
                object_type="objectType",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.list(
            object_type="objectType",
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.list(
            object_type="objectType",
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.generic_objects.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.generic_objects.with_streaming_response.list(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = await response.parse()
            assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.delete(
            object_id="objectId",
            object_type="objectType",
        )
        assert generic_object is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.generic_objects.with_raw_response.delete(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = await response.parse()
        assert generic_object is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.generic_objects.with_streaming_response.delete(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = await response.parse()
            assert generic_object is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.delete(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.delete(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.get(
            object_id="objectId",
            object_type="objectType",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.get(
            object_id="objectId",
            object_type="objectType",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.generic_objects.with_raw_response.get(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generic_object = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.generic_objects.with_streaming_response.get(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generic_object = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.get(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.get(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        generic_object = await async_client.crm.objects.generic_objects.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.generic_objects.with_raw_response.search(
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
        generic_object = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.generic_objects.with_streaming_response.search(
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

            generic_object = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, generic_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.generic_objects.with_raw_response.search(
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
