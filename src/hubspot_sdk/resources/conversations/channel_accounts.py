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
from ...types.conversations.conversations_public_channel_account import ConversationsPublicChannelAccount
from ...types.conversations.collection_response_with_total_public_channel_account_forward_paging import (
    CollectionResponseWithTotalPublicChannelAccountForwardPaging,
)

__all__ = ["ChannelAccountsResource", "AsyncChannelAccountsResource"]


class ChannelAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChannelAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ChannelAccountsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicChannelAccountForwardPaging:
        """Retrieve a list of channel accounts, with optional filters and sorting."""
        return self._get(
            "/conversations/v3/conversations/channel-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicChannelAccountForwardPaging,
        )

    def get(
        self,
        channel_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """
        Retrieve details of a single channel account using the channel account ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_account_id:
            raise ValueError(f"Expected a non-empty value for `channel_account_id` but received {channel_account_id!r}")
        return self._get(
            f"/conversations/v3/conversations/channel-accounts/{channel_account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationsPublicChannelAccount,
        )


class AsyncChannelAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncChannelAccountsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicChannelAccountForwardPaging:
        """Retrieve a list of channel accounts, with optional filters and sorting."""
        return await self._get(
            "/conversations/v3/conversations/channel-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicChannelAccountForwardPaging,
        )

    async def get(
        self,
        channel_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """
        Retrieve details of a single channel account using the channel account ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_account_id:
            raise ValueError(f"Expected a non-empty value for `channel_account_id` but received {channel_account_id!r}")
        return await self._get(
            f"/conversations/v3/conversations/channel-accounts/{channel_account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationsPublicChannelAccount,
        )


class ChannelAccountsResourceWithRawResponse:
    def __init__(self, channel_accounts: ChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.list = to_raw_response_wrapper(
            channel_accounts.list,
        )
        self.get = to_raw_response_wrapper(
            channel_accounts.get,
        )


class AsyncChannelAccountsResourceWithRawResponse:
    def __init__(self, channel_accounts: AsyncChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.list = async_to_raw_response_wrapper(
            channel_accounts.list,
        )
        self.get = async_to_raw_response_wrapper(
            channel_accounts.get,
        )


class ChannelAccountsResourceWithStreamingResponse:
    def __init__(self, channel_accounts: ChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.list = to_streamed_response_wrapper(
            channel_accounts.list,
        )
        self.get = to_streamed_response_wrapper(
            channel_accounts.get,
        )


class AsyncChannelAccountsResourceWithStreamingResponse:
    def __init__(self, channel_accounts: AsyncChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.list = async_to_streamed_response_wrapper(
            channel_accounts.list,
        )
        self.get = async_to_streamed_response_wrapper(
            channel_accounts.get,
        )
