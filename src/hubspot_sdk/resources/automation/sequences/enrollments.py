# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.automation.sequences import enrollment_enroll_params
from ....types.automation.public_sequence_enrollment_response import PublicSequenceEnrollmentResponse
from ....types.automation.public_sequence_enrollment_lite_response import PublicSequenceEnrollmentLiteResponse

__all__ = ["EnrollmentsResource", "AsyncEnrollmentsResource"]


class EnrollmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EnrollmentsResourceWithStreamingResponse(self)

    def enroll(
        self,
        *,
        user_id: str,
        contact_id: str,
        sender_email: str,
        sequence_id: str,
        sender_alias_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSequenceEnrollmentLiteResponse:
        """
        Enroll a contact into a sequence using the specified user ID and sequence
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/automation/v4/sequences/enrollments",
            body=maybe_transform(
                {
                    "contact_id": contact_id,
                    "sender_email": sender_email,
                    "sequence_id": sequence_id,
                    "sender_alias_address": sender_alias_address,
                },
                enrollment_enroll_params.EnrollmentEnrollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"user_id": user_id}, enrollment_enroll_params.EnrollmentEnrollParams),
            ),
            cast_to=PublicSequenceEnrollmentLiteResponse,
        )

    def get_by_contact_id(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSequenceEnrollmentResponse:
        """
        Get the enrollment status of a contact in sequences by their contact ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            f"/automation/v4/sequences/enrollments/contact/{contact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSequenceEnrollmentResponse,
        )


class AsyncEnrollmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEnrollmentsResourceWithStreamingResponse(self)

    async def enroll(
        self,
        *,
        user_id: str,
        contact_id: str,
        sender_email: str,
        sequence_id: str,
        sender_alias_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSequenceEnrollmentLiteResponse:
        """
        Enroll a contact into a sequence using the specified user ID and sequence
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/automation/v4/sequences/enrollments",
            body=await async_maybe_transform(
                {
                    "contact_id": contact_id,
                    "sender_email": sender_email,
                    "sequence_id": sequence_id,
                    "sender_alias_address": sender_alias_address,
                },
                enrollment_enroll_params.EnrollmentEnrollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"user_id": user_id}, enrollment_enroll_params.EnrollmentEnrollParams
                ),
            ),
            cast_to=PublicSequenceEnrollmentLiteResponse,
        )

    async def get_by_contact_id(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSequenceEnrollmentResponse:
        """
        Get the enrollment status of a contact in sequences by their contact ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            f"/automation/v4/sequences/enrollments/contact/{contact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSequenceEnrollmentResponse,
        )


class EnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.enroll = to_raw_response_wrapper(
            enrollments.enroll,
        )
        self.get_by_contact_id = to_raw_response_wrapper(
            enrollments.get_by_contact_id,
        )


class AsyncEnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.enroll = async_to_raw_response_wrapper(
            enrollments.enroll,
        )
        self.get_by_contact_id = async_to_raw_response_wrapper(
            enrollments.get_by_contact_id,
        )


class EnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.enroll = to_streamed_response_wrapper(
            enrollments.enroll,
        )
        self.get_by_contact_id = to_streamed_response_wrapper(
            enrollments.get_by_contact_id,
        )


class AsyncEnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.enroll = async_to_streamed_response_wrapper(
            enrollments.enroll,
        )
        self.get_by_contact_id = async_to_streamed_response_wrapper(
            enrollments.get_by_contact_id,
        )
