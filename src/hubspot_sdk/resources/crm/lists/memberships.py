# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.crm.lists import (
    membership_list_params,
    membership_add_and_remove_params,
    membership_get_page_ordered_by_added_to_list_date_params,
)
from ....types.crm.join_time_and_record_id import JoinTimeAndRecordID
from ....types.crm.memberships_update_response import MembershipsUpdateResponse
from ....types.crm.api_collection_response_record_list_membership_no_paging import (
    APICollectionResponseRecordListMembershipNoPaging,
)

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MembershipsResourceWithStreamingResponse(self)

    def list(
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
        Fetch the memberships of a list in order sorted by the `recordId` of the records
        in the list.

        The `recordId`s are sorted in _ascending_ order if an `after` offset or no
        offset is provided. If only a `before` offset is provided, then the records are
        sorted in _descending_ order.

        The `after` offset parameter will take precedence over the `before` offset in a
        case where both are provided.

        Args:
          after: The paging offset token for the page that comes `after` the previously requested
              records.

              If provided, then the records in the response will be the records following the
              offset, sorted in _ascending_ order. Takes precedence over the `before` offset.

          before: The paging offset token for the page that comes `before` the previously
              requested records.

              If provided, then the records in the response will be the records preceding the
              offset, sorted in _descending_ order.

          limit: The number of records to return in the response. The maximum `limit` is 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            f"/crm/v3/lists/{list_id}/memberships",
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
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    def add(
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
        """Add the records provided to the list.

        Records that do not exist or that are
        already members of the list are ignored.

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/crm/v3/lists/{list_id}/memberships/add",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    def add_all_from_list(
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
        Add all of the records from a _source list_ (specified by the `sourceListId`) to
        a _destination list_ (specified by the `listId`). Records that are already
        members of the _destination list_ will be ignored. The _destination_ and _source
        list_ IDs must be different. The _destination_ and _source lists_ must contain
        records of the same type (e.g. contacts, companies, etc.).

        This endpoint only works for _destination lists_ that have a `processingType` of
        `MANUAL` or `SNAPSHOT`. The _source list_ can have any `processingType`.

        This endpoint only supports a `sourceListId` for lists with less than 100,000
        memberships.

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
            f"/crm/v3/lists/{list_id}/memberships/add-from/{source_list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_and_remove(
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
        Add and/or remove records that have already been created in the system to and/or
        from a list.

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/crm/v3/lists/{list_id}/memberships/add-and-remove",
            body=maybe_transform(
                {
                    "record_ids_to_add": record_ids_to_add,
                    "record_ids_to_remove": record_ids_to_remove,
                },
                membership_add_and_remove_params.MembershipAddAndRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    def get_lists(
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
    ) -> APICollectionResponseRecordListMembershipNoPaging:
        """
        For given record provide lists this record is member of.

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
            f"/crm/v3/lists/records/{object_type_id}/{record_id}/memberships",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APICollectionResponseRecordListMembershipNoPaging,
        )

    def get_page_ordered_by_added_to_list_date(
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
        Fetch the memberships of a list in order sorted by the time the records were
        added to the list.

        The `recordId`s are sorted in _ascending_ order if an `after` offset or no
        offset is provided. If only a `before` offset is provided, then the records are
        sorted in _descending_ order.

        The `after` offset parameter will take precedence over the `before` offset in a
        case where both are provided.

        Args:
          after: The paging offset token for the page that comes `after` the previously requested
              records.

              If provided, then the records in the response will be the records following the
              offset, sorted in _ascending_ order. Takes precedence over the `before` offset.

          before: The paging offset token for the page that comes `before` the previously
              requested records.

              If provided, then the records in the response will be the records preceding the
              offset, sorted in _descending_ order.

          limit: The number of records to return in the response. The maximum `limit` is 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            f"/crm/v3/lists/{list_id}/memberships/join-order",
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
                    membership_get_page_ordered_by_added_to_list_date_params.MembershipGetPageOrderedByAddedToListDateParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    def remove(
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
        """Remove the records provided from the list.

        Records that do not exist or that are
        not members of the list are ignored.

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/crm/v3/lists/{list_id}/memberships/remove",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    def remove_all(
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
        """Remove **all** of the records from a list.

        **_Note:_** _The list is not
        deleted._

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        This endpoint only supports lists that have less than 100,000 memberships.

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
            f"/crm/v3/lists/{list_id}/memberships",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMembershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMembershipsResourceWithStreamingResponse(self)

    def list(
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
        Fetch the memberships of a list in order sorted by the `recordId` of the records
        in the list.

        The `recordId`s are sorted in _ascending_ order if an `after` offset or no
        offset is provided. If only a `before` offset is provided, then the records are
        sorted in _descending_ order.

        The `after` offset parameter will take precedence over the `before` offset in a
        case where both are provided.

        Args:
          after: The paging offset token for the page that comes `after` the previously requested
              records.

              If provided, then the records in the response will be the records following the
              offset, sorted in _ascending_ order. Takes precedence over the `before` offset.

          before: The paging offset token for the page that comes `before` the previously
              requested records.

              If provided, then the records in the response will be the records preceding the
              offset, sorted in _descending_ order.

          limit: The number of records to return in the response. The maximum `limit` is 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            f"/crm/v3/lists/{list_id}/memberships",
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
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    async def add(
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
        """Add the records provided to the list.

        Records that do not exist or that are
        already members of the list are ignored.

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/crm/v3/lists/{list_id}/memberships/add",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    async def add_all_from_list(
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
        Add all of the records from a _source list_ (specified by the `sourceListId`) to
        a _destination list_ (specified by the `listId`). Records that are already
        members of the _destination list_ will be ignored. The _destination_ and _source
        list_ IDs must be different. The _destination_ and _source lists_ must contain
        records of the same type (e.g. contacts, companies, etc.).

        This endpoint only works for _destination lists_ that have a `processingType` of
        `MANUAL` or `SNAPSHOT`. The _source list_ can have any `processingType`.

        This endpoint only supports a `sourceListId` for lists with less than 100,000
        memberships.

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
            f"/crm/v3/lists/{list_id}/memberships/add-from/{source_list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_and_remove(
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
        Add and/or remove records that have already been created in the system to and/or
        from a list.

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/crm/v3/lists/{list_id}/memberships/add-and-remove",
            body=await async_maybe_transform(
                {
                    "record_ids_to_add": record_ids_to_add,
                    "record_ids_to_remove": record_ids_to_remove,
                },
                membership_add_and_remove_params.MembershipAddAndRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    async def get_lists(
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
    ) -> APICollectionResponseRecordListMembershipNoPaging:
        """
        For given record provide lists this record is member of.

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
            f"/crm/v3/lists/records/{object_type_id}/{record_id}/memberships",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APICollectionResponseRecordListMembershipNoPaging,
        )

    def get_page_ordered_by_added_to_list_date(
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
        Fetch the memberships of a list in order sorted by the time the records were
        added to the list.

        The `recordId`s are sorted in _ascending_ order if an `after` offset or no
        offset is provided. If only a `before` offset is provided, then the records are
        sorted in _descending_ order.

        The `after` offset parameter will take precedence over the `before` offset in a
        case where both are provided.

        Args:
          after: The paging offset token for the page that comes `after` the previously requested
              records.

              If provided, then the records in the response will be the records following the
              offset, sorted in _ascending_ order. Takes precedence over the `before` offset.

          before: The paging offset token for the page that comes `before` the previously
              requested records.

              If provided, then the records in the response will be the records preceding the
              offset, sorted in _descending_ order.

          limit: The number of records to return in the response. The maximum `limit` is 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            f"/crm/v3/lists/{list_id}/memberships/join-order",
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
                    membership_get_page_ordered_by_added_to_list_date_params.MembershipGetPageOrderedByAddedToListDateParams,
                ),
            ),
            model=JoinTimeAndRecordID,
        )

    async def remove(
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
        """Remove the records provided from the list.

        Records that do not exist or that are
        not members of the list are ignored.

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/crm/v3/lists/{list_id}/memberships/remove",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipsUpdateResponse,
        )

    async def remove_all(
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
        """Remove **all** of the records from a list.

        **_Note:_** _The list is not
        deleted._

        This endpoint only works for lists that have a `processingType` of `MANUAL` or
        `SNAPSHOT`.

        This endpoint only supports lists that have less than 100,000 memberships.

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
            f"/crm/v3/lists/{list_id}/memberships",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.list = to_raw_response_wrapper(
            memberships.list,
        )
        self.add = to_raw_response_wrapper(
            memberships.add,
        )
        self.add_all_from_list = to_raw_response_wrapper(
            memberships.add_all_from_list,
        )
        self.add_and_remove = to_raw_response_wrapper(
            memberships.add_and_remove,
        )
        self.get_lists = to_raw_response_wrapper(
            memberships.get_lists,
        )
        self.get_page_ordered_by_added_to_list_date = to_raw_response_wrapper(
            memberships.get_page_ordered_by_added_to_list_date,
        )
        self.remove = to_raw_response_wrapper(
            memberships.remove,
        )
        self.remove_all = to_raw_response_wrapper(
            memberships.remove_all,
        )


class AsyncMembershipsResourceWithRawResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.list = async_to_raw_response_wrapper(
            memberships.list,
        )
        self.add = async_to_raw_response_wrapper(
            memberships.add,
        )
        self.add_all_from_list = async_to_raw_response_wrapper(
            memberships.add_all_from_list,
        )
        self.add_and_remove = async_to_raw_response_wrapper(
            memberships.add_and_remove,
        )
        self.get_lists = async_to_raw_response_wrapper(
            memberships.get_lists,
        )
        self.get_page_ordered_by_added_to_list_date = async_to_raw_response_wrapper(
            memberships.get_page_ordered_by_added_to_list_date,
        )
        self.remove = async_to_raw_response_wrapper(
            memberships.remove,
        )
        self.remove_all = async_to_raw_response_wrapper(
            memberships.remove_all,
        )


class MembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.list = to_streamed_response_wrapper(
            memberships.list,
        )
        self.add = to_streamed_response_wrapper(
            memberships.add,
        )
        self.add_all_from_list = to_streamed_response_wrapper(
            memberships.add_all_from_list,
        )
        self.add_and_remove = to_streamed_response_wrapper(
            memberships.add_and_remove,
        )
        self.get_lists = to_streamed_response_wrapper(
            memberships.get_lists,
        )
        self.get_page_ordered_by_added_to_list_date = to_streamed_response_wrapper(
            memberships.get_page_ordered_by_added_to_list_date,
        )
        self.remove = to_streamed_response_wrapper(
            memberships.remove,
        )
        self.remove_all = to_streamed_response_wrapper(
            memberships.remove_all,
        )


class AsyncMembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.list = async_to_streamed_response_wrapper(
            memberships.list,
        )
        self.add = async_to_streamed_response_wrapper(
            memberships.add,
        )
        self.add_all_from_list = async_to_streamed_response_wrapper(
            memberships.add_all_from_list,
        )
        self.add_and_remove = async_to_streamed_response_wrapper(
            memberships.add_and_remove,
        )
        self.get_lists = async_to_streamed_response_wrapper(
            memberships.get_lists,
        )
        self.get_page_ordered_by_added_to_list_date = async_to_streamed_response_wrapper(
            memberships.get_page_ordered_by_added_to_list_date,
        )
        self.remove = async_to_streamed_response_wrapper(
            memberships.remove,
        )
        self.remove_all = async_to_streamed_response_wrapper(
            memberships.remove_all,
        )
