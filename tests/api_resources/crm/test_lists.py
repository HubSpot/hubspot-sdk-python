# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    ListFetchResponse,
    ListsByIDResponse,
    ListCreateResponse,
    ListSearchResponse,
    ListUpdateResponse,
    PublicListConversionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        list_ = client.crm.lists.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        list_ = client.crm.lists.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
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
                                            "operator": "IS_EQUAL_TO",
                                            "value": True,
                                        },
                                        "property": "hs_is_closed_won",
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
                                    "operator": "IS_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "firstname",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        list_ = client.crm.lists.list()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        list_ = client.crm.lists.list(
            include_filters=True,
            list_ids=["string"],
        )
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListsByIDResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        list_ = client.crm.lists.delete(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.delete(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.delete(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_schedule_conversion(self, client: Hubspot) -> None:
        list_ = client.crm.lists.delete_schedule_conversion(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_schedule_conversion(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.delete_schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_schedule_conversion(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.delete_schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_schedule_conversion(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.delete_schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        list_ = client.crm.lists.get(
            list_id="listId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        list_ = client.crm.lists.get(
            list_id="listId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.get(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.get(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.get(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_object_type_id_and_name(self, client: Hubspot) -> None:
        list_ = client.crm.lists.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_object_type_id_and_name_with_all_params(self, client: Hubspot) -> None:
        list_ = client.crm.lists.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_type_id_and_name(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_type_id_and_name(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_object_type_id_and_name(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.lists.with_raw_response.get_by_object_type_id_and_name(
                list_name="listName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_name` but received ''"):
            client.crm.lists.with_raw_response.get_by_object_type_id_and_name(
                list_name="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_schedule_conversion(self, client: Hubspot) -> None:
        list_ = client.crm.lists.get_schedule_conversion(
            "listId",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_schedule_conversion(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.get_schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_schedule_conversion(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.get_schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_schedule_conversion(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.get_schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore(self, client: Hubspot) -> None:
        list_ = client.crm.lists.restore(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.restore(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.restore(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.restore(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule_conversion_overload_1(self, client: Hubspot) -> None:
        list_ = client.crm.lists.schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_schedule_conversion_overload_1(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.schedule_conversion(
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_schedule_conversion_overload_1(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.schedule_conversion(
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_schedule_conversion_overload_1(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.schedule_conversion(
                list_id="",
                conversion_type="CONVERSION_DATE",
                day=0,
                month=0,
                year=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule_conversion_overload_2(self, client: Hubspot) -> None:
        list_ = client.crm.lists.schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_schedule_conversion_overload_2(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_schedule_conversion_overload_2(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.schedule_conversion(
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_schedule_conversion_overload_2(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.schedule_conversion(
                list_id="",
                conversion_type="INACTIVITY",
                offset=0,
                time_unit="DAY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        list_ = client.crm.lists.search()
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        list_ = client.crm.lists.search(
            additional_properties=["hs_list_size_week_delta"],
            count=100,
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
            query="Test",
            sort="sort",
        )
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListSearchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_filters(self, client: Hubspot) -> None:
        list_ = client.crm.lists.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_filters_with_all_params(self, client: Hubspot) -> None:
        list_ = client.crm.lists.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                                "subscription_type": "subscriptionType",
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_filters(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_filters(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_filters(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.update_filters(
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
                                        "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                        "value": True,
                                    },
                                    "property": "hs_predictivecontactscore_v2",
                                },
                                {
                                    "filter_type": "PROPERTY",
                                    "operation": {
                                        "include_objects_with_no_value_set": True,
                                        "operation_type": "BOOL",
                                        "operator": "IS_UNKNOWN",
                                        "value": True,
                                    },
                                    "property": "engagements_last_meeting_booked_source",
                                },
                                {
                                    "accepted_statuses": ["OPT_IN"],
                                    "filter_type": "EMAIL_SUBSCRIPTION",
                                    "subscription_ids": ["81537745", "321981152"],
                                },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_name(self, client: Hubspot) -> None:
        list_ = client.crm.lists.update_name(
            list_id="listId",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_name_with_all_params(self, client: Hubspot) -> None:
        list_ = client.crm.lists.update_name(
            list_id="listId",
            include_filters=True,
            list_name="listName",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_name(self, client: Hubspot) -> None:
        response = client.crm.lists.with_raw_response.update_name(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_name(self, client: Hubspot) -> None:
        with client.crm.lists.with_streaming_response.update_name(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_name(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.crm.lists.with_raw_response.update_name(
                list_id="",
            )


class TestAsyncLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
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
                                            "operator": "IS_EQUAL_TO",
                                            "value": True,
                                        },
                                        "property": "hs_is_closed_won",
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
                                    "operator": "IS_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "firstname",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.create(
            name="Dynamic Association List Example",
            object_type_id="0-1",
            processing_type="DYNAMIC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.list()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.list(
            include_filters=True,
            list_ids=["string"],
        )
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListsByIDResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListsByIDResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.delete(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.delete(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.delete(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.delete_schedule_conversion(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.delete_schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.delete_schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.delete_schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.get(
            list_id="listId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.get(
            list_id="listId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.get(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.get(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_id_and_name(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_id_and_name_with_all_params(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
            include_filters=True,
        )
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_type_id_and_name(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListFetchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_type_id_and_name(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_by_object_type_id_and_name(
            list_name="listName",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListFetchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_type_id_and_name(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_by_object_type_id_and_name(
                list_name="listName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_name` but received ''"):
            await async_client.crm.lists.with_raw_response.get_by_object_type_id_and_name(
                list_name="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.get_schedule_conversion(
            "listId",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.get_schedule_conversion(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.get_schedule_conversion(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(PublicListConversionResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_schedule_conversion(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.get_schedule_conversion(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.restore(
            "listId",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.restore(
            "listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.restore(
            "listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.restore(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule_conversion_overload_1(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.schedule_conversion(
            list_id="listId",
            conversion_type="CONVERSION_DATE",
            day=0,
            month=0,
            year=0,
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_schedule_conversion_overload_1(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.schedule_conversion(
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_schedule_conversion_overload_1(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.schedule_conversion(
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_schedule_conversion_overload_1(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.schedule_conversion(
                list_id="",
                conversion_type="CONVERSION_DATE",
                day=0,
                month=0,
                year=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule_conversion_overload_2(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_schedule_conversion_overload_2(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.schedule_conversion(
            list_id="listId",
            conversion_type="INACTIVITY",
            offset=0,
            time_unit="DAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(PublicListConversionResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_schedule_conversion_overload_2(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.schedule_conversion(
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_schedule_conversion_overload_2(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.schedule_conversion(
                list_id="",
                conversion_type="INACTIVITY",
                offset=0,
                time_unit="DAY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.search()
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.search(
            additional_properties=["hs_list_size_week_delta"],
            count=100,
            list_ids=["string"],
            offset=0,
            processing_types=["string"],
            query="Test",
            sort="sort",
        )
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListSearchResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_filters(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_filters_with_all_params(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                                "subscription_type": "subscriptionType",
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_filters(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_filters(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.update_filters(
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
                                    "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                    "value": True,
                                },
                                "property": "hs_predictivecontactscore_v2",
                            },
                            {
                                "filter_type": "PROPERTY",
                                "operation": {
                                    "include_objects_with_no_value_set": True,
                                    "operation_type": "BOOL",
                                    "operator": "IS_UNKNOWN",
                                    "value": True,
                                },
                                "property": "engagements_last_meeting_booked_source",
                            },
                            {
                                "accepted_statuses": ["OPT_IN"],
                                "filter_type": "EMAIL_SUBSCRIPTION",
                                "subscription_ids": ["81537745", "321981152"],
                            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_filters(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.update_filters(
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
                                        "operator": "IS_GREATER_THAN_OR_EQUAL_TO",
                                        "value": True,
                                    },
                                    "property": "hs_predictivecontactscore_v2",
                                },
                                {
                                    "filter_type": "PROPERTY",
                                    "operation": {
                                        "include_objects_with_no_value_set": True,
                                        "operation_type": "BOOL",
                                        "operator": "IS_UNKNOWN",
                                        "value": True,
                                    },
                                    "property": "engagements_last_meeting_booked_source",
                                },
                                {
                                    "accepted_statuses": ["OPT_IN"],
                                    "filter_type": "EMAIL_SUBSCRIPTION",
                                    "subscription_ids": ["81537745", "321981152"],
                                },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_name(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.update_name(
            list_id="listId",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_name_with_all_params(self, async_client: AsyncHubspot) -> None:
        list_ = await async_client.crm.lists.update_name(
            list_id="listId",
            include_filters=True,
            list_name="listName",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_name(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.lists.with_raw_response.update_name(
            list_id="listId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_name(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.lists.with_streaming_response.update_name(
            list_id="listId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_name(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.crm.lists.with_raw_response.update_name(
                list_id="",
            )
