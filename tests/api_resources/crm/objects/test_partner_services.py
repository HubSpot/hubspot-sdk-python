# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    SimplePublicObject,
    MultiAssociatedObjectWithLabel,
    SimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPartnerServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.objects.partner_services.with_raw_response.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_service = response.parse()
        assert_matches_type(SimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.objects.partner_services.with_streaming_response.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_service = response.parse()
            assert_matches_type(SimplePublicObject, partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_service_id` but received ''"):
            client.crm.objects.partner_services.with_raw_response.update(
                partner_service_id="",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
        )
        assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.objects.partner_services.with_raw_response.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_service = response.parse()
        assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.objects.partner_services.with_streaming_response.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_service = response.parse()
            assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_service_id` but received ''"):
            client.crm.objects.partner_services.with_raw_response.list(
                to_object_type="toObjectType",
                partner_service_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.objects.partner_services.with_raw_response.list(
                to_object_type="",
                partner_service_id="partnerServiceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.get(
            partner_service_id="partnerServiceId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.get(
            partner_service_id="partnerServiceId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.partner_services.with_raw_response.get(
            partner_service_id="partnerServiceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_service = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.partner_services.with_streaming_response.get(
            partner_service_id="partnerServiceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_service = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_service_id` but received ''"):
            client.crm.objects.partner_services.with_raw_response.get(
                partner_service_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        partner_service = client.crm.objects.partner_services.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.objects.partner_services.with_raw_response.search(
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
        partner_service = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.objects.partner_services.with_streaming_response.search(
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

            partner_service = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPartnerServices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.partner_services.with_raw_response.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_service = await response.parse()
        assert_matches_type(SimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.partner_services.with_streaming_response.update(
            partner_service_id="partnerServiceId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_service = await response.parse()
            assert_matches_type(SimplePublicObject, partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_service_id` but received ''"):
            await async_client.crm.objects.partner_services.with_raw_response.update(
                partner_service_id="",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
        )
        assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.partner_services.with_raw_response.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_service = await response.parse()
        assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.partner_services.with_streaming_response.list(
            to_object_type="toObjectType",
            partner_service_id="partnerServiceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_service = await response.parse()
            assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_service_id` but received ''"):
            await async_client.crm.objects.partner_services.with_raw_response.list(
                to_object_type="toObjectType",
                partner_service_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.objects.partner_services.with_raw_response.list(
                to_object_type="",
                partner_service_id="partnerServiceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.get(
            partner_service_id="partnerServiceId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.get(
            partner_service_id="partnerServiceId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.partner_services.with_raw_response.get(
            partner_service_id="partnerServiceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_service = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.partner_services.with_streaming_response.get(
            partner_service_id="partnerServiceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_service = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_service_id` but received ''"):
            await async_client.crm.objects.partner_services.with_raw_response.get(
                partner_service_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        partner_service = await async_client.crm.objects.partner_services.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.partner_services.with_raw_response.search(
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
        partner_service = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.partner_services.with_streaming_response.search(
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

            partner_service = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, partner_service, path=["response"])

        assert cast(Any, response.is_closed) is True
