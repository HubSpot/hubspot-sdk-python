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
from ....types.webhooks_journal import (
    journal_local_get_latest_params,
    journal_local_get_earliest_params,
    journal_local_get_next_from_offset_params,
)
from ....types.shared.snapshot_status_response import SnapshotStatusResponse

__all__ = ["JournalLocalResource", "AsyncJournalLocalResource"]


class JournalLocalResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> JournalLocalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return JournalLocalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JournalLocalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return JournalLocalResourceWithStreamingResponse(self)

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
        """Retrieve the earliest webhook journal entries for the specified portal.

        This
        endpoint can be used to access the oldest records available in the webhook
        journal, which may be useful for auditing or historical analysis.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the earliest webhook journal entries.
              This parameter is optional and should be an integer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/webhooks-journal/journal-local/2026-03/earliest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_local_get_earliest_params.JournalLocalGetEarliestParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_latest(
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
        Retrieve the latest entries from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the most recent webhook events and their
        statuses, allowing you to monitor and debug webhook activity effectively.

        Args:
          install_portal_id: The unique identifier of the portal installation for which to retrieve the
              latest journal entries. This parameter is optional and should be an integer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/webhooks-journal/journal/2026-03/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_local_get_latest_params.JournalLocalGetLatestParams,
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
        Retrieve the next set of webhook journal entries starting from a specified
        offset. This endpoint is useful for paginating through large sets of webhook
        data, allowing you to continue from where a previous request left off.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. This is
              an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/webhooks-journal/journal-local/2026-03/offset/{offset}/next", offset=offset),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_local_get_next_from_offset_params.JournalLocalGetNextFromOffsetParams,
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
        ID. This endpoint is useful for monitoring the progress or outcome of webhook
        journal entries, allowing you to check if an entry is pending, in progress,
        completed, failed, or expired.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not status_id:
            raise ValueError(f"Expected a non-empty value for `status_id` but received {status_id!r}")
        return self._get(
            path_template("/webhooks-journal/journal-local/2026-03/status/{status_id}", status_id=status_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotStatusResponse,
        )


class AsyncJournalLocalResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJournalLocalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJournalLocalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJournalLocalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncJournalLocalResourceWithStreamingResponse(self)

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
        """Retrieve the earliest webhook journal entries for the specified portal.

        This
        endpoint can be used to access the oldest records available in the webhook
        journal, which may be useful for auditing or historical analysis.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the earliest webhook journal entries.
              This parameter is optional and should be an integer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/webhooks-journal/journal-local/2026-03/earliest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_local_get_earliest_params.JournalLocalGetEarliestParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_latest(
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
        Retrieve the latest entries from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the most recent webhook events and their
        statuses, allowing you to monitor and debug webhook activity effectively.

        Args:
          install_portal_id: The unique identifier of the portal installation for which to retrieve the
              latest journal entries. This parameter is optional and should be an integer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/webhooks-journal/journal/2026-03/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_local_get_latest_params.JournalLocalGetLatestParams,
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
        Retrieve the next set of webhook journal entries starting from a specified
        offset. This endpoint is useful for paginating through large sets of webhook
        data, allowing you to continue from where a previous request left off.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. This is
              an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/webhooks-journal/journal-local/2026-03/offset/{offset}/next", offset=offset),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    journal_local_get_next_from_offset_params.JournalLocalGetNextFromOffsetParams,
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
        ID. This endpoint is useful for monitoring the progress or outcome of webhook
        journal entries, allowing you to check if an entry is pending, in progress,
        completed, failed, or expired.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not status_id:
            raise ValueError(f"Expected a non-empty value for `status_id` but received {status_id!r}")
        return await self._get(
            path_template("/webhooks-journal/journal-local/2026-03/status/{status_id}", status_id=status_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotStatusResponse,
        )


class JournalLocalResourceWithRawResponse:
    def __init__(self, journal_local: JournalLocalResource) -> None:
        self._journal_local = journal_local

        self.get_earliest = to_custom_raw_response_wrapper(
            journal_local.get_earliest,
            BinaryAPIResponse,
        )
        self.get_latest = to_custom_raw_response_wrapper(
            journal_local.get_latest,
            BinaryAPIResponse,
        )
        self.get_next_from_offset = to_custom_raw_response_wrapper(
            journal_local.get_next_from_offset,
            BinaryAPIResponse,
        )
        self.get_status = to_raw_response_wrapper(
            journal_local.get_status,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._journal_local.batch)


class AsyncJournalLocalResourceWithRawResponse:
    def __init__(self, journal_local: AsyncJournalLocalResource) -> None:
        self._journal_local = journal_local

        self.get_earliest = async_to_custom_raw_response_wrapper(
            journal_local.get_earliest,
            AsyncBinaryAPIResponse,
        )
        self.get_latest = async_to_custom_raw_response_wrapper(
            journal_local.get_latest,
            AsyncBinaryAPIResponse,
        )
        self.get_next_from_offset = async_to_custom_raw_response_wrapper(
            journal_local.get_next_from_offset,
            AsyncBinaryAPIResponse,
        )
        self.get_status = async_to_raw_response_wrapper(
            journal_local.get_status,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._journal_local.batch)


class JournalLocalResourceWithStreamingResponse:
    def __init__(self, journal_local: JournalLocalResource) -> None:
        self._journal_local = journal_local

        self.get_earliest = to_custom_streamed_response_wrapper(
            journal_local.get_earliest,
            StreamedBinaryAPIResponse,
        )
        self.get_latest = to_custom_streamed_response_wrapper(
            journal_local.get_latest,
            StreamedBinaryAPIResponse,
        )
        self.get_next_from_offset = to_custom_streamed_response_wrapper(
            journal_local.get_next_from_offset,
            StreamedBinaryAPIResponse,
        )
        self.get_status = to_streamed_response_wrapper(
            journal_local.get_status,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._journal_local.batch)


class AsyncJournalLocalResourceWithStreamingResponse:
    def __init__(self, journal_local: AsyncJournalLocalResource) -> None:
        self._journal_local = journal_local

        self.get_earliest = async_to_custom_streamed_response_wrapper(
            journal_local.get_earliest,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_latest = async_to_custom_streamed_response_wrapper(
            journal_local.get_latest,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_next_from_offset = async_to_custom_streamed_response_wrapper(
            journal_local.get_next_from_offset,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_status = async_to_streamed_response_wrapper(
            journal_local.get_status,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._journal_local.batch)
