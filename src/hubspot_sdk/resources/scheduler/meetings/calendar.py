# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.scheduler.meetings import calendar_create_params
from ....types.scheduler.external_email_reminder_schedule_param import ExternalEmailReminderScheduleParam
from ....types.scheduler.external_calender_meeting_event_response import ExternalCalenderMeetingEventResponse
from ....types.scheduler.external_association_create_request_param import ExternalAssociationCreateRequestParam
from ....types.scheduler.external_calendar_meeting_event_create_properties_param import (
    ExternalCalendarMeetingEventCreatePropertiesParam,
)

__all__ = ["CalendarResource", "AsyncCalendarResource"]


class CalendarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CalendarResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        associations: Iterable[ExternalAssociationCreateRequestParam],
        email_reminder_schedule: ExternalEmailReminderScheduleParam,
        properties: ExternalCalendarMeetingEventCreatePropertiesParam,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalCalenderMeetingEventResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scheduler/v3/meetings/calendar",
            body=maybe_transform(
                {
                    "associations": associations,
                    "email_reminder_schedule": email_reminder_schedule,
                    "properties": properties,
                    "timezone": timezone,
                },
                calendar_create_params.CalendarCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalCalenderMeetingEventResponse,
        )


class AsyncCalendarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCalendarResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        associations: Iterable[ExternalAssociationCreateRequestParam],
        email_reminder_schedule: ExternalEmailReminderScheduleParam,
        properties: ExternalCalendarMeetingEventCreatePropertiesParam,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalCalenderMeetingEventResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scheduler/v3/meetings/calendar",
            body=await async_maybe_transform(
                {
                    "associations": associations,
                    "email_reminder_schedule": email_reminder_schedule,
                    "properties": properties,
                    "timezone": timezone,
                },
                calendar_create_params.CalendarCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalCalenderMeetingEventResponse,
        )


class CalendarResourceWithRawResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

        self.create = to_raw_response_wrapper(
            calendar.create,
        )


class AsyncCalendarResourceWithRawResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

        self.create = async_to_raw_response_wrapper(
            calendar.create,
        )


class CalendarResourceWithStreamingResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

        self.create = to_streamed_response_wrapper(
            calendar.create,
        )


class AsyncCalendarResourceWithStreamingResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

        self.create = async_to_streamed_response_wrapper(
            calendar.create,
        )
