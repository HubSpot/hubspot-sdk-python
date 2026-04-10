# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    SimplePublicObject,
    SimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.create(
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
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.objects.custom.with_raw_response.create(
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
        custom = response.parse()
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.objects.custom.with_streaming_response.create(
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

            custom = response.parse()
            assert_matches_type(SimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.create(
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
    def test_method_update(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.objects.custom.with_raw_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.objects.custom.with_streaming_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(SimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.update(
                object_id="objectId",
                object_type="",
                properties={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.objects.custom.with_raw_response.update(
                object_id="",
                object_type="objectType",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.list(
            object_type="objectType",
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
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
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.objects.custom.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
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
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.delete(
            object_id="objectId",
            object_type="objectType",
        )
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.objects.custom.with_raw_response.delete(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.objects.custom.with_streaming_response.delete(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert custom is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.delete(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.objects.custom.with_raw_response.delete(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.get(
            object_id="objectId",
            object_type="objectType",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.get(
            object_id="objectId",
            object_type="objectType",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.objects.custom.with_raw_response.get(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.objects.custom.with_streaming_response.get(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.get(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.objects.custom.with_raw_response.get(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merge(self, client: HubSpot) -> None:
        custom = client.crm.objects.custom.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merge(self, client: HubSpot) -> None:
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
    def test_streaming_response_merge(self, client: HubSpot) -> None:
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
    def test_path_params_merge(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.custom.with_raw_response.merge(
                object_type="",
                object_id_to_merge="objectIdToMerge",
                primary_object_id="primaryObjectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: HubSpot) -> None:
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
    def test_method_search_with_all_params(self, client: HubSpot) -> None:
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
    def test_raw_response_search(self, client: HubSpot) -> None:
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
    def test_streaming_response_search(self, client: HubSpot) -> None:
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
    def test_path_params_search(self, client: HubSpot) -> None:
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


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.create(
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
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.create(
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
        custom = await response.parse()
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.create(
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

            custom = await response.parse()
            assert_matches_type(SimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.create(
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
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.update(
            object_id="objectId",
            object_type="objectType",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(SimplePublicObject, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.update(
                object_id="objectId",
                object_type="",
                properties={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.update(
                object_id="",
                object_type="objectType",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.list(
            object_type="objectType",
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
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
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
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
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.delete(
            object_id="objectId",
            object_type="objectType",
        )
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.delete(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert custom is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.delete(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert custom is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.delete(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.delete(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.get(
            object_id="objectId",
            object_type="objectType",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.get(
            object_id="objectId",
            object_type="objectType",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.custom.with_raw_response.get(
            object_id="objectId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.custom.with_streaming_response.get(
            object_id="objectId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.get(
                object_id="objectId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.get(
                object_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merge(self, async_client: AsyncHubSpot) -> None:
        custom = await async_client.crm.objects.custom.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, custom, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncHubSpot) -> None:
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
    async def test_streaming_response_merge(self, async_client: AsyncHubSpot) -> None:
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
    async def test_path_params_merge(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.custom.with_raw_response.merge(
                object_type="",
                object_id_to_merge="objectIdToMerge",
                primary_object_id="primaryObjectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubSpot) -> None:
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
    async def test_method_search_with_all_params(self, async_client: AsyncHubSpot) -> None:
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
    async def test_raw_response_search(self, async_client: AsyncHubSpot) -> None:
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
    async def test_streaming_response_search(self, async_client: AsyncHubSpot) -> None:
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
    async def test_path_params_search(self, async_client: AsyncHubSpot) -> None:
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
