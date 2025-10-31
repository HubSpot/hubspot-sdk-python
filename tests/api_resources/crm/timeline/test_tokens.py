# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.crm import TimelineEventTemplateToken

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        token = client.crm.timeline.tokens.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        token = client.crm.timeline.tokens.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
            created_at=parse_datetime("2020-02-12T20:58:26Z"),
            object_property_name="customPropertyPetType",
            options=[
                {
                    "label": "Dog",
                    "value": "dog",
                },
                {
                    "label": "Cat",
                    "value": "cat",
                },
            ],
            updated_at=parse_datetime("2020-02-12T20:58:26Z"),
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.timeline.tokens.with_raw_response.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.timeline.tokens.with_streaming_response.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.tokens.with_raw_response.create(
                event_template_id="",
                app_id=0,
                label="Pet Type",
                name="petType",
                type="enumeration",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        token = client.crm.timeline.tokens.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        token = client.crm.timeline.tokens.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
            object_property_name="objectPropertyName",
            options=[
                {
                    "label": "Dog",
                    "value": "dog",
                },
                {
                    "label": "Cat",
                    "value": "cat",
                },
                {
                    "label": "Bird",
                    "value": "bird",
                },
            ],
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.timeline.tokens.with_raw_response.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.timeline.tokens.with_streaming_response.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.tokens.with_raw_response.update(
                token_name="tokenName",
                app_id=0,
                event_template_id="",
                label="petType edit",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            client.crm.timeline.tokens.with_raw_response.update(
                token_name="",
                app_id=0,
                event_template_id="eventTemplateId",
                label="petType edit",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        token = client.crm.timeline.tokens.delete(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.timeline.tokens.with_raw_response.delete(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.timeline.tokens.with_streaming_response.delete(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            client.crm.timeline.tokens.with_raw_response.delete(
                token_name="tokenName",
                app_id=0,
                event_template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            client.crm.timeline.tokens.with_raw_response.delete(
                token_name="",
                app_id=0,
                event_template_id="eventTemplateId",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        token = await async_client.crm.timeline.tokens.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        token = await async_client.crm.timeline.tokens.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
            created_at=parse_datetime("2020-02-12T20:58:26Z"),
            object_property_name="customPropertyPetType",
            options=[
                {
                    "label": "Dog",
                    "value": "dog",
                },
                {
                    "label": "Cat",
                    "value": "cat",
                },
            ],
            updated_at=parse_datetime("2020-02-12T20:58:26Z"),
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.timeline.tokens.with_raw_response.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.timeline.tokens.with_streaming_response.create(
            event_template_id="eventTemplateId",
            app_id=0,
            label="Pet Type",
            name="petType",
            type="enumeration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.tokens.with_raw_response.create(
                event_template_id="",
                app_id=0,
                label="Pet Type",
                name="petType",
                type="enumeration",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        token = await async_client.crm.timeline.tokens.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        token = await async_client.crm.timeline.tokens.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
            object_property_name="objectPropertyName",
            options=[
                {
                    "label": "Dog",
                    "value": "dog",
                },
                {
                    "label": "Cat",
                    "value": "cat",
                },
                {
                    "label": "Bird",
                    "value": "bird",
                },
            ],
        )
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.timeline.tokens.with_raw_response.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.timeline.tokens.with_streaming_response.update(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
            label="petType edit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TimelineEventTemplateToken, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.tokens.with_raw_response.update(
                token_name="tokenName",
                app_id=0,
                event_template_id="",
                label="petType edit",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            await async_client.crm.timeline.tokens.with_raw_response.update(
                token_name="",
                app_id=0,
                event_template_id="eventTemplateId",
                label="petType edit",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        token = await async_client.crm.timeline.tokens.delete(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.timeline.tokens.with_raw_response.delete(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.timeline.tokens.with_streaming_response.delete(
            token_name="tokenName",
            app_id=0,
            event_template_id="eventTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_template_id` but received ''"):
            await async_client.crm.timeline.tokens.with_raw_response.delete(
                token_name="tokenName",
                app_id=0,
                event_template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            await async_client.crm.timeline.tokens.with_raw_response.delete(
                token_name="",
                app_id=0,
                event_template_id="eventTemplateId",
            )
