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
    IntegratorCardPayloadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
                "card_type": "EXTERNAL",
                "serverless_function": "serverlessFunction",
            },
            title="PetSpot",
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards.with_raw_response.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.extensions.cards.with_streaming_response.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(PublicCardResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.update(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.update(
            card_id="cardId",
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "card_type": "EXTERNAL",
                "serverless_function": "serverlessFunction",
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards.with_raw_response.update(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.extensions.cards.with_streaming_response.update(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(PublicCardResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.crm.extensions.cards.with_raw_response.update(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.list(
            0,
        )
        assert_matches_type(PublicCardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(PublicCardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.extensions.cards.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(PublicCardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.delete(
            card_id="cardId",
            app_id=0,
        )
        assert card is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards.with_raw_response.delete(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert card is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.extensions.cards.with_streaming_response.delete(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert card is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.crm.extensions.cards.with_raw_response.delete(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.get(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards.with_raw_response.get(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.extensions.cards.with_streaming_response.get(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(PublicCardResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.crm.extensions.cards.with_raw_response.get(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_sample_response(self, client: HubSpot) -> None:
        card = client.crm.extensions.cards.get_sample_response()
        assert_matches_type(IntegratorCardPayloadResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_sample_response(self, client: HubSpot) -> None:
        response = client.crm.extensions.cards.with_raw_response.get_sample_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(IntegratorCardPayloadResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_sample_response(self, client: HubSpot) -> None:
        with client.crm.extensions.cards.with_streaming_response.get_sample_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(IntegratorCardPayloadResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
                "card_type": "EXTERNAL",
                "serverless_function": "serverlessFunction",
            },
            title="PetSpot",
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards.with_raw_response.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards.with_streaming_response.create(
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(PublicCardResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.update(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.update(
            card_id="cardId",
            app_id=0,
            actions={"base_urls": ["https://www.example.com/hubspot"]},
            display={
                "properties": [
                    {
                        "data_type": "STRING",
                        "label": "Pets Name",
                        "name": "pet_name",
                        "options": [
                            {
                                "label": "label",
                                "name": "name",
                                "type": "DEFAULT",
                            }
                        ],
                    }
                ]
            },
            fetch={
                "object_types": [
                    {
                        "name": "contacts",
                        "properties_to_send": ["email", "firstname"],
                    }
                ],
                "card_type": "EXTERNAL",
                "serverless_function": "serverlessFunction",
                "target_url": "https://www.example.com/hubspot/target",
            },
            title="PetSpot",
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards.with_raw_response.update(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards.with_streaming_response.update(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(PublicCardResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.crm.extensions.cards.with_raw_response.update(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.list(
            0,
        )
        assert_matches_type(PublicCardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(PublicCardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(PublicCardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.delete(
            card_id="cardId",
            app_id=0,
        )
        assert card is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards.with_raw_response.delete(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert card is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards.with_streaming_response.delete(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert card is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.crm.extensions.cards.with_raw_response.delete(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.get(
            card_id="cardId",
            app_id=0,
        )
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards.with_raw_response.get(
            card_id="cardId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(PublicCardResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards.with_streaming_response.get(
            card_id="cardId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(PublicCardResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.crm.extensions.cards.with_raw_response.get(
                card_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_sample_response(self, async_client: AsyncHubSpot) -> None:
        card = await async_client.crm.extensions.cards.get_sample_response()
        assert_matches_type(IntegratorCardPayloadResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_sample_response(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.cards.with_raw_response.get_sample_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(IntegratorCardPayloadResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_sample_response(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.cards.with_streaming_response.get_sample_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(IntegratorCardPayloadResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True
