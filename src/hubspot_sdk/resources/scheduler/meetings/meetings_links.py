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
from ....types.scheduler.meetings import meetings_link_book_params
from ....types.scheduler.external_booking_info import ExternalBookingInfo
from ....types.scheduler.external_booking_form_field_param import ExternalBookingFormFieldParam
from ....types.scheduler.external_meeting_booking_response import ExternalMeetingBookingResponse
from ....types.scheduler.external_legal_consent_response_param import ExternalLegalConsentResponseParam
from ....types.scheduler.external_link_availability_and_busy_times import ExternalLinkAvailabilityAndBusyTimes
from ....types.scheduler.collection_response_with_total_external_link_metadata_forward_paging import (
    CollectionResponseWithTotalExternalLinkMetadataForwardPaging,
)

__all__ = ["MeetingsLinksResource", "AsyncMeetingsLinksResource"]


class MeetingsLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MeetingsLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MeetingsLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeetingsLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MeetingsLinksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalExternalLinkMetadataForwardPaging:
        """Get a paged list meeting scheduling pages"""
        return self._get(
            "/scheduler/v3/meetings/meeting-links",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalExternalLinkMetadataForwardPaging,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scheduler/v3/meetings/meeting-links/book",
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
                meetings_link_book_params.MeetingsLinkBookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalMeetingBookingResponse,
        )

    def get_availability_by_slug(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalLinkAvailabilityAndBusyTimes:
        """
        Get the next availability times for a meeting page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/scheduler/v3/meetings/meeting-links/book/availability-page/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalLinkAvailabilityAndBusyTimes,
        )

    def get_booking_info_by_slug(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBookingInfo:
        """
        Get details about the initial information necessary for a meeting scheduler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/scheduler/v3/meetings/meeting-links/book/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBookingInfo,
        )


class AsyncMeetingsLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMeetingsLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeetingsLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeetingsLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMeetingsLinksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalExternalLinkMetadataForwardPaging:
        """Get a paged list meeting scheduling pages"""
        return await self._get(
            "/scheduler/v3/meetings/meeting-links",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalExternalLinkMetadataForwardPaging,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scheduler/v3/meetings/meeting-links/book",
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
                meetings_link_book_params.MeetingsLinkBookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalMeetingBookingResponse,
        )

    async def get_availability_by_slug(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalLinkAvailabilityAndBusyTimes:
        """
        Get the next availability times for a meeting page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/scheduler/v3/meetings/meeting-links/book/availability-page/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalLinkAvailabilityAndBusyTimes,
        )

    async def get_booking_info_by_slug(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBookingInfo:
        """
        Get details about the initial information necessary for a meeting scheduler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/scheduler/v3/meetings/meeting-links/book/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBookingInfo,
        )


class MeetingsLinksResourceWithRawResponse:
    def __init__(self, meetings_links: MeetingsLinksResource) -> None:
        self._meetings_links = meetings_links

        self.list = to_raw_response_wrapper(
            meetings_links.list,
        )
        self.book = to_raw_response_wrapper(
            meetings_links.book,
        )
        self.get_availability_by_slug = to_raw_response_wrapper(
            meetings_links.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = to_raw_response_wrapper(
            meetings_links.get_booking_info_by_slug,
        )


class AsyncMeetingsLinksResourceWithRawResponse:
    def __init__(self, meetings_links: AsyncMeetingsLinksResource) -> None:
        self._meetings_links = meetings_links

        self.list = async_to_raw_response_wrapper(
            meetings_links.list,
        )
        self.book = async_to_raw_response_wrapper(
            meetings_links.book,
        )
        self.get_availability_by_slug = async_to_raw_response_wrapper(
            meetings_links.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = async_to_raw_response_wrapper(
            meetings_links.get_booking_info_by_slug,
        )


class MeetingsLinksResourceWithStreamingResponse:
    def __init__(self, meetings_links: MeetingsLinksResource) -> None:
        self._meetings_links = meetings_links

        self.list = to_streamed_response_wrapper(
            meetings_links.list,
        )
        self.book = to_streamed_response_wrapper(
            meetings_links.book,
        )
        self.get_availability_by_slug = to_streamed_response_wrapper(
            meetings_links.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = to_streamed_response_wrapper(
            meetings_links.get_booking_info_by_slug,
        )


class AsyncMeetingsLinksResourceWithStreamingResponse:
    def __init__(self, meetings_links: AsyncMeetingsLinksResource) -> None:
        self._meetings_links = meetings_links

        self.list = async_to_streamed_response_wrapper(
            meetings_links.list,
        )
        self.book = async_to_streamed_response_wrapper(
            meetings_links.book,
        )
        self.get_availability_by_slug = async_to_streamed_response_wrapper(
            meetings_links.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = async_to_streamed_response_wrapper(
            meetings_links.get_booking_info_by_slug,
        )
