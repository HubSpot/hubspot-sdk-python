# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

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
from ....types.conversations.custom_channels import message_create_params, message_update_params
from ....types.conversations.pre_resolved_contacts_param import PreResolvedContactsParam
from ....types.conversations.public_conversations_message import PublicConversationsMessage
from ....types.conversations.channel_integration_participant_param import ChannelIntegrationParticipantParam

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def create(
        self,
        channel_id: str,
        *,
        attachments: Iterable[message_create_params.Attachment],
        channel_account_id: str,
        integration_thread_id: str,
        message_direction: Literal["INCOMING", "OUTGOING"],
        recipients: Iterable[ChannelIntegrationParticipantParam],
        senders: Iterable[ChannelIntegrationParticipantParam],
        text: str,
        timestamp: Union[str, datetime],
        in_reply_to_id: str | Omit = omit,
        integration_idempotency_id: str | Omit = omit,
        pre_resolved_contacts: PreResolvedContactsParam | Omit = omit,
        rich_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicConversationsMessage:
        """
        Publish a message over your custom channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._post(
            f"/conversations/v3/custom-channels/{channel_id}/messages",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "channel_account_id": channel_account_id,
                    "integration_thread_id": integration_thread_id,
                    "message_direction": message_direction,
                    "recipients": recipients,
                    "senders": senders,
                    "text": text,
                    "timestamp": timestamp,
                    "in_reply_to_id": in_reply_to_id,
                    "integration_idempotency_id": integration_idempotency_id,
                    "pre_resolved_contacts": pre_resolved_contacts,
                    "rich_text": rich_text,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicConversationsMessage,
        )

    def update(
        self,
        message_id: str,
        *,
        channel_id: str,
        status_type: Literal["SENT", "FAILED", "READ"],
        error_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicConversationsMessage:
        """
        Update a message's status to indicate if it was successfully sent, failed to
        send, or was read. For failed messages, this can also include the error message
        for the failure.

        Args:
          status_type: Valid status are SENT, FAILED, and READ

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._patch(
            f"/conversations/v3/custom-channels/{channel_id}/messages/{message_id}",
            body=maybe_transform(
                {
                    "status_type": status_type,
                    "error_message": error_message,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicConversationsMessage,
        )

    def get(
        self,
        message_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicConversationsMessage:
        """
        Get the details for a specific message sent over a custom channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/conversations/v3/custom-channels/{channel_id}/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicConversationsMessage,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        channel_id: str,
        *,
        attachments: Iterable[message_create_params.Attachment],
        channel_account_id: str,
        integration_thread_id: str,
        message_direction: Literal["INCOMING", "OUTGOING"],
        recipients: Iterable[ChannelIntegrationParticipantParam],
        senders: Iterable[ChannelIntegrationParticipantParam],
        text: str,
        timestamp: Union[str, datetime],
        in_reply_to_id: str | Omit = omit,
        integration_idempotency_id: str | Omit = omit,
        pre_resolved_contacts: PreResolvedContactsParam | Omit = omit,
        rich_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicConversationsMessage:
        """
        Publish a message over your custom channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._post(
            f"/conversations/v3/custom-channels/{channel_id}/messages",
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "channel_account_id": channel_account_id,
                    "integration_thread_id": integration_thread_id,
                    "message_direction": message_direction,
                    "recipients": recipients,
                    "senders": senders,
                    "text": text,
                    "timestamp": timestamp,
                    "in_reply_to_id": in_reply_to_id,
                    "integration_idempotency_id": integration_idempotency_id,
                    "pre_resolved_contacts": pre_resolved_contacts,
                    "rich_text": rich_text,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicConversationsMessage,
        )

    async def update(
        self,
        message_id: str,
        *,
        channel_id: str,
        status_type: Literal["SENT", "FAILED", "READ"],
        error_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicConversationsMessage:
        """
        Update a message's status to indicate if it was successfully sent, failed to
        send, or was read. For failed messages, this can also include the error message
        for the failure.

        Args:
          status_type: Valid status are SENT, FAILED, and READ

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._patch(
            f"/conversations/v3/custom-channels/{channel_id}/messages/{message_id}",
            body=await async_maybe_transform(
                {
                    "status_type": status_type,
                    "error_message": error_message,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicConversationsMessage,
        )

    async def get(
        self,
        message_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicConversationsMessage:
        """
        Get the details for a specific message sent over a custom channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/conversations/v3/custom-channels/{channel_id}/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicConversationsMessage,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.get = to_raw_response_wrapper(
            messages.get,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.get = async_to_raw_response_wrapper(
            messages.get,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.get = to_streamed_response_wrapper(
            messages.get,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.get = async_to_streamed_response_wrapper(
            messages.get,
        )
