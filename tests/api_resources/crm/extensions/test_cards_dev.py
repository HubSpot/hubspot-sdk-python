# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.extensions import (
    PublicCardResponse,
    PublicCardListResponse,
    CardMigrateViewsResponse,
    IntegratorCardPayloadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardsDev:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
            },
            title="title",
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
                "serverless_function": "serverlessFunction",
            },
            title="title",
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards_dev.with_raw_response.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
            },
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = response.parse()
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.extensions.cards_dev.with_streaming_response.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
            },
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = response.parse()
            assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.update(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.update(
            card_id="cardId",
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "card_type": "EXTERNAL",
                "serverless_function": "serverlessFunction",
                "target_url": "targetUrl",
            },
            title="title",
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards_dev.with_raw_response.update(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = response.parse()
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.extensions.cards_dev.with_streaming_response.update(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = response.parse()
            assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.crm.extensions.cards_dev.with_raw_response.update(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.delete(
            card_id="cardId",
            app_id=0,
        )
        assert cards_dev is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards_dev.with_raw_response.delete(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = response.parse()
        assert cards_dev is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.extensions.cards_dev.with_streaming_response.delete(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = response.parse()
            assert cards_dev is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.crm.extensions.cards_dev.with_raw_response.delete(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.get(
            0,
        )
        assert_matches_type(PublicCardListResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards_dev.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = response.parse()
        assert_matches_type(PublicCardListResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.extensions.cards_dev.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = response.parse()
            assert_matches_type(PublicCardListResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_id(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.get_by_id(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_id(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards_dev.with_raw_response.get_by_id(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = response.parse()
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_id(self, client: HubSpot) -> None:
        with client.crm.extensions.cards_dev.with_streaming_response.get_by_id(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = response.parse()
            assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.crm.extensions.cards_dev.with_raw_response.get_by_id(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_sample_response(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.get_sample_response()
        assert_matches_type(IntegratorCardPayloadResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_sample_response(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards_dev.with_raw_response.get_sample_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = response.parse()
        assert_matches_type(IntegratorCardPayloadResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_sample_response(self, client: HubSpot) -> None:
        with client.crm.extensions.cards_dev.with_streaming_response.get_sample_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = response.parse()
            assert_matches_type(IntegratorCardPayloadResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_migrate_views(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
        )
        assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_migrate_views_with_all_params(self, client: HubSpot) -> None:
        cards_dev = client.crm.extensions.cards_dev.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
            helpdesk_app_card_id=0,
        )
        assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_migrate_views(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards_dev.with_raw_response.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = response.parse()
        assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_migrate_views(self, client: HubSpot) -> None:
        with client.crm.extensions.cards_dev.with_streaming_response.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = response.parse()
            assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardsDev:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
            },
            title="title",
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
                "serverless_function": "serverlessFunction",
            },
            title="title",
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards_dev.with_raw_response.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
            },
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = await response.parse()
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards_dev.with_streaming_response.create(
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "card_type": "EXTERNAL",
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "target_url": "targetUrl",
            },
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = await response.parse()
            assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.update(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.update(
            card_id="cardId",
            app_id=0,
            actions={"base_urls": ["string"]},
            display={
                "properties": [
                    {
                        "data_type": "BOOLEAN",
                        "label": "label",
                        "name": "name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DANGER",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "companies",
                        "properties_to_send": ["string"],
                    }
                ],
                "card_type": "EXTERNAL",
                "serverless_function": "serverlessFunction",
                "target_url": "targetUrl",
            },
            title="title",
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards_dev.with_raw_response.update(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = await response.parse()
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards_dev.with_streaming_response.update(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = await response.parse()
            assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.crm.extensions.cards_dev.with_raw_response.update(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.delete(
            card_id="cardId",
            app_id=0,
        )
        assert cards_dev is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards_dev.with_raw_response.delete(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = await response.parse()
        assert cards_dev is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards_dev.with_streaming_response.delete(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = await response.parse()
            assert cards_dev is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.crm.extensions.cards_dev.with_raw_response.delete(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.get(
            0,
        )
        assert_matches_type(PublicCardListResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards_dev.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = await response.parse()
        assert_matches_type(PublicCardListResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards_dev.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = await response.parse()
            assert_matches_type(PublicCardListResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.get_by_id(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards_dev.with_raw_response.get_by_id(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = await response.parse()
        assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards_dev.with_streaming_response.get_by_id(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = await response.parse()
            assert_matches_type(PublicCardResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.crm.extensions.cards_dev.with_raw_response.get_by_id(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_sample_response(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.get_sample_response()
        assert_matches_type(IntegratorCardPayloadResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_sample_response(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards_dev.with_raw_response.get_sample_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = await response.parse()
        assert_matches_type(IntegratorCardPayloadResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_sample_response(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards_dev.with_streaming_response.get_sample_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = await response.parse()
            assert_matches_type(IntegratorCardPayloadResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_migrate_views(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
        )
        assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_migrate_views_with_all_params(self, async_client: AsyncHubSpot) -> None:
        cards_dev = await async_client.crm.extensions.cards_dev.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
            helpdesk_app_card_id=0,
        )
        assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_migrate_views(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards_dev.with_raw_response.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cards_dev = await response.parse()
        assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_migrate_views(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards_dev.with_streaming_response.migrate_views(
            app_id=0,
            allow_duplicate_app_card_ids=True,
            app_card_id=0,
            legacy_crm_card_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cards_dev = await response.parse()
            assert_matches_type(CardMigrateViewsResponse, cards_dev, path=["response"])

        assert cast(Any, response.is_closed) is True
