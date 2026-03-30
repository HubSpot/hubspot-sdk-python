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


class TestListings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.create(
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
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.objects.listings.with_raw_response.create(
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
        listing = response.parse()
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.objects.listings.with_streaming_response.create(
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

            listing = response.parse()
            assert_matches_type(SimplePublicObject, listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.update(
            listing_id="listingId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.update(
            listing_id="listingId",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.objects.listings.with_raw_response.update(
            listing_id="listingId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = response.parse()
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.objects.listings.with_streaming_response.update(
            listing_id="listingId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = response.parse()
            assert_matches_type(SimplePublicObject, listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listing_id` but received ''"):
            client.crm.objects.listings.with_raw_response.update(
                listing_id="",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.list()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.objects.listings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.objects.listings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = response.parse()
            assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.delete(
            "listingId",
        )
        assert listing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.objects.listings.with_raw_response.delete(
            "listingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = response.parse()
        assert listing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.objects.listings.with_streaming_response.delete(
            "listingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = response.parse()
            assert listing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listing_id` but received ''"):
            client.crm.objects.listings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.get(
            listing_id="listingId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.get(
            listing_id="listingId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.listings.with_raw_response.get(
            listing_id="listingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.listings.with_streaming_response.get(
            listing_id="listingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listing_id` but received ''"):
            client.crm.objects.listings.with_raw_response.get(
                listing_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        listing = client.crm.objects.listings.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.objects.listings.with_raw_response.search(
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
        listing = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.objects.listings.with_streaming_response.search(
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

            listing = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncListings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.create(
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
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.listings.with_raw_response.create(
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
        listing = await response.parse()
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.listings.with_streaming_response.create(
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

            listing = await response.parse()
            assert_matches_type(SimplePublicObject, listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.update(
            listing_id="listingId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.update(
            listing_id="listingId",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.listings.with_raw_response.update(
            listing_id="listingId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = await response.parse()
        assert_matches_type(SimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.listings.with_streaming_response.update(
            listing_id="listingId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = await response.parse()
            assert_matches_type(SimplePublicObject, listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listing_id` but received ''"):
            await async_client.crm.objects.listings.with_raw_response.update(
                listing_id="",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.list()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.listings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.listings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = await response.parse()
            assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.delete(
            "listingId",
        )
        assert listing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.listings.with_raw_response.delete(
            "listingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = await response.parse()
        assert listing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.listings.with_streaming_response.delete(
            "listingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = await response.parse()
            assert listing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listing_id` but received ''"):
            await async_client.crm.objects.listings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.get(
            listing_id="listingId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.get(
            listing_id="listingId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.listings.with_raw_response.get(
            listing_id="listingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        listing = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.listings.with_streaming_response.get(
            listing_id="listingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            listing = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, listing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `listing_id` but received ''"):
            await async_client.crm.objects.listings.with_raw_response.get(
                listing_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        listing = await async_client.crm.objects.listings.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.listings.with_raw_response.search(
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
        listing = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.listings.with_streaming_response.search(
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

            listing = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, listing, path=["response"])

        assert cast(Any, response.is_closed) is True
