# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import CollectionResponsePropertyNoPaging
from hubspot_sdk.types.shared import Property, BatchResponseProperty

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.create(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.create(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
            calculation_formula="calculationFormula",
            data_sensitivity="non_sensitive",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.create(
            object_type="objectType",
            app_id="appId",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.create(
            object_type="objectType",
            app_id="appId",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.create(
                object_type="objectType",
                app_id="",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.create(
                object_type="",
                app_id="appId",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=0,
            field_type="booleancheckbox",
            form_field=True,
            group_name="groupName",
            has_unique_value=True,
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.update(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.update(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.update(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.list(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.list(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.list(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.list(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.list(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.delete(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.delete(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.delete(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.delete(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.delete(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.delete(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_batch(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.archive_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[{"name": "name"}],
        )
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_batch(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.archive_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_batch(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.archive_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.archive_batch(
                object_type="objectType",
                app_id="",
                inputs=[{"name": "name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.archive_batch(
                object_type="",
                app_id="appId",
                inputs=[{"name": "name"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.create_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[
                {
                    "field_type": "booleancheckbox",
                    "group_name": "groupName",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.create_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[
                {
                    "field_type": "booleancheckbox",
                    "group_name": "groupName",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.create_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[
                {
                    "field_type": "booleancheckbox",
                    "group_name": "groupName",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(BatchResponseProperty, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.create_batch(
                object_type="objectType",
                app_id="",
                inputs=[
                    {
                        "field_type": "booleancheckbox",
                        "group_name": "groupName",
                        "label": "label",
                        "name": "name",
                        "type": "bool",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.create_batch(
                object_type="",
                app_id="appId",
                inputs=[
                    {
                        "field_type": "booleancheckbox",
                        "group_name": "groupName",
                        "label": "label",
                        "name": "name",
                        "type": "bool",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.get(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.get(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.get(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.get(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.get(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.get(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch_with_all_params(self, client: Hubspot) -> None:
        property = client.cms.media_bridge.properties.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
            data_sensitivity="non_sensitive",
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_batch(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.properties.with_raw_response.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_batch(self, client: Hubspot) -> None:
        with client.cms.media_bridge.properties.with_streaming_response.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(BatchResponseProperty, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_batch(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.get_batch(
                object_type="objectType",
                app_id="",
                archived=True,
                inputs=[{"name": "name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.properties.with_raw_response.get_batch(
                object_type="",
                app_id="appId",
                archived=True,
                inputs=[{"name": "name"}],
            )


class TestAsyncProperties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.create(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.create(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
            calculation_formula="calculationFormula",
            data_sensitivity="non_sensitive",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.create(
            object_type="objectType",
            app_id="appId",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.create(
            object_type="objectType",
            app_id="appId",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.create(
                object_type="objectType",
                app_id="",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.create(
                object_type="",
                app_id="appId",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=0,
            field_type="booleancheckbox",
            form_field=True,
            group_name="groupName",
            has_unique_value=True,
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.update(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.update(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.update(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.update(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.list(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.list(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.list(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(CollectionResponsePropertyNoPaging, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.list(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.list(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.delete(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.delete(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.delete(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.delete(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.delete(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.delete(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_batch(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.archive_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[{"name": "name"}],
        )
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.archive_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.archive_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.archive_batch(
                object_type="objectType",
                app_id="",
                inputs=[{"name": "name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.archive_batch(
                object_type="",
                app_id="appId",
                inputs=[{"name": "name"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.create_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[
                {
                    "field_type": "booleancheckbox",
                    "group_name": "groupName",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.create_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[
                {
                    "field_type": "booleancheckbox",
                    "group_name": "groupName",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.create_batch(
            object_type="objectType",
            app_id="appId",
            inputs=[
                {
                    "field_type": "booleancheckbox",
                    "group_name": "groupName",
                    "label": "label",
                    "name": "name",
                    "type": "bool",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(BatchResponseProperty, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.create_batch(
                object_type="objectType",
                app_id="",
                inputs=[
                    {
                        "field_type": "booleancheckbox",
                        "group_name": "groupName",
                        "label": "label",
                        "name": "name",
                        "type": "bool",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.create_batch(
                object_type="",
                app_id="appId",
                inputs=[
                    {
                        "field_type": "booleancheckbox",
                        "group_name": "groupName",
                        "label": "label",
                        "name": "name",
                        "type": "bool",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.get(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.get(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.get(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.get(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.get(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.get(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch_with_all_params(self, async_client: AsyncHubspot) -> None:
        property = await async_client.cms.media_bridge.properties.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
            data_sensitivity="non_sensitive",
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.properties.with_raw_response.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.properties.with_streaming_response.get_batch(
            object_type="objectType",
            app_id="appId",
            archived=True,
            inputs=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(BatchResponseProperty, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_batch(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.get_batch(
                object_type="objectType",
                app_id="",
                archived=True,
                inputs=[{"name": "name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.properties.with_raw_response.get_batch(
                object_type="",
                app_id="appId",
                archived=True,
                inputs=[{"name": "name"}],
            )
