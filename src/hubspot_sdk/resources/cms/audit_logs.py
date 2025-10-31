# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cms import audit_log_list_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cms.public_audit_log import PublicAuditLog

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
        Returns audit logs based on filters.

        Args:
          after: Timestamp after which audit logs will be returned

          before: Timestamp before which audit logs will be returned

          event_type: Comma separated list of event types to filter by (CREATED, UPDATED, PUBLISHED,
              DELETED, UNPUBLISHED).

          limit: The number of logs to return.

          object_id: Comma separated list of object ids to filter by.

          object_type: Comma separated list of object types to filter by (BLOG, LANDING_PAGE, DOMAIN,
              HUBDB_TABLE etc.)

          sort: The sort direction for the audit logs. (Can only sort by timestamp).

          user_id: Comma separated list of user ids to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/audit-logs/",
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
        Returns audit logs based on filters.

        Args:
          after: Timestamp after which audit logs will be returned

          before: Timestamp before which audit logs will be returned

          event_type: Comma separated list of event types to filter by (CREATED, UPDATED, PUBLISHED,
              DELETED, UNPUBLISHED).

          limit: The number of logs to return.

          object_id: Comma separated list of object ids to filter by.

          object_type: Comma separated list of object types to filter by (BLOG, LANDING_PAGE, DOMAIN,
              HUBDB_TABLE etc.)

          sort: The sort direction for the audit logs. (Can only sort by timestamp).

          user_id: Comma separated list of user ids to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/audit-logs/",
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


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
