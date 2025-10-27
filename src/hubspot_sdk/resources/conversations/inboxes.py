# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.conversations.public_inbox import PublicInbox
from ...types.conversations.collection_response_with_total_public_inbox_forward_paging import (
    CollectionResponseWithTotalPublicInboxForwardPaging,
)

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicInboxForwardPaging:
        """Retrieve a list of conversations inboxes, with optional filters and sorting."""
        return self._get(
            "/conversations/v3/conversations/inboxes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicInboxForwardPaging,
        )

    def get(
        self,
        inbox_id: str,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._get(
            f"/conversations/v3/conversations/inboxes/{inbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicInboxForwardPaging:
        """Retrieve a list of conversations inboxes, with optional filters and sorting."""
        return await self._get(
            "/conversations/v3/conversations/inboxes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicInboxForwardPaging,
        )

    async def get(
        self,
        inbox_id: str,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return await self._get(
            f"/conversations/v3/conversations/inboxes/{inbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
