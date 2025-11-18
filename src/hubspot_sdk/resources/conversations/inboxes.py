# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.conversations import inbox_get_params, inbox_list_params
from ...types.conversations.public_inbox import PublicInbox

__all__ = ["InboxesResource", "AsyncInboxesResource"]


class InboxesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return InboxesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        default_page_length: int | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicInbox]:
        """
        Retrieve a list of conversations inboxes, with optional filters and sorting.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to include archived inboxes in the response.

          default_page_length: The default number of results to display per page.

          limit: The maximum number of results to display per page.

          sort: Specify the sort order for the inboxes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/inboxes",
            page=SyncPage[PublicInbox],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "default_page_length": default_page_length,
                        "limit": limit,
                        "sort": sort,
                    },
                    inbox_list_params.InboxListParams,
                ),
            ),
            model=PublicInbox,
        )

    def get(
        self,
        inbox_id: int,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicInbox:
        """
        Retrieve details of a single conversations inbox using the inbox ID.

        Args:
          archived: Whether to include archived inboxes in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/conversations/v3/conversations/inboxes/{inbox_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, inbox_get_params.InboxGetParams),
            ),
            cast_to=PublicInbox,
        )


class AsyncInboxesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncInboxesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        default_page_length: int | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicInbox, AsyncPage[PublicInbox]]:
        """
        Retrieve a list of conversations inboxes, with optional filters and sorting.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to include archived inboxes in the response.

          default_page_length: The default number of results to display per page.

          limit: The maximum number of results to display per page.

          sort: Specify the sort order for the inboxes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/inboxes",
            page=AsyncPage[PublicInbox],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "default_page_length": default_page_length,
                        "limit": limit,
                        "sort": sort,
                    },
                    inbox_list_params.InboxListParams,
                ),
            ),
            model=PublicInbox,
        )

    async def get(
        self,
        inbox_id: int,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicInbox:
        """
        Retrieve details of a single conversations inbox using the inbox ID.

        Args:
          archived: Whether to include archived inboxes in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/conversations/v3/conversations/inboxes/{inbox_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, inbox_get_params.InboxGetParams),
            ),
            cast_to=PublicInbox,
        )


class InboxesResourceWithRawResponse:
    def __init__(self, inboxes: InboxesResource) -> None:
        self._inboxes = inboxes

        self.list = to_raw_response_wrapper(
            inboxes.list,
        )
        self.get = to_raw_response_wrapper(
            inboxes.get,
        )


class AsyncInboxesResourceWithRawResponse:
    def __init__(self, inboxes: AsyncInboxesResource) -> None:
        self._inboxes = inboxes

        self.list = async_to_raw_response_wrapper(
            inboxes.list,
        )
        self.get = async_to_raw_response_wrapper(
            inboxes.get,
        )


class InboxesResourceWithStreamingResponse:
    def __init__(self, inboxes: InboxesResource) -> None:
        self._inboxes = inboxes

        self.list = to_streamed_response_wrapper(
            inboxes.list,
        )
        self.get = to_streamed_response_wrapper(
            inboxes.get,
        )


class AsyncInboxesResourceWithStreamingResponse:
    def __init__(self, inboxes: AsyncInboxesResource) -> None:
        self._inboxes = inboxes

        self.list = async_to_streamed_response_wrapper(
            inboxes.list,
        )
        self.get = async_to_streamed_response_wrapper(
            inboxes.get,
        )
