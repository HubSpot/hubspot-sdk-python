# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .send import (
    SendResource,
    AsyncSendResource,
    SendResourceWithRawResponse,
    AsyncSendResourceWithRawResponse,
    SendResourceWithStreamingResponse,
    AsyncSendResourceWithStreamingResponse,
)
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
from ...types.events import event_list_params
from .event_definitions import (
    EventDefinitionsResource,
    AsyncEventDefinitionsResource,
    EventDefinitionsResourceWithRawResponse,
    AsyncEventDefinitionsResourceWithRawResponse,
    EventDefinitionsResourceWithStreamingResponse,
    AsyncEventDefinitionsResourceWithStreamingResponse,
)
from ...types.events.external_unified_event import ExternalUnifiedEvent
from ...types.events.visible_external_event_type_names import VisibleExternalEventTypeNames

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def event_definitions(self) -> EventDefinitionsResource:
        return EventDefinitionsResource(self._client)

    @cached_property
    def send(self) -> SendResource:
        return SendResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        event_type: str | Omit = omit,
        limit: int | Omit = omit,
        object_id: int | Omit = omit,
        object_property: event_list_params.ObjectProperty | Omit = omit,
        object_type: str | Omit = omit,
        occurred_after: Union[str, datetime] | Omit = omit,
        occurred_before: Union[str, datetime] | Omit = omit,
        property: event_list_params.Property | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ExternalUnifiedEvent]:
        """Retrieve instances of event completion data.

        For example, retrieve all event
        completions associated with a specific contact.

        Args:
          id: ID of an event instance. IDs are 1:1 with event instances. If you provide this
              filter and additional filters, the other filters must match the values on the
              event instance to yield results.

          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          before: Pagination cursor for backward navigation. Retrieves events occurring before the
              specified cursor position. Note: Currently only forward pagination with after is
              supported.

          event_type: The event type name. You can retrieve available event types using the
              [event types endpoint](#get-%2Fevents%2Fv3%2Fevents%2Fevent-types).

          limit: The maximum number of results to display per page.

          object_id: The ID of the CRM Object to filter event instances on. When including this
              parameter, you must also include the `objectType` parameter.

          object_type: The type of CRM object to filter event instances on (e.g., `contact`). To
              retrieve event data for a specific CRM record, include the additional `objectId`
              query parameter (below).

          occurred_after: Filter for event data that occurred after a specific datetime.

          occurred_before: Filter for event data that occurred before a specific datetime.

          sort: Sort direction based on the timestamp of the event instance, `ASCENDING` or
              `DESCENDING`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/v3/events/",
            page=SyncPage[ExternalUnifiedEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "event_type": event_type,
                        "limit": limit,
                        "object_id": object_id,
                        "object_property": object_property,
                        "object_type": object_type,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "property": property,
                        "sort": sort,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=ExternalUnifiedEvent,
        )

    def list_event_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibleExternalEventTypeNames:
        """This endpoint returns a list of event type names which are visible to you.

        You
        may use these event type names to query the API for specific event instances of
        a desired type.

        Note: the `get_types` method is only supported in the Python SDK version
        `12.0.0-beta.1` or later.
        """
        return self._get(
            "/events/v3/events/event-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibleExternalEventTypeNames,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def event_definitions(self) -> AsyncEventDefinitionsResource:
        return AsyncEventDefinitionsResource(self._client)

    @cached_property
    def send(self) -> AsyncSendResource:
        return AsyncSendResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        event_type: str | Omit = omit,
        limit: int | Omit = omit,
        object_id: int | Omit = omit,
        object_property: event_list_params.ObjectProperty | Omit = omit,
        object_type: str | Omit = omit,
        occurred_after: Union[str, datetime] | Omit = omit,
        occurred_before: Union[str, datetime] | Omit = omit,
        property: event_list_params.Property | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExternalUnifiedEvent, AsyncPage[ExternalUnifiedEvent]]:
        """Retrieve instances of event completion data.

        For example, retrieve all event
        completions associated with a specific contact.

        Args:
          id: ID of an event instance. IDs are 1:1 with event instances. If you provide this
              filter and additional filters, the other filters must match the values on the
              event instance to yield results.

          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          before: Pagination cursor for backward navigation. Retrieves events occurring before the
              specified cursor position. Note: Currently only forward pagination with after is
              supported.

          event_type: The event type name. You can retrieve available event types using the
              [event types endpoint](#get-%2Fevents%2Fv3%2Fevents%2Fevent-types).

          limit: The maximum number of results to display per page.

          object_id: The ID of the CRM Object to filter event instances on. When including this
              parameter, you must also include the `objectType` parameter.

          object_type: The type of CRM object to filter event instances on (e.g., `contact`). To
              retrieve event data for a specific CRM record, include the additional `objectId`
              query parameter (below).

          occurred_after: Filter for event data that occurred after a specific datetime.

          occurred_before: Filter for event data that occurred before a specific datetime.

          sort: Sort direction based on the timestamp of the event instance, `ASCENDING` or
              `DESCENDING`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/v3/events/",
            page=AsyncPage[ExternalUnifiedEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "event_type": event_type,
                        "limit": limit,
                        "object_id": object_id,
                        "object_property": object_property,
                        "object_type": object_type,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "property": property,
                        "sort": sort,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=ExternalUnifiedEvent,
        )

    async def list_event_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibleExternalEventTypeNames:
        """This endpoint returns a list of event type names which are visible to you.

        You
        may use these event type names to query the API for specific event instances of
        a desired type.

        Note: the `get_types` method is only supported in the Python SDK version
        `12.0.0-beta.1` or later.
        """
        return await self._get(
            "/events/v3/events/event-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibleExternalEventTypeNames,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.list_event_types = to_raw_response_wrapper(
            events.list_event_types,
        )

    @cached_property
    def event_definitions(self) -> EventDefinitionsResourceWithRawResponse:
        return EventDefinitionsResourceWithRawResponse(self._events.event_definitions)

    @cached_property
    def send(self) -> SendResourceWithRawResponse:
        return SendResourceWithRawResponse(self._events.send)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.list_event_types = async_to_raw_response_wrapper(
            events.list_event_types,
        )

    @cached_property
    def event_definitions(self) -> AsyncEventDefinitionsResourceWithRawResponse:
        return AsyncEventDefinitionsResourceWithRawResponse(self._events.event_definitions)

    @cached_property
    def send(self) -> AsyncSendResourceWithRawResponse:
        return AsyncSendResourceWithRawResponse(self._events.send)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.list_event_types = to_streamed_response_wrapper(
            events.list_event_types,
        )

    @cached_property
    def event_definitions(self) -> EventDefinitionsResourceWithStreamingResponse:
        return EventDefinitionsResourceWithStreamingResponse(self._events.event_definitions)

    @cached_property
    def send(self) -> SendResourceWithStreamingResponse:
        return SendResourceWithStreamingResponse(self._events.send)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.list_event_types = async_to_streamed_response_wrapper(
            events.list_event_types,
        )

    @cached_property
    def event_definitions(self) -> AsyncEventDefinitionsResourceWithStreamingResponse:
        return AsyncEventDefinitionsResourceWithStreamingResponse(self._events.event_definitions)

    @cached_property
    def send(self) -> AsyncSendResourceWithStreamingResponse:
        return AsyncSendResourceWithStreamingResponse(self._events.send)
