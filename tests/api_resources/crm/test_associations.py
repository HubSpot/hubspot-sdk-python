# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    ReportCreationResponse,
    LabelsBetweenObjectPair,
    MultiAssociatedObjectWithLabel,
    BatchResponsePublicDefaultAssociation,
    CollectionResponseWithTotalSimplePublicObject,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        association = client.crm.associations.create(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.create(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.create(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.with_raw_response.create(
                to_object_id="toObjectId",
                from_object_type="",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_id` but received ''"):
            client.crm.associations.with_raw_response.create(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.create(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.with_raw_response.create(
                to_object_id="",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        association = client.crm.associations.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )
        assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        association = client.crm.associations.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(SyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.with_raw_response.list(
                to_object_type="toObjectType",
                object_type="",
                object_id="objectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.with_raw_response.list(
                to_object_type="toObjectType",
                object_type="objectType",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.list(
                to_object_type="",
                object_type="objectType",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        association = client.crm.associations.delete(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.delete(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.delete(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.with_raw_response.delete(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.with_raw_response.delete(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.delete(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.with_raw_response.delete(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_high_usage_report(self, client: HubSpot) -> None:
        association = client.crm.associations.request_high_usage_report(
            0,
        )
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_high_usage_report(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.request_high_usage_report(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_high_usage_report(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.request_high_usage_report(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(ReportCreationResponse, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: HubSpot) -> None:
        association = client.crm.associations.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HubSpot) -> None:
        association = client.crm.associations.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.search(
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
        association = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.search(
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

            association = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.with_raw_response.search(
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
    def test_method_update_labels(self, client: HubSpot) -> None:
        association = client.crm.associations.update_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_labels(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.update_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_labels(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.update_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_labels(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.with_raw_response.update_labels(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.with_raw_response.update_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.update_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.with_raw_response.update_labels(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )


class TestAsyncAssociations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.create(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.create(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.create(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.create(
                to_object_id="toObjectId",
                from_object_type="",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.create(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.create(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.create(
                to_object_id="",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )
        assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.list(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(AsyncPage[MultiAssociatedObjectWithLabel], association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.list(
                to_object_type="toObjectType",
                object_type="",
                object_id="objectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.list(
                to_object_type="toObjectType",
                object_type="objectType",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.list(
                to_object_type="",
                object_type="objectType",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.delete(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.delete(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.delete(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.delete(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.delete(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.delete(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.delete(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_high_usage_report(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.request_high_usage_report(
            0,
        )
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_high_usage_report(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.request_high_usage_report(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_high_usage_report(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.request_high_usage_report(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(ReportCreationResponse, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.search(
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
        association = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.search(
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

            association = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.search(
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
    async def test_method_update_labels(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.update_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_labels(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.update_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_labels(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.update_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_labels(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.update_labels(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.update_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.update_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.update_labels(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )
