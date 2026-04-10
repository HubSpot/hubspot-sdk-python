# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.events import (
    Property,
    ExternalBehavioralEventTypeDefinition,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        definition = client.events.definitions.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        definition = client.events.definitions.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                    "description": "description",
                    "name": "name",
                    "options": [
                        {
                            "display_order": 0,
                            "hidden": True,
                            "label": "label",
                            "value": "value",
                            "description": "description",
                        }
                    ],
                }
            ],
            custom_matching_id={
                "primary_object_rule": {
                    "event_property_name": "eventPropertyName",
                    "target_object_property_name": "targetObjectPropertyName",
                }
            },
            description="description",
            name="name",
            primary_object="primaryObject",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        definition = client.events.definitions.update(
            event_name="eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        definition = client.events.definitions.update(
            event_name="eventName",
            description="description",
            label="label",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.update(
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.update(
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.definitions.with_raw_response.update(
                event_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        definition = client.events.definitions.list()
        assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        definition = client.events.definitions.list(
            after="after",
            include_properties=True,
            limit=0,
            search_string="searchString",
            sort_order="sortOrder",
        )
        assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        definition = client.events.definitions.delete(
            "eventName",
        )
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.delete(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.delete(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.definitions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_property(self, client: HubSpot) -> None:
        definition = client.events.definitions.create_property(
            event_name="eventName",
            label="label",
            type="type",
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_property_with_all_params(self, client: HubSpot) -> None:
        definition = client.events.definitions.create_property(
            event_name="eventName",
            label="label",
            type="type",
            description="description",
            name="name",
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_property(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.create_property(
            event_name="eventName",
            label="label",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_property(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.create_property(
            event_name="eventName",
            label="label",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(Property, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_property(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.definitions.with_raw_response.create_property(
                event_name="",
                label="label",
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_property(self, client: HubSpot) -> None:
        definition = client.events.definitions.delete_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_property(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.delete_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_property(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.delete_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_property(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.definitions.with_raw_response.delete_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.events.definitions.with_raw_response.delete_property(
                property_name="",
                event_name="eventName",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        definition = client.events.definitions.get(
            "eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.get(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.get(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.definitions.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_batch(self, client: HubSpot) -> None:
        definition = client.events.definitions.send_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_batch(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.send_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_batch(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.send_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_property(self, client: HubSpot) -> None:
        definition = client.events.definitions.update_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_property_with_all_params(self, client: HubSpot) -> None:
        definition = client.events.definitions.update_property(
            property_name="propertyName",
            event_name="eventName",
            description="description",
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
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_property(self, client: HubSpot) -> None:
        response = client.events.definitions.with_raw_response.update_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_property(self, client: HubSpot) -> None:
        with client.events.definitions.with_streaming_response.update_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(Property, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_property(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.definitions.with_raw_response.update_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.events.definitions.with_raw_response.update_property(
                property_name="",
                event_name="eventName",
            )


class TestAsyncDefinitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                    "description": "description",
                    "name": "name",
                    "options": [
                        {
                            "display_order": 0,
                            "hidden": True,
                            "label": "label",
                            "value": "value",
                            "description": "description",
                        }
                    ],
                }
            ],
            custom_matching_id={
                "primary_object_rule": {
                    "event_property_name": "eventPropertyName",
                    "target_object_property_name": "targetObjectPropertyName",
                }
            },
            description="description",
            name="name",
            primary_object="primaryObject",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.create(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.update(
            event_name="eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.update(
            event_name="eventName",
            description="description",
            label="label",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.update(
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.update(
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.definitions.with_raw_response.update(
                event_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.list()
        assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.list(
            after="after",
            include_properties=True,
            limit=0,
            search_string="searchString",
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.delete(
            "eventName",
        )
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.delete(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.delete(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.definitions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_property(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.create_property(
            event_name="eventName",
            label="label",
            type="type",
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_property_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.create_property(
            event_name="eventName",
            label="label",
            type="type",
            description="description",
            name="name",
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_property(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.create_property(
            event_name="eventName",
            label="label",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_property(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.create_property(
            event_name="eventName",
            label="label",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(Property, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_property(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.definitions.with_raw_response.create_property(
                event_name="",
                label="label",
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_property(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.delete_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_property(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.delete_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_property(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.delete_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_property(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.definitions.with_raw_response.delete_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.events.definitions.with_raw_response.delete_property(
                property_name="",
                event_name="eventName",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.get(
            "eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.get(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.get(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.definitions.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_batch(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.send_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.send_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.send_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_property(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.update_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_property_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.events.definitions.update_property(
            property_name="propertyName",
            event_name="eventName",
            description="description",
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
        )
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_property(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.events.definitions.with_raw_response.update_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(Property, definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_property(self, async_client: AsyncHubSpot) -> None:
        async with async_client.events.definitions.with_streaming_response.update_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(Property, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_property(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.definitions.with_raw_response.update_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.events.definitions.with_raw_response.update_property(
                property_name="",
                event_name="eventName",
            )
