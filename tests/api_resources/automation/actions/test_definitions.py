# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.automation import PublicActionDefinition

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                    "id": "id",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    },
                    "automation_field_type": "automationFieldType",
                    "supported_value_types": ["STATIC_VALUE"],
                }
            ],
            labels={
                "foo": {
                    "action_name": "actionName",
                    "action_card_content": "actionCardContent",
                    "action_description": "actionDescription",
                    "app_display_name": "appDisplayName",
                    "execution_rules": {"foo": "string"},
                    "input_field_descriptions": {"foo": "string"},
                    "input_field_labels": {"foo": "string"},
                    "input_field_option_labels": {"foo": {"foo": "string"}},
                    "output_field_labels": {"foo": "string"},
                }
            },
            object_types=["string"],
            published=True,
            archived_at=0,
            execution_rules=[
                {
                    "conditions": {"foo": {}},
                    "label_name": "labelName",
                }
            ],
            input_field_dependencies=[
                {
                    "controlling_field_name": "controllingFieldName",
                    "dependency_type": "SINGLE_FIELD",
                    "dependent_field_names": ["string"],
                }
            ],
            object_request_options={"properties": ["string"]},
            output_fields=[
                {
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    }
                }
            ],
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.automation.actions.definitions.with_raw_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.automation.actions.definitions.with_streaming_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(PublicActionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.update(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.update(
            definition_id="definitionId",
            app_id=0,
            action_url="actionUrl",
            execution_rules=[
                {
                    "conditions": {"foo": {}},
                    "label_name": "labelName",
                }
            ],
            input_field_dependencies=[
                {
                    "controlling_field_name": "controllingFieldName",
                    "dependency_type": "SINGLE_FIELD",
                    "dependent_field_names": ["string"],
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    },
                    "automation_field_type": "automationFieldType",
                    "supported_value_types": ["STATIC_VALUE"],
                }
            ],
            labels={
                "foo": {
                    "action_name": "actionName",
                    "action_card_content": "actionCardContent",
                    "action_description": "actionDescription",
                    "app_display_name": "appDisplayName",
                    "execution_rules": {"foo": "string"},
                    "input_field_descriptions": {"foo": "string"},
                    "input_field_labels": {"foo": "string"},
                    "input_field_option_labels": {"foo": {"foo": "string"}},
                    "output_field_labels": {"foo": "string"},
                }
            },
            object_request_options={"properties": ["string"]},
            object_types=["string"],
            output_fields=[
                {
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    }
                }
            ],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.automation.actions.definitions.with_raw_response.update(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.automation.actions.definitions.with_streaming_response.update(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(PublicActionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.definitions.with_raw_response.update(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.list(
            app_id=0,
        )
        assert_matches_type(SyncPage[PublicActionDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.list(
            app_id=0,
            after="after",
            archived=True,
            limit=0,
        )
        assert_matches_type(SyncPage[PublicActionDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.automation.actions.definitions.with_raw_response.list(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(SyncPage[PublicActionDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.automation.actions.definitions.with_streaming_response.list(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(SyncPage[PublicActionDefinition], definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.delete(
            definition_id="definitionId",
            app_id=0,
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.automation.actions.definitions.with_raw_response.delete(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.automation.actions.definitions.with_streaming_response.delete(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.definitions.with_raw_response.delete(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.read(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: HubSpot) -> None:
        definition = client.automation.actions.definitions.read(
            definition_id="definitionId",
            app_id=0,
            archived=True,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.automation.actions.definitions.with_raw_response.read(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.automation.actions.definitions.with_streaming_response.read(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(PublicActionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.definitions.with_raw_response.read(
                definition_id="",
                app_id=0,
            )


class TestAsyncDefinitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                    "id": "id",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    },
                    "automation_field_type": "automationFieldType",
                    "supported_value_types": ["STATIC_VALUE"],
                }
            ],
            labels={
                "foo": {
                    "action_name": "actionName",
                    "action_card_content": "actionCardContent",
                    "action_description": "actionDescription",
                    "app_display_name": "appDisplayName",
                    "execution_rules": {"foo": "string"},
                    "input_field_descriptions": {"foo": "string"},
                    "input_field_labels": {"foo": "string"},
                    "input_field_option_labels": {"foo": {"foo": "string"}},
                    "output_field_labels": {"foo": "string"},
                }
            },
            object_types=["string"],
            published=True,
            archived_at=0,
            execution_rules=[
                {
                    "conditions": {"foo": {}},
                    "label_name": "labelName",
                }
            ],
            input_field_dependencies=[
                {
                    "controlling_field_name": "controllingFieldName",
                    "dependency_type": "SINGLE_FIELD",
                    "dependent_field_names": ["string"],
                }
            ],
            object_request_options={"properties": ["string"]},
            output_fields=[
                {
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    }
                }
            ],
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.definitions.with_raw_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.definitions.with_streaming_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "PRE_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(PublicActionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.update(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.update(
            definition_id="definitionId",
            app_id=0,
            action_url="actionUrl",
            execution_rules=[
                {
                    "conditions": {"foo": {}},
                    "label_name": "labelName",
                }
            ],
            input_field_dependencies=[
                {
                    "controlling_field_name": "controllingFieldName",
                    "dependency_type": "SINGLE_FIELD",
                    "dependent_field_names": ["string"],
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    },
                    "automation_field_type": "automationFieldType",
                    "supported_value_types": ["STATIC_VALUE"],
                }
            ],
            labels={
                "foo": {
                    "action_name": "actionName",
                    "action_card_content": "actionCardContent",
                    "action_description": "actionDescription",
                    "app_display_name": "appDisplayName",
                    "execution_rules": {"foo": "string"},
                    "input_field_descriptions": {"foo": "string"},
                    "input_field_labels": {"foo": "string"},
                    "input_field_option_labels": {"foo": {"foo": "string"}},
                    "output_field_labels": {"foo": "string"},
                }
            },
            object_request_options={"properties": ["string"]},
            object_types=["string"],
            output_fields=[
                {
                    "type_definition": {
                        "external_options": True,
                        "name": "name",
                        "options": [
                            {
                                "description": "",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": False,
                                "label": "",
                                "read_only": False,
                                "value": "",
                            }
                        ],
                        "type": "string",
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "CONTACT",
                    }
                }
            ],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.definitions.with_raw_response.update(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.definitions.with_streaming_response.update(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(PublicActionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.definitions.with_raw_response.update(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.list(
            app_id=0,
        )
        assert_matches_type(AsyncPage[PublicActionDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.list(
            app_id=0,
            after="after",
            archived=True,
            limit=0,
        )
        assert_matches_type(AsyncPage[PublicActionDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.definitions.with_raw_response.list(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(AsyncPage[PublicActionDefinition], definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.definitions.with_streaming_response.list(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(AsyncPage[PublicActionDefinition], definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.delete(
            definition_id="definitionId",
            app_id=0,
        )
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.definitions.with_raw_response.delete(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert definition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.definitions.with_streaming_response.delete(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.definitions.with_raw_response.delete(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.read(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubSpot) -> None:
        definition = await async_client.automation.actions.definitions.read(
            definition_id="definitionId",
            app_id=0,
            archived=True,
        )
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.definitions.with_raw_response.read(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(PublicActionDefinition, definition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.definitions.with_streaming_response.read(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(PublicActionDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.definitions.with_raw_response.read(
                definition_id="",
                app_id=0,
            )
