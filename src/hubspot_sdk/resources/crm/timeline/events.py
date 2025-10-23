# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime

import httpx

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
from ....types.crm.timeline import event_create_params, event_batch_create_params
from ....types.crm.event_detail import EventDetail
from ....types.crm.timeline_event_param import TimelineEventParam
from ....types.crm.timeline_event_response import TimelineEventResponse
from ....types.crm.timeline_event_i_frame_param import TimelineEventIFrameParam

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
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

    def create(
        self,
        *,
        event_template_id: str,
        tokens: Dict[str, str],
        id: str | Omit = omit,
        domain: str | Omit = omit,
        email: str | Omit = omit,
        extra_data: object | Omit = omit,
        object_id: str | Omit = omit,
        timeline_i_frame: TimelineEventIFrameParam | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        utk: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventResponse:
        """
        Send a single instance of event data to a specified event type.

        Args:
          event_template_id: The event template ID.

          tokens: A collection of token keys and values associated with the template tokens.

          id: Identifier for the event. This is optional, and we recommend you do not pass
              this in. We will create one for you if you omit this. You can also use
              `{{uuid}}` anywhere in the ID to generate a unique string, guaranteeing
              uniqueness.

          domain: The event domain (often paired with utk).

          email: The email address used for contact-specific events. This can be used to identify
              existing contacts, create new ones, or change the email for an existing contact
              (if paired with the `objectId`).

          extra_data: Additional event-specific data that can be interpreted by the template's
              markdown.

          object_id: The CRM object identifier. This is required for every event other than contacts
              (where utk or email can be used).

          timestamp: The time the event occurred. If not passed in, the curren time will be assumed.
              This is used to determine where an event is shown on a CRM object's timeline.

          utk: Use the `utk` parameter to associate an event with a contact by `usertoken`.
              This is recommended if you don't know a user's email, but have an identifying
              user token in your cookie.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integrators/timeline/v3/events",
            body=maybe_transform(
                {
                    "event_template_id": event_template_id,
                    "tokens": tokens,
                    "id": id,
                    "domain": domain,
                    "email": email,
                    "extra_data": extra_data,
                    "object_id": object_id,
                    "timeline_i_frame": timeline_i_frame,
                    "timestamp": timestamp,
                    "utk": utk,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventResponse,
        )

    def batch_create(
        self,
        *,
        inputs: Iterable[TimelineEventParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Batch create multiple instances of timeline events based on an event template.
        Once created, these event are immutable on the object timeline and cannot be
        modified. If the event template was configured to update object properties via
        `objectPropertyName`, this call will also attempt to updates those properties,
        or add them if they don't exist.

        Args:
          inputs: A collection of timeline events we want to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/integrators/timeline/v3/events/batch/create",
            body=maybe_transform({"inputs": inputs}, event_batch_create_params.EventBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        event_id: str,
        *,
        event_template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventResponse:
        """
        Retrieve an event instance, specified by template ID and event ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/integrators/timeline/v3/events/{event_template_id}/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventResponse,
        )

    def get_detail(
        self,
        event_id: str,
        *,
        event_template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDetail:
        """
        Retrieve details for a specific event, specified by template ID and event ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/integrators/timeline/v3/events/{event_template_id}/{event_id}/detail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDetail,
        )


class AsyncEventsResource(AsyncAPIResource):
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

    async def create(
        self,
        *,
        event_template_id: str,
        tokens: Dict[str, str],
        id: str | Omit = omit,
        domain: str | Omit = omit,
        email: str | Omit = omit,
        extra_data: object | Omit = omit,
        object_id: str | Omit = omit,
        timeline_i_frame: TimelineEventIFrameParam | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        utk: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventResponse:
        """
        Send a single instance of event data to a specified event type.

        Args:
          event_template_id: The event template ID.

          tokens: A collection of token keys and values associated with the template tokens.

          id: Identifier for the event. This is optional, and we recommend you do not pass
              this in. We will create one for you if you omit this. You can also use
              `{{uuid}}` anywhere in the ID to generate a unique string, guaranteeing
              uniqueness.

          domain: The event domain (often paired with utk).

          email: The email address used for contact-specific events. This can be used to identify
              existing contacts, create new ones, or change the email for an existing contact
              (if paired with the `objectId`).

          extra_data: Additional event-specific data that can be interpreted by the template's
              markdown.

          object_id: The CRM object identifier. This is required for every event other than contacts
              (where utk or email can be used).

          timestamp: The time the event occurred. If not passed in, the curren time will be assumed.
              This is used to determine where an event is shown on a CRM object's timeline.

          utk: Use the `utk` parameter to associate an event with a contact by `usertoken`.
              This is recommended if you don't know a user's email, but have an identifying
              user token in your cookie.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integrators/timeline/v3/events",
            body=await async_maybe_transform(
                {
                    "event_template_id": event_template_id,
                    "tokens": tokens,
                    "id": id,
                    "domain": domain,
                    "email": email,
                    "extra_data": extra_data,
                    "object_id": object_id,
                    "timeline_i_frame": timeline_i_frame,
                    "timestamp": timestamp,
                    "utk": utk,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventResponse,
        )

    async def batch_create(
        self,
        *,
        inputs: Iterable[TimelineEventParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Batch create multiple instances of timeline events based on an event template.
        Once created, these event are immutable on the object timeline and cannot be
        modified. If the event template was configured to update object properties via
        `objectPropertyName`, this call will also attempt to updates those properties,
        or add them if they don't exist.

        Args:
          inputs: A collection of timeline events we want to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/integrators/timeline/v3/events/batch/create",
            body=await async_maybe_transform({"inputs": inputs}, event_batch_create_params.EventBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        event_id: str,
        *,
        event_template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventResponse:
        """
        Retrieve an event instance, specified by template ID and event ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/integrators/timeline/v3/events/{event_template_id}/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventResponse,
        )

    async def get_detail(
        self,
        event_id: str,
        *,
        event_template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDetail:
        """
        Retrieve details for a specific event, specified by template ID and event ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/integrators/timeline/v3/events/{event_template_id}/{event_id}/detail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDetail,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )
        self.batch_create = to_raw_response_wrapper(
            events.batch_create,
        )
        self.get = to_raw_response_wrapper(
            events.get,
        )
        self.get_detail = to_raw_response_wrapper(
            events.get_detail,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )
        self.batch_create = async_to_raw_response_wrapper(
            events.batch_create,
        )
        self.get = async_to_raw_response_wrapper(
            events.get,
        )
        self.get_detail = async_to_raw_response_wrapper(
            events.get_detail,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )
        self.batch_create = to_streamed_response_wrapper(
            events.batch_create,
        )
        self.get = to_streamed_response_wrapper(
            events.get,
        )
        self.get_detail = to_streamed_response_wrapper(
            events.get_detail,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
        self.batch_create = async_to_streamed_response_wrapper(
            events.batch_create,
        )
        self.get = async_to_streamed_response_wrapper(
            events.get,
        )
        self.get_detail = async_to_streamed_response_wrapper(
            events.get_detail,
        )
