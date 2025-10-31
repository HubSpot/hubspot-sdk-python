# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    SimplePublicObject,
    CreatedResponseSimplePublicObject,
    SimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTickets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.create(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.create(
            properties={"foo": "string"},
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.objects.tickets.with_raw_response.create(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.objects.tickets.with_streaming_response.create(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
        )
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.objects.tickets.with_raw_response.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.objects.tickets.with_streaming_response.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(SimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            client.crm.objects.tickets.with_raw_response.update(
                ticket_id="",
                properties={
                    "property_checkbox": "false",
                    "property_date": "1572480000000",
                    "property_dropdown": "choice_b",
                    "property_multiple_checkboxes": "chocolate;strawberry",
                    "property_number": "17",
                    "property_radio": "option_1",
                    "property_string": "value",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.list()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.objects.tickets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.objects.tickets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.delete(
            "ticketId",
        )
        assert ticket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.objects.tickets.with_raw_response.delete(
            "ticketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert ticket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.objects.tickets.with_streaming_response.delete(
            "ticketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert ticket is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            client.crm.objects.tickets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.get(
            ticket_id="ticketId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.get(
            ticket_id="ticketId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.tickets.with_raw_response.get(
            ticket_id="ticketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.tickets.with_streaming_response.get(
            ticket_id="ticketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            client.crm.objects.tickets.with_raw_response.get(
                ticket_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_merge(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_merge(self, client: Hubspot) -> None:
        response = client.crm.objects.tickets.with_raw_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_merge(self, client: Hubspot) -> None:
        with client.crm.objects.tickets.with_streaming_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(SimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.search()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        ticket = client.crm.objects.tickets.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "EQ",
                            "property_name": "",
                            "high_value": "",
                            "value": "",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            query="query",
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.objects.tickets.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.objects.tickets.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTickets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.create(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.create(
            properties={"foo": "string"},
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.tickets.with_raw_response.create(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.tickets.with_streaming_response.create(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
        )
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.tickets.with_raw_response.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.tickets.with_streaming_response.update(
            ticket_id="ticketId",
            properties={
                "property_checkbox": "false",
                "property_date": "1572480000000",
                "property_dropdown": "choice_b",
                "property_multiple_checkboxes": "chocolate;strawberry",
                "property_number": "17",
                "property_radio": "option_1",
                "property_string": "value",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(SimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            await async_client.crm.objects.tickets.with_raw_response.update(
                ticket_id="",
                properties={
                    "property_checkbox": "false",
                    "property_date": "1572480000000",
                    "property_dropdown": "choice_b",
                    "property_multiple_checkboxes": "chocolate;strawberry",
                    "property_number": "17",
                    "property_radio": "option_1",
                    "property_string": "value",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.list()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.tickets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.tickets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.delete(
            "ticketId",
        )
        assert ticket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.tickets.with_raw_response.delete(
            "ticketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert ticket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.tickets.with_streaming_response.delete(
            "ticketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert ticket is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            await async_client.crm.objects.tickets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.get(
            ticket_id="ticketId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.get(
            ticket_id="ticketId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.tickets.with_raw_response.get(
            ticket_id="ticketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.tickets.with_streaming_response.get(
            ticket_id="ticketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            await async_client.crm.objects.tickets.with_raw_response.get(
                ticket_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_merge(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.tickets.with_raw_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(SimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.tickets.with_streaming_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(SimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.search()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        ticket = await async_client.crm.objects.tickets.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "EQ",
                            "property_name": "",
                            "high_value": "",
                            "value": "",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            query="query",
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.tickets.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.tickets.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True
