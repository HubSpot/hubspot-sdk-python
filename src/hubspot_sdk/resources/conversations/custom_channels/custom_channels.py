# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from .channel_accounts import (
    ChannelAccountsResource,
    AsyncChannelAccountsResource,
    ChannelAccountsResourceWithRawResponse,
    AsyncChannelAccountsResourceWithRawResponse,
    ChannelAccountsResourceWithStreamingResponse,
    AsyncChannelAccountsResourceWithStreamingResponse,
)
from ....types.conversations import custom_channel_create_params, custom_channel_update_params
from .channel_account_staging_tokens import (
    ChannelAccountStagingTokensResource,
    AsyncChannelAccountStagingTokensResource,
    ChannelAccountStagingTokensResourceWithRawResponse,
    AsyncChannelAccountStagingTokensResourceWithRawResponse,
    ChannelAccountStagingTokensResourceWithStreamingResponse,
    AsyncChannelAccountStagingTokensResourceWithStreamingResponse,
)
from ....types.conversations.custom_channel_get_response import CustomChannelGetResponse
from ....types.conversations.custom_channel_list_response import CustomChannelListResponse
from ....types.conversations.custom_channel_create_response import CustomChannelCreateResponse
from ....types.conversations.custom_channel_update_response import CustomChannelUpdateResponse

__all__ = ["CustomChannelsResource", "AsyncCustomChannelsResource"]


class CustomChannelsResource(SyncAPIResource):
    @cached_property
    def channel_account_staging_tokens(self) -> ChannelAccountStagingTokensResource:
        return ChannelAccountStagingTokensResource(self._client)

    @cached_property
    def channel_accounts(self) -> ChannelAccountsResource:
        return ChannelAccountsResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CustomChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CustomChannelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        capabilities: Dict[str, object],
        name: str,
        channel_account_connection_redirect_url: str | Omit = omit,
        channel_description: str | Omit = omit,
        channel_logo_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelCreateResponse:
        """
        Register a new channel along with its capabilities and the webhook url that will
        be used to receive messages published over the channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conversations/v3/custom-channels/",
            body=maybe_transform(
                {
                    "capabilities": capabilities,
                    "name": name,
                    "channel_account_connection_redirect_url": channel_account_connection_redirect_url,
                    "channel_description": channel_description,
                    "channel_logo_url": channel_logo_url,
                    "webhook_url": webhook_url,
                },
                custom_channel_create_params.CustomChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelCreateResponse,
        )

    def update(
        self,
        channel_id: str,
        *,
        capabilities: Dict[str, object],
        channel_description: object,
        channel_logo_url: object,
        channel_account_connection_redirect_url: object | Omit = omit,
        name: object | Omit = omit,
        webhook_url: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelUpdateResponse:
        """Update the capabilities for an existing.

        You can also use it to update the
        channel's webhookUri and its channelAccountConnectionRedirectUrl.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._patch(
            f"/conversations/v3/custom-channels/{channel_id}",
            body=maybe_transform(
                {
                    "capabilities": capabilities,
                    "channel_description": channel_description,
                    "channel_logo_url": channel_logo_url,
                    "channel_account_connection_redirect_url": channel_account_connection_redirect_url,
                    "name": name,
                    "webhook_url": webhook_url,
                },
                custom_channel_update_params.CustomChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelListResponse:
        """Retrieve all custom channels associated with the app."""
        return self._get(
            "/conversations/v3/custom-channels/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelListResponse,
        )

    def delete(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive an existing registered custom channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/conversations/v3/custom-channels/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelGetResponse:
        """Retrieve the details about a custom channel.

        This API allows you to see a custom
        channel's current capabilties and other configuration metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/conversations/v3/custom-channels/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelGetResponse,
        )


class AsyncCustomChannelsResource(AsyncAPIResource):
    @cached_property
    def channel_account_staging_tokens(self) -> AsyncChannelAccountStagingTokensResource:
        return AsyncChannelAccountStagingTokensResource(self._client)

    @cached_property
    def channel_accounts(self) -> AsyncChannelAccountsResource:
        return AsyncChannelAccountsResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCustomChannelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        capabilities: Dict[str, object],
        name: str,
        channel_account_connection_redirect_url: str | Omit = omit,
        channel_description: str | Omit = omit,
        channel_logo_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelCreateResponse:
        """
        Register a new channel along with its capabilities and the webhook url that will
        be used to receive messages published over the channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conversations/v3/custom-channels/",
            body=await async_maybe_transform(
                {
                    "capabilities": capabilities,
                    "name": name,
                    "channel_account_connection_redirect_url": channel_account_connection_redirect_url,
                    "channel_description": channel_description,
                    "channel_logo_url": channel_logo_url,
                    "webhook_url": webhook_url,
                },
                custom_channel_create_params.CustomChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelCreateResponse,
        )

    async def update(
        self,
        channel_id: str,
        *,
        capabilities: Dict[str, object],
        channel_description: object,
        channel_logo_url: object,
        channel_account_connection_redirect_url: object | Omit = omit,
        name: object | Omit = omit,
        webhook_url: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelUpdateResponse:
        """Update the capabilities for an existing.

        You can also use it to update the
        channel's webhookUri and its channelAccountConnectionRedirectUrl.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._patch(
            f"/conversations/v3/custom-channels/{channel_id}",
            body=await async_maybe_transform(
                {
                    "capabilities": capabilities,
                    "channel_description": channel_description,
                    "channel_logo_url": channel_logo_url,
                    "channel_account_connection_redirect_url": channel_account_connection_redirect_url,
                    "name": name,
                    "webhook_url": webhook_url,
                },
                custom_channel_update_params.CustomChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelListResponse:
        """Retrieve all custom channels associated with the app."""
        return await self._get(
            "/conversations/v3/custom-channels/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelListResponse,
        )

    async def delete(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive an existing registered custom channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/conversations/v3/custom-channels/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomChannelGetResponse:
        """Retrieve the details about a custom channel.

        This API allows you to see a custom
        channel's current capabilties and other configuration metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/conversations/v3/custom-channels/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomChannelGetResponse,
        )


class CustomChannelsResourceWithRawResponse:
    def __init__(self, custom_channels: CustomChannelsResource) -> None:
        self._custom_channels = custom_channels

        self.create = to_raw_response_wrapper(
            custom_channels.create,
        )
        self.update = to_raw_response_wrapper(
            custom_channels.update,
        )
        self.list = to_raw_response_wrapper(
            custom_channels.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_channels.delete,
        )
        self.get = to_raw_response_wrapper(
            custom_channels.get,
        )

    @cached_property
    def channel_account_staging_tokens(self) -> ChannelAccountStagingTokensResourceWithRawResponse:
        return ChannelAccountStagingTokensResourceWithRawResponse(self._custom_channels.channel_account_staging_tokens)

    @cached_property
    def channel_accounts(self) -> ChannelAccountsResourceWithRawResponse:
        return ChannelAccountsResourceWithRawResponse(self._custom_channels.channel_accounts)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._custom_channels.messages)


class AsyncCustomChannelsResourceWithRawResponse:
    def __init__(self, custom_channels: AsyncCustomChannelsResource) -> None:
        self._custom_channels = custom_channels

        self.create = async_to_raw_response_wrapper(
            custom_channels.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_channels.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_channels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_channels.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom_channels.get,
        )

    @cached_property
    def channel_account_staging_tokens(self) -> AsyncChannelAccountStagingTokensResourceWithRawResponse:
        return AsyncChannelAccountStagingTokensResourceWithRawResponse(
            self._custom_channels.channel_account_staging_tokens
        )

    @cached_property
    def channel_accounts(self) -> AsyncChannelAccountsResourceWithRawResponse:
        return AsyncChannelAccountsResourceWithRawResponse(self._custom_channels.channel_accounts)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._custom_channels.messages)


