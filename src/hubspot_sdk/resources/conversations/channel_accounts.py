# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.conversations import channel_account_get_params, channel_account_list_params
from ...types.conversations.public_channel_account import PublicChannelAccount

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
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        channel_id: Iterable[int] | Omit = omit,
        default_page_length: int | Omit = omit,
        inbox_id: Iterable[int] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicChannelAccount]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/channel-accounts",
            page=SyncPage[PublicChannelAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "channel_id": channel_id,
                        "default_page_length": default_page_length,
                        "inbox_id": inbox_id,
                        "limit": limit,
                        "sort": sort,
                    },
                    channel_account_list_params.ChannelAccountListParams,
                ),
            ),
            model=PublicChannelAccount,
        )

    def get(
        self,
        channel_account_id: int,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/conversations/v3/conversations/channel-accounts/{channel_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, channel_account_get_params.ChannelAccountGetParams),
            ),
            cast_to=PublicChannelAccount,
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

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        channel_id: Iterable[int] | Omit = omit,
        default_page_length: int | Omit = omit,
        inbox_id: Iterable[int] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicChannelAccount, AsyncPage[PublicChannelAccount]]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/channel-accounts",
            page=AsyncPage[PublicChannelAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "channel_id": channel_id,
                        "default_page_length": default_page_length,
                        "inbox_id": inbox_id,
                        "limit": limit,
                        "sort": sort,
                    },
                    channel_account_list_params.ChannelAccountListParams,
                ),
            ),
            model=PublicChannelAccount,
        )

    async def get(
        self,
        channel_account_id: int,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/conversations/v3/conversations/channel-accounts/{channel_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, channel_account_get_params.ChannelAccountGetParams
                ),
            ),
            cast_to=PublicChannelAccount,
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
