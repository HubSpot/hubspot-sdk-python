# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.scheduler.meetings import advanced_book_params, advanced_create_params
from ....types.scheduler.external_booking_form_field_param import ExternalBookingFormFieldParam
from ....types.scheduler.external_meeting_booking_response import ExternalMeetingBookingResponse
from ....types.scheduler.external_legal_consent_response_param import ExternalLegalConsentResponseParam
from ....types.scheduler.external_email_reminder_schedule_param import ExternalEmailReminderScheduleParam
from ....types.scheduler.external_calender_meeting_event_response import ExternalCalenderMeetingEventResponse
from ....types.scheduler.external_association_create_request_param import ExternalAssociationCreateRequestParam
from ....types.scheduler.external_calendar_meeting_event_create_properties_param import (
    ExternalCalendarMeetingEventCreatePropertiesParam,
)

__all__ = ["AdvancedResource", "AsyncAdvancedResource"]


class AdvancedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvancedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AdvancedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvancedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AdvancedResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        organizer_user_id: str,
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
        Create a new calendar event and meeting object by providing the necessary
        details such as associations, email reminders, meeting object properties, and
        timezone.

        Args:
          timezone: The timezone property that will be set on the meeting event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scheduler/2026-03/meetings/calendar",
            body=maybe_transform(
                {
                    "associations": associations,
                    "email_reminder_schedule": email_reminder_schedule,
                    "properties": properties,
                    "timezone": timezone,
                },
                advanced_create_params.AdvancedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organizer_user_id": organizer_user_id}, advanced_create_params.AdvancedCreateParams
                ),
            ),
            cast_to=ExternalCalenderMeetingEventResponse,
        )

    def book(
        self,
        *,
        duration: int,
        email: str,
        first_name: str,
        form_fields: Iterable[ExternalBookingFormFieldParam],
        last_name: str,
        legal_consent_responses: Iterable[ExternalLegalConsentResponseParam],
        likely_available_user_ids: SequenceNotStr[str],
        slug: str,
        start_time: Union[str, datetime],
        locale: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalMeetingBookingResponse:
        """
        Book a meeting for a specified meeting page.

        Args:
          duration: The duration of the meeting in milliseconds.

          email: The email address of the person booking the meeting.

          first_name: The first name of the person booking the meeting.

          last_name: The last name of the person booking the meeting.

          slug: The unique path identifier for the meeting page.

          start_time: The date and time when the meeting is scheduled to start, in ISO 8601 format.

          locale: The locale used for formatting dates and times in the meeting booking.

          timezone: The timezone in which the meeting is scheduled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scheduler/2026-03/meetings/meeting-links/book",
            body=maybe_transform(
                {
                    "duration": duration,
                    "email": email,
                    "first_name": first_name,
                    "form_fields": form_fields,
                    "last_name": last_name,
                    "legal_consent_responses": legal_consent_responses,
                    "likely_available_user_ids": likely_available_user_ids,
                    "slug": slug,
                    "start_time": start_time,
                    "locale": locale,
                    "timezone": timezone,
                },
                advanced_book_params.AdvancedBookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalMeetingBookingResponse,
        )


class AsyncAdvancedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvancedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvancedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvancedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAdvancedResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        organizer_user_id: str,
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
        Create a new calendar event and meeting object by providing the necessary
        details such as associations, email reminders, meeting object properties, and
        timezone.

        Args:
          timezone: The timezone property that will be set on the meeting event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scheduler/2026-03/meetings/calendar",
            body=await async_maybe_transform(
                {
                    "associations": associations,
                    "email_reminder_schedule": email_reminder_schedule,
                    "properties": properties,
                    "timezone": timezone,
                },
                advanced_create_params.AdvancedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organizer_user_id": organizer_user_id}, advanced_create_params.AdvancedCreateParams
                ),
            ),
            cast_to=ExternalCalenderMeetingEventResponse,
        )

    async def book(
        self,
        *,
        duration: int,
        email: str,
        first_name: str,
        form_fields: Iterable[ExternalBookingFormFieldParam],
        last_name: str,
        legal_consent_responses: Iterable[ExternalLegalConsentResponseParam],
        likely_available_user_ids: SequenceNotStr[str],
        slug: str,
        start_time: Union[str, datetime],
        locale: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalMeetingBookingResponse:
        """
        Book a meeting for a specified meeting page.

        Args:
          duration: The duration of the meeting in milliseconds.

          email: The email address of the person booking the meeting.

          first_name: The first name of the person booking the meeting.

          last_name: The last name of the person booking the meeting.

          slug: The unique path identifier for the meeting page.

          start_time: The date and time when the meeting is scheduled to start, in ISO 8601 format.

          locale: The locale used for formatting dates and times in the meeting booking.

          timezone: The timezone in which the meeting is scheduled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scheduler/2026-03/meetings/meeting-links/book",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "email": email,
                    "first_name": first_name,
                    "form_fields": form_fields,
                    "last_name": last_name,
                    "legal_consent_responses": legal_consent_responses,
                    "likely_available_user_ids": likely_available_user_ids,
                    "slug": slug,
                    "start_time": start_time,
                    "locale": locale,
                    "timezone": timezone,
                },
                advanced_book_params.AdvancedBookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalMeetingBookingResponse,
        )


class AdvancedResourceWithRawResponse:
    def __init__(self, advanced: AdvancedResource) -> None:
        self._advanced = advanced

        self.create = to_raw_response_wrapper(
            advanced.create,
        )
        self.book = to_raw_response_wrapper(
            advanced.book,
        )


class AsyncAdvancedResourceWithRawResponse:
    def __init__(self, advanced: AsyncAdvancedResource) -> None:
        self._advanced = advanced

        self.create = async_to_raw_response_wrapper(
            advanced.create,
        )
        self.book = async_to_raw_response_wrapper(
            advanced.book,
        )


class AdvancedResourceWithStreamingResponse:
    def __init__(self, advanced: AdvancedResource) -> None:
        self._advanced = advanced

        self.create = to_streamed_response_wrapper(
            advanced.create,
        )
        self.book = to_streamed_response_wrapper(
            advanced.book,
        )


class AsyncAdvancedResourceWithStreamingResponse:
    def __init__(self, advanced: AsyncAdvancedResource) -> None:
        self._advanced = advanced

        self.create = async_to_streamed_response_wrapper(
            advanced.create,
        )
        self.book = async_to_streamed_response_wrapper(
            advanced.book,
        )
