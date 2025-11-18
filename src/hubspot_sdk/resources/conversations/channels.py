# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
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
from ...types.conversations import channel_list_params
from ...types.conversations.public_channel import PublicChannel

__all__ = ["ChannelsResource", "AsyncChannelsResource"]


class ChannelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ChannelsResourceWithStreamingResponse(self)

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
    ) -> SyncPage[PublicChannel]:
        """
        Retrieve a list of channels, with optional filters and sorting.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          default_page_length: The default number of results to display per page.

          limit: The maximum number of results to display per page.

          sort: Specify the sort order for the channels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/channels",
            page=SyncPage[PublicChannel],
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
                    channel_list_params.ChannelListParams,
                ),
            ),
            model=PublicChannel,
        )

    def get(
        self,
        channel_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannel:
        """
        Retrieve details of a single channel using the channel ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/conversations/v3/conversations/channels/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannel,
        )


class AsyncChannelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncChannelsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[PublicChannel, AsyncPage[PublicChannel]]:
        """
        Retrieve a list of channels, with optional filters and sorting.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          default_page_length: The default number of results to display per page.

          limit: The maximum number of results to display per page.

          sort: Specify the sort order for the channels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/channels",
            page=AsyncPage[PublicChannel],
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
                    channel_list_params.ChannelListParams,
                ),
            ),
            model=PublicChannel,
        )

    async def get(
        self,
        channel_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannel:
        """
        Retrieve details of a single channel using the channel ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/conversations/v3/conversations/channels/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannel,
        )


class ChannelsResourceWithRawResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.list = to_raw_response_wrapper(
            channels.list,
        )
        self.get = to_raw_response_wrapper(
            channels.get,
        )


class AsyncChannelsResourceWithRawResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.list = async_to_raw_response_wrapper(
            channels.list,
        )
        self.get = async_to_raw_response_wrapper(
            channels.get,
        )


class ChannelsResourceWithStreamingResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.list = to_streamed_response_wrapper(
            channels.list,
        )
        self.get = to_streamed_response_wrapper(
            channels.get,
        )


class AsyncChannelsResourceWithStreamingResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.list = async_to_streamed_response_wrapper(
            channels.list,
        )
        self.get = async_to_streamed_response_wrapper(
            channels.get,
        )
