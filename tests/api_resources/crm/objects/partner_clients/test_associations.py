# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import AssociatedID, SimplePublicObjectWithAssociations
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        association = client.crm.objects.partner_clients.associations.update(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.objects.partner_clients.associations.with_raw_response.update(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.objects.partner_clients.associations.with_streaming_response.update(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_client_id` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="associationType",
                partner_client_id="",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_type` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        association = client.crm.objects.partner_clients.associations.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
        )
        assert_matches_type(SyncPage[AssociatedID], association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        association = client.crm.objects.partner_clients.associations.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
            after="after",
            include_fa=True,
            limit=0,
        )
        assert_matches_type(SyncPage[AssociatedID], association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.objects.partner_clients.associations.with_raw_response.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(SyncPage[AssociatedID], association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.objects.partner_clients.associations.with_streaming_response.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(SyncPage[AssociatedID], association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_client_id` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.list(
                to_object_type="toObjectType",
                partner_client_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.list(
                to_object_type="",
                partner_client_id="partnerClientId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        association = client.crm.objects.partner_clients.associations.delete(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.objects.partner_clients.associations.with_raw_response.delete(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.objects.partner_clients.associations.with_streaming_response.delete(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_client_id` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="associationType",
                partner_client_id="",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_type` but received ''"):
            client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )


class TestAsyncAssociations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.objects.partner_clients.associations.update(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.partner_clients.associations.with_raw_response.update(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.partner_clients.associations.with_streaming_response.update(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_client_id` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="associationType",
                partner_client_id="",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_type` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.update(
                association_type="",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.objects.partner_clients.associations.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
        )
        assert_matches_type(AsyncPage[AssociatedID], association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.objects.partner_clients.associations.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
            after="after",
            include_fa=True,
            limit=0,
        )
        assert_matches_type(AsyncPage[AssociatedID], association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.partner_clients.associations.with_raw_response.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(AsyncPage[AssociatedID], association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.partner_clients.associations.with_streaming_response.list(
            to_object_type="toObjectType",
            partner_client_id="partnerClientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(AsyncPage[AssociatedID], association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_client_id` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.list(
                to_object_type="toObjectType",
                partner_client_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.list(
                to_object_type="",
                partner_client_id="partnerClientId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.objects.partner_clients.associations.delete(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.partner_clients.associations.with_raw_response.delete(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.partner_clients.associations.with_streaming_response.delete(
            association_type="associationType",
            partner_client_id="partnerClientId",
            to_object_type="toObjectType",
            to_object_id="toObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_client_id` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="associationType",
                partner_client_id="",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="",
                to_object_id="toObjectId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="associationType",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_type` but received ''"):
            await async_client.crm.objects.partner_clients.associations.with_raw_response.delete(
                association_type="",
                partner_client_id="partnerClientId",
                to_object_type="toObjectType",
                to_object_id="toObjectId",
            )
