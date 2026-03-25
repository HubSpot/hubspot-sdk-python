# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cms import audit_log_list_params, audit_log_export_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cms.public_audit_log import PublicAuditLog
from ...types.cms.cms_audit_logging_export_filters_param import CmsAuditLoggingExportFiltersParam

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        event_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        object_id: SequenceNotStr[str] | Omit = omit,
        object_type: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        user_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicAuditLog]:
        """
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
            "/cms/audit-logs/2026-03",
            page=SyncPage[PublicAuditLog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "event_type": event_type,
                        "limit": limit,
                        "object_id": object_id,
                        "object_type": object_type,
                        "sort": sort,
                        "user_id": user_id,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=PublicAuditLog,
        )

    def export(
        self,
        *,
        email: str,
        format: Literal["CSV", "XLS", "XLSX"],
        portal_id: int,
        recipient_user_ids: Iterable[int],
        should_mark_export_file_as_sensitive: bool,
        type: str,
        filters: CmsAuditLoggingExportFiltersParam | Omit = omit,
        partition: int | Omit = omit,
        user_id: int | Omit = omit,
        user_time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/audit-logs/2026-03/export",
            body=maybe_transform(
                {
                    "email": email,
                    "format": format,
                    "portal_id": portal_id,
                    "recipient_user_ids": recipient_user_ids,
                    "should_mark_export_file_as_sensitive": should_mark_export_file_as_sensitive,
                    "type": type,
                    "filters": filters,
                    "partition": partition,
                    "user_id": user_id,
                    "user_time_zone": user_time_zone,
                },
                audit_log_export_params.AuditLogExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        event_type: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        object_id: SequenceNotStr[str] | Omit = omit,
        object_type: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        user_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicAuditLog, AsyncPage[PublicAuditLog]]:
        """
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
            "/cms/audit-logs/2026-03",
            page=AsyncPage[PublicAuditLog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "event_type": event_type,
                        "limit": limit,
                        "object_id": object_id,
                        "object_type": object_type,
                        "sort": sort,
                        "user_id": user_id,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=PublicAuditLog,
        )

    async def export(
        self,
        *,
        email: str,
        format: Literal["CSV", "XLS", "XLSX"],
        portal_id: int,
        recipient_user_ids: Iterable[int],
        should_mark_export_file_as_sensitive: bool,
        type: str,
        filters: CmsAuditLoggingExportFiltersParam | Omit = omit,
        partition: int | Omit = omit,
        user_id: int | Omit = omit,
        user_time_zone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/audit-logs/2026-03/export",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "format": format,
                    "portal_id": portal_id,
                    "recipient_user_ids": recipient_user_ids,
                    "should_mark_export_file_as_sensitive": should_mark_export_file_as_sensitive,
                    "type": type,
                    "filters": filters,
                    "partition": partition,
                    "user_id": user_id,
                    "user_time_zone": user_time_zone,
                },
                audit_log_export_params.AuditLogExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )
        self.export = to_raw_response_wrapper(
            audit_logs.export,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )
        self.export = async_to_raw_response_wrapper(
            audit_logs.export,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.export = to_streamed_response_wrapper(
            audit_logs.export,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.export = async_to_streamed_response_wrapper(
            audit_logs.export,
        )
