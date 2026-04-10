# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

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
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.account import (
    activity_list_audit_logs_params,
    activity_list_login_activities_params,
    activity_list_security_activities_params,
)
from ...types.account.public_login_audit import PublicLoginAudit
from ...types.account.hydrated_critical_action import HydratedCriticalAction
from ...types.account.public_api_user_action_event import PublicAPIUserActionEvent

__all__ = ["ActivityResource", "AsyncActivityResource"]


class ActivityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return ActivityResourceWithStreamingResponse(self)

    def list_audit_logs(
        self,
        *,
        acting_user_id: Iterable[int] | Omit = omit,
        after: str | Omit = omit,
        fill_final_timestamp: bool | Omit = omit,
        limit: int | Omit = omit,
        occurred_after: Union[str, datetime] | Omit = omit,
        occurred_before: Union[str, datetime] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicAPIUserActionEvent]:
        """
        Retrieve activity history for user actions related to approvals, content
        updates, CRM object updates, security activity, and more (Enterprise only).
        Learn more about
        [activities included in audit log exports](https://knowledge.hubspot.com/account-management/view-and-export-account-activity-history-in-a-centralized-audit-log?hubs_content=knowledge.hubspot.com/account-management/view-and-export-account-activity-history&hubs_content-cta=centralized%20audit%20log#data-included-in-the-centralized-audit-log).

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
            "/account-info/2026-03/activity/audit-logs",
            page=SyncPage[PublicAPIUserActionEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "acting_user_id": acting_user_id,
                        "after": after,
                        "fill_final_timestamp": fill_final_timestamp,
                        "limit": limit,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "sort": sort,
                    },
                    activity_list_audit_logs_params.ActivityListAuditLogsParams,
                ),
            ),
            model=PublicAPIUserActionEvent,
        )

    def list_login_activities(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicLoginAudit]:
        """
        Retrieve logs of user actions related to
        [login activity](https://knowledge.hubspot.com/account-management/view-and-export-account-activity-history#account-login-history).

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
            "/account-info/2026-03/activity/login",
            page=SyncPage[PublicLoginAudit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    activity_list_login_activities_params.ActivityListLoginActivitiesParams,
                ),
            ),
            model=PublicLoginAudit,
        )

    def list_security_activities(
        self,
        *,
        after: str | Omit = omit,
        from_timestamp: int | Omit = omit,
        limit: int | Omit = omit,
        to_timestamp: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[HydratedCriticalAction]:
        """
        Retrieve logs of user actions related to
        [security activity](https://knowledge.hubspot.com/account-management/view-and-export-account-activity-history#security-activity-history).

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
            "/account-info/2026-03/activity/security",
            page=SyncPage[HydratedCriticalAction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "from_timestamp": from_timestamp,
                        "limit": limit,
                        "to_timestamp": to_timestamp,
                        "user_id": user_id,
                    },
                    activity_list_security_activities_params.ActivityListSecurityActivitiesParams,
                ),
            ),
            model=HydratedCriticalAction,
        )


class AsyncActivityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncActivityResourceWithStreamingResponse(self)

    def list_audit_logs(
        self,
        *,
        acting_user_id: Iterable[int] | Omit = omit,
        after: str | Omit = omit,
        fill_final_timestamp: bool | Omit = omit,
        limit: int | Omit = omit,
        occurred_after: Union[str, datetime] | Omit = omit,
        occurred_before: Union[str, datetime] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicAPIUserActionEvent, AsyncPage[PublicAPIUserActionEvent]]:
        """
        Retrieve activity history for user actions related to approvals, content
        updates, CRM object updates, security activity, and more (Enterprise only).
        Learn more about
        [activities included in audit log exports](https://knowledge.hubspot.com/account-management/view-and-export-account-activity-history-in-a-centralized-audit-log?hubs_content=knowledge.hubspot.com/account-management/view-and-export-account-activity-history&hubs_content-cta=centralized%20audit%20log#data-included-in-the-centralized-audit-log).

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
            "/account-info/2026-03/activity/audit-logs",
            page=AsyncPage[PublicAPIUserActionEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "acting_user_id": acting_user_id,
                        "after": after,
                        "fill_final_timestamp": fill_final_timestamp,
                        "limit": limit,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "sort": sort,
                    },
                    activity_list_audit_logs_params.ActivityListAuditLogsParams,
                ),
            ),
            model=PublicAPIUserActionEvent,
        )

    def list_login_activities(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicLoginAudit, AsyncPage[PublicLoginAudit]]:
        """
        Retrieve logs of user actions related to
        [login activity](https://knowledge.hubspot.com/account-management/view-and-export-account-activity-history#account-login-history).

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
            "/account-info/2026-03/activity/login",
            page=AsyncPage[PublicLoginAudit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    activity_list_login_activities_params.ActivityListLoginActivitiesParams,
                ),
            ),
            model=PublicLoginAudit,
        )

    def list_security_activities(
        self,
        *,
        after: str | Omit = omit,
        from_timestamp: int | Omit = omit,
        limit: int | Omit = omit,
        to_timestamp: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[HydratedCriticalAction, AsyncPage[HydratedCriticalAction]]:
        """
        Retrieve logs of user actions related to
        [security activity](https://knowledge.hubspot.com/account-management/view-and-export-account-activity-history#security-activity-history).

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
            "/account-info/2026-03/activity/security",
            page=AsyncPage[HydratedCriticalAction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "from_timestamp": from_timestamp,
                        "limit": limit,
                        "to_timestamp": to_timestamp,
                        "user_id": user_id,
                    },
                    activity_list_security_activities_params.ActivityListSecurityActivitiesParams,
                ),
            ),
            model=HydratedCriticalAction,
        )


class ActivityResourceWithRawResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list_audit_logs = to_raw_response_wrapper(
            activity.list_audit_logs,
        )
        self.list_login_activities = to_raw_response_wrapper(
            activity.list_login_activities,
        )
        self.list_security_activities = to_raw_response_wrapper(
            activity.list_security_activities,
        )


class AsyncActivityResourceWithRawResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list_audit_logs = async_to_raw_response_wrapper(
            activity.list_audit_logs,
        )
        self.list_login_activities = async_to_raw_response_wrapper(
            activity.list_login_activities,
        )
        self.list_security_activities = async_to_raw_response_wrapper(
            activity.list_security_activities,
        )


class ActivityResourceWithStreamingResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list_audit_logs = to_streamed_response_wrapper(
            activity.list_audit_logs,
        )
        self.list_login_activities = to_streamed_response_wrapper(
            activity.list_login_activities,
        )
        self.list_security_activities = to_streamed_response_wrapper(
            activity.list_security_activities,
        )


class AsyncActivityResourceWithStreamingResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list_audit_logs = async_to_streamed_response_wrapper(
            activity.list_audit_logs,
        )
        self.list_login_activities = async_to_streamed_response_wrapper(
            activity.list_login_activities,
        )
        self.list_security_activities = async_to_streamed_response_wrapper(
            activity.list_security_activities,
        )
