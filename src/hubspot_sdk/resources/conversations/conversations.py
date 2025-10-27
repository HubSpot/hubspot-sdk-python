# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .actors import (
    ActorsResource,
    AsyncActorsResource,
    ActorsResourceWithRawResponse,
    AsyncActorsResourceWithRawResponse,
    ActorsResourceWithStreamingResponse,
    AsyncActorsResourceWithStreamingResponse,
)
from .inboxes import (
    InboxesResource,
    AsyncInboxesResource,
    InboxesResourceWithRawResponse,
    AsyncInboxesResourceWithRawResponse,
    InboxesResourceWithStreamingResponse,
    AsyncInboxesResourceWithStreamingResponse,
)
from .threads import (
    ThreadsResource,
    AsyncThreadsResource,
    ThreadsResourceWithRawResponse,
    AsyncThreadsResourceWithRawResponse,
    ThreadsResourceWithStreamingResponse,
    AsyncThreadsResourceWithStreamingResponse,
)
from .channels import (
    ChannelsResource,
    AsyncChannelsResource,
    ChannelsResourceWithRawResponse,
    AsyncChannelsResourceWithRawResponse,
    ChannelsResourceWithStreamingResponse,
    AsyncChannelsResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .channel_accounts import (
    ChannelAccountsResource,
    AsyncChannelAccountsResource,
    ChannelAccountsResourceWithRawResponse,
    AsyncChannelAccountsResourceWithRawResponse,
    ChannelAccountsResourceWithStreamingResponse,
    AsyncChannelAccountsResourceWithStreamingResponse,
)
from .visitor_identification import (
    VisitorIdentificationResource,
    AsyncVisitorIdentificationResource,
    VisitorIdentificationResourceWithRawResponse,
    AsyncVisitorIdentificationResourceWithRawResponse,
    VisitorIdentificationResourceWithStreamingResponse,
    AsyncVisitorIdentificationResourceWithStreamingResponse,
)
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
    def actors(self) -> ActorsResource:
        return ActorsResource(self._client)

    @cached_property
    def channel_accounts(self) -> ChannelAccountsResource:
        return ChannelAccountsResource(self._client)

    @cached_property
    def channels(self) -> ChannelsResource:
        return ChannelsResource(self._client)

    @cached_property
    def custom_channels(self) -> CustomChannelsResource:
        return CustomChannelsResource(self._client)

    @cached_property
    def inboxes(self) -> InboxesResource:
        return InboxesResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def threads(self) -> ThreadsResource:
        return ThreadsResource(self._client)

    @cached_property
    def visitor_identification(self) -> VisitorIdentificationResource:
        return VisitorIdentificationResource(self._client)

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
    def actors(self) -> AsyncActorsResource:
        return AsyncActorsResource(self._client)

    @cached_property
    def channel_accounts(self) -> AsyncChannelAccountsResource:
        return AsyncChannelAccountsResource(self._client)

    @cached_property
    def channels(self) -> AsyncChannelsResource:
        return AsyncChannelsResource(self._client)

    @cached_property
    def custom_channels(self) -> AsyncCustomChannelsResource:
        return AsyncCustomChannelsResource(self._client)

    @cached_property
    def inboxes(self) -> AsyncInboxesResource:
        return AsyncInboxesResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def threads(self) -> AsyncThreadsResource:
        return AsyncThreadsResource(self._client)

    @cached_property
    def visitor_identification(self) -> AsyncVisitorIdentificationResource:
        return AsyncVisitorIdentificationResource(self._client)

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
    def actors(self) -> ActorsResourceWithRawResponse:
        return ActorsResourceWithRawResponse(self._conversations.actors)

    @cached_property
    def channel_accounts(self) -> ChannelAccountsResourceWithRawResponse:
        return ChannelAccountsResourceWithRawResponse(self._conversations.channel_accounts)

    @cached_property
    def channels(self) -> ChannelsResourceWithRawResponse:
        return ChannelsResourceWithRawResponse(self._conversations.channels)

    @cached_property
    def custom_channels(self) -> CustomChannelsResourceWithRawResponse:
        return CustomChannelsResourceWithRawResponse(self._conversations.custom_channels)

    @cached_property
    def inboxes(self) -> InboxesResourceWithRawResponse:
        return InboxesResourceWithRawResponse(self._conversations.inboxes)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._conversations.messages)

    @cached_property
    def threads(self) -> ThreadsResourceWithRawResponse:
        return ThreadsResourceWithRawResponse(self._conversations.threads)

    @cached_property
    def visitor_identification(self) -> VisitorIdentificationResourceWithRawResponse:
        return VisitorIdentificationResourceWithRawResponse(self._conversations.visitor_identification)


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

    @cached_property
    def actors(self) -> AsyncActorsResourceWithRawResponse:
        return AsyncActorsResourceWithRawResponse(self._conversations.actors)

    @cached_property
    def channel_accounts(self) -> AsyncChannelAccountsResourceWithRawResponse:
        return AsyncChannelAccountsResourceWithRawResponse(self._conversations.channel_accounts)

    @cached_property
    def channels(self) -> AsyncChannelsResourceWithRawResponse:
        return AsyncChannelsResourceWithRawResponse(self._conversations.channels)

    @cached_property
    def custom_channels(self) -> AsyncCustomChannelsResourceWithRawResponse:
        return AsyncCustomChannelsResourceWithRawResponse(self._conversations.custom_channels)

    @cached_property
    def inboxes(self) -> AsyncInboxesResourceWithRawResponse:
        return AsyncInboxesResourceWithRawResponse(self._conversations.inboxes)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._conversations.messages)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithRawResponse:
        return AsyncThreadsResourceWithRawResponse(self._conversations.threads)

    @cached_property
    def visitor_identification(self) -> AsyncVisitorIdentificationResourceWithRawResponse:
        return AsyncVisitorIdentificationResourceWithRawResponse(self._conversations.visitor_identification)


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

    @cached_property
    def actors(self) -> ActorsResourceWithStreamingResponse:
        return ActorsResourceWithStreamingResponse(self._conversations.actors)

    @cached_property
    def channel_accounts(self) -> ChannelAccountsResourceWithStreamingResponse:
        return ChannelAccountsResourceWithStreamingResponse(self._conversations.channel_accounts)

    @cached_property
    def channels(self) -> ChannelsResourceWithStreamingResponse:
        return ChannelsResourceWithStreamingResponse(self._conversations.channels)

    @cached_property
    def custom_channels(self) -> CustomChannelsResourceWithStreamingResponse:
        return CustomChannelsResourceWithStreamingResponse(self._conversations.custom_channels)

    @cached_property
    def inboxes(self) -> InboxesResourceWithStreamingResponse:
        return InboxesResourceWithStreamingResponse(self._conversations.inboxes)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._conversations.messages)

    @cached_property
    def threads(self) -> ThreadsResourceWithStreamingResponse:
        return ThreadsResourceWithStreamingResponse(self._conversations.threads)

    @cached_property
    def visitor_identification(self) -> VisitorIdentificationResourceWithStreamingResponse:
        return VisitorIdentificationResourceWithStreamingResponse(self._conversations.visitor_identification)


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

    @cached_property
    def actors(self) -> AsyncActorsResourceWithStreamingResponse:
        return AsyncActorsResourceWithStreamingResponse(self._conversations.actors)

    @cached_property
    def channel_accounts(self) -> AsyncChannelAccountsResourceWithStreamingResponse:
        return AsyncChannelAccountsResourceWithStreamingResponse(self._conversations.channel_accounts)

    @cached_property
    def channels(self) -> AsyncChannelsResourceWithStreamingResponse:
        return AsyncChannelsResourceWithStreamingResponse(self._conversations.channels)

    @cached_property
    def custom_channels(self) -> AsyncCustomChannelsResourceWithStreamingResponse:
        return AsyncCustomChannelsResourceWithStreamingResponse(self._conversations.custom_channels)

    @cached_property
    def inboxes(self) -> AsyncInboxesResourceWithStreamingResponse:
        return AsyncInboxesResourceWithStreamingResponse(self._conversations.inboxes)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._conversations.messages)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithStreamingResponse:
        return AsyncThreadsResourceWithStreamingResponse(self._conversations.threads)

    @cached_property
    def visitor_identification(self) -> AsyncVisitorIdentificationResourceWithStreamingResponse:
        return AsyncVisitorIdentificationResourceWithStreamingResponse(self._conversations.visitor_identification)
