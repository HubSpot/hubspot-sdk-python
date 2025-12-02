# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.events import AssociationDefinition
from hubspot_sdk.types.crm.objects import ObjectSchema, ObjectsSchemasObjectTypeDefinition
from hubspot_sdk.types.cms.media_bridge import (
    SchemaListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.update(
            object_type="objectType",
            app_id=0,
        )
        assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.update(
            object_type="objectType",
            app_id=0,
            clear_description=True,
            description="description",
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            primary_display_property="my_object_property",
            required_properties=["my_object_property"],
            restorable=True,
            searchable_properties=["my_object_property"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.schemas.with_raw_response.update(
            object_type="objectType",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.cms.media_bridge.schemas.with_streaming_response.update(
            object_type="objectType",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.schemas.with_raw_response.update(
                object_type="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.list(
            app_id=0,
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.list(
            app_id=0,
            archived=True,
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.schemas.with_raw_response.list(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.media_bridge.schemas.with_streaming_response.list(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_association(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_association_with_all_params(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
            name="name",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_association(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.schemas.with_raw_response.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_association(self, client: Hubspot) -> None:
        with client.cms.media_bridge.schemas.with_streaming_response.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(AssociationDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_association(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.schemas.with_raw_response.create_association(
                object_type="",
                app_id=0,
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_association(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.delete_association(
            association_id="associationId",
            app_id=0,
            object_type="objectType",
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_association(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.schemas.with_raw_response.delete_association(
            association_id="associationId",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_association(self, client: Hubspot) -> None:
        with client.cms.media_bridge.schemas.with_streaming_response.delete_association(
            association_id="associationId",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_association(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.schemas.with_raw_response.delete_association(
                association_id="associationId",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_id` but received ''"):
            client.cms.media_bridge.schemas.with_raw_response.delete_association(
                association_id="",
                app_id=0,
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        schema = client.cms.media_bridge.schemas.get(
            object_type="objectType",
            app_id=0,
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.schemas.with_raw_response.get(
            object_type="objectType",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.media_bridge.schemas.with_streaming_response.get(
            object_type="objectType",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(ObjectSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.schemas.with_raw_response.get(
                object_type="",
                app_id=0,
            )


class TestAsyncSchemas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.update(
            object_type="objectType",
            app_id=0,
        )
        assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.update(
            object_type="objectType",
            app_id=0,
            clear_description=True,
            description="description",
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            primary_display_property="my_object_property",
            required_properties=["my_object_property"],
            restorable=True,
            searchable_properties=["my_object_property"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.schemas.with_raw_response.update(
            object_type="objectType",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.schemas.with_streaming_response.update(
            object_type="objectType",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(ObjectsSchemasObjectTypeDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.schemas.with_raw_response.update(
                object_type="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.list(
            app_id=0,
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.list(
            app_id=0,
            archived=True,
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.schemas.with_raw_response.list(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.schemas.with_streaming_response.list(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_association(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_association_with_all_params(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
            name="name",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_association(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.schemas.with_raw_response.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_association(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.schemas.with_streaming_response.create_association(
            object_type="objectType",
            app_id=0,
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(AssociationDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_association(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.schemas.with_raw_response.create_association(
                object_type="",
                app_id=0,
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_association(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.delete_association(
            association_id="associationId",
            app_id=0,
            object_type="objectType",
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_association(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.schemas.with_raw_response.delete_association(
            association_id="associationId",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_association(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.schemas.with_streaming_response.delete_association(
            association_id="associationId",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_association(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.schemas.with_raw_response.delete_association(
                association_id="associationId",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_id` but received ''"):
            await async_client.cms.media_bridge.schemas.with_raw_response.delete_association(
                association_id="",
                app_id=0,
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        schema = await async_client.cms.media_bridge.schemas.get(
            object_type="objectType",
            app_id=0,
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.schemas.with_raw_response.get(
            object_type="objectType",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.schemas.with_streaming_response.get(
            object_type="objectType",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(ObjectSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.schemas.with_raw_response.get(
                object_type="",
                app_id=0,
            )
