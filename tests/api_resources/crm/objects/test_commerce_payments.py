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


class TestCommercePayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.create(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.create(
            properties={"foo": "string"},
            associations=[
                {
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.objects.commerce_payments.with_raw_response.create(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.objects.commerce_payments.with_streaming_response.create(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.update(
            commerce_payment_id="commercePaymentId",
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
        assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.update(
            commerce_payment_id="commercePaymentId",
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
        assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.objects.commerce_payments.with_raw_response.update(
            commerce_payment_id="commercePaymentId",
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
        commerce_payment = response.parse()
        assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.objects.commerce_payments.with_streaming_response.update(
            commerce_payment_id="commercePaymentId",
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

            commerce_payment = response.parse()
            assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commerce_payment_id` but received ''"):
            client.crm.objects.commerce_payments.with_raw_response.update(
                commerce_payment_id="",
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
        commerce_payment = client.crm.objects.commerce_payments.list()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.objects.commerce_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.objects.commerce_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = response.parse()
            assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.delete(
            "commercePaymentId",
        )
        assert commerce_payment is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.objects.commerce_payments.with_raw_response.delete(
            "commercePaymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = response.parse()
        assert commerce_payment is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.objects.commerce_payments.with_streaming_response.delete(
            "commercePaymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = response.parse()
            assert commerce_payment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commerce_payment_id` but received ''"):
            client.crm.objects.commerce_payments.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.get(
            commerce_payment_id="commercePaymentId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.get(
            commerce_payment_id="commercePaymentId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.commerce_payments.with_raw_response.get(
            commerce_payment_id="commercePaymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.commerce_payments.with_streaming_response.get(
            commerce_payment_id="commercePaymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commerce_payment_id` but received ''"):
            client.crm.objects.commerce_payments.with_raw_response.get(
                commerce_payment_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.search()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        commerce_payment = client.crm.objects.commerce_payments.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.objects.commerce_payments.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.objects.commerce_payments.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCommercePayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.create(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.create(
            properties={"foo": "string"},
            associations=[
                {
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.commerce_payments.with_raw_response.create(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = await response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.commerce_payments.with_streaming_response.create(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = await response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.update(
            commerce_payment_id="commercePaymentId",
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
        assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.update(
            commerce_payment_id="commercePaymentId",
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
        assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.commerce_payments.with_raw_response.update(
            commerce_payment_id="commercePaymentId",
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
        commerce_payment = await response.parse()
        assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.commerce_payments.with_streaming_response.update(
            commerce_payment_id="commercePaymentId",
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

            commerce_payment = await response.parse()
            assert_matches_type(SimplePublicObject, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commerce_payment_id` but received ''"):
            await async_client.crm.objects.commerce_payments.with_raw_response.update(
                commerce_payment_id="",
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
        commerce_payment = await async_client.crm.objects.commerce_payments.list()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.commerce_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.commerce_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = await response.parse()
            assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.delete(
            "commercePaymentId",
        )
        assert commerce_payment is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.commerce_payments.with_raw_response.delete(
            "commercePaymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = await response.parse()
        assert commerce_payment is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.commerce_payments.with_streaming_response.delete(
            "commercePaymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = await response.parse()
            assert commerce_payment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commerce_payment_id` but received ''"):
            await async_client.crm.objects.commerce_payments.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.get(
            commerce_payment_id="commercePaymentId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.get(
            commerce_payment_id="commercePaymentId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.commerce_payments.with_raw_response.get(
            commerce_payment_id="commercePaymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.commerce_payments.with_streaming_response.get(
            commerce_payment_id="commercePaymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commerce_payment_id` but received ''"):
            await async_client.crm.objects.commerce_payments.with_raw_response.get(
                commerce_payment_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.search()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        commerce_payment = await async_client.crm.objects.commerce_payments.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.commerce_payments.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commerce_payment = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.commerce_payments.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commerce_payment = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, commerce_payment, path=["response"])

        assert cast(Any, response.is_closed) is True
