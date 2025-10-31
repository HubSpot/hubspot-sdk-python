# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.marketing import (
    FormDefinitionBase,
    HubSpotFormDefinition,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        form = client.marketing.forms.create()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.marketing.forms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.marketing.forms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        form = client.marketing.forms.update(
            form_id="formId",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        form = client.marketing.forms.update(
            form_id="formId",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
                "lifecycle_stages": [
                    {
                        "object_type_id": "objectTypeId",
                        "value": "value",
                    }
                ],
            },
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
                "css_class": "cssClass",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                        "default_value": "defaultValue",
                                        "description": "description",
                                        "placeholder": "placeholder",
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                            "default_value": "defaultValue",
                            "description": "description",
                            "placeholder": "placeholder",
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                    "rich_text": "richText",
                }
            ],
            legal_consent_options={"type": "none"},
            name="name",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.marketing.forms.with_raw_response.update(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.marketing.forms.with_streaming_response.update(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.update(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        form = client.marketing.forms.list()
        assert_matches_type(SyncPage[HubSpotFormDefinition], form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        form = client.marketing.forms.list(
            after="after",
            archived=True,
            form_types=["hubspot"],
            limit=0,
        )
        assert_matches_type(SyncPage[HubSpotFormDefinition], form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.marketing.forms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(SyncPage[HubSpotFormDefinition], form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.marketing.forms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(SyncPage[HubSpotFormDefinition], form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        form = client.marketing.forms.delete(
            "formId",
        )
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.marketing.forms.with_raw_response.delete(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.marketing.forms.with_streaming_response.delete(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        form = client.marketing.forms.get(
            form_id="formId",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        form = client.marketing.forms.get(
            form_id="formId",
            archived=True,
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.marketing.forms.with_raw_response.get(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.marketing.forms.with_streaming_response.get(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.get(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace(self, client: Hubspot) -> None:
        form = client.marketing.forms.replace(
            "formId",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Hubspot) -> None:
        response = client.marketing.forms.with_raw_response.replace(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Hubspot) -> None:
        with client.marketing.forms.with_streaming_response.replace(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.replace(
                "",
            )


class TestAsyncForms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.create()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.forms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.forms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.update(
            form_id="formId",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.update(
            form_id="formId",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
                "lifecycle_stages": [
                    {
                        "object_type_id": "objectTypeId",
                        "value": "value",
                    }
                ],
            },
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
                "css_class": "cssClass",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                        "default_value": "defaultValue",
                                        "description": "description",
                                        "placeholder": "placeholder",
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                            "default_value": "defaultValue",
                            "description": "description",
                            "placeholder": "placeholder",
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                    "rich_text": "richText",
                }
            ],
            legal_consent_options={"type": "none"},
            name="name",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.forms.with_raw_response.update(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.forms.with_streaming_response.update(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.update(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.list()
        assert_matches_type(AsyncPage[HubSpotFormDefinition], form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.list(
            after="after",
            archived=True,
            form_types=["hubspot"],
            limit=0,
        )
        assert_matches_type(AsyncPage[HubSpotFormDefinition], form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.forms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(AsyncPage[HubSpotFormDefinition], form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.forms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(AsyncPage[HubSpotFormDefinition], form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.delete(
            "formId",
        )
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.forms.with_raw_response.delete(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.forms.with_streaming_response.delete(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.get(
            form_id="formId",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.get(
            form_id="formId",
            archived=True,
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.forms.with_raw_response.get(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.forms.with_streaming_response.get(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.get(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncHubspot) -> None:
        form = await async_client.marketing.forms.replace(
            "formId",
        )
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.forms.with_raw_response.replace(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormDefinitionBase, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.forms.with_streaming_response.replace(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormDefinitionBase, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.replace(
                "",
            )
