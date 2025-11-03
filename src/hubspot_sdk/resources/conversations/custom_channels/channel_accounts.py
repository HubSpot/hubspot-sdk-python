# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.conversations.custom_channels import channel_account_create_params, channel_account_update_params
from ....types.conversations.public_delivery_identifier_param import PublicDeliveryIdentifierParam
from ....types.conversations.conversations_public_channel_account import ConversationsPublicChannelAccount
from ....types.conversations.collection_response_with_total_public_channel_account_forward_paging import (
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

    def create(
        self,
        channel_id: str,
        *,
        authorized: bool,
        inbox_id: str,
        name: str,
        delivery_identifier: PublicDeliveryIdentifierParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """Create a new account for a channel.

        Multiple accounts can communicate over a
        single channel using different delivery identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._post(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts",
            body=maybe_transform(
                {
                    "authorized": authorized,
                    "inbox_id": inbox_id,
                    "name": name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_create_params.ChannelAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationsPublicChannelAccount,
        )

    def update(
        self,
        channel_account_id: str,
        *,
        channel_id: str,
        authorized: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """
        This API is used to update the name of the channel account and it's isAuthorized
        status. Setting to isAuthorized flag to False disables the channel account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not channel_account_id:
            raise ValueError(f"Expected a non-empty value for `channel_account_id` but received {channel_account_id!r}")
        return self._patch(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts/{channel_account_id}",
            body=maybe_transform(
                {
                    "authorized": authorized,
                    "name": name,
                },
                channel_account_update_params.ChannelAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationsPublicChannelAccount,
        )

    def list(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicChannelAccountForwardPaging:
        """
        Retrieve a list of accounts for a custom channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicChannelAccountForwardPaging,
        )

    def get(
        self,
        channel_account_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """Retrieve the details for a specific channel account.

        This contains all the
        metadata about your channel account, including its channel, associated inbox id,
        and delivery identifier information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not channel_account_id:
            raise ValueError(f"Expected a non-empty value for `channel_account_id` but received {channel_account_id!r}")
        return self._get(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts/{channel_account_id}",
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

    async def create(
        self,
        channel_id: str,
        *,
        authorized: bool,
        inbox_id: str,
        name: str,
        delivery_identifier: PublicDeliveryIdentifierParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """Create a new account for a channel.

        Multiple accounts can communicate over a
        single channel using different delivery identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._post(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts",
            body=await async_maybe_transform(
                {
                    "authorized": authorized,
                    "inbox_id": inbox_id,
                    "name": name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_create_params.ChannelAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationsPublicChannelAccount,
        )

    async def update(
        self,
        channel_account_id: str,
        *,
        channel_id: str,
        authorized: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """
        This API is used to update the name of the channel account and it's isAuthorized
        status. Setting to isAuthorized flag to False disables the channel account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not channel_account_id:
            raise ValueError(f"Expected a non-empty value for `channel_account_id` but received {channel_account_id!r}")
        return await self._patch(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts/{channel_account_id}",
            body=await async_maybe_transform(
                {
                    "authorized": authorized,
                    "name": name,
                },
                channel_account_update_params.ChannelAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationsPublicChannelAccount,
        )

    async def list(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicChannelAccountForwardPaging:
        """
        Retrieve a list of accounts for a custom channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicChannelAccountForwardPaging,
        )

    async def get(
        self,
        channel_account_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationsPublicChannelAccount:
        """Retrieve the details for a specific channel account.

        This contains all the
        metadata about your channel account, including its channel, associated inbox id,
        and delivery identifier information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not channel_account_id:
            raise ValueError(f"Expected a non-empty value for `channel_account_id` but received {channel_account_id!r}")
        return await self._get(
            f"/conversations/v3/custom-channels/{channel_id}/channel-accounts/{channel_account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationsPublicChannelAccount,
        )


class ChannelAccountsResourceWithRawResponse:
    def __init__(self, channel_accounts: ChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = to_raw_response_wrapper(
            channel_accounts.create,
        )
        self.update = to_raw_response_wrapper(
            channel_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            channel_accounts.list,
        )
        self.get = to_raw_response_wrapper(
            channel_accounts.get,
        )


class AsyncChannelAccountsResourceWithRawResponse:
    def __init__(self, channel_accounts: AsyncChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = async_to_raw_response_wrapper(
            channel_accounts.create,
        )
        self.update = async_to_raw_response_wrapper(
            channel_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            channel_accounts.list,
        )
        self.get = async_to_raw_response_wrapper(
            channel_accounts.get,
        )


class ChannelAccountsResourceWithStreamingResponse:
    def __init__(self, channel_accounts: ChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = to_streamed_response_wrapper(
            channel_accounts.create,
        )
        self.update = to_streamed_response_wrapper(
            channel_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            channel_accounts.list,
        )
        self.get = to_streamed_response_wrapper(
            channel_accounts.get,
        )


class AsyncChannelAccountsResourceWithStreamingResponse:
    def __init__(self, channel_accounts: AsyncChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = async_to_streamed_response_wrapper(
            channel_accounts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            channel_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            channel_accounts.list,
        )
        self.get = async_to_streamed_response_wrapper(
            channel_accounts.get,
        )
