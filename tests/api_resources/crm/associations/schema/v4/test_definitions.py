# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.associations.schema import CollectionResponseAssociationSpecWithLabelNoPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        definition = client.crm.associations.schema.v4.definitions.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        definition = client.crm.associations.schema.v4.definitions.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
            inverse_label="inverseLabel",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        definition = client.crm.associations.schema.v4.definitions.update(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        definition = client.crm.associations.schema.v4.definitions.update(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
            inverse_label="inverseLabel",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.update(
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
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.update(
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
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.update(
                to_object_type="toObjectType",
                from_object_type="",
                association_type_id=0,
                label="label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.update(
                to_object_type="",
                from_object_type="fromObjectType",
                association_type_id=0,
                label="label",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        definition = client.crm.associations.schema.v4.definitions.list(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.list(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.list(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.list(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.list(
                to_object_type="",
                from_object_type="fromObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        definition = client.crm.associations.schema.v4.definitions.delete(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.definitions.with_raw_response.delete(
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
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.definitions.with_streaming_response.delete(
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
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.delete(
                association_type_id=0,
                from_object_type="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.definitions.with_raw_response.delete(
                association_type_id=0,
                from_object_type="fromObjectType",
                to_object_type="",
            )


class TestAsyncDefinitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
            inverse_label="inverseLabel",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.update(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.update(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
            inverse_label="inverseLabel",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.update(
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
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.update(
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
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.update(
                to_object_type="toObjectType",
                from_object_type="",
                association_type_id=0,
                label="label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.update(
                to_object_type="",
                from_object_type="fromObjectType",
                association_type_id=0,
                label="label",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.list(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.list(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.list(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.list(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.list(
                to_object_type="",
                from_object_type="fromObjectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.crm.associations.schema.v4.definitions.delete(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.schema.v4.definitions.with_raw_response.delete(
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
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.schema.v4.definitions.with_streaming_response.delete(
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
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.delete(
                association_type_id=0,
                from_object_type="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.definitions.with_raw_response.delete(
                association_type_id=0,
                from_object_type="fromObjectType",
                to_object_type="",
            )
