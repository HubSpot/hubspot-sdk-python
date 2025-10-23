# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .custom_channels.custom_channels import (
    CustomChannelsResource,
    AsyncCustomChannelsResource,
    CustomChannelsResourceWithRawResponse,
    AsyncCustomChannelsResourceWithRawResponse,
    CustomChannelsResourceWithStreamingResponse,
    AsyncCustomChannelsResourceWithStreamingResponse,
)

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def custom_channels(self) -> CustomChannelsResource:
        return CustomChannelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def custom_channels(self) -> AsyncCustomChannelsResource:
        return AsyncCustomChannelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

    @cached_property
    def custom_channels(self) -> CustomChannelsResourceWithRawResponse:
        return CustomChannelsResourceWithRawResponse(self._conversations.custom_channels)


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

    @cached_property
    def custom_channels(self) -> AsyncCustomChannelsResourceWithRawResponse:
        return AsyncCustomChannelsResourceWithRawResponse(self._conversations.custom_channels)


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

    @cached_property
    def custom_channels(self) -> CustomChannelsResourceWithStreamingResponse:
        return CustomChannelsResourceWithStreamingResponse(self._conversations.custom_channels)


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

    @cached_property
    def custom_channels(self) -> AsyncCustomChannelsResourceWithStreamingResponse:
        return AsyncCustomChannelsResourceWithStreamingResponse(self._conversations.custom_channels)
