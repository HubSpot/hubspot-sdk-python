# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.marketing.collection_response_with_total_public_list import CollectionResponseWithTotalPublicList

__all__ = ["ListAssociationsResource", "AsyncListAssociationsResource"]


class ListAssociationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ListAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ListAssociationsResourceWithStreamingResponse(self)

    def list(
        self,
        marketing_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicList:
        """
        Gets lists associated with a marketing event by marketing event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        return self._get(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{marketing_event_id}/lists",
                marketing_event_id=marketing_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicList,
        )

    def delete(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by marketing event id and ILS list
        id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{marketing_event_id}/lists/{list_id}",
                marketing_event_id=marketing_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def associate(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by marketing event id and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{marketing_event_id}/lists/{list_id}",
                marketing_event_id=marketing_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def associate_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by external account id, external event
        id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by external account id, external
        event id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_by_external_account(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicList:
        """
        Gets lists associated with a marketing event by external account id and external
        event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._get(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{external_account_id}/{external_event_id}/lists",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicList,
        )


class AsyncListAssociationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncListAssociationsResourceWithStreamingResponse(self)

    async def list(
        self,
        marketing_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicList:
        """
        Gets lists associated with a marketing event by marketing event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        return await self._get(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{marketing_event_id}/lists",
                marketing_event_id=marketing_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicList,
        )

    async def delete(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by marketing event id and ILS list
        id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{marketing_event_id}/lists/{list_id}",
                marketing_event_id=marketing_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def associate(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by marketing event id and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{marketing_event_id}/lists/{list_id}",
                marketing_event_id=marketing_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def associate_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by external account id, external event
        id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by external account id, external
        event id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
                list_id=list_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_by_external_account(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicList:
        """
        Gets lists associated with a marketing event by external account id and external
        event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._get(
            path_template(
                "/marketing/marketing-events/2026-03/associations/{external_account_id}/{external_event_id}/lists",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicList,
        )


class ListAssociationsResourceWithRawResponse:
    def __init__(self, list_associations: ListAssociationsResource) -> None:
        self._list_associations = list_associations

        self.list = to_raw_response_wrapper(
            list_associations.list,
        )
        self.delete = to_raw_response_wrapper(
            list_associations.delete,
        )
        self.associate = to_raw_response_wrapper(
            list_associations.associate,
        )
        self.associate_by_external_account = to_raw_response_wrapper(
            list_associations.associate_by_external_account,
        )
        self.delete_by_external_account = to_raw_response_wrapper(
            list_associations.delete_by_external_account,
        )
        self.list_by_external_account = to_raw_response_wrapper(
            list_associations.list_by_external_account,
        )


class AsyncListAssociationsResourceWithRawResponse:
    def __init__(self, list_associations: AsyncListAssociationsResource) -> None:
        self._list_associations = list_associations

        self.list = async_to_raw_response_wrapper(
            list_associations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            list_associations.delete,
        )
        self.associate = async_to_raw_response_wrapper(
            list_associations.associate,
        )
        self.associate_by_external_account = async_to_raw_response_wrapper(
            list_associations.associate_by_external_account,
        )
        self.delete_by_external_account = async_to_raw_response_wrapper(
            list_associations.delete_by_external_account,
        )
        self.list_by_external_account = async_to_raw_response_wrapper(
            list_associations.list_by_external_account,
        )


class ListAssociationsResourceWithStreamingResponse:
    def __init__(self, list_associations: ListAssociationsResource) -> None:
        self._list_associations = list_associations

        self.list = to_streamed_response_wrapper(
            list_associations.list,
        )
        self.delete = to_streamed_response_wrapper(
            list_associations.delete,
        )
        self.associate = to_streamed_response_wrapper(
            list_associations.associate,
        )
        self.associate_by_external_account = to_streamed_response_wrapper(
            list_associations.associate_by_external_account,
        )
        self.delete_by_external_account = to_streamed_response_wrapper(
            list_associations.delete_by_external_account,
        )
        self.list_by_external_account = to_streamed_response_wrapper(
            list_associations.list_by_external_account,
        )


class AsyncListAssociationsResourceWithStreamingResponse:
    def __init__(self, list_associations: AsyncListAssociationsResource) -> None:
        self._list_associations = list_associations

        self.list = async_to_streamed_response_wrapper(
            list_associations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            list_associations.delete,
        )
        self.associate = async_to_streamed_response_wrapper(
            list_associations.associate,
        )
        self.associate_by_external_account = async_to_streamed_response_wrapper(
            list_associations.associate_by_external_account,
        )
        self.delete_by_external_account = async_to_streamed_response_wrapper(
            list_associations.delete_by_external_account,
        )
        self.list_by_external_account = async_to_streamed_response_wrapper(
            list_associations.list_by_external_account,
        )
