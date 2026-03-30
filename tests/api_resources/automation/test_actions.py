# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.automation import (
    PublicActionFunction,
    PublicActionRevision,
    PublicActionDefinition,
    PublicActionFunctionIdentifier,
    PublicActionDefinitionRequiresObjectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        action = client.automation.actions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "type": "bool",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        action = client.automation.actions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                    "id": "id",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                                "description": "description",
                                "display_order": 0,
                            }
                        ],
                        "type": "bool",
                        "description": "description",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "OWNER",
                    },
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
                                "description": "description",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": True,
                                "label": "label",
                                "read_only": True,
                                "value": "value",
                            }
                        ],
                        "schema": {
                            "type": "INTEGER",
                            "maximum": 0,
                            "minimum": 0,
                        },
                        "type": "bool",
                        "use_chirp": True,
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "ABANDONED_CART",
                    }
                }
            ],
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "type": "bool",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "type": "bool",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(PublicActionDefinition, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        action = client.automation.actions.update(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        action = client.automation.actions.update(
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
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                                "description": "description",
                                "display_order": 0,
                            }
                        ],
                        "type": "bool",
                        "description": "description",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "OWNER",
                    },
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
                                "description": "description",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": True,
                                "label": "label",
                                "read_only": True,
                                "value": "value",
                            }
                        ],
                        "schema": {
                            "type": "INTEGER",
                            "maximum": 0,
                            "minimum": 0,
                        },
                        "type": "bool",
                        "use_chirp": True,
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "ABANDONED_CART",
                    }
                }
            ],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.update(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.update(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(PublicActionDefinition, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.update(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        action = client.automation.actions.list(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(SyncPage[PublicActionRevision], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        action = client.automation.actions.list(
            definition_id="definitionId",
            app_id=0,
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[PublicActionRevision], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.list(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(SyncPage[PublicActionRevision], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.list(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(SyncPage[PublicActionRevision], action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.list(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        action = client.automation.actions.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.delete(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.automation.actions.with_raw_response.delete(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete(self, client: Hubspot) -> None:
        action = client.automation.actions.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_with_all_params(self, client: Hubspot) -> None:
        action = client.automation.actions.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
            failure_reason_type="failureReasonType",
            request_context={
                "source": "WORKFLOWS",
                "workflow_id": 0,
                "action_execution_index_identifier": {
                    "action_execution_index": 0,
                    "enrollment_id": 0,
                },
                "action_id": 0,
            },
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_complete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `callback_id` but received ''"):
            client.automation.actions.with_raw_response.complete(
                callback_id="",
                output_fields={"foo": "string"},
                typed_outputs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_batch(self, client: Hubspot) -> None:
        action = client.automation.actions.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                    "typed_outputs": {},
                }
            ],
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete_batch(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                    "typed_outputs": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete_batch(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                    "typed_outputs": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_or_replace(self, client: Hubspot) -> None:
        action = client.automation.actions.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_or_replace(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_or_replace(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_or_replace(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.create_or_replace(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.automation.actions.with_raw_response.create_or_replace(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_or_replace_by_function_type(self, client: Hubspot) -> None:
        action = client.automation.actions.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_or_replace_by_function_type(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_or_replace_by_function_type(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_or_replace_by_function_type(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.create_or_replace_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_requires_object(self, client: Hubspot) -> None:
        action = client.automation.actions.create_requires_object(
            definition_id="definitionId",
            app_id=0,
            requires_object=True,
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_requires_object(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.create_requires_object(
            definition_id="definitionId",
            app_id=0,
            requires_object=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_requires_object(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.create_requires_object(
            definition_id="definitionId",
            app_id=0,
            requires_object=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_requires_object(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.create_requires_object(
                definition_id="",
                app_id=0,
                requires_object=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_function_type(self, client: Hubspot) -> None:
        action = client.automation.actions.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_by_function_type(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_function_type(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_by_function_type(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.delete_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        action = client.automation.actions.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionRevision, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(PublicActionRevision, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(PublicActionRevision, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.get(
                revision_id="revisionId",
                app_id=0,
                definition_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.automation.actions.with_raw_response.get(
                revision_id="",
                app_id=0,
                definition_id="definitionId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_function_type(self, client: Hubspot) -> None:
        action = client.automation.actions.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionFunction, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_function_type(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(PublicActionFunction, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_function_type(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(PublicActionFunction, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_function_type(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.get_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_requires_object(self, client: Hubspot) -> None:
        action = client.automation.actions.get_requires_object(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinitionRequiresObjectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_requires_object(self, client: Hubspot) -> None:
        response = client.automation.actions.with_raw_response.get_requires_object(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(PublicActionDefinitionRequiresObjectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_requires_object(self, client: Hubspot) -> None:
        with client.automation.actions.with_streaming_response.get_requires_object(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(PublicActionDefinitionRequiresObjectResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_requires_object(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.with_raw_response.get_requires_object(
                definition_id="",
                app_id=0,
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "type": "bool",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                    "id": "id",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                                "description": "description",
                                "display_order": 0,
                            }
                        ],
                        "type": "bool",
                        "description": "description",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "OWNER",
                    },
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
                                "description": "description",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": True,
                                "label": "label",
                                "read_only": True,
                                "value": "value",
                            }
                        ],
                        "schema": {
                            "type": "INTEGER",
                            "maximum": 0,
                            "minimum": 0,
                        },
                        "type": "bool",
                        "use_chirp": True,
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "ABANDONED_CART",
                    }
                }
            ],
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "type": "bool",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.create(
            app_id=0,
            action_url="actionUrl",
            functions=[
                {
                    "function_source": "functionSource",
                    "function_type": "POST_ACTION_EXECUTION",
                }
            ],
            input_fields=[
                {
                    "is_required": True,
                    "type_definition": {
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "type": "bool",
                    },
                }
            ],
            labels={"foo": {"action_name": "actionName"}},
            object_types=["string"],
            published=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(PublicActionDefinition, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.update(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.update(
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
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                                "description": "description",
                                "display_order": 0,
                            }
                        ],
                        "type": "bool",
                        "description": "description",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "OWNER",
                    },
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
                                "description": "description",
                                "display_order": 0,
                                "double_data": 0,
                                "hidden": True,
                                "label": "label",
                                "read_only": True,
                                "value": "value",
                            }
                        ],
                        "schema": {
                            "type": "INTEGER",
                            "maximum": 0,
                            "minimum": 0,
                        },
                        "type": "bool",
                        "use_chirp": True,
                        "description": "description",
                        "external_options_reference_type": "externalOptionsReferenceType",
                        "field_type": "booleancheckbox",
                        "help_text": "helpText",
                        "label": "label",
                        "options_url": "optionsUrl",
                        "referenced_object_type": "ABANDONED_CART",
                    }
                }
            ],
            published=True,
        )
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.update(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(PublicActionDefinition, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.update(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(PublicActionDefinition, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.update(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.list(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(AsyncPage[PublicActionRevision], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.list(
            definition_id="definitionId",
            app_id=0,
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[PublicActionRevision], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.list(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(AsyncPage[PublicActionRevision], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.list(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(AsyncPage[PublicActionRevision], action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.list(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.delete(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.automation.actions.with_raw_response.delete(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
            failure_reason_type="failureReasonType",
            request_context={
                "source": "WORKFLOWS",
                "workflow_id": 0,
                "action_execution_index_identifier": {
                    "action_execution_index": 0,
                    "enrollment_id": 0,
                },
                "action_id": 0,
            },
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
            typed_outputs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `callback_id` but received ''"):
            await async_client.automation.actions.with_raw_response.complete(
                callback_id="",
                output_fields={"foo": "string"},
                typed_outputs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_batch(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                    "typed_outputs": {},
                }
            ],
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                    "typed_outputs": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                    "typed_outputs": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_or_replace(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_or_replace(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_or_replace(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_or_replace(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.create_or_replace(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.automation.actions.with_raw_response.create_or_replace(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_or_replace_by_function_type(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_or_replace_by_function_type(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_or_replace_by_function_type(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_or_replace_by_function_type(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.create_or_replace_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_requires_object(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.create_requires_object(
            definition_id="definitionId",
            app_id=0,
            requires_object=True,
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_requires_object(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.create_requires_object(
            definition_id="definitionId",
            app_id=0,
            requires_object=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_requires_object(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.create_requires_object(
            definition_id="definitionId",
            app_id=0,
            requires_object=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_requires_object(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.create_requires_object(
                definition_id="",
                app_id=0,
                requires_object=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_function_type(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_function_type(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert action is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_function_type(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_by_function_type(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.delete_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionRevision, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(PublicActionRevision, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(PublicActionRevision, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.get(
                revision_id="revisionId",
                app_id=0,
                definition_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.automation.actions.with_raw_response.get(
                revision_id="",
                app_id=0,
                definition_id="definitionId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_function_type(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionFunction, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_function_type(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(PublicActionFunction, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_function_type(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(PublicActionFunction, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_function_type(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.get_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_requires_object(self, async_client: AsyncHubspot) -> None:
        action = await async_client.automation.actions.get_requires_object(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(PublicActionDefinitionRequiresObjectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_requires_object(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.actions.with_raw_response.get_requires_object(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(PublicActionDefinitionRequiresObjectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_requires_object(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.actions.with_streaming_response.get_requires_object(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(PublicActionDefinitionRequiresObjectResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_requires_object(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.with_raw_response.get_requires_object(
                definition_id="",
                app_id=0,
            )
