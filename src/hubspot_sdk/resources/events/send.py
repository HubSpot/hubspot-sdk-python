# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.events import send_send_params, send_send_batch_params
from ...types.events.behavioral_event_http_completion_request_param import BehavioralEventHTTPCompletionRequestParam

__all__ = ["SendResource", "AsyncSendResource"]


class SendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SendResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        event_name: str,
        email: str | Omit = omit,
        object_id: str | Omit = omit,
        occurred_at: Union[str, datetime] | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        utk: str | Omit = omit,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send data for a single event completion.

        Args:
          event_name: The internal name of the event (`pe<portalID>_eventName`). Can be retrieved
              through the
              [event definitions API](https://developers.hubspot.com/docs/reference/api/analytics-and-events/custom-events/custom-event-definitions#get-%2Fevents%2Fv3%2Fevent-definitions)
              or in
              [HubSpot's UI](https://knowledge.hubspot.com/reports/create-custom-behavioral-events-with-the-code-wizard#find-internal-name).

          email: The visitor's email address. Used for associating the event data with a CRM
              record.

          object_id: The ID of the object that completed the event (e.g., contact ID or visitor ID).

          occurred_at: The time when this event occurred. If this isn't set, the current time will be
              used.

          properties: The event properties to update. Takes the format of key-value pairs (property
              internal name and property value). Learn more about
              [HubSpot's default event properties](https://developers.hubspot.com/docs/guides/api/analytics-and-events/custom-events/custom-event-definitions#hubspot-s-default-event-properties).

          utk: The visitor's usertoken. Used for associating the event data with a CRM record.

          uuid: Include a universally unique identifier to assign a unique ID to the event
              completion. Can be useful for matching data between HubSpot and other external
              systems.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/events/v3/send",
            body=maybe_transform(
                {
                    "event_name": event_name,
                    "email": email,
                    "object_id": object_id,
                    "occurred_at": occurred_at,
                    "properties": properties,
                    "utk": utk,
                    "uuid": uuid,
                },
                send_send_params.SendSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_batch(
        self,
        *,
        inputs: Iterable[BehavioralEventHTTPCompletionRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send multiple event completions at once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/events/v3/send/batch",
            body=maybe_transform({"inputs": inputs}, send_send_batch_params.SendSendBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSendResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        event_name: str,
        email: str | Omit = omit,
        object_id: str | Omit = omit,
        occurred_at: Union[str, datetime] | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        utk: str | Omit = omit,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send data for a single event completion.

        Args:
          event_name: The internal name of the event (`pe<portalID>_eventName`). Can be retrieved
              through the
              [event definitions API](https://developers.hubspot.com/docs/reference/api/analytics-and-events/custom-events/custom-event-definitions#get-%2Fevents%2Fv3%2Fevent-definitions)
              or in
              [HubSpot's UI](https://knowledge.hubspot.com/reports/create-custom-behavioral-events-with-the-code-wizard#find-internal-name).

          email: The visitor's email address. Used for associating the event data with a CRM
              record.

          object_id: The ID of the object that completed the event (e.g., contact ID or visitor ID).

          occurred_at: The time when this event occurred. If this isn't set, the current time will be
              used.

          properties: The event properties to update. Takes the format of key-value pairs (property
              internal name and property value). Learn more about
              [HubSpot's default event properties](https://developers.hubspot.com/docs/guides/api/analytics-and-events/custom-events/custom-event-definitions#hubspot-s-default-event-properties).

          utk: The visitor's usertoken. Used for associating the event data with a CRM record.

          uuid: Include a universally unique identifier to assign a unique ID to the event
              completion. Can be useful for matching data between HubSpot and other external
              systems.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/events/v3/send",
            body=await async_maybe_transform(
                {
                    "event_name": event_name,
                    "email": email,
                    "object_id": object_id,
                    "occurred_at": occurred_at,
                    "properties": properties,
                    "utk": utk,
                    "uuid": uuid,
                },
                send_send_params.SendSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_batch(
        self,
        *,
        inputs: Iterable[BehavioralEventHTTPCompletionRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send multiple event completions at once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/events/v3/send/batch",
            body=await async_maybe_transform({"inputs": inputs}, send_send_batch_params.SendSendBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SendResourceWithRawResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.send = to_raw_response_wrapper(
            send.send,
        )
        self.send_batch = to_raw_response_wrapper(
            send.send_batch,
        )


class AsyncSendResourceWithRawResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.send = async_to_raw_response_wrapper(
            send.send,
        )
        self.send_batch = async_to_raw_response_wrapper(
            send.send_batch,
        )


class SendResourceWithStreamingResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.send = to_streamed_response_wrapper(
            send.send,
        )
        self.send_batch = to_streamed_response_wrapper(
            send.send_batch,
        )


class AsyncSendResourceWithStreamingResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.send = async_to_streamed_response_wrapper(
            send.send,
        )
        self.send_batch = async_to_streamed_response_wrapper(
            send.send_batch,
        )
