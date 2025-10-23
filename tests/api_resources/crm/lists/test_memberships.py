# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    JoinTimeAndRecordID,
    MembershipsUpdateResponse,
    APICollectionResponseRecordListMembershipNoPaging,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemberships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.list(
            list_id="listId",
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.list(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.list(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.list(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.list(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.add(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.add(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.add(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.add(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_all_from_list(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.add_all_from_list(
            source_list_id="sourceListId",
            list_id="listId",
        )
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_all_from_list(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.add_all_from_list(
            source_list_id="sourceListId",
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_all_from_list(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.add_all_from_list(
            source_list_id="sourceListId",
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert membership is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_all_from_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.add_all_from_list(
                source_list_id="sourceListId",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.add_all_from_list(
                source_list_id="",
                list_id="listId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_and_remove(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.add_and_remove(
            list_id="listId",
            record_ids_to_add=["123", "456", "789"],
            record_ids_to_remove=["654"],
        )
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_and_remove(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.add_and_remove(
            list_id="listId",
            record_ids_to_add=["123", "456", "789"],
            record_ids_to_remove=["654"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_and_remove(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.add_and_remove(
            list_id="listId",
            record_ids_to_add=["123", "456", "789"],
            record_ids_to_remove=["654"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_and_remove(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.add_and_remove(
                list_id="",
                record_ids_to_add=["123", "456", "789"],
                record_ids_to_remove=["654"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_lists(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.get_lists(
            record_id="recordId",
            object_type_id="objectTypeId",
        )
        assert_matches_type(APICollectionResponseRecordListMembershipNoPaging, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_lists(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.get_lists(
            record_id="recordId",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(APICollectionResponseRecordListMembershipNoPaging, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_lists(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.get_lists(
            record_id="recordId",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(APICollectionResponseRecordListMembershipNoPaging, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_lists(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.get_lists(
                record_id="recordId",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.get_lists(
                record_id="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_page_ordered_by_added_to_list_date(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.get_page_ordered_by_added_to_list_date(
            list_id="listId",
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_page_ordered_by_added_to_list_date_with_all_params(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.get_page_ordered_by_added_to_list_date(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_page_ordered_by_added_to_list_date(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.get_page_ordered_by_added_to_list_date(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_page_ordered_by_added_to_list_date(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.get_page_ordered_by_added_to_list_date(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(SyncPage[JoinTimeAndRecordID], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_page_ordered_by_added_to_list_date(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.get_page_ordered_by_added_to_list_date(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.remove(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.remove(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.remove(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.remove(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_all(self, client: HubSpot) -> None:
        membership = client.crm.lists.memberships.remove_all(
            "listId",
        )
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_all(self, client: HubSpot) -> None:
        response = client.crm.lists.memberships.with_raw_response.remove_all(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_all(self, client: HubSpot) -> None:
        with client.crm.lists.memberships.with_streaming_response.remove_all(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert membership is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove_all(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.memberships.with_raw_response.remove_all(
                "",
            )


class TestAsyncMemberships:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.list(
            list_id="listId",
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.list(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.list(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.list(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.list(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.add(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.add(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.add(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.add(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_all_from_list(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.add_all_from_list(
            source_list_id="sourceListId",
            list_id="listId",
        )
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_all_from_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.add_all_from_list(
            source_list_id="sourceListId",
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_all_from_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.add_all_from_list(
            source_list_id="sourceListId",
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert membership is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_all_from_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.add_all_from_list(
                source_list_id="sourceListId",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.add_all_from_list(
                source_list_id="",
                list_id="listId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_and_remove(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.add_and_remove(
            list_id="listId",
            record_ids_to_add=["123", "456", "789"],
            record_ids_to_remove=["654"],
        )
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_and_remove(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.add_and_remove(
            list_id="listId",
            record_ids_to_add=["123", "456", "789"],
            record_ids_to_remove=["654"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_and_remove(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.add_and_remove(
            list_id="listId",
            record_ids_to_add=["123", "456", "789"],
            record_ids_to_remove=["654"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_and_remove(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.add_and_remove(
                list_id="",
                record_ids_to_add=["123", "456", "789"],
                record_ids_to_remove=["654"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_lists(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.get_lists(
            record_id="recordId",
            object_type_id="objectTypeId",
        )
        assert_matches_type(APICollectionResponseRecordListMembershipNoPaging, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_lists(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.get_lists(
            record_id="recordId",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(APICollectionResponseRecordListMembershipNoPaging, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_lists(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.get_lists(
            record_id="recordId",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(APICollectionResponseRecordListMembershipNoPaging, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_lists(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.get_lists(
                record_id="recordId",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.get_lists(
                record_id="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_page_ordered_by_added_to_list_date(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.get_page_ordered_by_added_to_list_date(
            list_id="listId",
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_page_ordered_by_added_to_list_date_with_all_params(
        self, async_client: AsyncHubSpot
    ) -> None:
        membership = await async_client.crm.lists.memberships.get_page_ordered_by_added_to_list_date(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_page_ordered_by_added_to_list_date(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.get_page_ordered_by_added_to_list_date(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_page_ordered_by_added_to_list_date(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.get_page_ordered_by_added_to_list_date(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(AsyncPage[JoinTimeAndRecordID], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_page_ordered_by_added_to_list_date(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.get_page_ordered_by_added_to_list_date(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.remove(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.remove(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.remove(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipsUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.remove(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_all(self, async_client: AsyncHubSpot) -> None:
        membership = await async_client.crm.lists.memberships.remove_all(
            "listId",
        )
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_all(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.memberships.with_raw_response.remove_all(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert membership is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_all(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.memberships.with_streaming_response.remove_all(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert membership is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove_all(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.memberships.with_raw_response.remove_all(
                "",
            )
