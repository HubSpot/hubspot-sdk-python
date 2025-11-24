# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
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
from ....types.cms.media_bridge import (
    event_create_media_played_event_params,
    event_create_attention_span_event_params,
    event_create_media_played_percent_event_params,
)
from ....types.cms.media_played_event import MediaPlayedEvent
from ....types.cms.attention_span_event import AttentionSpanEvent
from ....types.cms.media_played_percentage_event import MediaPlayedPercentageEvent
from ....types.cms.attention_span_calculated_values_param import AttentionSpanCalculatedValuesParam

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

    def create_attention_span_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        raw_data_map: Dict[str, int],
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        derived_values: AttentionSpanCalculatedValuesParam | Omit = omit,
        external_id: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        raw_data_string: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttentionSpanEvent:
        """
        Create an event containing the viewers attention span details for the media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media-bridge/v1/events/attention-span",
            body=maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "raw_data_map": raw_data_map,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "derived_values": derived_values,
                    "external_id": external_id,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                    "raw_data_string": raw_data_string,
                },
                event_create_attention_span_event_params.EventCreateAttentionSpanEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttentionSpanEvent,
        )

    def create_media_played_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        session_id: str,
        state: Literal["STARTED", "VIEWED"],
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        iframe_url: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedEvent:
        """
        Create an event for when a user begins playing a piece of media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media-bridge/v1/events/media-played",
            body=maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "session_id": session_id,
                    "state": state,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "iframe_url": iframe_url,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                event_create_media_played_event_params.EventCreateMediaPlayedEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedEvent,
        )

    def create_media_played_percent_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        played_percent: int,
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedPercentageEvent:
        """
        Create an event representing a user reaching quarterly milestones in a piece of
        media they're viewing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media-bridge/v1/events/media-played-percent",
            body=maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "played_percent": played_percent,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                event_create_media_played_percent_event_params.EventCreateMediaPlayedPercentEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedPercentageEvent,
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

    async def create_attention_span_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        raw_data_map: Dict[str, int],
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        derived_values: AttentionSpanCalculatedValuesParam | Omit = omit,
        external_id: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        raw_data_string: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttentionSpanEvent:
        """
        Create an event containing the viewers attention span details for the media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media-bridge/v1/events/attention-span",
            body=await async_maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "raw_data_map": raw_data_map,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "derived_values": derived_values,
                    "external_id": external_id,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                    "raw_data_string": raw_data_string,
                },
                event_create_attention_span_event_params.EventCreateAttentionSpanEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttentionSpanEvent,
        )

    async def create_media_played_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        session_id: str,
        state: Literal["STARTED", "VIEWED"],
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        iframe_url: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedEvent:
        """
        Create an event for when a user begins playing a piece of media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media-bridge/v1/events/media-played",
            body=await async_maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "session_id": session_id,
                    "state": state,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "iframe_url": iframe_url,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                event_create_media_played_event_params.EventCreateMediaPlayedEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedEvent,
        )

    async def create_media_played_percent_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        played_percent: int,
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedPercentageEvent:
        """
        Create an event representing a user reaching quarterly milestones in a piece of
        media they're viewing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media-bridge/v1/events/media-played-percent",
            body=await async_maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "played_percent": played_percent,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                event_create_media_played_percent_event_params.EventCreateMediaPlayedPercentEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedPercentageEvent,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create_attention_span_event = to_raw_response_wrapper(
            events.create_attention_span_event,
        )
        self.create_media_played_event = to_raw_response_wrapper(
            events.create_media_played_event,
        )
        self.create_media_played_percent_event = to_raw_response_wrapper(
            events.create_media_played_percent_event,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create_attention_span_event = async_to_raw_response_wrapper(
            events.create_attention_span_event,
        )
        self.create_media_played_event = async_to_raw_response_wrapper(
            events.create_media_played_event,
        )
        self.create_media_played_percent_event = async_to_raw_response_wrapper(
            events.create_media_played_percent_event,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create_attention_span_event = to_streamed_response_wrapper(
            events.create_attention_span_event,
        )
        self.create_media_played_event = to_streamed_response_wrapper(
            events.create_media_played_event,
        )
        self.create_media_played_percent_event = to_streamed_response_wrapper(
            events.create_media_played_percent_event,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create_attention_span_event = async_to_streamed_response_wrapper(
            events.create_attention_span_event,
        )
        self.create_media_played_event = async_to_streamed_response_wrapper(
            events.create_media_played_event,
        )
        self.create_media_played_percent_event = async_to_streamed_response_wrapper(
            events.create_media_played_percent_event,
        )
