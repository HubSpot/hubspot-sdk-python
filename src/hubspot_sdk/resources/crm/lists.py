# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import (
    list_get_params,
    list_list_params,
    list_create_params,
    list_search_params,
    list_move_list_params,
    list_list_folders_params,
    list_create_folder_params,
    list_rename_folder_params,
    list_get_id_mapping_params,
    list_list_memberships_params,
    list_update_list_name_params,
    list_update_list_filters_params,
    list_batch_read_memberships_params,
    list_add_and_remove_memberships_params,
    list_update_schedule_conversion_params,
    list_list_memberships_join_order_params,
    list_get_by_object_type_id_and_name_params,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.crm.list_fetch_response import ListFetchResponse
from ...types.crm.list_create_response import ListCreateResponse
from ...types.crm.list_search_response import ListSearchResponse
from ...types.crm.list_update_response import ListUpdateResponse
from ...types.crm.lists_by_id_response import ListsByIDResponse
from ...types.crm.record_id_input_param import RecordIDInputParam
from ...types.crm.join_time_and_record_id import JoinTimeAndRecordID
from ...types.crm.public_migration_mapping import PublicMigrationMapping
from ...types.crm.list_folder_fetch_response import ListFolderFetchResponse
from ...types.crm.list_folder_create_response import ListFolderCreateResponse
from ...types.crm.memberships_update_response import MembershipsUpdateResponse
from ...types.crm.public_list_permissions_param import PublicListPermissionsParam
from ...types.crm.public_batch_migration_mapping import PublicBatchMigrationMapping
from ...types.crm.public_list_conversion_response import PublicListConversionResponse
from ...types.crm.public_membership_settings_param import PublicMembershipSettingsParam
from ...types.crm.batch_response_record_id_with_memberships import BatchResponseRecordIDWithMemberships
from ...types.crm.api_collection_response_record_list_membership import APICollectionResponseRecordListMembership

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ListsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        object_type_id: str,
        processing_type: str,
        custom_properties: Dict[str, str] | Omit = omit,
        filter_branch: list_create_params.FilterBranch | Omit = omit,
        list_folder_id: int | Omit = omit,
        list_permissions: PublicListPermissionsParam | Omit = omit,
        membership_settings: PublicMembershipSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListCreateResponse:
        """
        Args:
          name: The name of the list, which must be globally unique across all public lists in
              the portal.

          object_type_id: The object type ID of the type of objects that the list will store.

          processing_type: The processing type of the list. One of: `SNAPSHOT`, `MANUAL`, or `DYNAMIC`.

          custom_properties: The list of custom properties to tie to the list. Custom property name is the
              key, the value is the value.

          filter_branch: Filter branch object containing filtering criteria for the list

          list_folder_id: The ID of the folder that the list should be created in. If left blank, then the
              list will be created in the root of the list folder structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/lists/2026-03",
            body=maybe_transform(
                {
                    "name": name,
                    "object_type_id": object_type_id,
                    "processing_type": processing_type,
                    "custom_properties": custom_properties,
                    "filter_branch": filter_branch,
                    "list_folder_id": list_folder_id,
                    "list_permissions": list_permissions,
                    "membership_settings": membership_settings,
                },
                list_create_params.ListCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListCreateResponse,
        )

    def list(
        self,
        *,
        include_filters: bool | Omit = omit,
        list_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListsByIDResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/lists/2026-03",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_filters": include_filters,
                        "list_ids": list_ids,
                    },
                    list_list_params.ListListParams,
                ),
            ),
            cast_to=ListsByIDResponse,
        )

    def delete(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/lists/2026-03/{list_id}", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_and_remove_memberships(
        self,
        list_id: str,
        *,
        record_ids_to_add: SequenceNotStr[str],
        record_ids_to_remove: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipsUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            path_template("/crm/lists/2026-03/{list_id}/memberships/add-and-remove", list_id=list_id),
            body=maybe_transform(
                {
                    "record_ids_to_add": record_ids_to_add,
                    "record_ids_to_remove": record_ids_to_remove,
                },
                list_add_and_remove_memberships_params.ListAddAndRemoveMembershipsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    def add_memberships(
        self,
        list_id: str,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipsUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            path_template("/crm/lists/2026-03/{list_id}/memberships/add", list_id=list_id),
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    def add_memberships_from(
        self,
        source_list_id: str,
        *,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not source_list_id:
            raise ValueError(f"Expected a non-empty value for `source_list_id` but received {source_list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template(
                "/crm/lists/2026-03/{list_id}/memberships/add-from/{source_list_id}",
                list_id=list_id,
                source_list_id=source_list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def batch_read_memberships(
        self,
        *,
        inputs: Iterable[RecordIDInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseRecordIDWithMemberships:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/lists/2026-03/records/memberships/batch/read",
            body=maybe_transform({"inputs": inputs}, list_batch_read_memberships_params.ListBatchReadMembershipsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseRecordIDWithMemberships,
        )

    def create_folder(
        self,
        *,
        name: str,
        parent_folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderCreateResponse:
        """
        Args:
          name: The name of the folder to be created.

          parent_folder_id: The folder this should be created in, if not specified will be created in the
              root folder 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/lists/2026-03/folders",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                list_create_folder_params.ListCreateFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFolderCreateResponse,
        )

    def create_id_mapping(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBatchMigrationMapping:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/lists/2026-03/idmapping",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBatchMigrationMapping,
        )

    def delete_folder(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/lists/2026-03/folders/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_memberships(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/lists/2026-03/{list_id}/memberships", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_schedule_conversion(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/lists/2026-03/{list_id}/schedule-conversion", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        list_id: str,
        *,
        include_filters: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            path_template("/crm/lists/2026-03/{list_id}", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_filters": include_filters}, list_get_params.ListGetParams),
            ),
            cast_to=ListFetchResponse,
        )

    def get_by_object_type_id_and_name(
        self,
        list_name: str,
        *,
        object_type_id: str,
        include_filters: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not list_name:
            raise ValueError(f"Expected a non-empty value for `list_name` but received {list_name!r}")
        return self._get(
            path_template(
                "/crm/lists/2026-03/object-type-id/{object_type_id}/name/{list_name}",
                object_type_id=object_type_id,
                list_name=list_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_filters": include_filters},
                    list_get_by_object_type_id_and_name_params.ListGetByObjectTypeIDAndNameParams,
                ),
            ),
            cast_to=ListFetchResponse,
        )

    def get_id_mapping(
        self,
        *,
        legacy_list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicMigrationMapping:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/lists/2026-03/idmapping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"legacy_list_id": legacy_list_id}, list_get_id_mapping_params.ListGetIDMappingParams
                ),
            ),
            cast_to=PublicMigrationMapping,
        )

    def get_record_memberships(
        self,
        record_id: str,
        *,
        object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APICollectionResponseRecordListMembership:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return self._get(
            path_template(
                "/crm/lists/2026-03/records/{object_type_id}/{record_id}/memberships",
                object_type_id=object_type_id,
                record_id=record_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APICollectionResponseRecordListMembership,
        )

    def get_schedule_conversion(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            path_template("/crm/lists/2026-03/{list_id}/schedule-conversion", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
        )

    def list_folders(
        self,
        *,
        folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/lists/2026-03/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"folder_id": folder_id}, list_list_folders_params.ListListFoldersParams),
            ),
            cast_to=ListFolderFetchResponse,
        )

    def list_memberships(
        self,
        list_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[JoinTimeAndRecordID]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            path_template("/crm/lists/2026-03/{list_id}/memberships", list_id=list_id),
            page=SyncPage[JoinTimeAndRecordID],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    list_list_memberships_params.ListListMembershipsParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    def list_memberships_join_order(
        self,
        list_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[JoinTimeAndRecordID]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            path_template("/crm/lists/2026-03/{list_id}/memberships/join-order", list_id=list_id),
            page=SyncPage[JoinTimeAndRecordID],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    list_list_memberships_join_order_params.ListListMembershipsJoinOrderParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    def move_folder(
        self,
        new_parent_folder_id: str,
        *,
        folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        if not new_parent_folder_id:
            raise ValueError(
                f"Expected a non-empty value for `new_parent_folder_id` but received {new_parent_folder_id!r}"
            )
        return self._put(
            path_template(
                "/crm/lists/2026-03/folders/{folder_id}/move/{new_parent_folder_id}",
                folder_id=folder_id,
                new_parent_folder_id=new_parent_folder_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFolderFetchResponse,
        )

    def move_list(
        self,
        *,
        list_id: str,
        new_folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          list_id: The Id of the list to move.

          new_folder_id: The Id of folder to move the list to, the root folder is Id 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/crm/lists/2026-03/folders/move-list",
            body=maybe_transform(
                {
                    "list_id": list_id,
                    "new_folder_id": new_folder_id,
                },
                list_move_list_params.ListMoveListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_memberships(
        self,
        list_id: str,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipsUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            path_template("/crm/lists/2026-03/{list_id}/memberships/remove", list_id=list_id),
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    def rename_folder(
        self,
        folder_id: str,
        *,
        new_folder_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._put(
            path_template("/crm/lists/2026-03/folders/{folder_id}/rename", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"new_folder_name": new_folder_name}, list_rename_folder_params.ListRenameFolderParams
                ),
            ),
            cast_to=ListFolderFetchResponse,
        )

    def restore(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/crm/lists/2026-03/{list_id}/restore", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        *,
        additional_properties: SequenceNotStr[str],
        list_ids: SequenceNotStr[str],
        offset: int,
        processing_types: SequenceNotStr[str],
        count: int | Omit = omit,
        object_type_id: str | Omit = omit,
        query: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListSearchResponse:
        """
        Args:
          additional_properties: The property names of any additional list properties to include in the response.
              Properties that do not exist or that are empty for a particular list are not
              included in the response.

              By default, all requests will fetch the following properties for each list:
              `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`,
              `hs_folder_name`, and `hs_list_reference_count`.

          list_ids: The `listIds` that will be used to filter results by `listId`. If values are
              provided, then the response will only include results that have a `listId` in
              this array.

              If no value is provided, or if an empty list is provided, then the results will
              not be filtered by `listId`.

          offset: Value used to paginate through lists. The `offset` provided in the response can
              be used in the next request to fetch the next page of results. Defaults to `0`
              if no offset is provided.

          processing_types: The `processingTypes` that will be used to filter results by `processingType`.
              If values are provided, then the response will only include results that have a
              `processingType` in this array.

              If no value is provided, or if an empty list is provided, then results will not
              be filtered by `processingType`.

              Valid `processingTypes` are: `MANUAL`, `SNAPSHOT`, or `DYNAMIC`.

          count: The number of lists to include in the response. Defaults to `20` if no value is
              provided. The max `count` is `500`.

          query: The `query` that will be used to search for lists by list name. If no `query` is
              provided, then the results will include all lists.

          sort: Sort field and order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/lists/2026-03/search",
            body=maybe_transform(
                {
                    "additional_properties": additional_properties,
                    "list_ids": list_ids,
                    "offset": offset,
                    "processing_types": processing_types,
                    "count": count,
                    "object_type_id": object_type_id,
                    "query": query,
                    "sort": sort,
                },
                list_search_params.ListSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListSearchResponse,
        )

    def update_list_filters(
        self,
        list_id: str,
        *,
        filter_branch: list_update_list_filters_params.FilterBranch,
        enroll_objects_in_workflows: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUpdateResponse:
        """
        Args:
          filter_branch: Updated filtering criteria for the list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            path_template("/crm/lists/2026-03/{list_id}/update-list-filters", list_id=list_id),
            body=maybe_transform(
                {"filter_branch": filter_branch}, list_update_list_filters_params.ListUpdateListFiltersParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"enroll_objects_in_workflows": enroll_objects_in_workflows},
                    list_update_list_filters_params.ListUpdateListFiltersParams,
                ),
            ),
            cast_to=ListUpdateResponse,
        )

    def update_list_name(
        self,
        list_id: str,
        *,
        include_filters: bool | Omit = omit,
        list_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            path_template("/crm/lists/2026-03/{list_id}/update-list-name", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_filters": include_filters,
                        "list_name": list_name,
                    },
                    list_update_list_name_params.ListUpdateListNameParams,
                ),
            ),
            cast_to=ListUpdateResponse,
        )

    @overload
    def update_schedule_conversion(
        self,
        list_id: str,
        *,
        conversion_type: Literal["CONVERSION_DATE"],
        day: int,
        month: int,
        year: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        """
        Args:
          conversion_type: Specifies the type of conversion (CONVERSION_DATE).

          day: The day component of the conversion date.

          month: The month component of the conversion date.

          year: The year component of the conversion date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update_schedule_conversion(
        self,
        list_id: str,
        *,
        conversion_type: Literal["INACTIVITY"],
        offset: int,
        time_unit: Literal["DAY", "MONTH", "WEEK"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        """
        Args:
          conversion_type: Specifies the type of conversion (INACTIVITY).

          offset: The number of time units for the inactivity period.

          time_unit: The unit of time for the inactivity period, such as (DAY, MONTH, WEEK).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversion_type", "day", "month", "year"], ["conversion_type", "offset", "time_unit"])
    def update_schedule_conversion(
        self,
        list_id: str,
        *,
        conversion_type: Literal["CONVERSION_DATE"] | Literal["INACTIVITY"],
        day: int | Omit = omit,
        month: int | Omit = omit,
        year: int | Omit = omit,
        offset: int | Omit = omit,
        time_unit: Literal["DAY", "MONTH", "WEEK"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            path_template("/crm/lists/2026-03/{list_id}/schedule-conversion", list_id=list_id),
            body=maybe_transform(
                {
                    "conversion_type": conversion_type,
                    "day": day,
                    "month": month,
                    "year": year,
                    "offset": offset,
                    "time_unit": time_unit,
                },
                list_update_schedule_conversion_params.ListUpdateScheduleConversionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
        )


class AsyncListsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncListsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        object_type_id: str,
        processing_type: str,
        custom_properties: Dict[str, str] | Omit = omit,
        filter_branch: list_create_params.FilterBranch | Omit = omit,
        list_folder_id: int | Omit = omit,
        list_permissions: PublicListPermissionsParam | Omit = omit,
        membership_settings: PublicMembershipSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListCreateResponse:
        """
        Args:
          name: The name of the list, which must be globally unique across all public lists in
              the portal.

          object_type_id: The object type ID of the type of objects that the list will store.

          processing_type: The processing type of the list. One of: `SNAPSHOT`, `MANUAL`, or `DYNAMIC`.

          custom_properties: The list of custom properties to tie to the list. Custom property name is the
              key, the value is the value.

          filter_branch: Filter branch object containing filtering criteria for the list

          list_folder_id: The ID of the folder that the list should be created in. If left blank, then the
              list will be created in the root of the list folder structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/lists/2026-03",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "object_type_id": object_type_id,
                    "processing_type": processing_type,
                    "custom_properties": custom_properties,
                    "filter_branch": filter_branch,
                    "list_folder_id": list_folder_id,
                    "list_permissions": list_permissions,
                    "membership_settings": membership_settings,
                },
                list_create_params.ListCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListCreateResponse,
        )

    async def list(
        self,
        *,
        include_filters: bool | Omit = omit,
        list_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListsByIDResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/lists/2026-03",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_filters": include_filters,
                        "list_ids": list_ids,
                    },
                    list_list_params.ListListParams,
                ),
            ),
            cast_to=ListsByIDResponse,
        )

    async def delete(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/lists/2026-03/{list_id}", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_and_remove_memberships(
        self,
        list_id: str,
        *,
        record_ids_to_add: SequenceNotStr[str],
        record_ids_to_remove: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipsUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            path_template("/crm/lists/2026-03/{list_id}/memberships/add-and-remove", list_id=list_id),
            body=await async_maybe_transform(
                {
                    "record_ids_to_add": record_ids_to_add,
                    "record_ids_to_remove": record_ids_to_remove,
                },
                list_add_and_remove_memberships_params.ListAddAndRemoveMembershipsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    async def add_memberships(
        self,
        list_id: str,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipsUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            path_template("/crm/lists/2026-03/{list_id}/memberships/add", list_id=list_id),
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    async def add_memberships_from(
        self,
        source_list_id: str,
        *,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not source_list_id:
            raise ValueError(f"Expected a non-empty value for `source_list_id` but received {source_list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/crm/lists/2026-03/{list_id}/memberships/add-from/{source_list_id}",
                list_id=list_id,
                source_list_id=source_list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def batch_read_memberships(
        self,
        *,
        inputs: Iterable[RecordIDInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseRecordIDWithMemberships:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/lists/2026-03/records/memberships/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, list_batch_read_memberships_params.ListBatchReadMembershipsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseRecordIDWithMemberships,
        )

    async def create_folder(
        self,
        *,
        name: str,
        parent_folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderCreateResponse:
        """
        Args:
          name: The name of the folder to be created.

          parent_folder_id: The folder this should be created in, if not specified will be created in the
              root folder 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/lists/2026-03/folders",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                list_create_folder_params.ListCreateFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFolderCreateResponse,
        )

    async def create_id_mapping(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBatchMigrationMapping:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/lists/2026-03/idmapping",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBatchMigrationMapping,
        )

    async def delete_folder(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/lists/2026-03/folders/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_memberships(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/lists/2026-03/{list_id}/memberships", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_schedule_conversion(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/lists/2026-03/{list_id}/schedule-conversion", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        list_id: str,
        *,
        include_filters: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            path_template("/crm/lists/2026-03/{list_id}", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include_filters": include_filters}, list_get_params.ListGetParams),
            ),
            cast_to=ListFetchResponse,
        )

    async def get_by_object_type_id_and_name(
        self,
        list_name: str,
        *,
        object_type_id: str,
        include_filters: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not list_name:
            raise ValueError(f"Expected a non-empty value for `list_name` but received {list_name!r}")
        return await self._get(
            path_template(
                "/crm/lists/2026-03/object-type-id/{object_type_id}/name/{list_name}",
                object_type_id=object_type_id,
                list_name=list_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_filters": include_filters},
                    list_get_by_object_type_id_and_name_params.ListGetByObjectTypeIDAndNameParams,
                ),
            ),
            cast_to=ListFetchResponse,
        )

    async def get_id_mapping(
        self,
        *,
        legacy_list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicMigrationMapping:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/lists/2026-03/idmapping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"legacy_list_id": legacy_list_id}, list_get_id_mapping_params.ListGetIDMappingParams
                ),
            ),
            cast_to=PublicMigrationMapping,
        )

    async def get_record_memberships(
        self,
        record_id: str,
        *,
        object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APICollectionResponseRecordListMembership:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return await self._get(
            path_template(
                "/crm/lists/2026-03/records/{object_type_id}/{record_id}/memberships",
                object_type_id=object_type_id,
                record_id=record_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APICollectionResponseRecordListMembership,
        )

    async def get_schedule_conversion(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            path_template("/crm/lists/2026-03/{list_id}/schedule-conversion", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
        )

    async def list_folders(
        self,
        *,
        folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/lists/2026-03/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"folder_id": folder_id}, list_list_folders_params.ListListFoldersParams
                ),
            ),
            cast_to=ListFolderFetchResponse,
        )

    def list_memberships(
        self,
        list_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JoinTimeAndRecordID, AsyncPage[JoinTimeAndRecordID]]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            path_template("/crm/lists/2026-03/{list_id}/memberships", list_id=list_id),
            page=AsyncPage[JoinTimeAndRecordID],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    list_list_memberships_params.ListListMembershipsParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    def list_memberships_join_order(
        self,
        list_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JoinTimeAndRecordID, AsyncPage[JoinTimeAndRecordID]]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            path_template("/crm/lists/2026-03/{list_id}/memberships/join-order", list_id=list_id),
            page=AsyncPage[JoinTimeAndRecordID],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    list_list_memberships_join_order_params.ListListMembershipsJoinOrderParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    async def move_folder(
        self,
        new_parent_folder_id: str,
        *,
        folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        if not new_parent_folder_id:
            raise ValueError(
                f"Expected a non-empty value for `new_parent_folder_id` but received {new_parent_folder_id!r}"
            )
        return await self._put(
            path_template(
                "/crm/lists/2026-03/folders/{folder_id}/move/{new_parent_folder_id}",
                folder_id=folder_id,
                new_parent_folder_id=new_parent_folder_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFolderFetchResponse,
        )

    async def move_list(
        self,
        *,
        list_id: str,
        new_folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          list_id: The Id of the list to move.

          new_folder_id: The Id of folder to move the list to, the root folder is Id 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/crm/lists/2026-03/folders/move-list",
            body=await async_maybe_transform(
                {
                    "list_id": list_id,
                    "new_folder_id": new_folder_id,
                },
                list_move_list_params.ListMoveListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_memberships(
        self,
        list_id: str,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipsUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            path_template("/crm/lists/2026-03/{list_id}/memberships/remove", list_id=list_id),
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    async def rename_folder(
        self,
        folder_id: str,
        *,
        new_folder_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListFolderFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._put(
            path_template("/crm/lists/2026-03/folders/{folder_id}/rename", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"new_folder_name": new_folder_name}, list_rename_folder_params.ListRenameFolderParams
                ),
            ),
            cast_to=ListFolderFetchResponse,
        )

    async def restore(
        self,
        list_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/crm/lists/2026-03/{list_id}/restore", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def search(
        self,
        *,
        additional_properties: SequenceNotStr[str],
        list_ids: SequenceNotStr[str],
        offset: int,
        processing_types: SequenceNotStr[str],
        count: int | Omit = omit,
        object_type_id: str | Omit = omit,
        query: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListSearchResponse:
        """
        Args:
          additional_properties: The property names of any additional list properties to include in the response.
              Properties that do not exist or that are empty for a particular list are not
              included in the response.

              By default, all requests will fetch the following properties for each list:
              `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`,
              `hs_folder_name`, and `hs_list_reference_count`.

          list_ids: The `listIds` that will be used to filter results by `listId`. If values are
              provided, then the response will only include results that have a `listId` in
              this array.

              If no value is provided, or if an empty list is provided, then the results will
              not be filtered by `listId`.

          offset: Value used to paginate through lists. The `offset` provided in the response can
              be used in the next request to fetch the next page of results. Defaults to `0`
              if no offset is provided.

          processing_types: The `processingTypes` that will be used to filter results by `processingType`.
              If values are provided, then the response will only include results that have a
              `processingType` in this array.

              If no value is provided, or if an empty list is provided, then results will not
              be filtered by `processingType`.

              Valid `processingTypes` are: `MANUAL`, `SNAPSHOT`, or `DYNAMIC`.

          count: The number of lists to include in the response. Defaults to `20` if no value is
              provided. The max `count` is `500`.

          query: The `query` that will be used to search for lists by list name. If no `query` is
              provided, then the results will include all lists.

          sort: Sort field and order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/lists/2026-03/search",
            body=await async_maybe_transform(
                {
                    "additional_properties": additional_properties,
                    "list_ids": list_ids,
                    "offset": offset,
                    "processing_types": processing_types,
                    "count": count,
                    "object_type_id": object_type_id,
                    "query": query,
                    "sort": sort,
                },
                list_search_params.ListSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListSearchResponse,
        )

    async def update_list_filters(
        self,
        list_id: str,
        *,
        filter_branch: list_update_list_filters_params.FilterBranch,
        enroll_objects_in_workflows: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUpdateResponse:
        """
        Args:
          filter_branch: Updated filtering criteria for the list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            path_template("/crm/lists/2026-03/{list_id}/update-list-filters", list_id=list_id),
            body=await async_maybe_transform(
                {"filter_branch": filter_branch}, list_update_list_filters_params.ListUpdateListFiltersParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"enroll_objects_in_workflows": enroll_objects_in_workflows},
                    list_update_list_filters_params.ListUpdateListFiltersParams,
                ),
            ),
            cast_to=ListUpdateResponse,
        )

    async def update_list_name(
        self,
        list_id: str,
        *,
        include_filters: bool | Omit = omit,
        list_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            path_template("/crm/lists/2026-03/{list_id}/update-list-name", list_id=list_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_filters": include_filters,
                        "list_name": list_name,
                    },
                    list_update_list_name_params.ListUpdateListNameParams,
                ),
            ),
            cast_to=ListUpdateResponse,
        )

    @overload
    async def update_schedule_conversion(
        self,
        list_id: str,
        *,
        conversion_type: Literal["CONVERSION_DATE"],
        day: int,
        month: int,
        year: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        """
        Args:
          conversion_type: Specifies the type of conversion (CONVERSION_DATE).

          day: The day component of the conversion date.

          month: The month component of the conversion date.

          year: The year component of the conversion date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update_schedule_conversion(
        self,
        list_id: str,
        *,
        conversion_type: Literal["INACTIVITY"],
        offset: int,
        time_unit: Literal["DAY", "MONTH", "WEEK"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        """
        Args:
          conversion_type: Specifies the type of conversion (INACTIVITY).

          offset: The number of time units for the inactivity period.

          time_unit: The unit of time for the inactivity period, such as (DAY, MONTH, WEEK).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversion_type", "day", "month", "year"], ["conversion_type", "offset", "time_unit"])
    async def update_schedule_conversion(
        self,
        list_id: str,
        *,
        conversion_type: Literal["CONVERSION_DATE"] | Literal["INACTIVITY"],
        day: int | Omit = omit,
        month: int | Omit = omit,
        year: int | Omit = omit,
        offset: int | Omit = omit,
        time_unit: Literal["DAY", "MONTH", "WEEK"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicListConversionResponse:
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            path_template("/crm/lists/2026-03/{list_id}/schedule-conversion", list_id=list_id),
            body=await async_maybe_transform(
                {
                    "conversion_type": conversion_type,
                    "day": day,
                    "month": month,
                    "year": year,
                    "offset": offset,
                    "time_unit": time_unit,
                },
                list_update_schedule_conversion_params.ListUpdateScheduleConversionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_raw_response_wrapper(
            lists.create,
        )
        self.list = to_raw_response_wrapper(
            lists.list,
        )
        self.delete = to_raw_response_wrapper(
            lists.delete,
        )
        self.add_and_remove_memberships = to_raw_response_wrapper(
            lists.add_and_remove_memberships,
        )
        self.add_memberships = to_raw_response_wrapper(
            lists.add_memberships,
        )
        self.add_memberships_from = to_raw_response_wrapper(
            lists.add_memberships_from,
        )
        self.batch_read_memberships = to_raw_response_wrapper(
            lists.batch_read_memberships,
        )
        self.create_folder = to_raw_response_wrapper(
            lists.create_folder,
        )
        self.create_id_mapping = to_raw_response_wrapper(
            lists.create_id_mapping,
        )
        self.delete_folder = to_raw_response_wrapper(
            lists.delete_folder,
        )
        self.delete_memberships = to_raw_response_wrapper(
            lists.delete_memberships,
        )
        self.delete_schedule_conversion = to_raw_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = to_raw_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = to_raw_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_id_mapping = to_raw_response_wrapper(
            lists.get_id_mapping,
        )
        self.get_record_memberships = to_raw_response_wrapper(
            lists.get_record_memberships,
        )
        self.get_schedule_conversion = to_raw_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.list_folders = to_raw_response_wrapper(
            lists.list_folders,
        )
        self.list_memberships = to_raw_response_wrapper(
            lists.list_memberships,
        )
        self.list_memberships_join_order = to_raw_response_wrapper(
            lists.list_memberships_join_order,
        )
        self.move_folder = to_raw_response_wrapper(
            lists.move_folder,
        )
        self.move_list = to_raw_response_wrapper(
            lists.move_list,
        )
        self.remove_memberships = to_raw_response_wrapper(
            lists.remove_memberships,
        )
        self.rename_folder = to_raw_response_wrapper(
            lists.rename_folder,
        )
        self.restore = to_raw_response_wrapper(
            lists.restore,
        )
        self.search = to_raw_response_wrapper(
            lists.search,
        )
        self.update_list_filters = to_raw_response_wrapper(
            lists.update_list_filters,
        )
        self.update_list_name = to_raw_response_wrapper(
            lists.update_list_name,
        )
        self.update_schedule_conversion = to_raw_response_wrapper(
            lists.update_schedule_conversion,
        )


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_raw_response_wrapper(
            lists.create,
        )
        self.list = async_to_raw_response_wrapper(
            lists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lists.delete,
        )
        self.add_and_remove_memberships = async_to_raw_response_wrapper(
            lists.add_and_remove_memberships,
        )
        self.add_memberships = async_to_raw_response_wrapper(
            lists.add_memberships,
        )
        self.add_memberships_from = async_to_raw_response_wrapper(
            lists.add_memberships_from,
        )
        self.batch_read_memberships = async_to_raw_response_wrapper(
            lists.batch_read_memberships,
        )
        self.create_folder = async_to_raw_response_wrapper(
            lists.create_folder,
        )
        self.create_id_mapping = async_to_raw_response_wrapper(
            lists.create_id_mapping,
        )
        self.delete_folder = async_to_raw_response_wrapper(
            lists.delete_folder,
        )
        self.delete_memberships = async_to_raw_response_wrapper(
            lists.delete_memberships,
        )
        self.delete_schedule_conversion = async_to_raw_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = async_to_raw_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = async_to_raw_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_id_mapping = async_to_raw_response_wrapper(
            lists.get_id_mapping,
        )
        self.get_record_memberships = async_to_raw_response_wrapper(
            lists.get_record_memberships,
        )
        self.get_schedule_conversion = async_to_raw_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.list_folders = async_to_raw_response_wrapper(
            lists.list_folders,
        )
        self.list_memberships = async_to_raw_response_wrapper(
            lists.list_memberships,
        )
        self.list_memberships_join_order = async_to_raw_response_wrapper(
            lists.list_memberships_join_order,
        )
        self.move_folder = async_to_raw_response_wrapper(
            lists.move_folder,
        )
        self.move_list = async_to_raw_response_wrapper(
            lists.move_list,
        )
        self.remove_memberships = async_to_raw_response_wrapper(
            lists.remove_memberships,
        )
        self.rename_folder = async_to_raw_response_wrapper(
            lists.rename_folder,
        )
        self.restore = async_to_raw_response_wrapper(
            lists.restore,
        )
        self.search = async_to_raw_response_wrapper(
            lists.search,
        )
        self.update_list_filters = async_to_raw_response_wrapper(
            lists.update_list_filters,
        )
        self.update_list_name = async_to_raw_response_wrapper(
            lists.update_list_name,
        )
        self.update_schedule_conversion = async_to_raw_response_wrapper(
            lists.update_schedule_conversion,
        )


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_streamed_response_wrapper(
            lists.create,
        )
        self.list = to_streamed_response_wrapper(
            lists.list,
        )
        self.delete = to_streamed_response_wrapper(
            lists.delete,
        )
        self.add_and_remove_memberships = to_streamed_response_wrapper(
            lists.add_and_remove_memberships,
        )
        self.add_memberships = to_streamed_response_wrapper(
            lists.add_memberships,
        )
        self.add_memberships_from = to_streamed_response_wrapper(
            lists.add_memberships_from,
        )
        self.batch_read_memberships = to_streamed_response_wrapper(
            lists.batch_read_memberships,
        )
        self.create_folder = to_streamed_response_wrapper(
            lists.create_folder,
        )
        self.create_id_mapping = to_streamed_response_wrapper(
            lists.create_id_mapping,
        )
        self.delete_folder = to_streamed_response_wrapper(
            lists.delete_folder,
        )
        self.delete_memberships = to_streamed_response_wrapper(
            lists.delete_memberships,
        )
        self.delete_schedule_conversion = to_streamed_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = to_streamed_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = to_streamed_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_id_mapping = to_streamed_response_wrapper(
            lists.get_id_mapping,
        )
        self.get_record_memberships = to_streamed_response_wrapper(
            lists.get_record_memberships,
        )
        self.get_schedule_conversion = to_streamed_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.list_folders = to_streamed_response_wrapper(
            lists.list_folders,
        )
        self.list_memberships = to_streamed_response_wrapper(
            lists.list_memberships,
        )
        self.list_memberships_join_order = to_streamed_response_wrapper(
            lists.list_memberships_join_order,
        )
        self.move_folder = to_streamed_response_wrapper(
            lists.move_folder,
        )
        self.move_list = to_streamed_response_wrapper(
            lists.move_list,
        )
        self.remove_memberships = to_streamed_response_wrapper(
            lists.remove_memberships,
        )
        self.rename_folder = to_streamed_response_wrapper(
            lists.rename_folder,
        )
        self.restore = to_streamed_response_wrapper(
            lists.restore,
        )
        self.search = to_streamed_response_wrapper(
            lists.search,
        )
        self.update_list_filters = to_streamed_response_wrapper(
            lists.update_list_filters,
        )
        self.update_list_name = to_streamed_response_wrapper(
            lists.update_list_name,
        )
        self.update_schedule_conversion = to_streamed_response_wrapper(
            lists.update_schedule_conversion,
        )


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_streamed_response_wrapper(
            lists.create,
        )
        self.list = async_to_streamed_response_wrapper(
            lists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lists.delete,
        )
        self.add_and_remove_memberships = async_to_streamed_response_wrapper(
            lists.add_and_remove_memberships,
        )
        self.add_memberships = async_to_streamed_response_wrapper(
            lists.add_memberships,
        )
        self.add_memberships_from = async_to_streamed_response_wrapper(
            lists.add_memberships_from,
        )
        self.batch_read_memberships = async_to_streamed_response_wrapper(
            lists.batch_read_memberships,
        )
        self.create_folder = async_to_streamed_response_wrapper(
            lists.create_folder,
        )
        self.create_id_mapping = async_to_streamed_response_wrapper(
            lists.create_id_mapping,
        )
        self.delete_folder = async_to_streamed_response_wrapper(
            lists.delete_folder,
        )
        self.delete_memberships = async_to_streamed_response_wrapper(
            lists.delete_memberships,
        )
        self.delete_schedule_conversion = async_to_streamed_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = async_to_streamed_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = async_to_streamed_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_id_mapping = async_to_streamed_response_wrapper(
            lists.get_id_mapping,
        )
        self.get_record_memberships = async_to_streamed_response_wrapper(
            lists.get_record_memberships,
        )
        self.get_schedule_conversion = async_to_streamed_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.list_folders = async_to_streamed_response_wrapper(
            lists.list_folders,
        )
        self.list_memberships = async_to_streamed_response_wrapper(
            lists.list_memberships,
        )
        self.list_memberships_join_order = async_to_streamed_response_wrapper(
            lists.list_memberships_join_order,
        )
        self.move_folder = async_to_streamed_response_wrapper(
            lists.move_folder,
        )
        self.move_list = async_to_streamed_response_wrapper(
            lists.move_list,
        )
        self.remove_memberships = async_to_streamed_response_wrapper(
            lists.remove_memberships,
        )
        self.rename_folder = async_to_streamed_response_wrapper(
            lists.rename_folder,
        )
        self.restore = async_to_streamed_response_wrapper(
            lists.restore,
        )
        self.search = async_to_streamed_response_wrapper(
            lists.search,
        )
        self.update_list_filters = async_to_streamed_response_wrapper(
            lists.update_list_filters,
        )
        self.update_list_name = async_to_streamed_response_wrapper(
            lists.update_list_name,
        )
        self.update_schedule_conversion = async_to_streamed_response_wrapper(
            lists.update_schedule_conversion,
        )
