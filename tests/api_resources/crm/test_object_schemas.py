# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    ObjectSchema,
    CollectionResponseObjectSchemaNoPaging,
)
from hubspot_sdk.types.shared import ObjectTypeDefinition, AssociationDefinition

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjectSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={},
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                    "description": "description",
                    "display_order": 0,
                    "external_options_reference_type": "externalOptionsReferenceType",
                    "form_field": True,
                    "group_name": "groupName",
                    "has_unique_value": True,
                    "hidden": True,
                    "number_display_hint": "currency",
                    "options": [
                        {
                            "display_order": 0,
                            "hidden": True,
                            "label": "label",
                            "value": "value",
                            "description": "description",
                        }
                    ],
                    "option_sort_strategy": "ALPHABETICAL",
                    "referenced_object_type": "referencedObjectType",
                    "searchable_in_global_search": True,
                    "show_currency_symbol": True,
                    "text_display_hint": "domain_name",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
            description="description",
            primary_display_property="primaryDisplayProperty",
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.object_schemas.with_raw_response.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={},
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = response.parse()
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.object_schemas.with_streaming_response.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={},
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = response.parse()
            assert_matches_type(ObjectSchema, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.update(
            object_type="objectType",
            clear_description=True,
        )
        assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.update(
            object_type="objectType",
            clear_description=True,
            allows_sensitive_properties=True,
            description="description",
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            primary_display_property="primaryDisplayProperty",
            required_properties=["string"],
            restorable=True,
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.object_schemas.with_raw_response.update(
            object_type="objectType",
            clear_description=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = response.parse()
        assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.object_schemas.with_streaming_response.update(
            object_type="objectType",
            clear_description=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = response.parse()
            assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.object_schemas.with_raw_response.update(
                object_type="",
                clear_description=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.list()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.list(
            archived=True,
            include_association_definitions=True,
            include_audit_metadata=True,
            include_property_definitions=True,
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.object_schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = response.parse()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.object_schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = response.parse()
            assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.delete(
            object_type="objectType",
        )
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.delete(
            object_type="objectType",
            archived=True,
        )
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.object_schemas.with_raw_response.delete(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = response.parse()
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.object_schemas.with_streaming_response.delete(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = response.parse()
            assert object_schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.object_schemas.with_raw_response.delete(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_association(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(AssociationDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_association_with_all_params(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
            name="name",
        )
        assert_matches_type(AssociationDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_association(self, client: HubSpot) -> None:
        response = client.crm.object_schemas.with_raw_response.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = response.parse()
        assert_matches_type(AssociationDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_association(self, client: HubSpot) -> None:
        with client.crm.object_schemas.with_streaming_response.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = response.parse()
            assert_matches_type(AssociationDefinition, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_association(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.object_schemas.with_raw_response.create_association(
                object_type="",
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_association(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.delete_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_association(self, client: HubSpot) -> None:
        response = client.crm.object_schemas.with_raw_response.delete_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = response.parse()
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_association(self, client: HubSpot) -> None:
        with client.crm.object_schemas.with_streaming_response.delete_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = response.parse()
            assert object_schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_association(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.object_schemas.with_raw_response.delete_association(
                association_identifier="associationIdentifier",
                object_type="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `association_identifier` but received ''"
        ):
            client.crm.object_schemas.with_raw_response.delete_association(
                association_identifier="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.get(
            object_type="objectType",
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        object_schema = client.crm.object_schemas.get(
            object_type="objectType",
            include_association_definitions=True,
            include_audit_metadata=True,
            include_property_definitions=True,
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.object_schemas.with_raw_response.get(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = response.parse()
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.object_schemas.with_streaming_response.get(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = response.parse()
            assert_matches_type(ObjectSchema, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.object_schemas.with_raw_response.get(
                object_type="",
            )


class TestAsyncObjectSchemas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={},
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                    "description": "description",
                    "display_order": 0,
                    "external_options_reference_type": "externalOptionsReferenceType",
                    "form_field": True,
                    "group_name": "groupName",
                    "has_unique_value": True,
                    "hidden": True,
                    "number_display_hint": "currency",
                    "options": [
                        {
                            "display_order": 0,
                            "hidden": True,
                            "label": "label",
                            "value": "value",
                            "description": "description",
                        }
                    ],
                    "option_sort_strategy": "ALPHABETICAL",
                    "referenced_object_type": "referencedObjectType",
                    "searchable_in_global_search": True,
                    "show_currency_symbol": True,
                    "text_display_hint": "domain_name",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
            description="description",
            primary_display_property="primaryDisplayProperty",
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.object_schemas.with_raw_response.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={},
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = await response.parse()
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.object_schemas.with_streaming_response.create(
            allows_sensitive_properties=True,
            associated_objects=["string"],
            labels={},
            name="name",
            properties=[
                {
                    "field_type": "fieldType",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
            required_properties=["string"],
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = await response.parse()
            assert_matches_type(ObjectSchema, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.update(
            object_type="objectType",
            clear_description=True,
        )
        assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.update(
            object_type="objectType",
            clear_description=True,
            allows_sensitive_properties=True,
            description="description",
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            primary_display_property="primaryDisplayProperty",
            required_properties=["string"],
            restorable=True,
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.object_schemas.with_raw_response.update(
            object_type="objectType",
            clear_description=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = await response.parse()
        assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.object_schemas.with_streaming_response.update(
            object_type="objectType",
            clear_description=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = await response.parse()
            assert_matches_type(ObjectTypeDefinition, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.object_schemas.with_raw_response.update(
                object_type="",
                clear_description=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.list()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.list(
            archived=True,
            include_association_definitions=True,
            include_audit_metadata=True,
            include_property_definitions=True,
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.object_schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = await response.parse()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.object_schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = await response.parse()
            assert_matches_type(CollectionResponseObjectSchemaNoPaging, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.delete(
            object_type="objectType",
        )
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.delete(
            object_type="objectType",
            archived=True,
        )
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.object_schemas.with_raw_response.delete(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = await response.parse()
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.object_schemas.with_streaming_response.delete(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = await response.parse()
            assert object_schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.object_schemas.with_raw_response.delete(
                object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_association(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(AssociationDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_association_with_all_params(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
            name="name",
        )
        assert_matches_type(AssociationDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_association(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.object_schemas.with_raw_response.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = await response.parse()
        assert_matches_type(AssociationDefinition, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_association(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.object_schemas.with_streaming_response.create_association(
            object_type="objectType",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = await response.parse()
            assert_matches_type(AssociationDefinition, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_association(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.object_schemas.with_raw_response.create_association(
                object_type="",
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_association(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.delete_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_association(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.object_schemas.with_raw_response.delete_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = await response.parse()
        assert object_schema is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_association(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.object_schemas.with_streaming_response.delete_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = await response.parse()
            assert object_schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_association(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.object_schemas.with_raw_response.delete_association(
                association_identifier="associationIdentifier",
                object_type="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `association_identifier` but received ''"
        ):
            await async_client.crm.object_schemas.with_raw_response.delete_association(
                association_identifier="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.get(
            object_type="objectType",
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        object_schema = await async_client.crm.object_schemas.get(
            object_type="objectType",
            include_association_definitions=True,
            include_audit_metadata=True,
            include_property_definitions=True,
        )
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.object_schemas.with_raw_response.get(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_schema = await response.parse()
        assert_matches_type(ObjectSchema, object_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.object_schemas.with_streaming_response.get(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_schema = await response.parse()
            assert_matches_type(ObjectSchema, object_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.object_schemas.with_raw_response.get(
                object_type="",
            )
