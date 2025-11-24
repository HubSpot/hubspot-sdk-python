# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, overload

import httpx

from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from .mapping import (
    MappingResource,
    AsyncMappingResource,
    MappingResourceWithRawResponse,
    AsyncMappingResourceWithRawResponse,
    MappingResourceWithStreamingResponse,
    AsyncMappingResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .memberships import (
    MembershipsResource,
    AsyncMembershipsResource,
    MembershipsResourceWithRawResponse,
    AsyncMembershipsResourceWithRawResponse,
    MembershipsResourceWithStreamingResponse,
    AsyncMembershipsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.crm import (
    list_get_params,
    list_list_params,
    list_create_params,
    list_search_params,
    list_update_name_params,
    list_update_filters_params,
    list_schedule_conversion_params,
    list_get_by_object_type_id_and_name_params,
)
from ...._base_client import make_request_options
from ....types.crm.list_fetch_response import ListFetchResponse
from ....types.crm.list_create_response import ListCreateResponse
from ....types.crm.list_search_response import ListSearchResponse
from ....types.crm.list_update_response import ListUpdateResponse
from ....types.crm.lists_by_id_response import ListsByIDResponse
from ....types.crm.public_list_permissions_param import PublicListPermissionsParam
from ....types.crm.public_list_conversion_response import PublicListConversionResponse
from ....types.crm.public_membership_settings_param import PublicMembershipSettingsParam

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def mapping(self) -> MappingResource:
        return MappingResource(self._client)

    @cached_property
    def memberships(self) -> MembershipsResource:
        return MembershipsResource(self._client)

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
        Create a new list with the provided object list definition.

        Args:
          name: The name of the list, which must be globally unique across all public lists in
              the portal.

          object_type_id: The object type ID of the type of objects that the list will store.

          processing_type: The processing type of the list. One of: `SNAPSHOT`, `MANUAL`, or `DYNAMIC`.

          custom_properties: The list of custom properties to tie to the list. Custom property name is the
              key, the value is the value.

          list_folder_id: The ID of the folder that the list should be created in. If left blank, then the
              list will be created in the root of the list folder structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/lists/",
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
        """Fetch multiple lists in a single request by **ILS list ID**.

        The response will
        include the definitions of all lists that exist for the `listIds` provided.

        Args:
          include_filters: A flag indicating whether or not the response object list definitions should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

          list_ids: The **ILS IDs** of the lists to fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/v3/lists/",
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
        """Delete a list by **ILS list ID**.

        Lists deleted through this endpoint can be
        restored up to 90-days following the delete. After 90-days, the list is purged
        and can no longer be restored.

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
            f"/crm/v3/lists/{list_id}",
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
        Delete an existing scheduled conversion for a list.

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
            f"/crm/v3/lists/{list_id}/schedule-conversion",
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
        Fetch a single list by **ILS list ID**.

        Args:
          include_filters: A flag indicating whether or not the response object list definition should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            f"/crm/v3/lists/{list_id}",
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
        Fetch a single list by list name and object type.

        Args:
          include_filters: A flag indicating whether or not the response object list definition should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

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
            f"/crm/v3/lists/object-type-id/{object_type_id}/name/{list_name}",
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
        """Retrieve the conversion details for a list.

        This can be used to check for an
        upcoming conversion, or to get the details of when a list was already converted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            f"/crm/v3/lists/{list_id}/schedule-conversion",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
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
        """Restore a previously deleted list by **ILS list ID**.

        Deleted lists are eligible
        to be restored up-to 90-days after the list has been deleted.

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
            f"/crm/v3/lists/{list_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    def schedule_conversion(
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
        Schedule the conversion of an active list into a static list, or update the
        already scheduled conversion. This can be scheduled for a specific date or based
        on activity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def schedule_conversion(
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
        Schedule the conversion of an active list into a static list, or update the
        already scheduled conversion. This can be scheduled for a specific date or based
        on activity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversion_type", "day", "month", "year"], ["conversion_type", "offset", "time_unit"])
    def schedule_conversion(
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
            f"/crm/v3/lists/{list_id}/schedule-conversion",
            body=maybe_transform(
                {
                    "conversion_type": conversion_type,
                    "day": day,
                    "month": month,
                    "year": year,
                    "offset": offset,
                    "time_unit": time_unit,
                },
                list_schedule_conversion_params.ListScheduleConversionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
        )

    def search(
        self,
        *,
        additional_properties: SequenceNotStr[str],
        offset: int,
        count: int | Omit = omit,
        list_ids: SequenceNotStr[str] | Omit = omit,
        processing_types: SequenceNotStr[str] | Omit = omit,
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
        Search lists by list name or page through all lists by providing an empty
        `query` value.

        Args:
          additional_properties: The property names of any additional list properties to include in the response.
              Properties that do not exist or that are empty for a particular list are not
              included in the response.

              By default, all requests will fetch the following properties for each list:
              `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`,
              `hs_folder_name`, and `hs_list_reference_count`.

          offset: Value used to paginate through lists. The `offset` provided in the response can
              be used in the next request to fetch the next page of results. Defaults to `0`
              if no offset is provided.

          count: The number of lists to include in the response. Defaults to `20` if no value is
              provided. The max `count` is `500`.

          list_ids: The `listIds` that will be used to filter results by `listId`. If values are
              provided, then the response will only include results that have a `listId` in
              this array.

              If no value is provided, or if an empty list is provided, then the results will
              not be filtered by `listId`.

          processing_types: The `processingTypes` that will be used to filter results by `processingType`.
              If values are provided, then the response will only include results that have a
              `processingType` in this array.

              If no value is provided, or if an empty list is provided, then results will not
              be filtered by `processingType`.

              Valid `processingTypes` are: `MANUAL`, `SNAPSHOT`, or `DYNAMIC`.

          query: The `query` that will be used to search for lists by list name. If no `query` is
              provided, then the results will include all lists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/lists/search",
            body=maybe_transform(
                {
                    "additional_properties": additional_properties,
                    "offset": offset,
                    "count": count,
                    "list_ids": list_ids,
                    "processing_types": processing_types,
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

    def update_filters(
        self,
        list_id: str,
        *,
        filter_branch: list_update_filters_params.FilterBranch,
        enroll_objects_in_workflows: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUpdateResponse:
        """Update the filter branch definition of a `DYNAMIC` list.

        Once updated, the list
        memberships will be re-evaluated and updated to match the new definition.

        Args:
          enroll_objects_in_workflows: A flag indicating whether or not the memberships added to the list as a result
              of the filter change should be enrolled in workflows that are relevant to this
              list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/crm/v3/lists/{list_id}/update-list-filters",
            body=maybe_transform({"filter_branch": filter_branch}, list_update_filters_params.ListUpdateFiltersParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"enroll_objects_in_workflows": enroll_objects_in_workflows},
                    list_update_filters_params.ListUpdateFiltersParams,
                ),
            ),
            cast_to=ListUpdateResponse,
        )

    def update_name(
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
        """Update the name of a list.

        The name must be globally unique relative to all
        other public lists in the portal.

        Args:
          include_filters: A flag indicating whether or not the response object list definition should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

          list_name: The name to update the list to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/crm/v3/lists/{list_id}/update-list-name",
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
                    list_update_name_params.ListUpdateNameParams,
                ),
            ),
            cast_to=ListUpdateResponse,
        )


class AsyncListsResource(AsyncAPIResource):
    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def mapping(self) -> AsyncMappingResource:
        return AsyncMappingResource(self._client)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        return AsyncMembershipsResource(self._client)

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
        Create a new list with the provided object list definition.

        Args:
          name: The name of the list, which must be globally unique across all public lists in
              the portal.

          object_type_id: The object type ID of the type of objects that the list will store.

          processing_type: The processing type of the list. One of: `SNAPSHOT`, `MANUAL`, or `DYNAMIC`.

          custom_properties: The list of custom properties to tie to the list. Custom property name is the
              key, the value is the value.

          list_folder_id: The ID of the folder that the list should be created in. If left blank, then the
              list will be created in the root of the list folder structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/lists/",
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
        """Fetch multiple lists in a single request by **ILS list ID**.

        The response will
        include the definitions of all lists that exist for the `listIds` provided.

        Args:
          include_filters: A flag indicating whether or not the response object list definitions should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

          list_ids: The **ILS IDs** of the lists to fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/v3/lists/",
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
        """Delete a list by **ILS list ID**.

        Lists deleted through this endpoint can be
        restored up to 90-days following the delete. After 90-days, the list is purged
        and can no longer be restored.

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
            f"/crm/v3/lists/{list_id}",
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
        Delete an existing scheduled conversion for a list.

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
            f"/crm/v3/lists/{list_id}/schedule-conversion",
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
        Fetch a single list by **ILS list ID**.

        Args:
          include_filters: A flag indicating whether or not the response object list definition should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            f"/crm/v3/lists/{list_id}",
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
        Fetch a single list by list name and object type.

        Args:
          include_filters: A flag indicating whether or not the response object list definition should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

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
            f"/crm/v3/lists/object-type-id/{object_type_id}/name/{list_name}",
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
        """Retrieve the conversion details for a list.

        This can be used to check for an
        upcoming conversion, or to get the details of when a list was already converted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            f"/crm/v3/lists/{list_id}/schedule-conversion",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
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
        """Restore a previously deleted list by **ILS list ID**.

        Deleted lists are eligible
        to be restored up-to 90-days after the list has been deleted.

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
            f"/crm/v3/lists/{list_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    async def schedule_conversion(
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
        Schedule the conversion of an active list into a static list, or update the
        already scheduled conversion. This can be scheduled for a specific date or based
        on activity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def schedule_conversion(
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
        Schedule the conversion of an active list into a static list, or update the
        already scheduled conversion. This can be scheduled for a specific date or based
        on activity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversion_type", "day", "month", "year"], ["conversion_type", "offset", "time_unit"])
    async def schedule_conversion(
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
            f"/crm/v3/lists/{list_id}/schedule-conversion",
            body=await async_maybe_transform(
                {
                    "conversion_type": conversion_type,
                    "day": day,
                    "month": month,
                    "year": year,
                    "offset": offset,
                    "time_unit": time_unit,
                },
                list_schedule_conversion_params.ListScheduleConversionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicListConversionResponse,
        )

    async def search(
        self,
        *,
        additional_properties: SequenceNotStr[str],
        offset: int,
        count: int | Omit = omit,
        list_ids: SequenceNotStr[str] | Omit = omit,
        processing_types: SequenceNotStr[str] | Omit = omit,
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
        Search lists by list name or page through all lists by providing an empty
        `query` value.

        Args:
          additional_properties: The property names of any additional list properties to include in the response.
              Properties that do not exist or that are empty for a particular list are not
              included in the response.

              By default, all requests will fetch the following properties for each list:
              `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`,
              `hs_folder_name`, and `hs_list_reference_count`.

          offset: Value used to paginate through lists. The `offset` provided in the response can
              be used in the next request to fetch the next page of results. Defaults to `0`
              if no offset is provided.

          count: The number of lists to include in the response. Defaults to `20` if no value is
              provided. The max `count` is `500`.

          list_ids: The `listIds` that will be used to filter results by `listId`. If values are
              provided, then the response will only include results that have a `listId` in
              this array.

              If no value is provided, or if an empty list is provided, then the results will
              not be filtered by `listId`.

          processing_types: The `processingTypes` that will be used to filter results by `processingType`.
              If values are provided, then the response will only include results that have a
              `processingType` in this array.

              If no value is provided, or if an empty list is provided, then results will not
              be filtered by `processingType`.

              Valid `processingTypes` are: `MANUAL`, `SNAPSHOT`, or `DYNAMIC`.

          query: The `query` that will be used to search for lists by list name. If no `query` is
              provided, then the results will include all lists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/lists/search",
            body=await async_maybe_transform(
                {
                    "additional_properties": additional_properties,
                    "offset": offset,
                    "count": count,
                    "list_ids": list_ids,
                    "processing_types": processing_types,
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

    async def update_filters(
        self,
        list_id: str,
        *,
        filter_branch: list_update_filters_params.FilterBranch,
        enroll_objects_in_workflows: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUpdateResponse:
        """Update the filter branch definition of a `DYNAMIC` list.

        Once updated, the list
        memberships will be re-evaluated and updated to match the new definition.

        Args:
          enroll_objects_in_workflows: A flag indicating whether or not the memberships added to the list as a result
              of the filter change should be enrolled in workflows that are relevant to this
              list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/crm/v3/lists/{list_id}/update-list-filters",
            body=await async_maybe_transform(
                {"filter_branch": filter_branch}, list_update_filters_params.ListUpdateFiltersParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"enroll_objects_in_workflows": enroll_objects_in_workflows},
                    list_update_filters_params.ListUpdateFiltersParams,
                ),
            ),
            cast_to=ListUpdateResponse,
        )

    async def update_name(
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
        """Update the name of a list.

        The name must be globally unique relative to all
        other public lists in the portal.

        Args:
          include_filters: A flag indicating whether or not the response object list definition should
              include a filter branch definition. By default, object list definitions will not
              have their filter branch definitions included in the response.

          list_name: The name to update the list to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/crm/v3/lists/{list_id}/update-list-name",
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
                    list_update_name_params.ListUpdateNameParams,
                ),
            ),
            cast_to=ListUpdateResponse,
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
        self.delete_schedule_conversion = to_raw_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = to_raw_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = to_raw_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_schedule_conversion = to_raw_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.restore = to_raw_response_wrapper(
            lists.restore,
        )
        self.schedule_conversion = to_raw_response_wrapper(
            lists.schedule_conversion,
        )
        self.search = to_raw_response_wrapper(
            lists.search,
        )
        self.update_filters = to_raw_response_wrapper(
            lists.update_filters,
        )
        self.update_name = to_raw_response_wrapper(
            lists.update_name,
        )

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._lists.folders)

    @cached_property
    def mapping(self) -> MappingResourceWithRawResponse:
        return MappingResourceWithRawResponse(self._lists.mapping)

    @cached_property
    def memberships(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self._lists.memberships)


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
        self.delete_schedule_conversion = async_to_raw_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = async_to_raw_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = async_to_raw_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_schedule_conversion = async_to_raw_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.restore = async_to_raw_response_wrapper(
            lists.restore,
        )
        self.schedule_conversion = async_to_raw_response_wrapper(
            lists.schedule_conversion,
        )
        self.search = async_to_raw_response_wrapper(
            lists.search,
        )
        self.update_filters = async_to_raw_response_wrapper(
            lists.update_filters,
        )
        self.update_name = async_to_raw_response_wrapper(
            lists.update_name,
        )

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._lists.folders)

    @cached_property
    def mapping(self) -> AsyncMappingResourceWithRawResponse:
        return AsyncMappingResourceWithRawResponse(self._lists.mapping)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self._lists.memberships)


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
        self.delete_schedule_conversion = to_streamed_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = to_streamed_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = to_streamed_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_schedule_conversion = to_streamed_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.restore = to_streamed_response_wrapper(
            lists.restore,
        )
        self.schedule_conversion = to_streamed_response_wrapper(
            lists.schedule_conversion,
        )
        self.search = to_streamed_response_wrapper(
            lists.search,
        )
        self.update_filters = to_streamed_response_wrapper(
            lists.update_filters,
        )
        self.update_name = to_streamed_response_wrapper(
            lists.update_name,
        )

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._lists.folders)

    @cached_property
    def mapping(self) -> MappingResourceWithStreamingResponse:
        return MappingResourceWithStreamingResponse(self._lists.mapping)

    @cached_property
    def memberships(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self._lists.memberships)


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
        self.delete_schedule_conversion = async_to_streamed_response_wrapper(
            lists.delete_schedule_conversion,
        )
        self.get = async_to_streamed_response_wrapper(
            lists.get,
        )
        self.get_by_object_type_id_and_name = async_to_streamed_response_wrapper(
            lists.get_by_object_type_id_and_name,
        )
        self.get_schedule_conversion = async_to_streamed_response_wrapper(
            lists.get_schedule_conversion,
        )
        self.restore = async_to_streamed_response_wrapper(
            lists.restore,
        )
        self.schedule_conversion = async_to_streamed_response_wrapper(
            lists.schedule_conversion,
        )
        self.search = async_to_streamed_response_wrapper(
            lists.search,
        )
        self.update_filters = async_to_streamed_response_wrapper(
            lists.update_filters,
        )
        self.update_name = async_to_streamed_response_wrapper(
            lists.update_name,
        )

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._lists.folders)

    @cached_property
    def mapping(self) -> AsyncMappingResourceWithStreamingResponse:
        return AsyncMappingResourceWithStreamingResponse(self._lists.mapping)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._lists.memberships)
