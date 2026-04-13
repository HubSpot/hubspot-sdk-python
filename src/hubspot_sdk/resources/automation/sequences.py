# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.automation import sequence_get_params, sequence_list_params, sequence_create_enrollment_params
from ...types.automation.public_sequence_response import PublicSequenceResponse
from ...types.automation.public_sequence_lite_response import PublicSequenceLiteResponse
from ...types.automation.public_sequence_enrollment_response import PublicSequenceEnrollmentResponse
from ...types.automation.public_sequence_enrollment_lite_response import PublicSequenceEnrollmentLiteResponse

__all__ = ["SequencesResource", "AsyncSequencesResource"]


class SequencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SequencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SequencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SequencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SequencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        user_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicSequenceLiteResponse]:
        """Retrieve a list of sequences available in your HubSpot account.

        This endpoint
        allows you to filter sequences by user ID and name, and supports pagination for
        large result sets. Use this endpoint to manage and review your sequences
        effectively.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/automation/sequences/2026-03",
            page=SyncPage[PublicSequenceLiteResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "user_id": user_id,
                        "after": after,
                        "limit": limit,
                        "name": name,
                    },
                    sequence_list_params.SequenceListParams,
                ),
            ),
            model=PublicSequenceLiteResponse,
        )

    def create_enrollment(
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
          contact_id: The unique identifier of the contact to be enrolled in the sequence.

          sender_email: The email address of the sender enrolling the contact in the sequence.

          sequence_id: The unique identifier of the sequence in which the contact will be enrolled.

          sender_alias_address: The alias email address used by the sender when enrolling the contact.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/automation/sequences/2026-03/enrollments",
            body=maybe_transform(
                {
                    "contact_id": contact_id,
                    "sender_email": sender_email,
                    "sequence_id": sequence_id,
                    "sender_alias_address": sender_alias_address,
                },
                sequence_create_enrollment_params.SequenceCreateEnrollmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"user_id": user_id}, sequence_create_enrollment_params.SequenceCreateEnrollmentParams
                ),
            ),
            cast_to=PublicSequenceEnrollmentLiteResponse,
        )

    def get(
        self,
        sequence_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSequenceResponse:
        """
        Retrieve details of a specific sequence by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return self._get(
            path_template("/automation/sequences/2026-03/{sequence_id}", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"user_id": user_id}, sequence_get_params.SequenceGetParams),
            ),
            cast_to=PublicSequenceResponse,
        )

    def get_enrollment_by_contact_id(
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
            path_template("/automation/sequences/2026-03/enrollments/contact/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSequenceEnrollmentResponse,
        )


class AsyncSequencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSequencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSequencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSequencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSequencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        user_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicSequenceLiteResponse, AsyncPage[PublicSequenceLiteResponse]]:
        """Retrieve a list of sequences available in your HubSpot account.

        This endpoint
        allows you to filter sequences by user ID and name, and supports pagination for
        large result sets. Use this endpoint to manage and review your sequences
        effectively.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/automation/sequences/2026-03",
            page=AsyncPage[PublicSequenceLiteResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "user_id": user_id,
                        "after": after,
                        "limit": limit,
                        "name": name,
                    },
                    sequence_list_params.SequenceListParams,
                ),
            ),
            model=PublicSequenceLiteResponse,
        )

    async def create_enrollment(
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
          contact_id: The unique identifier of the contact to be enrolled in the sequence.

          sender_email: The email address of the sender enrolling the contact in the sequence.

          sequence_id: The unique identifier of the sequence in which the contact will be enrolled.

          sender_alias_address: The alias email address used by the sender when enrolling the contact.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/automation/sequences/2026-03/enrollments",
            body=await async_maybe_transform(
                {
                    "contact_id": contact_id,
                    "sender_email": sender_email,
                    "sequence_id": sequence_id,
                    "sender_alias_address": sender_alias_address,
                },
                sequence_create_enrollment_params.SequenceCreateEnrollmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"user_id": user_id}, sequence_create_enrollment_params.SequenceCreateEnrollmentParams
                ),
            ),
            cast_to=PublicSequenceEnrollmentLiteResponse,
        )

    async def get(
        self,
        sequence_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSequenceResponse:
        """
        Retrieve details of a specific sequence by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sequence_id:
            raise ValueError(f"Expected a non-empty value for `sequence_id` but received {sequence_id!r}")
        return await self._get(
            path_template("/automation/sequences/2026-03/{sequence_id}", sequence_id=sequence_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"user_id": user_id}, sequence_get_params.SequenceGetParams),
            ),
            cast_to=PublicSequenceResponse,
        )

    async def get_enrollment_by_contact_id(
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
            path_template("/automation/sequences/2026-03/enrollments/contact/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSequenceEnrollmentResponse,
        )


class SequencesResourceWithRawResponse:
    def __init__(self, sequences: SequencesResource) -> None:
        self._sequences = sequences

        self.list = to_raw_response_wrapper(
            sequences.list,
        )
        self.create_enrollment = to_raw_response_wrapper(
            sequences.create_enrollment,
        )
        self.get = to_raw_response_wrapper(
            sequences.get,
        )
        self.get_enrollment_by_contact_id = to_raw_response_wrapper(
            sequences.get_enrollment_by_contact_id,
        )


class AsyncSequencesResourceWithRawResponse:
    def __init__(self, sequences: AsyncSequencesResource) -> None:
        self._sequences = sequences

        self.list = async_to_raw_response_wrapper(
            sequences.list,
        )
        self.create_enrollment = async_to_raw_response_wrapper(
            sequences.create_enrollment,
        )
        self.get = async_to_raw_response_wrapper(
            sequences.get,
        )
        self.get_enrollment_by_contact_id = async_to_raw_response_wrapper(
            sequences.get_enrollment_by_contact_id,
        )


class SequencesResourceWithStreamingResponse:
    def __init__(self, sequences: SequencesResource) -> None:
        self._sequences = sequences

        self.list = to_streamed_response_wrapper(
            sequences.list,
        )
        self.create_enrollment = to_streamed_response_wrapper(
            sequences.create_enrollment,
        )
        self.get = to_streamed_response_wrapper(
            sequences.get,
        )
        self.get_enrollment_by_contact_id = to_streamed_response_wrapper(
            sequences.get_enrollment_by_contact_id,
        )


class AsyncSequencesResourceWithStreamingResponse:
    def __init__(self, sequences: AsyncSequencesResource) -> None:
        self._sequences = sequences

        self.list = async_to_streamed_response_wrapper(
            sequences.list,
        )
        self.create_enrollment = async_to_streamed_response_wrapper(
            sequences.create_enrollment,
        )
        self.get = async_to_streamed_response_wrapper(
            sequences.get,
        )
        self.get_enrollment_by_contact_id = async_to_streamed_response_wrapper(
            sequences.get_enrollment_by_contact_id,
        )
