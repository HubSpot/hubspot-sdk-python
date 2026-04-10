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
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from .channel_accounts import (
    ChannelAccountsResource,
    AsyncChannelAccountsResource,
    ChannelAccountsResourceWithRawResponse,
    AsyncChannelAccountsResourceWithRawResponse,
    ChannelAccountsResourceWithStreamingResponse,
    AsyncChannelAccountsResourceWithStreamingResponse,
)
from ....types.conversations import (
    custom_channel_get_params,
    custom_channel_list_params,
    custom_channel_create_params,
    custom_channel_update_params,
)
from ....types.conversations.public_channel_account import PublicChannelAccount
from ....types.conversations.public_channel_integration_channel import PublicChannelIntegrationChannel

__all__ = ["CustomChannelsResource", "AsyncCustomChannelsResource"]


class CustomChannelsResource(SyncAPIResource):
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

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CustomChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
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
    ) -> PublicChannelIntegrationChannel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conversations/custom-channels/2026-03",
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
            cast_to=PublicChannelIntegrationChannel,
        )

    def update(
        self,
        channel_id: int,
        *,
        capabilities: Dict[str, object],
        channel_account_connection_redirect_url: object,
        channel_description: object,
        channel_logo_url: object,
        name: object,
        webhook_url: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelIntegrationChannel:
        """Update the capabilities for an existing.

        You can also use it to update the
        channel's webhookUri and its channelAccountConnectionRedirectUrl.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/conversations/custom-channels/2026-03/{channel_id}", channel_id=channel_id),
            body=maybe_transform(
                {
                    "capabilities": capabilities,
                    "channel_account_connection_redirect_url": channel_account_connection_redirect_url,
                    "channel_description": channel_description,
                    "channel_logo_url": channel_logo_url,
                    "name": name,
                    "webhook_url": webhook_url,
                },
                custom_channel_update_params.CustomChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelIntegrationChannel,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        default_page_length: int | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicChannelIntegrationChannel]:
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
        return self._get_api_list(
            "/conversations/custom-channels/2026-03",
            page=SyncPage[PublicChannelIntegrationChannel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "default_page_length": default_page_length,
                        "limit": limit,
                        "sort": sort,
                    },
                    custom_channel_list_params.CustomChannelListParams,
                ),
            ),
            model=PublicChannelIntegrationChannel,
        )

    def delete(
        self,
        channel_id: int,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/conversations/custom-channels/2026-03/{channel_id}", channel_id=channel_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        channel_account_id: int,
        *,
        channel_id: int,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """Retrieve the details for a specific channel account.

        This contains all the
        metadata about your channel account, including its channel, associated inbox id,
        and delivery identifier information.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts/{channel_account_id}",
                channel_id=channel_id,
                channel_account_id=channel_account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, custom_channel_get_params.CustomChannelGetParams),
            ),
            cast_to=PublicChannelAccount,
        )


class AsyncCustomChannelsResource(AsyncAPIResource):
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

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
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
    ) -> PublicChannelIntegrationChannel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conversations/custom-channels/2026-03",
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
            cast_to=PublicChannelIntegrationChannel,
        )

    async def update(
        self,
        channel_id: int,
        *,
        capabilities: Dict[str, object],
        channel_account_connection_redirect_url: object,
        channel_description: object,
        channel_logo_url: object,
        name: object,
        webhook_url: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelIntegrationChannel:
        """Update the capabilities for an existing.

        You can also use it to update the
        channel's webhookUri and its channelAccountConnectionRedirectUrl.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/conversations/custom-channels/2026-03/{channel_id}", channel_id=channel_id),
            body=await async_maybe_transform(
                {
                    "capabilities": capabilities,
                    "channel_account_connection_redirect_url": channel_account_connection_redirect_url,
                    "channel_description": channel_description,
                    "channel_logo_url": channel_logo_url,
                    "name": name,
                    "webhook_url": webhook_url,
                },
                custom_channel_update_params.CustomChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelIntegrationChannel,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        default_page_length: int | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicChannelIntegrationChannel, AsyncPage[PublicChannelIntegrationChannel]]:
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
        return self._get_api_list(
            "/conversations/custom-channels/2026-03",
            page=AsyncPage[PublicChannelIntegrationChannel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "default_page_length": default_page_length,
                        "limit": limit,
                        "sort": sort,
                    },
                    custom_channel_list_params.CustomChannelListParams,
                ),
            ),
            model=PublicChannelIntegrationChannel,
        )

    async def delete(
        self,
        channel_id: int,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/conversations/custom-channels/2026-03/{channel_id}", channel_id=channel_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        channel_account_id: int,
        *,
        channel_id: int,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """Retrieve the details for a specific channel account.

        This contains all the
        metadata about your channel account, including its channel, associated inbox id,
        and delivery identifier information.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts/{channel_account_id}",
                channel_id=channel_id,
                channel_account_id=channel_account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, custom_channel_get_params.CustomChannelGetParams
                ),
            ),
            cast_to=PublicChannelAccount,
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
    def channel_accounts(self) -> AsyncChannelAccountsResourceWithStreamingResponse:
        return AsyncChannelAccountsResourceWithStreamingResponse(self._custom_channels.channel_accounts)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._custom_channels.messages)
