# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.crm import TimelineEventTemplate, CollectionResponseTimelineEventTemplateNoPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        template = client.crm.timeline.templates.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        template = client.crm.timeline.templates.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "White",
                            "value": "white",
                        },
                        {
                            "label": "Black",
                            "value": "black",
                        },
                        {
                            "label": "Brown",
                            "value": "brown",
                        },
                        {
                            "label": "Other",
                            "value": "other",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
            ],
            detail_template="Registration occurred at {{#formatDate timestamp}}{{/formatDate}}\n\n#### Questions\n{{#each extraData.questions}}\n  **{{question}}**: {{answer}}\n{{/each}}",
            header_template="Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})",
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.timeline.templates.with_raw_response.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.timeline.templates.with_streaming_response.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TimelineEventTemplate, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        template = client.crm.timeline.templates.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        template = client.crm.timeline.templates.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "firstname",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "White",
                            "value": "white",
                        },
                        {
                            "label": "Black",
                            "value": "black",
                        },
                        {
                            "label": "Brown",
                            "value": "brown",
                        },
                        {
                            "label": "Yellow",
                            "value": "yellow",
                        },
                        {
                            "label": "Other",
                            "value": "other",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
            ],
            detail_template="Registration occurred at {{#formatDate timestamp}}{{/formatDate}}\n\n#### Questions\n{{#each extraData.questions}}\n  **{{question}}**: {{answer}}\n{{/each}}\n\nEDIT",
            header_template="Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})",
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.timeline.templates.with_raw_response.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.timeline.templates.with_streaming_response.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TimelineEventTemplate, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.templates.with_raw_response.update(
                event_template_id="",
                app_id=0,
                id="1001298",
                name="PetSpot Registration",
                tokens=[
                    {
                        "label": "Pet Name",
                        "name": "petName",
                        "type": "string",
                    },
                    {
                        "label": "Pet Age",
                        "name": "petAge",
                        "type": "number",
                    },
                    {
                        "label": "Pet Color",
                        "name": "petColor",
                        "type": "enumeration",
                    },
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        template = client.crm.timeline.templates.list(
            0,
        )
        assert_matches_type(CollectionResponseTimelineEventTemplateNoPaging, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.timeline.templates.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(CollectionResponseTimelineEventTemplateNoPaging, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.timeline.templates.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(CollectionResponseTimelineEventTemplateNoPaging, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        template = client.crm.timeline.templates.delete(
            event_template_id="eventTemplateId",
            app_id=0,
        )
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.timeline.templates.with_raw_response.delete(
            event_template_id="eventTemplateId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.timeline.templates.with_streaming_response.delete(
            event_template_id="eventTemplateId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.templates.with_raw_response.delete(
                event_template_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        template = client.crm.timeline.templates.get(
            event_template_id="eventTemplateId",
            app_id=0,
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.timeline.templates.with_raw_response.get(
            event_template_id="eventTemplateId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.timeline.templates.with_streaming_response.get(
            event_template_id="eventTemplateId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TimelineEventTemplate, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.templates.with_raw_response.get(
                event_template_id="",
                app_id=0,
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        template = await async_client.crm.timeline.templates.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        template = await async_client.crm.timeline.templates.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "White",
                            "value": "white",
                        },
                        {
                            "label": "Black",
                            "value": "black",
                        },
                        {
                            "label": "Brown",
                            "value": "brown",
                        },
                        {
                            "label": "Other",
                            "value": "other",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
            ],
            detail_template="Registration occurred at {{#formatDate timestamp}}{{/formatDate}}\n\n#### Questions\n{{#each extraData.questions}}\n  **{{question}}**: {{answer}}\n{{/each}}",
            header_template="Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})",
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.templates.with_raw_response.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.templates.with_streaming_response.create(
            app_id=0,
            name="PetSpot Registration",
            object_type="contacts",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TimelineEventTemplate, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        template = await async_client.crm.timeline.templates.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        template = await async_client.crm.timeline.templates.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "firstname",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "Dog",
                            "value": "dog",
                        },
                        {
                            "label": "Cat",
                            "value": "cat",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                    "created_at": parse_datetime("2020-02-12T20:58:26Z"),
                    "object_property_name": "customPropertyPetType",
                    "options": [
                        {
                            "label": "White",
                            "value": "white",
                        },
                        {
                            "label": "Black",
                            "value": "black",
                        },
                        {
                            "label": "Brown",
                            "value": "brown",
                        },
                        {
                            "label": "Yellow",
                            "value": "yellow",
                        },
                        {
                            "label": "Other",
                            "value": "other",
                        },
                    ],
                    "updated_at": parse_datetime("2020-02-12T20:58:26Z"),
                },
            ],
            detail_template="Registration occurred at {{#formatDate timestamp}}{{/formatDate}}\n\n#### Questions\n{{#each extraData.questions}}\n  **{{question}}**: {{answer}}\n{{/each}}\n\nEDIT",
            header_template="Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})",
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.templates.with_raw_response.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.templates.with_streaming_response.update(
            event_template_id="eventTemplateId",
            app_id=0,
            id="1001298",
            name="PetSpot Registration",
            tokens=[
                {
                    "label": "Pet Name",
                    "name": "petName",
                    "type": "string",
                },
                {
                    "label": "Pet Age",
                    "name": "petAge",
                    "type": "number",
                },
                {
                    "label": "Pet Color",
                    "name": "petColor",
                    "type": "enumeration",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TimelineEventTemplate, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.templates.with_raw_response.update(
                event_template_id="",
                app_id=0,
                id="1001298",
                name="PetSpot Registration",
                tokens=[
                    {
                        "label": "Pet Name",
                        "name": "petName",
                        "type": "string",
                    },
                    {
                        "label": "Pet Age",
                        "name": "petAge",
                        "type": "number",
                    },
                    {
                        "label": "Pet Color",
                        "name": "petColor",
                        "type": "enumeration",
                    },
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        template = await async_client.crm.timeline.templates.list(
            0,
        )
        assert_matches_type(CollectionResponseTimelineEventTemplateNoPaging, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.templates.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(CollectionResponseTimelineEventTemplateNoPaging, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.templates.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(CollectionResponseTimelineEventTemplateNoPaging, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        template = await async_client.crm.timeline.templates.delete(
            event_template_id="eventTemplateId",
            app_id=0,
        )
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.templates.with_raw_response.delete(
            event_template_id="eventTemplateId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.templates.with_streaming_response.delete(
            event_template_id="eventTemplateId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.templates.with_raw_response.delete(
                event_template_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        template = await async_client.crm.timeline.templates.get(
            event_template_id="eventTemplateId",
            app_id=0,
        )
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.timeline.templates.with_raw_response.get(
            event_template_id="eventTemplateId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TimelineEventTemplate, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.timeline.templates.with_streaming_response.get(
            event_template_id="eventTemplateId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TimelineEventTemplate, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.templates.with_raw_response.get(
                event_template_id="",
                app_id=0,
            )