class CustomChannelsResourceWithStreamingResponse:
    def __init__(self, custom_channels: CustomChannelsResource) -> None:
        self._custom_channels = custom_channels

        self.create = to_streamed_response_wrapper(
            custom_channels.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_channels.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_channels.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_channels.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom_channels.get,
        )

    @cached_property
    def channel_account_staging_tokens(self) -> ChannelAccountStagingTokensResourceWithStreamingResponse:
        return ChannelAccountStagingTokensResourceWithStreamingResponse(
            self._custom_channels.channel_account_staging_tokens
        )

    @cached_property
    def channel_accounts(self) -> ChannelAccountsResourceWithStreamingResponse:
        return ChannelAccountsResourceWithStreamingResponse(self._custom_channels.channel_accounts)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._custom_channels.messages)


class AsyncCustomChannelsResourceWithStreamingResponse:
    def __init__(self, custom_channels: AsyncCustomChannelsResource) -> None:
        self._custom_channels = custom_channels

        self.create = async_to_streamed_response_wrapper(
            custom_channels.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_channels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_channels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_channels.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_channels.get,
        )

    @cached_property
    def channel_account_staging_tokens(self) -> AsyncChannelAccountStagingTokensResourceWithStreamingResponse:
        return AsyncChannelAccountStagingTokensResourceWithStreamingResponse(
            self._custom_channels.channel_account_staging_tokens
        )

    @cached_property
    def channel_accounts(self) -> AsyncChannelAccountsResourceWithStreamingResponse:
        return AsyncChannelAccountsResourceWithStreamingResponse(self._custom_channels.channel_accounts)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._custom_channels.messages)
