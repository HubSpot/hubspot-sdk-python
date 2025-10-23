# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    BatchResponsePublicDefaultAssociation,
    CreatedResponseLabelsBetweenObjectPair,
    CollectionResponseMultiAssociatedObjectWithLabel,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV4:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_default_association(self, client: HubSpot) -> None:
        v4 = client.crm.associations.v4.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_default_association(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.with_raw_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_default_association(self, client: HubSpot) -> None:
        with client.crm.associations.v4.with_streaming_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_default_association(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_id` but received ''"):
            client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_association(self, client: HubSpot) -> None:
        v4 = client.crm.associations.v4.delete_association(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )
        assert v4 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_association(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.with_raw_response.delete_association(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert v4 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_association(self, client: HubSpot) -> None:
        with client.crm.associations.v4.with_streaming_response.delete_association(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert v4 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_association(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_associations_by_type(self, client: HubSpot) -> None:
        v4 = client.crm.associations.v4.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )
        assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_associations_by_type_with_all_params(self, client: HubSpot) -> None:
        v4 = client.crm.associations.v4.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
            after="after",
            limit=0,
        )
        assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_associations_by_type(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.with_raw_response.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_associations_by_type(self, client: HubSpot) -> None:
        with client.crm.associations.v4.with_streaming_response.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_associations_by_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.list_associations_by_type(
                to_object_type="toObjectType",
                object_type="",
                object_id="objectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.v4.with_raw_response.list_associations_by_type(
                to_object_type="toObjectType",
                object_type="objectType",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.list_associations_by_type(
                to_object_type="",
                object_type="objectType",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_association_labels(self, client: HubSpot) -> None:
        v4 = client.crm.associations.v4.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 279,
                }
            ],
        )
        assert_matches_type(CreatedResponseLabelsBetweenObjectPair, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_association_labels(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.with_raw_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 279,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert_matches_type(CreatedResponseLabelsBetweenObjectPair, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_association_labels(self, client: HubSpot) -> None:
        with client.crm.associations.v4.with_streaming_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 279,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert_matches_type(CreatedResponseLabelsBetweenObjectPair, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_association_labels(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )


class TestAsyncV4:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_default_association(self, async_client: AsyncHubSpot) -> None:
        v4 = await async_client.crm.associations.v4.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_default_association(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.with_raw_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_default_association(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.with_streaming_response.create_default_association(
            to_object_id="toObjectId",
            from_object_type="fromObjectType",
            from_object_id="fromObjectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_default_association(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_id` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="toObjectId",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.create_default_association(
                to_object_id="",
                from_object_type="fromObjectType",
                from_object_id="fromObjectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_association(self, async_client: AsyncHubSpot) -> None:
        v4 = await async_client.crm.associations.v4.delete_association(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )
        assert v4 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_association(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.with_raw_response.delete_association(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert v4 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_association(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.with_streaming_response.delete_association(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert v4 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_association(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.delete_association(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_associations_by_type(self, async_client: AsyncHubSpot) -> None:
        v4 = await async_client.crm.associations.v4.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )
        assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_associations_by_type_with_all_params(self, async_client: AsyncHubSpot) -> None:
        v4 = await async_client.crm.associations.v4.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
            after="after",
            limit=0,
        )
        assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_associations_by_type(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.with_raw_response.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_associations_by_type(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.with_streaming_response.list_associations_by_type(
            to_object_type="toObjectType",
            object_type="objectType",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert_matches_type(CollectionResponseMultiAssociatedObjectWithLabel, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_associations_by_type(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.list_associations_by_type(
                to_object_type="toObjectType",
                object_type="",
                object_id="objectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.list_associations_by_type(
                to_object_type="toObjectType",
                object_type="objectType",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.list_associations_by_type(
                to_object_type="",
                object_type="objectType",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_association_labels(self, async_client: AsyncHubSpot) -> None:
        v4 = await async_client.crm.associations.v4.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 279,
                }
            ],
        )
        assert_matches_type(CreatedResponseLabelsBetweenObjectPair, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_association_labels(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.with_raw_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 279,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert_matches_type(CreatedResponseLabelsBetweenObjectPair, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_association_labels(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.with_streaming_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 279,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert_matches_type(CreatedResponseLabelsBetweenObjectPair, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_association_labels(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.update_association_labels(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 279,
                    }
                ],
            )
