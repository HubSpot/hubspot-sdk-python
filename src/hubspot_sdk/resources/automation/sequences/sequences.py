# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from .enrollments import (
    EnrollmentsResource,
    AsyncEnrollmentsResource,
    EnrollmentsResourceWithRawResponse,
    AsyncEnrollmentsResourceWithRawResponse,
    EnrollmentsResourceWithStreamingResponse,
    AsyncEnrollmentsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.automation.public_sequence_response import PublicSequenceResponse
from ....types.automation.collection_response_with_total_public_sequence_lite_response_forward_paging import (
    CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging,
)

__all__ = ["SequencesResource", "AsyncSequencesResource"]


class SequencesResource(SyncAPIResource):
    @cached_property
    def enrollments(self) -> EnrollmentsResource:
        return EnrollmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SequencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SequencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SequencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SequencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging:
        """Retrieve a list of sequences that belong to a specific user."""
        return self._get(
            "/automation/v4/sequences/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging,
        )

    def get(
        self,
        sequence_id: str,
        *,
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
            f"/automation/v4/sequences/{sequence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSequenceResponse,
        )


class AsyncSequencesResource(AsyncAPIResource):
    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResource:
        return AsyncEnrollmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSequencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSequencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSequencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSequencesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging:
        """Retrieve a list of sequences that belong to a specific user."""
        return await self._get(
            "/automation/v4/sequences/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging,
        )

    async def get(
        self,
        sequence_id: str,
        *,
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
            f"/automation/v4/sequences/{sequence_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSequenceResponse,
        )


class SequencesResourceWithRawResponse:
    def __init__(self, sequences: SequencesResource) -> None:
        self._sequences = sequences

        self.list = to_raw_response_wrapper(
            sequences.list,
        )
        self.get = to_raw_response_wrapper(
            sequences.get,
        )

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithRawResponse:
        return EnrollmentsResourceWithRawResponse(self._sequences.enrollments)


class AsyncSequencesResourceWithRawResponse:
    def __init__(self, sequences: AsyncSequencesResource) -> None:
        self._sequences = sequences

        self.list = async_to_raw_response_wrapper(
            sequences.list,
        )
        self.get = async_to_raw_response_wrapper(
            sequences.get,
        )

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithRawResponse:
        return AsyncEnrollmentsResourceWithRawResponse(self._sequences.enrollments)


class SequencesResourceWithStreamingResponse:
    def __init__(self, sequences: SequencesResource) -> None:
        self._sequences = sequences

        self.list = to_streamed_response_wrapper(
            sequences.list,
        )
        self.get = to_streamed_response_wrapper(
            sequences.get,
        )

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithStreamingResponse:
        return EnrollmentsResourceWithStreamingResponse(self._sequences.enrollments)


class AsyncSequencesResourceWithStreamingResponse:
    def __init__(self, sequences: AsyncSequencesResource) -> None:
        self._sequences = sequences

        self.list = async_to_streamed_response_wrapper(
            sequences.list,
        )
        self.get = async_to_streamed_response_wrapper(
            sequences.get,
        )

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        return AsyncEnrollmentsResourceWithStreamingResponse(self._sequences.enrollments)
