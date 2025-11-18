# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.associations.schema import CollectionResponseAssociationSpecWithLabel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_label(self, client: Hubspot) -> None:
        definition = client.crm.associations.schema.v4.definitions.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_label_with_all_params(self, client: Hubspot) -> None:
        definition = client.crm.associations.schema.v4.definitions.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
            inverse_label="inverseLabel",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_label(self, client: Hubspot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_label(self, client: Hubspot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_label(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.create_label(
                to_object_type="toObjectType",
                from_object_type="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.create_label(
                to_object_type="",
                from_object_type="fromObjectType",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_label(self, client: Hubspot) -> None:
        definition = client.crm.associations.schema.v4.definitions.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_label(self, client: Hubspot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_label(self, client: Hubspot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_label(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="fromObjectType",
                to_object_type="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_labels(self, client: Hubspot) -> None:
        definition = client.crm.associations.schema.v4.definitions.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_labels(self, client: Hubspot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_labels(self, client: Hubspot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_labels(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.list_labels(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.list_labels(
                to_object_type="",
                from_object_type="fromObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_label(self, client: Hubspot) -> None:
        definition = client.crm.associations.schema.v4.definitions.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_label_with_all_params(self, client: Hubspot) -> None:
        definition = client.crm.associations.schema.v4.definitions.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
            inverse_label="inverseLabel",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_label(self, client: Hubspot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_label(self, client: Hubspot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_label(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.update_label(
                to_object_type="toObjectType",
                from_object_type="",
                association_type_id=0,
                label="label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.update_label(
                to_object_type="",
                from_object_type="fromObjectType",
                association_type_id=0,
                label="label",
            )


class TestAsyncDefinitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_label(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_label_with_all_params(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
            inverse_label="inverseLabel",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_label(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_label(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_label(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.create_label(
                to_object_type="toObjectType",
                from_object_type="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.create_label(
                to_object_type="",
                from_object_type="fromObjectType",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_label(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_label(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_label(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_label(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="fromObjectType",
                to_object_type="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_labels(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_labels(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_labels(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabel, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_labels(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.list_labels(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.list_labels(
                to_object_type="",
                from_object_type="fromObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_label(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_label_with_all_params(self, async_client: AsyncHubspot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
            inverse_label="inverseLabel",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_label(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_label(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_label(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.update_label(
                to_object_type="toObjectType",
                from_object_type="",
                association_type_id=0,
                label="label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.update_label(
                to_object_type="",
                from_object_type="fromObjectType",
                association_type_id=0,
                label="label",
            )
