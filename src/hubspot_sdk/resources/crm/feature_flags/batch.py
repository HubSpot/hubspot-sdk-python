# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ....types.crm.feature_flags import batch_delete_params, batch_upsert_params
from ....types.crm.batch_portal_entry_param import BatchPortalEntryParam
from ....types.crm.portal_flag_state_batch_response import PortalFlagStateBatchResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def delete(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateBatchResponse:
        """Delete an account-level flag state for multiple HubSpot accounts at once.

        Use
        this endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._post(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/batch/delete",
                app_id=app_id,
                flag_name=flag_name,
            ),
            body=maybe_transform({"portal_ids": portal_ids}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateBatchResponse,
        )

    def upsert(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_states: Iterable[BatchPortalEntryParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateBatchResponse:
        """Set the portal flag state for multiple HubSpot accounts at once.

        Use this
        endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._post(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/batch/upsert",
                app_id=app_id,
                flag_name=flag_name,
            ),
            body=maybe_transform({"portal_states": portal_states}, batch_upsert_params.BatchUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateBatchResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def delete(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateBatchResponse:
        """Delete an account-level flag state for multiple HubSpot accounts at once.

        Use
        this endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._post(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/batch/delete",
                app_id=app_id,
                flag_name=flag_name,
            ),
            body=await async_maybe_transform({"portal_ids": portal_ids}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateBatchResponse,
        )

    async def upsert(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_states: Iterable[BatchPortalEntryParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateBatchResponse:
        """Set the portal flag state for multiple HubSpot accounts at once.

        Use this
        endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._post(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/batch/upsert",
                app_id=app_id,
                flag_name=flag_name,
            ),
            body=await async_maybe_transform({"portal_states": portal_states}, batch_upsert_params.BatchUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateBatchResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.delete = to_raw_response_wrapper(
            batch.delete,
        )
        self.upsert = to_raw_response_wrapper(
            batch.upsert,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.delete = async_to_raw_response_wrapper(
            batch.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            batch.upsert,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.delete = to_streamed_response_wrapper(
            batch.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            batch.upsert,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.delete = async_to_streamed_response_wrapper(
            batch.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            batch.upsert,
        )
