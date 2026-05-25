# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.webhooks_journal import journal_get_earliest_params, journal_get_next_from_offset_params
from ....types.shared.snapshot_status_response import SnapshotStatusResponse

__all__ = ["JournalResource", "AsyncJournalResource"]


class JournalResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> JournalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return JournalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JournalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return JournalResourceWithStreamingResponse(self)

    def get_earliest(
        self,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Retrieve the earliest entry from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the first recorded webhook event in the
        journal, which can be helpful for auditing or debugging purposes.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries by. This is an
              integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/webhooks-journal/journal/2026-03/earliest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id}, journal_get_earliest_params.JournalGetEarliestParams
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_next_from_offset(
        self,
        offset: str,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Retrieve the next set of entries from the webhooks journal starting from a
        specified offset. This endpoint is useful for paginating through journal entries
        to process or analyze webhook events sequentially.

        Args:
          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/offset/{offset}/next", offset=offset),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_get_next_from_offset_params.JournalGetNextFromOffsetParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_status(
        self,
        status_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotStatusResponse:
        """
        Retrieve the status of a specific webhook journal entry using its unique status
        ID. This endpoint provides detailed information about the status, including
        whether it is pending, in progress, completed, failed, or expired. It is useful
        for monitoring and managing the state of webhook journal entries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not status_id:
            raise ValueError(f"Expected a non-empty value for `status_id` but received {status_id!r}")
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/status/{status_id}", status_id=status_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotStatusResponse,
        )


class AsyncJournalResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJournalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJournalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJournalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncJournalResourceWithStreamingResponse(self)

    async def get_earliest(
        self,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve the earliest entry from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the first recorded webhook event in the
        journal, which can be helpful for auditing or debugging purposes.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries by. This is an
              integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/webhooks-journal/journal/2026-03/earliest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id}, journal_get_earliest_params.JournalGetEarliestParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_next_from_offset(
        self,
        offset: str,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve the next set of entries from the webhooks journal starting from a
        specified offset. This endpoint is useful for paginating through journal entries
        to process or analyze webhook events sequentially.

        Args:
          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/offset/{offset}/next", offset=offset),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_get_next_from_offset_params.JournalGetNextFromOffsetParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_status(
        self,
        status_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotStatusResponse:
        """
        Retrieve the status of a specific webhook journal entry using its unique status
        ID. This endpoint provides detailed information about the status, including
        whether it is pending, in progress, completed, failed, or expired. It is useful
        for monitoring and managing the state of webhook journal entries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not status_id:
            raise ValueError(f"Expected a non-empty value for `status_id` but received {status_id!r}")
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/status/{status_id}", status_id=status_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotStatusResponse,
        )


class JournalResourceWithRawResponse:
    def __init__(self, journal: JournalResource) -> None:
        self._journal = journal

        self.get_earliest = to_custom_raw_response_wrapper(
            journal.get_earliest,
            BinaryAPIResponse,
        )
        self.get_next_from_offset = to_custom_raw_response_wrapper(
            journal.get_next_from_offset,
            BinaryAPIResponse,
        )
        self.get_status = to_raw_response_wrapper(
            journal.get_status,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._journal.batch)


class AsyncJournalResourceWithRawResponse:
    def __init__(self, journal: AsyncJournalResource) -> None:
        self._journal = journal

        self.get_earliest = async_to_custom_raw_response_wrapper(
            journal.get_earliest,
            AsyncBinaryAPIResponse,
        )
        self.get_next_from_offset = async_to_custom_raw_response_wrapper(
            journal.get_next_from_offset,
            AsyncBinaryAPIResponse,
        )
        self.get_status = async_to_raw_response_wrapper(
            journal.get_status,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._journal.batch)


class JournalResourceWithStreamingResponse:
    def __init__(self, journal: JournalResource) -> None:
        self._journal = journal

        self.get_earliest = to_custom_streamed_response_wrapper(
            journal.get_earliest,
            StreamedBinaryAPIResponse,
        )
        self.get_next_from_offset = to_custom_streamed_response_wrapper(
            journal.get_next_from_offset,
            StreamedBinaryAPIResponse,
        )
        self.get_status = to_streamed_response_wrapper(
            journal.get_status,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._journal.batch)


class AsyncJournalResourceWithStreamingResponse:
    def __init__(self, journal: AsyncJournalResource) -> None:
        self._journal = journal

        self.get_earliest = async_to_custom_streamed_response_wrapper(
            journal.get_earliest,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_next_from_offset = async_to_custom_streamed_response_wrapper(
            journal.get_next_from_offset,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_status = async_to_streamed_response_wrapper(
            journal.get_status,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._journal.batch)
