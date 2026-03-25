# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.marketing.events import (
    event_cancel_by_external_event_id_params,
    event_complete_by_external_event_id_params,
)
from ....types.marketing.marketing_event_default_response import MarketingEventDefaultResponse

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

    def cancel_by_external_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventDefaultResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/cancel",
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    event_cancel_by_external_event_id_params.EventCancelByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventDefaultResponse,
        )

    def complete_by_external_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        end_date_time: Union[str, datetime],
        start_date_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventDefaultResponse:
        """
        Args:
          end_date_time: The end date and time of the marketing event in ISO 8601 format

          start_date_time: The start date and time of the marketing event in ISO 8601 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/complete",
                external_event_id=external_event_id,
            ),
            body=maybe_transform(
                {
                    "end_date_time": end_date_time,
                    "start_date_time": start_date_time,
                },
                event_complete_by_external_event_id_params.EventCompleteByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    event_complete_by_external_event_id_params.EventCompleteByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventDefaultResponse,
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

    async def cancel_by_external_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventDefaultResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/cancel",
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    event_cancel_by_external_event_id_params.EventCancelByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventDefaultResponse,
        )

    async def complete_by_external_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        end_date_time: Union[str, datetime],
        start_date_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventDefaultResponse:
        """
        Args:
          end_date_time: The end date and time of the marketing event in ISO 8601 format

          start_date_time: The start date and time of the marketing event in ISO 8601 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/complete",
                external_event_id=external_event_id,
            ),
            body=await async_maybe_transform(
                {
                    "end_date_time": end_date_time,
                    "start_date_time": start_date_time,
                },
                event_complete_by_external_event_id_params.EventCompleteByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    event_complete_by_external_event_id_params.EventCompleteByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventDefaultResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.cancel_by_external_event_id = to_raw_response_wrapper(
            events.cancel_by_external_event_id,
        )
        self.complete_by_external_event_id = to_raw_response_wrapper(
            events.complete_by_external_event_id,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.cancel_by_external_event_id = async_to_raw_response_wrapper(
            events.cancel_by_external_event_id,
        )
        self.complete_by_external_event_id = async_to_raw_response_wrapper(
            events.complete_by_external_event_id,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.cancel_by_external_event_id = to_streamed_response_wrapper(
            events.cancel_by_external_event_id,
        )
        self.complete_by_external_event_id = to_streamed_response_wrapper(
            events.complete_by_external_event_id,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.cancel_by_external_event_id = async_to_streamed_response_wrapper(
            events.cancel_by_external_event_id,
        )
        self.complete_by_external_event_id = async_to_streamed_response_wrapper(
            events.complete_by_external_event_id,
        )
