# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.crm import (
    ListFetchResponse,
    ListsByIDResponse,
    ListCreateResponse,
    ListSearchResponse,
    ListUpdateResponse,
    JoinTimeAndRecordID,
    PublicMigrationMapping,
    ListFolderFetchResponse,
    ListFolderCreateResponse,
    MembershipsUpdateResponse,
    PublicBatchMigrationMapping,
    PublicListConversionResponse,
    ListSizeAndEditHistoryResponse,
    BatchResponseRecordIDWithMemberships,
    APICollectionResponseRecordListMembership,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        list_ = client.crm.lists.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
            custom_properties={"foo": "string"},
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                        "coalescing_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                        "pruning_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
            list_folder_id=0,
            list_permissions={
                "teams_with_edit_access": [0],
                "users_with_edit_access": [0],
            },
            membership_settings={
                "include_unassigned": True,
                "membership_team_id": 0,
            },
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list(
            include_filters=True,
            list_ids=["string"],
        )
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListsByIDResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        list_ = client.crm.lists.delete(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.delete(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.delete(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_and_remove_memberships(self, client: HubSpot) -> None:
        list_ = client.crm.lists.add_and_remove_memberships(
            list_id="listId",
            record_ids_to_add=["string"],
            record_ids_to_remove=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_and_remove_memberships(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.add_and_remove_memberships(
            list_id="listId",
            record_ids_to_add=["string"],
            record_ids_to_remove=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_and_remove_memberships(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.add_and_remove_memberships(
            list_id="listId",
            record_ids_to_add=["string"],
            record_ids_to_remove=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_and_remove_memberships(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.add_and_remove_memberships(
                list_id="",
                record_ids_to_add=["string"],
                record_ids_to_remove=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_memberships(self, client: HubSpot) -> None:
        list_ = client.crm.lists.add_memberships(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_memberships(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.add_memberships(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_memberships(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.add_memberships(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_memberships(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.add_memberships(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_memberships_from(self, client: HubSpot) -> None:
        list_ = client.crm.lists.add_memberships_from(
            source_list_id="sourceListId",
            list_id="listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_memberships_from(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.add_memberships_from(
            source_list_id="sourceListId",
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_memberships_from(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.add_memberships_from(
            source_list_id="sourceListId",
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_memberships_from(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.add_memberships_from(
                source_list_id="sourceListId",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_list_id` but received ''"):
            client.crm.lists.with_raw_response.add_memberships_from(
                source_list_id="",
                list_id="listId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_read_memberships(self, client: HubSpot) -> None:
        list_ = client.crm.lists.batch_read_memberships(
            inputs=[
                {
                    "object_type_id": "objectTypeId",
                    "record_id": "recordId",
                }
            ],
        )
        assert_matches_type(BatchResponseRecordIDWithMemberships, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_read_memberships(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.batch_read_memberships(
            inputs=[
                {
                    "object_type_id": "objectTypeId",
                    "record_id": "recordId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(BatchResponseRecordIDWithMemberships, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_read_memberships(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.batch_read_memberships(
            inputs=[
                {
                    "object_type_id": "objectTypeId",
                    "record_id": "recordId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(BatchResponseRecordIDWithMemberships, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_folder(self, client: HubSpot) -> None:
        list_ = client.crm.lists.create_folder(
            name="name",
        )
        assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_folder_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.create_folder(
            name="name",
            parent_folder_id="parentFolderId",
        )
        assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_folder(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.create_folder(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_folder(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.create_folder(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_id_mapping(self, client: HubSpot) -> None:
        list_ = client.crm.lists.create_id_mapping(
            body=["string"],
        )
        assert_matches_type(PublicBatchMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_id_mapping(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.create_id_mapping(
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(PublicBatchMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_id_mapping(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.create_id_mapping(
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(PublicBatchMigrationMapping, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_folder(self, client: HubSpot) -> None:
        list_ = client.crm.lists.delete_folder(
            "folderId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_folder(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.delete_folder(
            "folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_folder(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.delete_folder(
            "folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_folder(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.crm.lists.with_raw_response.delete_folder(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_memberships(self, client: HubSpot) -> None:
        list_ = client.crm.lists.delete_memberships(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_memberships(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.delete_memberships(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_memberships(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.delete_memberships(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_memberships(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.delete_memberships(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get(
            list_id="listId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get(
            list_id="listId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.get(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.get(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.get(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_object_type_and_name(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_object_type_and_name_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_type_and_name(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_type_and_name(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_object_type_and_name(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.lists.with_raw_response.get_by_object_type_and_name(
                list_name="listName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_name` but received ''"):
            client.crm.lists.with_raw_response.get_by_object_type_and_name(
                list_name="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_id_mapping(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_id_mapping()
        assert_matches_type(PublicMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_id_mapping_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_id_mapping(
            legacy_list_id="legacyListId",
        )
        assert_matches_type(PublicMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_id_mapping(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.get_id_mapping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(PublicMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_id_mapping(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.get_id_mapping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(PublicMigrationMapping, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_memberships_join_order(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_memberships_join_order(
            list_id="listId",
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_memberships_join_order_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_memberships_join_order(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_memberships_join_order(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.get_memberships_join_order(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_memberships_join_order(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.get_memberships_join_order(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_memberships_join_order(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.get_memberships_join_order(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_record_memberships(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_record_memberships(
            record_id="recordId",
            object_type_id="objectTypeId",
        )
        assert_matches_type(APICollectionResponseRecordListMembership, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_record_memberships(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.get_record_memberships(
            record_id="recordId",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(APICollectionResponseRecordListMembership, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_record_memberships(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.get_record_memberships(
            record_id="recordId",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(APICollectionResponseRecordListMembership, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_record_memberships(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.lists.with_raw_response.get_record_memberships(
                record_id="recordId",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.crm.lists.with_raw_response.get_record_memberships(
                record_id="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_schedule_conversion(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_schedule_conversion(
            "listId",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_schedule_conversion(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.get_schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_schedule_conversion(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.get_schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_schedule_conversion(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.get_schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_size_and_edits_history_between(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_size_and_edits_history_between(
            list_id="listId",
        )
        assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_size_and_edits_history_between_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.get_size_and_edits_history_between(
            list_id="listId",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_size_and_edits_history_between(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.get_size_and_edits_history_between(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_size_and_edits_history_between(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.get_size_and_edits_history_between(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_size_and_edits_history_between(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.get_size_and_edits_history_between(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_search(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
        )
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_search_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
            additional_filter_properties=["string"],
            count=0,
            object_type_id="objectTypeId",
            query="query",
            sort="sort",
        )
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_search(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_search(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListSearchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_folders(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list_folders()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_folders_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list_folders(
            folder_id="folderId",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_folders(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_folders(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_memberships(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list_memberships(
            list_id="listId",
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_memberships_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.list_memberships(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_memberships(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.list_memberships(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_memberships(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.list_memberships(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(SyncPage[JoinTimeAndRecordID], list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_memberships(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.list_memberships(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_move_folder(self, client: HubSpot) -> None:
        list_ = client.crm.lists.move_folder(
            new_parent_folder_id="newParentFolderId",
            folder_id="folderId",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_move_folder(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.move_folder(
            new_parent_folder_id="newParentFolderId",
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_move_folder(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.move_folder(
            new_parent_folder_id="newParentFolderId",
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_move_folder(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.crm.lists.with_raw_response.move_folder(
                new_parent_folder_id="newParentFolderId",
                folder_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `new_parent_folder_id` but received ''"):
            client.crm.lists.with_raw_response.move_folder(
                new_parent_folder_id="",
                folder_id="folderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_move_list(self, client: HubSpot) -> None:
        list_ = client.crm.lists.move_list(
            list_id="listId",
            new_folder_id="newFolderId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_move_list(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.move_list(
            list_id="listId",
            new_folder_id="newFolderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_move_list(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.move_list(
            list_id="listId",
            new_folder_id="newFolderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_memberships(self, client: HubSpot) -> None:
        list_ = client.crm.lists.remove_memberships(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_memberships(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.remove_memberships(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_memberships(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.remove_memberships(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_memberships(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.remove_memberships(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rename_folder(self, client: HubSpot) -> None:
        list_ = client.crm.lists.rename_folder(
            folder_id="folderId",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rename_folder_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.rename_folder(
            folder_id="folderId",
            new_folder_name="newFolderName",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rename_folder(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.rename_folder(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rename_folder(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.rename_folder(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rename_folder(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.crm.lists.with_raw_response.rename_folder(
                folder_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: HubSpot) -> None:
        list_ = client.crm.lists.restore(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.restore(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.restore(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.restore(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_schedule_conversion(self, client: HubSpot) -> None:
        list_ = client.crm.lists.schedule_conversion(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_schedule_conversion(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_schedule_conversion(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_schedule_conversion(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_list_filters(self, client: HubSpot) -> None:
        list_ = client.crm.lists.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_list_filters_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                        "coalescing_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                        "pruning_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
            enroll_objects_in_workflows=True,
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_list_filters(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_list_filters(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_list_filters(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.update_list_filters(
                list_id="",
                filter_branch={
                    "filter_branches": [
                        {
                            "filter_branches": [
                                {
                                    "filter_branches": [
                                        {
                                            "filter_branches": [
                                                {
                                                    "filter_branches": [
                                                        {
                                                            "event_type_id": "eventTypeId",
                                                            "filter_branches": [
                                                                {
                                                                    "filter_branches": [
                                                                        {
                                                                            "association_category": "associationCategory",
                                                                            "association_type_id": 0,
                                                                            "filter_branches": [
                                                                                {
                                                                                    "filter_branches": [],
                                                                                    "filter_branch_operator": "filterBranchOperator",
                                                                                    "filter_branch_type": "OR",
                                                                                    "filters": [
                                                                                        {
                                                                                            "filter_type": "PROPERTY",
                                                                                            "operation": {
                                                                                                "include_objects_with_no_value_set": True,
                                                                                                "operation_type": "BOOL",
                                                                                                "operator": "operator",
                                                                                                "value": True,
                                                                                            },
                                                                                            "property": "property",
                                                                                        }
                                                                                    ],
                                                                                }
                                                                            ],
                                                                            "filter_branch_operator": "filterBranchOperator",
                                                                            "filter_branch_type": "ASSOCIATION",
                                                                            "filters": [
                                                                                {
                                                                                    "filter_type": "PROPERTY",
                                                                                    "operation": {
                                                                                        "include_objects_with_no_value_set": True,
                                                                                        "operation_type": "BOOL",
                                                                                        "operator": "operator",
                                                                                        "value": True,
                                                                                    },
                                                                                    "property": "property",
                                                                                }
                                                                            ],
                                                                            "object_type_id": "objectTypeId",
                                                                            "operator": "operator",
                                                                        }
                                                                    ],
                                                                    "filter_branch_operator": "filterBranchOperator",
                                                                    "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                    "filters": [
                                                                        {
                                                                            "filter_type": "PROPERTY",
                                                                            "operation": {
                                                                                "include_objects_with_no_value_set": True,
                                                                                "operation_type": "BOOL",
                                                                                "operator": "operator",
                                                                                "value": True,
                                                                            },
                                                                            "property": "property",
                                                                        }
                                                                    ],
                                                                    "object_type_id": "objectTypeId",
                                                                    "operator": "operator",
                                                                    "property_with_object_id": "propertyWithObjectId",
                                                                }
                                                            ],
                                                            "filter_branch_operator": "filterBranchOperator",
                                                            "filter_branch_type": "UNIFIED_EVENTS",
                                                            "filters": [
                                                                {
                                                                    "filter_type": "PROPERTY",
                                                                    "operation": {
                                                                        "include_objects_with_no_value_set": True,
                                                                        "operation_type": "BOOL",
                                                                        "operator": "operator",
                                                                        "value": True,
                                                                    },
                                                                    "property": "property",
                                                                }
                                                            ],
                                                            "operator": "HAS_COMPLETED",
                                                        }
                                                    ],
                                                    "filter_branch_operator": "filterBranchOperator",
                                                    "filter_branch_type": "RESTRICTED",
                                                    "filters": [
                                                        {
                                                            "filter_type": "PROPERTY",
                                                            "operation": {
                                                                "include_objects_with_no_value_set": True,
                                                                "operation_type": "BOOL",
                                                                "operator": "operator",
                                                                "value": True,
                                                            },
                                                            "property": "property",
                                                        }
                                                    ],
                                                }
                                            ],
                                            "filter_branch_operator": "filterBranchOperator",
                                            "filter_branch_type": "NOT_ANY",
                                            "filters": [
                                                {
                                                    "filter_type": "PROPERTY",
                                                    "operation": {
                                                        "include_objects_with_no_value_set": True,
                                                        "operation_type": "BOOL",
                                                        "operator": "operator",
                                                        "value": True,
                                                    },
                                                    "property": "property",
                                                }
                                            ],
                                        }
                                    ],
                                    "filter_branch_operator": "filterBranchOperator",
                                    "filter_branch_type": "NOT_ALL",
                                    "filters": [
                                        {
                                            "filter_type": "PROPERTY",
                                            "operation": {
                                                "include_objects_with_no_value_set": True,
                                                "operation_type": "BOOL",
                                                "operator": "operator",
                                                "value": True,
                                            },
                                            "property": "property",
                                        }
                                    ],
                                }
                            ],
                            "filter_branch_operator": "filterBranchOperator",
                            "filter_branch_type": "AND",
                            "filters": [
                                {
                                    "filter_type": "PROPERTY",
                                    "operation": {
                                        "include_objects_with_no_value_set": True,
                                        "operation_type": "BOOL",
                                        "operator": "operator",
                                        "value": True,
                                    },
                                    "property": "property",
                                }
                            ],
                        }
                    ],
                    "filter_branch_operator": "filterBranchOperator",
                    "filter_branch_type": "OR",
                    "filters": [
                        {
                            "filter_type": "PROPERTY",
                            "operation": {
                                "include_objects_with_no_value_set": True,
                                "operation_type": "BOOL",
                                "operator": "operator",
                                "value": True,
                            },
                            "property": "property",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_list_name(self, client: HubSpot) -> None:
        list_ = client.crm.lists.update_list_name(
            list_id="listId",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_list_name_with_all_params(self, client: HubSpot) -> None:
        list_ = client.crm.lists.update_list_name(
            list_id="listId",
            include_filters=True,
            list_name="listName",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_list_name(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.update_list_name(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_list_name(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.update_list_name(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_list_name(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.update_list_name(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_schedule_conversion_overload_1(self, client: HubSpot) -> None:
        list_ = client.crm.lists.update_schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_schedule_conversion_overload_1(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_schedule_conversion_overload_1(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_schedule_conversion_overload_1(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.update_schedule_conversion(
                list_id="",
                conversion_type="CONVERSION_DATE",
                day=0,
                month=0,
                year=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_schedule_conversion_overload_2(self, client: HubSpot) -> None:
        list_ = client.crm.lists.update_schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_schedule_conversion_overload_2(self, client: HubSpot) -> None:
        response = client.crm.lists.with_raw_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_schedule_conversion_overload_2(self, client: HubSpot) -> None:
        with client.crm.lists.with_streaming_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_schedule_conversion_overload_2(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.update_schedule_conversion(
                list_id="",
                conversion_type="INACTIVITY",
                offset=0,
                time_unit="DAY",
            )


class TestAsyncLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
            custom_properties={"foo": "string"},
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                        "coalescing_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                        "pruning_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
            list_folder_id=0,
            list_permissions={
                "teams_with_edit_access": [0],
                "users_with_edit_access": [0],
            },
            membership_settings={
                "include_unassigned": True,
                "membership_team_id": 0,
            },
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.create(
            name="name",
            object_type_id="objectTypeId",
            processing_type="processingType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list(
            include_filters=True,
            list_ids=["string"],
        )
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListsByIDResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.delete(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.delete(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.delete(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_and_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.add_and_remove_memberships(
            list_id="listId",
            record_ids_to_add=["string"],
            record_ids_to_remove=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_and_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.add_and_remove_memberships(
            list_id="listId",
            record_ids_to_add=["string"],
            record_ids_to_remove=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_and_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.add_and_remove_memberships(
            list_id="listId",
            record_ids_to_add=["string"],
            record_ids_to_remove=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_and_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.add_and_remove_memberships(
                list_id="",
                record_ids_to_add=["string"],
                record_ids_to_remove=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_memberships(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.add_memberships(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_memberships(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.add_memberships(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_memberships(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.add_memberships(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_memberships(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.add_memberships(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_memberships_from(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.add_memberships_from(
            source_list_id="sourceListId",
            list_id="listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_memberships_from(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.add_memberships_from(
            source_list_id="sourceListId",
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_memberships_from(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.add_memberships_from(
            source_list_id="sourceListId",
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_memberships_from(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.add_memberships_from(
                source_list_id="sourceListId",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.add_memberships_from(
                source_list_id="",
                list_id="listId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_read_memberships(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.batch_read_memberships(
            inputs=[
                {
                    "object_type_id": "objectTypeId",
                    "record_id": "recordId",
                }
            ],
        )
        assert_matches_type(BatchResponseRecordIDWithMemberships, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_read_memberships(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.batch_read_memberships(
            inputs=[
                {
                    "object_type_id": "objectTypeId",
                    "record_id": "recordId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(BatchResponseRecordIDWithMemberships, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_read_memberships(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.batch_read_memberships(
            inputs=[
                {
                    "object_type_id": "objectTypeId",
                    "record_id": "recordId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(BatchResponseRecordIDWithMemberships, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_folder(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.create_folder(
            name="name",
        )
        assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_folder_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.create_folder(
            name="name",
            parent_folder_id="parentFolderId",
        )
        assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_folder(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.create_folder(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_folder(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.create_folder(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFolderCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_id_mapping(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.create_id_mapping(
            body=["string"],
        )
        assert_matches_type(PublicBatchMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_id_mapping(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.create_id_mapping(
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(PublicBatchMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_id_mapping(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.create_id_mapping(
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(PublicBatchMigrationMapping, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_folder(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.delete_folder(
            "folderId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_folder(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.delete_folder(
            "folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_folder(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.delete_folder(
            "folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_folder(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.crm.lists.with_raw_response.delete_folder(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_memberships(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.delete_memberships(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_memberships(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.delete_memberships(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_memberships(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.delete_memberships(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_memberships(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.delete_memberships(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get(
            list_id="listId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get(
            list_id="listId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.get(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.get(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_and_name(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_and_name_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_type_and_name(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_type_and_name(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_by_object_type_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_type_and_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_by_object_type_and_name(
                list_name="listName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_name` but received ''"):
            await async_client.crm.lists.with_raw_response.get_by_object_type_and_name(
                list_name="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_id_mapping(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_id_mapping()
        assert_matches_type(PublicMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_id_mapping_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_id_mapping(
            legacy_list_id="legacyListId",
        )
        assert_matches_type(PublicMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_id_mapping(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_id_mapping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(PublicMigrationMapping, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_id_mapping(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_id_mapping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(PublicMigrationMapping, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_memberships_join_order(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_memberships_join_order(
            list_id="listId",
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_memberships_join_order_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_memberships_join_order(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_memberships_join_order(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_memberships_join_order(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_memberships_join_order(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_memberships_join_order(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_memberships_join_order(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_memberships_join_order(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_record_memberships(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_record_memberships(
            record_id="recordId",
            object_type_id="objectTypeId",
        )
        assert_matches_type(APICollectionResponseRecordListMembership, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_record_memberships(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_record_memberships(
            record_id="recordId",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(APICollectionResponseRecordListMembership, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_record_memberships(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_record_memberships(
            record_id="recordId",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(APICollectionResponseRecordListMembership, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_record_memberships(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_record_memberships(
                record_id="recordId",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_record_memberships(
                record_id="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_schedule_conversion(
            "listId",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_size_and_edits_history_between(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_size_and_edits_history_between(
            list_id="listId",
        )
        assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_size_and_edits_history_between_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.get_size_and_edits_history_between(
            list_id="listId",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_size_and_edits_history_between(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_size_and_edits_history_between(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_size_and_edits_history_between(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_size_and_edits_history_between(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListSizeAndEditHistoryResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_size_and_edits_history_between(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_size_and_edits_history_between(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_search(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
        )
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_search_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
            additional_filter_properties=["string"],
            count=0,
            object_type_id="objectTypeId",
            query="query",
            sort="sort",
        )
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_search(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_search(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.list_by_search(
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListSearchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_folders(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list_folders()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_folders_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list_folders(
            folder_id="folderId",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_folders(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_folders(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_memberships(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list_memberships(
            list_id="listId",
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_memberships_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.list_memberships(
            list_id="listId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_memberships(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.list_memberships(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_memberships(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.list_memberships(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(AsyncPage[JoinTimeAndRecordID], list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_memberships(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.list_memberships(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_move_folder(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.move_folder(
            new_parent_folder_id="newParentFolderId",
            folder_id="folderId",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_move_folder(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.move_folder(
            new_parent_folder_id="newParentFolderId",
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_move_folder(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.move_folder(
            new_parent_folder_id="newParentFolderId",
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_move_folder(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.crm.lists.with_raw_response.move_folder(
                new_parent_folder_id="newParentFolderId",
                folder_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `new_parent_folder_id` but received ''"):
            await async_client.crm.lists.with_raw_response.move_folder(
                new_parent_folder_id="",
                folder_id="folderId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_move_list(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.move_list(
            list_id="listId",
            new_folder_id="newFolderId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_move_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.move_list(
            list_id="listId",
            new_folder_id="newFolderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_move_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.move_list(
            list_id="listId",
            new_folder_id="newFolderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.remove_memberships(
            list_id="listId",
            body=["string"],
        )
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.remove_memberships(
            list_id="listId",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.remove_memberships(
            list_id="listId",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(MembershipsUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_memberships(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.remove_memberships(
                list_id="",
                body=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rename_folder(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.rename_folder(
            folder_id="folderId",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rename_folder_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.rename_folder(
            folder_id="folderId",
            new_folder_name="newFolderName",
        )
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rename_folder(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.rename_folder(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rename_folder(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.rename_folder(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFolderFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rename_folder(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.crm.lists.with_raw_response.rename_folder(
                folder_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.restore(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.restore(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.restore(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.restore(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.schedule_conversion(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_schedule_conversion(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_list_filters(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_list_filters_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                        "coalescing_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                        "pruning_refine_by": {
                                                            "type": "NUM_OCCURRENCES",
                                                            "max_occurrences": 0,
                                                            "min_occurrences": 0,
                                                        },
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
            enroll_objects_in_workflows=True,
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_list_filters(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_list_filters(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.update_list_filters(
            list_id="listId",
            filter_branch={
                "filter_branches": [
                    {
                        "filter_branches": [
                            {
                                "filter_branches": [
                                    {
                                        "filter_branches": [
                                            {
                                                "filter_branches": [
                                                    {
                                                        "event_type_id": "eventTypeId",
                                                        "filter_branches": [
                                                            {
                                                                "filter_branches": [
                                                                    {
                                                                        "association_category": "associationCategory",
                                                                        "association_type_id": 0,
                                                                        "filter_branches": [
                                                                            {
                                                                                "filter_branches": [],
                                                                                "filter_branch_operator": "filterBranchOperator",
                                                                                "filter_branch_type": "OR",
                                                                                "filters": [
                                                                                    {
                                                                                        "filter_type": "PROPERTY",
                                                                                        "operation": {
                                                                                            "include_objects_with_no_value_set": True,
                                                                                            "operation_type": "BOOL",
                                                                                            "operator": "operator",
                                                                                            "value": True,
                                                                                        },
                                                                                        "property": "property",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                        "filter_branch_operator": "filterBranchOperator",
                                                                        "filter_branch_type": "ASSOCIATION",
                                                                        "filters": [
                                                                            {
                                                                                "filter_type": "PROPERTY",
                                                                                "operation": {
                                                                                    "include_objects_with_no_value_set": True,
                                                                                    "operation_type": "BOOL",
                                                                                    "operator": "operator",
                                                                                    "value": True,
                                                                                },
                                                                                "property": "property",
                                                                            }
                                                                        ],
                                                                        "object_type_id": "objectTypeId",
                                                                        "operator": "operator",
                                                                    }
                                                                ],
                                                                "filter_branch_operator": "filterBranchOperator",
                                                                "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                "filters": [
                                                                    {
                                                                        "filter_type": "PROPERTY",
                                                                        "operation": {
                                                                            "include_objects_with_no_value_set": True,
                                                                            "operation_type": "BOOL",
                                                                            "operator": "operator",
                                                                            "value": True,
                                                                        },
                                                                        "property": "property",
                                                                    }
                                                                ],
                                                                "object_type_id": "objectTypeId",
                                                                "operator": "operator",
                                                                "property_with_object_id": "propertyWithObjectId",
                                                            }
                                                        ],
                                                        "filter_branch_operator": "filterBranchOperator",
                                                        "filter_branch_type": "UNIFIED_EVENTS",
                                                        "filters": [
                                                            {
                                                                "filter_type": "PROPERTY",
                                                                "operation": {
                                                                    "include_objects_with_no_value_set": True,
                                                                    "operation_type": "BOOL",
                                                                    "operator": "operator",
                                                                    "value": True,
                                                                },
                                                                "property": "property",
                                                            }
                                                        ],
                                                        "operator": "HAS_COMPLETED",
                                                    }
                                                ],
                                                "filter_branch_operator": "filterBranchOperator",
                                                "filter_branch_type": "RESTRICTED",
                                                "filters": [
                                                    {
                                                        "filter_type": "PROPERTY",
                                                        "operation": {
                                                            "include_objects_with_no_value_set": True,
                                                            "operation_type": "BOOL",
                                                            "operator": "operator",
                                                            "value": True,
                                                        },
                                                        "property": "property",
                                                    }
                                                ],
                                            }
                                        ],
                                        "filter_branch_operator": "filterBranchOperator",
                                        "filter_branch_type": "NOT_ANY",
                                        "filters": [
                                            {
                                                "filter_type": "PROPERTY",
                                                "operation": {
                                                    "include_objects_with_no_value_set": True,
                                                    "operation_type": "BOOL",
                                                    "operator": "operator",
                                                    "value": True,
                                                },
                                                "property": "property",
                                            }
                                        ],
                                    }
                                ],
                                "filter_branch_operator": "filterBranchOperator",
                                "filter_branch_type": "NOT_ALL",
                                "filters": [
                                    {
                                        "filter_type": "PROPERTY",
                                        "operation": {
                                            "include_objects_with_no_value_set": True,
                                            "operation_type": "BOOL",
                                            "operator": "operator",
                                            "value": True,
                                        },
                                        "property": "property",
                                    }
                                ],
                            }
                        ],
                        "filter_branch_operator": "filterBranchOperator",
                        "filter_branch_type": "AND",
                        "filters": [
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "operator",
                                    "value": True,
                                },
                                "property": "property",
                            }
                        ],
                    }
                ],
                "filter_branch_operator": "filterBranchOperator",
                "filter_branch_type": "OR",
                "filters": [
                    {
                        "filter_type": "PROPERTY",
                        "operation": {
                            "include_objects_with_no_value_set": True,
                            "operation_type": "BOOL",
                            "operator": "operator",
                            "value": True,
                        },
                        "property": "property",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_list_filters(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.update_list_filters(
                list_id="",
                filter_branch={
                    "filter_branches": [
                        {
                            "filter_branches": [
                                {
                                    "filter_branches": [
                                        {
                                            "filter_branches": [
                                                {
                                                    "filter_branches": [
                                                        {
                                                            "event_type_id": "eventTypeId",
                                                            "filter_branches": [
                                                                {
                                                                    "filter_branches": [
                                                                        {
                                                                            "association_category": "associationCategory",
                                                                            "association_type_id": 0,
                                                                            "filter_branches": [
                                                                                {
                                                                                    "filter_branches": [],
                                                                                    "filter_branch_operator": "filterBranchOperator",
                                                                                    "filter_branch_type": "OR",
                                                                                    "filters": [
                                                                                        {
                                                                                            "filter_type": "PROPERTY",
                                                                                            "operation": {
                                                                                                "include_objects_with_no_value_set": True,
                                                                                                "operation_type": "BOOL",
                                                                                                "operator": "operator",
                                                                                                "value": True,
                                                                                            },
                                                                                            "property": "property",
                                                                                        }
                                                                                    ],
                                                                                }
                                                                            ],
                                                                            "filter_branch_operator": "filterBranchOperator",
                                                                            "filter_branch_type": "ASSOCIATION",
                                                                            "filters": [
                                                                                {
                                                                                    "filter_type": "PROPERTY",
                                                                                    "operation": {
                                                                                        "include_objects_with_no_value_set": True,
                                                                                        "operation_type": "BOOL",
                                                                                        "operator": "operator",
                                                                                        "value": True,
                                                                                    },
                                                                                    "property": "property",
                                                                                }
                                                                            ],
                                                                            "object_type_id": "objectTypeId",
                                                                            "operator": "operator",
                                                                        }
                                                                    ],
                                                                    "filter_branch_operator": "filterBranchOperator",
                                                                    "filter_branch_type": "PROPERTY_ASSOCIATION",
                                                                    "filters": [
                                                                        {
                                                                            "filter_type": "PROPERTY",
                                                                            "operation": {
                                                                                "include_objects_with_no_value_set": True,
                                                                                "operation_type": "BOOL",
                                                                                "operator": "operator",
                                                                                "value": True,
                                                                            },
                                                                            "property": "property",
                                                                        }
                                                                    ],
                                                                    "object_type_id": "objectTypeId",
                                                                    "operator": "operator",
                                                                    "property_with_object_id": "propertyWithObjectId",
                                                                }
                                                            ],
                                                            "filter_branch_operator": "filterBranchOperator",
                                                            "filter_branch_type": "UNIFIED_EVENTS",
                                                            "filters": [
                                                                {
                                                                    "filter_type": "PROPERTY",
                                                                    "operation": {
                                                                        "include_objects_with_no_value_set": True,
                                                                        "operation_type": "BOOL",
                                                                        "operator": "operator",
                                                                        "value": True,
                                                                    },
                                                                    "property": "property",
                                                                }
                                                            ],
                                                            "operator": "HAS_COMPLETED",
                                                        }
                                                    ],
                                                    "filter_branch_operator": "filterBranchOperator",
                                                    "filter_branch_type": "RESTRICTED",
                                                    "filters": [
                                                        {
                                                            "filter_type": "PROPERTY",
                                                            "operation": {
                                                                "include_objects_with_no_value_set": True,
                                                                "operation_type": "BOOL",
                                                                "operator": "operator",
                                                                "value": True,
                                                            },
                                                            "property": "property",
                                                        }
                                                    ],
                                                }
                                            ],
                                            "filter_branch_operator": "filterBranchOperator",
                                            "filter_branch_type": "NOT_ANY",
                                            "filters": [
                                                {
                                                    "filter_type": "PROPERTY",
                                                    "operation": {
                                                        "include_objects_with_no_value_set": True,
                                                        "operation_type": "BOOL",
                                                        "operator": "operator",
                                                        "value": True,
                                                    },
                                                    "property": "property",
                                                }
                                            ],
                                        }
                                    ],
                                    "filter_branch_operator": "filterBranchOperator",
                                    "filter_branch_type": "NOT_ALL",
                                    "filters": [
                                        {
                                            "filter_type": "PROPERTY",
                                            "operation": {
                                                "include_objects_with_no_value_set": True,
                                                "operation_type": "BOOL",
                                                "operator": "operator",
                                                "value": True,
                                            },
                                            "property": "property",
                                        }
                                    ],
                                }
                            ],
                            "filter_branch_operator": "filterBranchOperator",
                            "filter_branch_type": "AND",
                            "filters": [
                                {
                                    "filter_type": "PROPERTY",
                                    "operation": {
                                        "include_objects_with_no_value_set": True,
                                        "operation_type": "BOOL",
                                        "operator": "operator",
                                        "value": True,
                                    },
                                    "property": "property",
                                }
                            ],
                        }
                    ],
                    "filter_branch_operator": "filterBranchOperator",
                    "filter_branch_type": "OR",
                    "filters": [
                        {
                            "filter_type": "PROPERTY",
                            "operation": {
                                "include_objects_with_no_value_set": True,
                                "operation_type": "BOOL",
                                "operator": "operator",
                                "value": True,
                            },
                            "property": "property",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_list_name(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.update_list_name(
            list_id="listId",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_list_name_with_all_params(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.update_list_name(
            list_id="listId",
            include_filters=True,
            list_name="listName",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_list_name(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.update_list_name(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_list_name(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.update_list_name(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_list_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.update_list_name(
                list_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_schedule_conversion_overload_1(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.update_schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_schedule_conversion_overload_1(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_schedule_conversion_overload_1(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_schedule_conversion_overload_1(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.update_schedule_conversion(
                list_id="",
                conversion_type="CONVERSION_DATE",
                day=0,
                month=0,
                year=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_schedule_conversion_overload_2(self, async_client: AsyncHubSpot) -> None:
        list_ = await async_client.crm.lists.update_schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_schedule_conversion_overload_2(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.lists.with_raw_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_schedule_conversion_overload_2(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.lists.with_streaming_response.update_schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_schedule_conversion_overload_2(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.update_schedule_conversion(
                list_id="",
                conversion_type="INACTIVITY",
                offset=0,
                time_unit="DAY",
            )
