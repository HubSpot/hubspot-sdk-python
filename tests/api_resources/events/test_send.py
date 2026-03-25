# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.events import (
    Property,
    ExternalBehavioralEventTypeDefinition,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event_definition(self, client: Hubspot) -> None:
        send = client.events.send.create_event_definition(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event_definition_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.create_event_definition(
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
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_event_definition(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.create_event_definition(
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
        send = response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_event_definition(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.create_event_definition(
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

            send = response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event_definition_property(self, client: Hubspot) -> None:
        send = client.events.send.create_event_definition_property(
            event_name="eventName",
            label="label",
            type="type",
        )
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event_definition_property_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.create_event_definition_property(
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
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_event_definition_property(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.create_event_definition_property(
            event_name="eventName",
            label="label",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_event_definition_property(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.create_event_definition_property(
            event_name="eventName",
            label="label",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(Property, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_event_definition_property(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.send.with_raw_response.create_event_definition_property(
                event_name="",
                label="label",
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_event_definition(self, client: Hubspot) -> None:
        send = client.events.send.delete_event_definition(
            "eventName",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_event_definition(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.delete_event_definition(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_event_definition(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.delete_event_definition(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_event_definition(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.send.with_raw_response.delete_event_definition(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_event_definition_property(self, client: Hubspot) -> None:
        send = client.events.send.delete_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_event_definition_property(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.delete_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_event_definition_property(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.delete_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_event_definition_property(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.send.with_raw_response.delete_event_definition_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.events.send.with_raw_response.delete_event_definition_property(
                property_name="",
                event_name="eventName",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_event_definition(self, client: Hubspot) -> None:
        send = client.events.send.get_event_definition(
            "eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_event_definition(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.get_event_definition(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_event_definition(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.get_event_definition(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_event_definition(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.send.with_raw_response.get_event_definition(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_event_definitions(self, client: Hubspot) -> None:
        send = client.events.send.list_event_definitions()
        assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_event_definitions_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.list_event_definitions(
            after="after",
            include_properties=True,
            limit=0,
            search_string="searchString",
            sort_order="sortOrder",
        )
        assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_event_definitions(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.list_event_definitions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_event_definitions(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.list_event_definitions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(SyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_event(self, client: Hubspot) -> None:
        send = client.events.send.send_event(
            event_name="eventName",
            properties={"foo": "string"},
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_event_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.send_event(
            event_name="eventName",
            properties={"foo": "string"},
            email="email",
            object_id="objectId",
            occurred_at=parse_datetime("2026-01-20T21:14:16.512Z"),
            utk="utk",
            uuid="uuid",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_event(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.send_event(
            event_name="eventName",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_event(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.send_event(
            event_name="eventName",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_event_batch(self, client: Hubspot) -> None:
        send = client.events.send.send_event_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_event_batch(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.send_event_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_event_batch(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.send_event_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_definition(self, client: Hubspot) -> None:
        send = client.events.send.update_event_definition(
            event_name="eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_definition_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.update_event_definition(
            event_name="eventName",
            description="description",
            label="label",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_event_definition(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.update_event_definition(
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_event_definition(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.update_event_definition(
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_event_definition(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.send.with_raw_response.update_event_definition(
                event_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_definition_property(self, client: Hubspot) -> None:
        send = client.events.send.update_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_definition_property_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.update_event_definition_property(
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
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_event_definition_property(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.update_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_event_definition_property(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.update_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(Property, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_event_definition_property(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            client.events.send.with_raw_response.update_event_definition_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.events.send.with_raw_response.update_event_definition_property(
                property_name="",
                event_name="eventName",
            )


class TestAsyncSend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event_definition(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.create_event_definition(
            include_default_properties=True,
            label="label",
            property_definitions=[
                {
                    "label": "label",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event_definition_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.create_event_definition(
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
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_event_definition(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.create_event_definition(
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
        send = await response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_event_definition(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.create_event_definition(
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

            send = await response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event_definition_property(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.create_event_definition_property(
            event_name="eventName",
            label="label",
            type="type",
        )
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event_definition_property_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.create_event_definition_property(
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
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_event_definition_property(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.create_event_definition_property(
            event_name="eventName",
            label="label",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_event_definition_property(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.create_event_definition_property(
            event_name="eventName",
            label="label",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(Property, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_event_definition_property(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.send.with_raw_response.create_event_definition_property(
                event_name="",
                label="label",
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_event_definition(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.delete_event_definition(
            "eventName",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_event_definition(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.delete_event_definition(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_event_definition(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.delete_event_definition(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_event_definition(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.send.with_raw_response.delete_event_definition(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_event_definition_property(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.delete_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_event_definition_property(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.delete_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_event_definition_property(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.delete_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_event_definition_property(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.send.with_raw_response.delete_event_definition_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.events.send.with_raw_response.delete_event_definition_property(
                property_name="",
                event_name="eventName",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_event_definition(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.get_event_definition(
            "eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_event_definition(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.get_event_definition(
            "eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_event_definition(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.get_event_definition(
            "eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_event_definition(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.send.with_raw_response.get_event_definition(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_event_definitions(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.list_event_definitions()
        assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_event_definitions_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.list_event_definitions(
            after="after",
            include_properties=True,
            limit=0,
            search_string="searchString",
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_event_definitions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.list_event_definitions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_event_definitions(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.list_event_definitions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(AsyncPage[ExternalBehavioralEventTypeDefinition], send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_event(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send_event(
            event_name="eventName",
            properties={"foo": "string"},
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_event_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send_event(
            event_name="eventName",
            properties={"foo": "string"},
            email="email",
            object_id="objectId",
            occurred_at=parse_datetime("2026-01-20T21:14:16.512Z"),
            utk="utk",
            uuid="uuid",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_event(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.send_event(
            event_name="eventName",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_event(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.send_event(
            event_name="eventName",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_event_batch(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send_event_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_event_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.send_event_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_event_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.send_event_batch(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_definition(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.update_event_definition(
            event_name="eventName",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_definition_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.update_event_definition(
            event_name="eventName",
            description="description",
            label="label",
        )
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_event_definition(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.update_event_definition(
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_event_definition(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.update_event_definition(
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(ExternalBehavioralEventTypeDefinition, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_event_definition(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.send.with_raw_response.update_event_definition(
                event_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_definition_property(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.update_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_definition_property_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.update_event_definition_property(
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
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_event_definition_property(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.update_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(Property, send, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_event_definition_property(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.update_event_definition_property(
            property_name="propertyName",
            event_name="eventName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(Property, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_event_definition_property(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_name` but received ''"):
            await async_client.events.send.with_raw_response.update_event_definition_property(
                property_name="propertyName",
                event_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.events.send.with_raw_response.update_event_definition_property(
                property_name="",
                event_name="eventName",
            )
