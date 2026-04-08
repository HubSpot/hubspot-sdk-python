# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ..._base_client import make_request_options
from ...types.webhooks import (
    webhook_update_settings_params,
    webhook_get_journal_batch_params,
    webhook_get_latest_journal_params,
    webhook_create_crm_snapshot_params,
    webhook_create_subscription_params,
    webhook_update_subscription_params,
    webhook_get_earliest_journal_params,
    webhook_get_local_journal_batch_params,
    webhook_get_latest_journal_batch_params,
    webhook_get_latest_local_journal_params,
    webhook_create_subscription_filter_params,
    webhook_create_subscriptions_batch_params,
    webhook_get_earliest_journal_batch_params,
    webhook_get_earliest_local_journal_params,
    webhook_get_next_journal_after_offset_params,
    webhook_get_journal_batch_after_offset_params,
    webhook_get_latest_local_journal_batch_params,
    webhook_get_earliest_local_journal_batch_params,
    webhook_get_next_local_journal_after_offset_params,
    webhook_get_local_journal_batch_after_offset_params,
)
from ...types.webhooks.filter_param import FilterParam
from ...types.webhooks.filter_response import FilterResponse
from ...types.webhooks.settings_response import SettingsResponse
from ...types.webhooks.subscription_response import SubscriptionResponse
from ...types.webhooks.filter_create_response import FilterCreateResponse
from ...types.webhooks.subscription_response_1 import SubscriptionResponse1
from ...types.webhooks.snapshot_status_response import SnapshotStatusResponse
from ...types.webhooks.throttling_settings_param import ThrottlingSettingsParam
from ...types.webhooks.subscription_list_response import SubscriptionListResponse
from ...types.webhooks.crm_object_snapshot_request_param import CrmObjectSnapshotRequestParam
from ...types.webhooks.crm_object_snapshot_batch_response import CrmObjectSnapshotBatchResponse
from ...types.webhooks.batch_response_subscription_response import BatchResponseSubscriptionResponse
from ...types.webhooks.batch_response_journal_fetch_response import BatchResponseJournalFetchResponse
from ...types.webhooks.subscription_batch_update_request_param import SubscriptionBatchUpdateRequestParam
from ...types.webhooks.webhook_get_subscription_filters_response import WebhookGetSubscriptionFiltersResponse
from ...types.webhooks.collection_response_subscription_response_no_paging import (
    CollectionResponseSubscriptionResponseNoPaging,
)

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create_crm_snapshot(
        self,
        *,
        snapshot_requests: Iterable[CrmObjectSnapshotRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrmObjectSnapshotBatchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/snapshots/2026-03/crm",
            body=maybe_transform(
                {"snapshot_requests": snapshot_requests},
                webhook_create_crm_snapshot_params.WebhookCreateCrmSnapshotParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmObjectSnapshotBatchResponse,
        )

    @overload
    def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    @overload
    def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    @overload
    def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    @overload
    def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1:
        return self._post(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse1,
        )

    def create_subscription(
        self,
        app_id: int,
        *,
        active: bool,
        event_type: Literal[
            "company.associationChange",
            "company.creation",
            "company.deletion",
            "company.merge",
            "company.propertyChange",
            "company.restore",
            "contact.associationChange",
            "contact.creation",
            "contact.deletion",
            "contact.merge",
            "contact.privacyDeletion",
            "contact.propertyChange",
            "contact.restore",
            "conversation.creation",
            "conversation.deletion",
            "conversation.newMessage",
            "conversation.privacyDeletion",
            "conversation.propertyChange",
            "deal.associationChange",
            "deal.creation",
            "deal.deletion",
            "deal.merge",
            "deal.propertyChange",
            "deal.restore",
            "event.completed",
            "line_item.associationChange",
            "line_item.creation",
            "line_item.deletion",
            "line_item.merge",
            "line_item.propertyChange",
            "line_item.restore",
            "object.associationChange",
            "object.creation",
            "object.deletion",
            "object.merge",
            "object.propertyChange",
            "object.restore",
            "product.creation",
            "product.deletion",
            "product.merge",
            "product.propertyChange",
            "product.restore",
            "ticket.associationChange",
            "ticket.creation",
            "ticket.deletion",
            "ticket.merge",
            "ticket.propertyChange",
            "ticket.restore",
        ],
        event_type_name: str | Omit = omit,
        object_type_id: str | Omit = omit,
        property_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create new event subscription for the specified app.

        Args:
          active: Determines if the subscription is active or paused. Defaults to false.

          event_type: Type of event to listen for. Can be one of `create`, `delete`,
              `deletedForPrivacy`, or `propertyChange`.

          event_type_name: The name of the event to listen for. This is used with custom objects to specify
              custom event types beyond the standard eventType enum values.

          object_type_id: The ID of the object type for the subscription. This can be a standard CRM
              object (e.g., 'contact', 'company', 'deal') or a custom object ID for custom
              object subscriptions.

          property_name: The internal name of the property to monitor for changes. Only applies when
              `eventType` is `propertyChange`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
            body=maybe_transform(
                {
                    "active": active,
                    "event_type": event_type,
                    "event_type_name": event_type_name,
                    "object_type_id": object_type_id,
                    "property_name": property_name,
                },
                webhook_create_subscription_params.WebhookCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    def create_subscription_filter(
        self,
        *,
        filter: FilterParam,
        subscription_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterCreateResponse:
        """
        Args:
          filter: Defines a single condition for searching CRM objects, specifying the property to
              filter on, the operator to use (such as equals, greater than, or contains), and
              the value(s) to compare against.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/subscriptions/2026-03/filters",
            body=maybe_transform(
                {
                    "filter": filter,
                    "subscription_id": subscription_id,
                },
                webhook_create_subscription_filter_params.WebhookCreateSubscriptionFilterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterCreateResponse,
        )

    def create_subscriptions_batch(
        self,
        app_id: int,
        *,
        inputs: Iterable[SubscriptionBatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriptionResponse:
        """
        Batch create event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=maybe_transform(
                {"inputs": inputs}, webhook_create_subscriptions_batch_params.WebhookCreateSubscriptionsBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
        )

    def delete_journal_subscription(
        self,
        subscription_id: int,
        *,
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
        return self._delete(
            path_template("/webhooks-journal/subscriptions/2026-03/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_portal_subscriptions(
        self,
        portal_id: int,
        *,
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
        return self._delete(
            path_template("/webhooks-journal/subscriptions/2026-03/portals/{portal_id}", portal_id=portal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_settings(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the webhook settings for the specified app.

        Event subscriptions will not
        be deleted, but will be paused until another webhook is created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/webhooks/2026-03/{app_id}/settings", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_subscription(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_subscription_filter(
        self,
        filter_id: int,
        *,
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
        return self._delete(
            path_template("/webhooks-journal/subscriptions/2026-03/filters/{filter_id}", filter_id=filter_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_earliest_journal(
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
        Args:
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
                    {"install_portal_id": install_portal_id},
                    webhook_get_earliest_journal_params.WebhookGetEarliestJournalParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_earliest_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/earliest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_earliest_journal_batch_params.WebhookGetEarliestJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_earliest_local_journal(
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
        Args:
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
                    webhook_get_earliest_local_journal_params.WebhookGetEarliestLocalJournalParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_earliest_local_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/journal-local/2026-03/batch/earliest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_earliest_local_journal_batch_params.WebhookGetEarliestLocalJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_journal_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=maybe_transform({"inputs": inputs}, webhook_get_journal_batch_params.WebhookGetJournalBatchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_journal_batch_params.WebhookGetJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_journal_batch_after_offset(
        self,
        count: int,
        *,
        offset: str,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/{offset}/next/{count}", offset=offset, count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_journal_batch_after_offset_params.WebhookGetJournalBatchAfterOffsetParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_journal_status(
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

    def get_latest_journal(
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
        Args:
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
                    webhook_get_latest_journal_params.WebhookGetLatestJournalParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_latest_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/latest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_latest_journal_batch_params.WebhookGetLatestJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_latest_local_journal(
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/webhooks-journal/journal-local/2026-03/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_latest_local_journal_params.WebhookGetLatestLocalJournalParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_latest_local_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/journal-local/2026-03/batch/latest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_latest_local_journal_batch_params.WebhookGetLatestLocalJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_local_journal_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/journal-local/2026-03/batch/read",
            body=maybe_transform(
                {"inputs": inputs}, webhook_get_local_journal_batch_params.WebhookGetLocalJournalBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_local_journal_batch_params.WebhookGetLocalJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_local_journal_batch_after_offset(
        self,
        count: int,
        *,
        offset: str,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return self._get(
            path_template(
                "/webhooks-journal/journal-local/2026-03/batch/{offset}/next/{count}", offset=offset, count=count
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_local_journal_batch_after_offset_params.WebhookGetLocalJournalBatchAfterOffsetParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_local_journal_status(
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

    def get_next_journal_after_offset(
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
        Args:
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
                    webhook_get_next_journal_after_offset_params.WebhookGetNextJournalAfterOffsetParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_next_local_journal_after_offset(
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
        Args:
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
                    webhook_get_next_local_journal_after_offset_params.WebhookGetNextLocalJournalAfterOffsetParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_settings(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Retrieve the webhook settings for the specified app, including the webhook’s
        target URL, throttle configuration, and create/update date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks/2026-03/{app_id}/settings", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    def get_subscription(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Retrieve a specific event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template(
                "/webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    def get_subscription_filter(
        self,
        filter_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/subscriptions/2026-03/filters/{filter_id}", filter_id=filter_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterResponse,
        )

    def get_subscription_filters(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetSubscriptionFiltersResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template(
                "/webhooks-journal/subscriptions/2026-03/filters/subscription/{subscription_id}",
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetSubscriptionFiltersResponse,
        )

    def list_journal_subscriptions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseSubscriptionResponseNoPaging:
        return self._get(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseSubscriptionResponseNoPaging,
        )

    def list_subscriptions(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """
        Retrieve event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
        )

    def update_settings(
        self,
        app_id: int,
        *,
        target_url: str,
        throttling: ThrottlingSettingsParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Update webhook settings for the specified app.

        Args:
          target_url: A publicly available URL for Hubspot to call where event payloads will be
              delivered. See [link-so-some-doc](#) for details about the format of these event
              payloads.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            path_template("/webhooks/2026-03/{app_id}/settings", app_id=app_id),
            body=maybe_transform(
                {
                    "target_url": target_url,
                    "throttling": throttling,
                },
                webhook_update_settings_params.WebhookUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    def update_subscription(
        self,
        subscription_id: int,
        *,
        app_id: int,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Update an existing event subscription by ID.

        Args:
          active: Whether to activate or pause the webhook subscription. If true, the subscription
              will send webhook notifications. If false, the subscription is paused and will
              not send notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template(
                "/webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            body=maybe_transform(
                {"active": active}, webhook_update_subscription_params.WebhookUpdateSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create_crm_snapshot(
        self,
        *,
        snapshot_requests: Iterable[CrmObjectSnapshotRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrmObjectSnapshotBatchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/snapshots/2026-03/crm",
            body=await async_maybe_transform(
                {"snapshot_requests": snapshot_requests},
                webhook_create_crm_snapshot_params.WebhookCreateCrmSnapshotParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmObjectSnapshotBatchResponse,
        )

    @overload
    async def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    @overload
    async def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    @overload
    async def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    @overload
    async def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1: ...
    async def create_journal_subscription(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1:
        return await self._post(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse1,
        )

    async def create_subscription(
        self,
        app_id: int,
        *,
        active: bool,
        event_type: Literal[
            "company.associationChange",
            "company.creation",
            "company.deletion",
            "company.merge",
            "company.propertyChange",
            "company.restore",
            "contact.associationChange",
            "contact.creation",
            "contact.deletion",
            "contact.merge",
            "contact.privacyDeletion",
            "contact.propertyChange",
            "contact.restore",
            "conversation.creation",
            "conversation.deletion",
            "conversation.newMessage",
            "conversation.privacyDeletion",
            "conversation.propertyChange",
            "deal.associationChange",
            "deal.creation",
            "deal.deletion",
            "deal.merge",
            "deal.propertyChange",
            "deal.restore",
            "event.completed",
            "line_item.associationChange",
            "line_item.creation",
            "line_item.deletion",
            "line_item.merge",
            "line_item.propertyChange",
            "line_item.restore",
            "object.associationChange",
            "object.creation",
            "object.deletion",
            "object.merge",
            "object.propertyChange",
            "object.restore",
            "product.creation",
            "product.deletion",
            "product.merge",
            "product.propertyChange",
            "product.restore",
            "ticket.associationChange",
            "ticket.creation",
            "ticket.deletion",
            "ticket.merge",
            "ticket.propertyChange",
            "ticket.restore",
        ],
        event_type_name: str | Omit = omit,
        object_type_id: str | Omit = omit,
        property_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create new event subscription for the specified app.

        Args:
          active: Determines if the subscription is active or paused. Defaults to false.

          event_type: Type of event to listen for. Can be one of `create`, `delete`,
              `deletedForPrivacy`, or `propertyChange`.

          event_type_name: The name of the event to listen for. This is used with custom objects to specify
              custom event types beyond the standard eventType enum values.

          object_type_id: The ID of the object type for the subscription. This can be a standard CRM
              object (e.g., 'contact', 'company', 'deal') or a custom object ID for custom
              object subscriptions.

          property_name: The internal name of the property to monitor for changes. Only applies when
              `eventType` is `propertyChange`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "event_type": event_type,
                    "event_type_name": event_type_name,
                    "object_type_id": object_type_id,
                    "property_name": property_name,
                },
                webhook_create_subscription_params.WebhookCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    async def create_subscription_filter(
        self,
        *,
        filter: FilterParam,
        subscription_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterCreateResponse:
        """
        Args:
          filter: Defines a single condition for searching CRM objects, specifying the property to
              filter on, the operator to use (such as equals, greater than, or contains), and
              the value(s) to compare against.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/subscriptions/2026-03/filters",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "subscription_id": subscription_id,
                },
                webhook_create_subscription_filter_params.WebhookCreateSubscriptionFilterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterCreateResponse,
        )

    async def create_subscriptions_batch(
        self,
        app_id: int,
        *,
        inputs: Iterable[SubscriptionBatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriptionResponse:
        """
        Batch create event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=await async_maybe_transform(
                {"inputs": inputs}, webhook_create_subscriptions_batch_params.WebhookCreateSubscriptionsBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
        )

    async def delete_journal_subscription(
        self,
        subscription_id: int,
        *,
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
        return await self._delete(
            path_template("/webhooks-journal/subscriptions/2026-03/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_portal_subscriptions(
        self,
        portal_id: int,
        *,
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
        return await self._delete(
            path_template("/webhooks-journal/subscriptions/2026-03/portals/{portal_id}", portal_id=portal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_settings(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the webhook settings for the specified app.

        Event subscriptions will not
        be deleted, but will be paused until another webhook is created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/webhooks/2026-03/{app_id}/settings", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_subscription(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_subscription_filter(
        self,
        filter_id: int,
        *,
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
        return await self._delete(
            path_template("/webhooks-journal/subscriptions/2026-03/filters/{filter_id}", filter_id=filter_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_earliest_journal(
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
        Args:
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
                    {"install_portal_id": install_portal_id},
                    webhook_get_earliest_journal_params.WebhookGetEarliestJournalParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_earliest_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/earliest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_earliest_journal_batch_params.WebhookGetEarliestJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_earliest_local_journal(
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
        Args:
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
                    webhook_get_earliest_local_journal_params.WebhookGetEarliestLocalJournalParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_earliest_local_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/journal-local/2026-03/batch/earliest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_earliest_local_journal_batch_params.WebhookGetEarliestLocalJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_journal_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, webhook_get_journal_batch_params.WebhookGetJournalBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_journal_batch_params.WebhookGetJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_journal_batch_after_offset(
        self,
        count: int,
        *,
        offset: str,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/{offset}/next/{count}", offset=offset, count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_journal_batch_after_offset_params.WebhookGetJournalBatchAfterOffsetParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_journal_status(
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

    async def get_latest_journal(
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
        Args:
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
                    webhook_get_latest_journal_params.WebhookGetLatestJournalParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_latest_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/journal/2026-03/batch/latest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_latest_journal_batch_params.WebhookGetLatestJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_latest_local_journal(
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/webhooks-journal/journal-local/2026-03/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_latest_local_journal_params.WebhookGetLatestLocalJournalParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_latest_local_journal_batch(
        self,
        count: int,
        *,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/journal-local/2026-03/batch/latest/{count}", count=count),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_latest_local_journal_batch_params.WebhookGetLatestLocalJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_local_journal_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/journal-local/2026-03/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, webhook_get_local_journal_batch_params.WebhookGetLocalJournalBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_local_journal_batch_params.WebhookGetLocalJournalBatchParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_local_journal_batch_after_offset(
        self,
        count: int,
        *,
        offset: str,
        install_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseJournalFetchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return await self._get(
            path_template(
                "/webhooks-journal/journal-local/2026-03/batch/{offset}/next/{count}", offset=offset, count=count
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_local_journal_batch_after_offset_params.WebhookGetLocalJournalBatchAfterOffsetParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_local_journal_status(
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

    async def get_next_journal_after_offset(
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
        Args:
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
                    webhook_get_next_journal_after_offset_params.WebhookGetNextJournalAfterOffsetParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_next_local_journal_after_offset(
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
        Args:
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
                    webhook_get_next_local_journal_after_offset_params.WebhookGetNextLocalJournalAfterOffsetParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_settings(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Retrieve the webhook settings for the specified app, including the webhook’s
        target URL, throttle configuration, and create/update date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks/2026-03/{app_id}/settings", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    async def get_subscription(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Retrieve a specific event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template(
                "/webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    async def get_subscription_filter(
        self,
        filter_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/subscriptions/2026-03/filters/{filter_id}", filter_id=filter_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterResponse,
        )

    async def get_subscription_filters(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetSubscriptionFiltersResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template(
                "/webhooks-journal/subscriptions/2026-03/filters/subscription/{subscription_id}",
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetSubscriptionFiltersResponse,
        )

    async def list_journal_subscriptions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseSubscriptionResponseNoPaging:
        return await self._get(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseSubscriptionResponseNoPaging,
        )

    async def list_subscriptions(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """
        Retrieve event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
        )

    async def update_settings(
        self,
        app_id: int,
        *,
        target_url: str,
        throttling: ThrottlingSettingsParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Update webhook settings for the specified app.

        Args:
          target_url: A publicly available URL for Hubspot to call where event payloads will be
              delivered. See [link-so-some-doc](#) for details about the format of these event
              payloads.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            path_template("/webhooks/2026-03/{app_id}/settings", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "target_url": target_url,
                    "throttling": throttling,
                },
                webhook_update_settings_params.WebhookUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    async def update_subscription(
        self,
        subscription_id: int,
        *,
        app_id: int,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Update an existing event subscription by ID.

        Args:
          active: Whether to activate or pause the webhook subscription. If true, the subscription
              will send webhook notifications. If false, the subscription is paused and will
              not send notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template(
                "/webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            body=await async_maybe_transform(
                {"active": active}, webhook_update_subscription_params.WebhookUpdateSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_crm_snapshot = to_raw_response_wrapper(
            webhooks.create_crm_snapshot,
        )
        self.create_journal_subscription = to_raw_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription = to_raw_response_wrapper(
            webhooks.create_subscription,
        )
        self.create_subscription_filter = to_raw_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.create_subscriptions_batch = to_raw_response_wrapper(
            webhooks.create_subscriptions_batch,
        )
        self.delete_journal_subscription = to_raw_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_portal_subscriptions = to_raw_response_wrapper(
            webhooks.delete_portal_subscriptions,
        )
        self.delete_settings = to_raw_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription = to_raw_response_wrapper(
            webhooks.delete_subscription,
        )
        self.delete_subscription_filter = to_raw_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal = to_custom_raw_response_wrapper(
            webhooks.get_earliest_journal,
            BinaryAPIResponse,
        )
        self.get_earliest_journal_batch = to_raw_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_local_journal = to_custom_raw_response_wrapper(
            webhooks.get_earliest_local_journal,
            BinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = to_raw_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_journal_batch = to_raw_response_wrapper(
            webhooks.get_journal_batch,
        )
        self.get_journal_batch_after_offset = to_raw_response_wrapper(
            webhooks.get_journal_batch_after_offset,
        )
        self.get_journal_status = to_raw_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_latest_journal = to_custom_raw_response_wrapper(
            webhooks.get_latest_journal,
            BinaryAPIResponse,
        )
        self.get_latest_journal_batch = to_raw_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_local_journal = to_custom_raw_response_wrapper(
            webhooks.get_latest_local_journal,
            BinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = to_raw_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_local_journal_batch = to_raw_response_wrapper(
            webhooks.get_local_journal_batch,
        )
        self.get_local_journal_batch_after_offset = to_raw_response_wrapper(
            webhooks.get_local_journal_batch_after_offset,
        )
        self.get_local_journal_status = to_raw_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_after_offset = to_custom_raw_response_wrapper(
            webhooks.get_next_journal_after_offset,
            BinaryAPIResponse,
        )
        self.get_next_local_journal_after_offset = to_custom_raw_response_wrapper(
            webhooks.get_next_local_journal_after_offset,
            BinaryAPIResponse,
        )
        self.get_settings = to_raw_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription = to_raw_response_wrapper(
            webhooks.get_subscription,
        )
        self.get_subscription_filter = to_raw_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.get_subscription_filters = to_raw_response_wrapper(
            webhooks.get_subscription_filters,
        )
        self.list_journal_subscriptions = to_raw_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            webhooks.list_subscriptions,
        )
        self.update_settings = to_raw_response_wrapper(
            webhooks.update_settings,
        )
        self.update_subscription = to_raw_response_wrapper(
            webhooks.update_subscription,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_crm_snapshot = async_to_raw_response_wrapper(
            webhooks.create_crm_snapshot,
        )
        self.create_journal_subscription = async_to_raw_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription = async_to_raw_response_wrapper(
            webhooks.create_subscription,
        )
        self.create_subscription_filter = async_to_raw_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.create_subscriptions_batch = async_to_raw_response_wrapper(
            webhooks.create_subscriptions_batch,
        )
        self.delete_journal_subscription = async_to_raw_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_portal_subscriptions = async_to_raw_response_wrapper(
            webhooks.delete_portal_subscriptions,
        )
        self.delete_settings = async_to_raw_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription = async_to_raw_response_wrapper(
            webhooks.delete_subscription,
        )
        self.delete_subscription_filter = async_to_raw_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal = async_to_custom_raw_response_wrapper(
            webhooks.get_earliest_journal,
            AsyncBinaryAPIResponse,
        )
        self.get_earliest_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_local_journal = async_to_custom_raw_response_wrapper(
            webhooks.get_earliest_local_journal,
            AsyncBinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_journal_batch,
        )
        self.get_journal_batch_after_offset = async_to_raw_response_wrapper(
            webhooks.get_journal_batch_after_offset,
        )
        self.get_journal_status = async_to_raw_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_latest_journal = async_to_custom_raw_response_wrapper(
            webhooks.get_latest_journal,
            AsyncBinaryAPIResponse,
        )
        self.get_latest_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_local_journal = async_to_custom_raw_response_wrapper(
            webhooks.get_latest_local_journal,
            AsyncBinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_local_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_local_journal_batch,
        )
        self.get_local_journal_batch_after_offset = async_to_raw_response_wrapper(
            webhooks.get_local_journal_batch_after_offset,
        )
        self.get_local_journal_status = async_to_raw_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_after_offset = async_to_custom_raw_response_wrapper(
            webhooks.get_next_journal_after_offset,
            AsyncBinaryAPIResponse,
        )
        self.get_next_local_journal_after_offset = async_to_custom_raw_response_wrapper(
            webhooks.get_next_local_journal_after_offset,
            AsyncBinaryAPIResponse,
        )
        self.get_settings = async_to_raw_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription = async_to_raw_response_wrapper(
            webhooks.get_subscription,
        )
        self.get_subscription_filter = async_to_raw_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.get_subscription_filters = async_to_raw_response_wrapper(
            webhooks.get_subscription_filters,
        )
        self.list_journal_subscriptions = async_to_raw_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            webhooks.list_subscriptions,
        )
        self.update_settings = async_to_raw_response_wrapper(
            webhooks.update_settings,
        )
        self.update_subscription = async_to_raw_response_wrapper(
            webhooks.update_subscription,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_crm_snapshot = to_streamed_response_wrapper(
            webhooks.create_crm_snapshot,
        )
        self.create_journal_subscription = to_streamed_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription = to_streamed_response_wrapper(
            webhooks.create_subscription,
        )
        self.create_subscription_filter = to_streamed_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.create_subscriptions_batch = to_streamed_response_wrapper(
            webhooks.create_subscriptions_batch,
        )
        self.delete_journal_subscription = to_streamed_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_portal_subscriptions = to_streamed_response_wrapper(
            webhooks.delete_portal_subscriptions,
        )
        self.delete_settings = to_streamed_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription = to_streamed_response_wrapper(
            webhooks.delete_subscription,
        )
        self.delete_subscription_filter = to_streamed_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal = to_custom_streamed_response_wrapper(
            webhooks.get_earliest_journal,
            StreamedBinaryAPIResponse,
        )
        self.get_earliest_journal_batch = to_streamed_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_local_journal = to_custom_streamed_response_wrapper(
            webhooks.get_earliest_local_journal,
            StreamedBinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = to_streamed_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_journal_batch = to_streamed_response_wrapper(
            webhooks.get_journal_batch,
        )
        self.get_journal_batch_after_offset = to_streamed_response_wrapper(
            webhooks.get_journal_batch_after_offset,
        )
        self.get_journal_status = to_streamed_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_latest_journal = to_custom_streamed_response_wrapper(
            webhooks.get_latest_journal,
            StreamedBinaryAPIResponse,
        )
        self.get_latest_journal_batch = to_streamed_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_local_journal = to_custom_streamed_response_wrapper(
            webhooks.get_latest_local_journal,
            StreamedBinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = to_streamed_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_local_journal_batch = to_streamed_response_wrapper(
            webhooks.get_local_journal_batch,
        )
        self.get_local_journal_batch_after_offset = to_streamed_response_wrapper(
            webhooks.get_local_journal_batch_after_offset,
        )
        self.get_local_journal_status = to_streamed_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_after_offset = to_custom_streamed_response_wrapper(
            webhooks.get_next_journal_after_offset,
            StreamedBinaryAPIResponse,
        )
        self.get_next_local_journal_after_offset = to_custom_streamed_response_wrapper(
            webhooks.get_next_local_journal_after_offset,
            StreamedBinaryAPIResponse,
        )
        self.get_settings = to_streamed_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription = to_streamed_response_wrapper(
            webhooks.get_subscription,
        )
        self.get_subscription_filter = to_streamed_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.get_subscription_filters = to_streamed_response_wrapper(
            webhooks.get_subscription_filters,
        )
        self.list_journal_subscriptions = to_streamed_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            webhooks.list_subscriptions,
        )
        self.update_settings = to_streamed_response_wrapper(
            webhooks.update_settings,
        )
        self.update_subscription = to_streamed_response_wrapper(
            webhooks.update_subscription,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_crm_snapshot = async_to_streamed_response_wrapper(
            webhooks.create_crm_snapshot,
        )
        self.create_journal_subscription = async_to_streamed_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription = async_to_streamed_response_wrapper(
            webhooks.create_subscription,
        )
        self.create_subscription_filter = async_to_streamed_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.create_subscriptions_batch = async_to_streamed_response_wrapper(
            webhooks.create_subscriptions_batch,
        )
        self.delete_journal_subscription = async_to_streamed_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_portal_subscriptions = async_to_streamed_response_wrapper(
            webhooks.delete_portal_subscriptions,
        )
        self.delete_settings = async_to_streamed_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription = async_to_streamed_response_wrapper(
            webhooks.delete_subscription,
        )
        self.delete_subscription_filter = async_to_streamed_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal = async_to_custom_streamed_response_wrapper(
            webhooks.get_earliest_journal,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_earliest_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_local_journal = async_to_custom_streamed_response_wrapper(
            webhooks.get_earliest_local_journal,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_journal_batch,
        )
        self.get_journal_batch_after_offset = async_to_streamed_response_wrapper(
            webhooks.get_journal_batch_after_offset,
        )
        self.get_journal_status = async_to_streamed_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_latest_journal = async_to_custom_streamed_response_wrapper(
            webhooks.get_latest_journal,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_latest_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_local_journal = async_to_custom_streamed_response_wrapper(
            webhooks.get_latest_local_journal,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_local_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_local_journal_batch,
        )
        self.get_local_journal_batch_after_offset = async_to_streamed_response_wrapper(
            webhooks.get_local_journal_batch_after_offset,
        )
        self.get_local_journal_status = async_to_streamed_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_after_offset = async_to_custom_streamed_response_wrapper(
            webhooks.get_next_journal_after_offset,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_next_local_journal_after_offset = async_to_custom_streamed_response_wrapper(
            webhooks.get_next_local_journal_after_offset,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_settings = async_to_streamed_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription = async_to_streamed_response_wrapper(
            webhooks.get_subscription,
        )
        self.get_subscription_filter = async_to_streamed_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.get_subscription_filters = async_to_streamed_response_wrapper(
            webhooks.get_subscription_filters,
        )
        self.list_journal_subscriptions = async_to_streamed_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            webhooks.list_subscriptions,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            webhooks.update_settings,
        )
        self.update_subscription = async_to_streamed_response_wrapper(
            webhooks.update_subscription,
        )
