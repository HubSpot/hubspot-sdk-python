# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.shared import Property, CollectionResponsePropertyNoPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        property = client.crm.properties.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        property = client.crm.properties.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
            calculation_formula="calculationFormula",
            data_sensitivity="highly_sensitive",
            description="description",
            display_order=0,
            external_options=True,
            form_field=True,
            has_unique_value=True,
            hidden=True,
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            referenced_object_type="referencedObjectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.properties.with_raw_response.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.properties.with_streaming_response.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.create(
                object_type="",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        property = client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        property = client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=0,
            field_type="booleancheckbox",
            form_field=True,
            group_name="groupName",
            hidden=True,
            label="label",
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            type="bool",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.properties.with_raw_response.update(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.properties.with_streaming_response.update(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.update(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties.with_raw_response.update(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        property = client.crm.properties.list(
            object_type="objectType",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        property = client.crm.properties.list(
            object_type="objectType",
            archived=True,
            data_sensitivity="highly_sensitive",
            locale="locale",
            properties="properties",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.properties.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.properties.with_streaming_response.list(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        property = client.crm.properties.delete(
            property_name="propertyName",
            object_type="objectType",
        )
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.properties.with_raw_response.delete(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.properties.with_streaming_response.delete(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.delete(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties.with_raw_response.delete(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        property = client.crm.properties.get(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        property = client.crm.properties.get(
            property_name="propertyName",
            object_type="objectType",
            archived=True,
            data_sensitivity="highly_sensitive",
            locale="locale",
            properties="properties",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.properties.with_raw_response.get(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.properties.with_streaming_response.get(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.get(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties.with_raw_response.get(
                property_name="",
                object_type="objectType",
            )


class TestAsyncProperties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
            calculation_formula="calculationFormula",
            data_sensitivity="highly_sensitive",
            description="description",
            display_order=0,
            external_options=True,
            form_field=True,
            has_unique_value=True,
            hidden=True,
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            referenced_object_type="referencedObjectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.properties.with_raw_response.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.properties.with_streaming_response.create(
            object_type="objectType",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.create(
                object_type="",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=0,
            field_type="booleancheckbox",
            form_field=True,
            group_name="groupName",
            hidden=True,
            label="label",
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            type="bool",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.properties.with_raw_response.update(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.properties.with_streaming_response.update(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.update(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties.with_raw_response.update(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.list(
            object_type="objectType",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.list(
            object_type="objectType",
            archived=True,
            data_sensitivity="highly_sensitive",
            locale="locale",
            properties="properties",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.properties.with_raw_response.list(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.properties.with_streaming_response.list(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.list(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.delete(
            property_name="propertyName",
            object_type="objectType",
        )
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.properties.with_raw_response.delete(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.properties.with_streaming_response.delete(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.delete(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties.with_raw_response.delete(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.get(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        property = await async_client.crm.properties.get(
            property_name="propertyName",
            object_type="objectType",
            archived=True,
            data_sensitivity="highly_sensitive",
            locale="locale",
            properties="properties",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.properties.with_raw_response.get(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.properties.with_streaming_response.get(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.get(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties.with_raw_response.get(
                property_name="",
                object_type="objectType",
            )
