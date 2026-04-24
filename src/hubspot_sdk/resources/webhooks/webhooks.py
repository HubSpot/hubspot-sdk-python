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
    webhook_create_crm_snapshots_params,
    webhook_get_latest_journal_batch_params,
    webhook_get_latest_journal_entry_params,
    webhook_get_next_journal_entries_params,
    webhook_create_event_subscription_params,
    webhook_update_event_subscription_params,
    webhook_create_subscription_filter_params,
    webhook_get_earliest_journal_batch_params,
    webhook_get_earliest_journal_entry_params,
    webhook_get_journal_batch_by_request_params,
    webhook_get_journal_batch_from_offset_params,
    webhook_get_latest_local_journal_batch_params,
    webhook_get_latest_local_journal_entry_params,
    webhook_get_next_local_journal_entries_params,
    webhook_create_batch_event_subscriptions_params,
    webhook_get_earliest_local_journal_batch_params,
    webhook_get_earliest_local_journal_entry_params,
    webhook_get_local_journal_batch_by_request_params,
    webhook_get_local_journal_batch_from_offset_params,
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
from ...types.webhooks.webhook_list_subscription_filters_response import WebhookListSubscriptionFiltersResponse
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

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create_batch_event_subscriptions(
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
          inputs: An array of SubscriptionBatchUpdateRequest objects, each representing a
              subscription to be updated. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=maybe_transform(
                {"inputs": inputs},
                webhook_create_batch_event_subscriptions_params.WebhookCreateBatchEventSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
        )

    def create_crm_snapshots(
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
        """Create a batch of CRM object snapshots for the specified portal.

        This endpoint
        allows you to capture the state of CRM objects at a specific point in time,
        which can be useful for auditing or historical analysis. The request requires a
        list of CRM object snapshot requests, each specifying the portal ID, object ID,
        object type ID, and properties to include in the snapshot.

        Args:
          snapshot_requests: An array of CrmObjectSnapshotRequest objects, each representing a request to
              create a snapshot for a specific CRM object. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/snapshots/2026-03/crm",
            body=maybe_transform(
                {"snapshot_requests": snapshot_requests},
                webhook_create_crm_snapshots_params.WebhookCreateCrmSnapshotsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmObjectSnapshotBatchResponse,
        )

    def create_event_subscription(
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
          active: A boolean indicating whether the subscription is active.

          event_type: A string representing the type of event to subscribe to. Valid values include
              various property changes, creations, deletions, merges, restorations,
              association changes, and event completions.

          event_type_name: A string providing a human-readable name for the event type.

          object_type_id: A string representing the ID of the object type associated with the
              subscription.

          property_name: A string indicating the specific property name related to the event type, if
              applicable.

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
                webhook_create_event_subscription_params.WebhookCreateEventSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
        """Create a new filter for a webhook subscription in your HubSpot account.

        This
        endpoint allows you to define specific conditions that a webhook event must meet
        to trigger the subscription. It is useful for managing and customizing the
        behavior of webhook subscriptions based on specific criteria.

        Args:
          filter: Defines a single condition for searching CRM objects, specifying the property to
              filter on, the operator to use (such as equals, greater than, or contains), and
              the value(s) to compare against.

          subscription_id: The unique identifier of the subscription to which the filter will be applied.
              It is an integer formatted as int64.

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

    def delete_event_subscription(
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
        """Delete a specific webhook journal subscription using its unique identifier.

        This
        operation is useful for managing and cleaning up subscriptions that are no
        longer needed or relevant.

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

    def delete_journal_subscription_for_portal(
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
        """Delete a webhook journal subscription for a specific portal.

        This operation
        removes the subscription associated with the given portalId, and no content is
        returned upon successful deletion.

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
        """Delete a specific filter associated with a webhook journal subscription.

        This
        operation is useful for managing and cleaning up filters that are no longer
        needed in your subscription setup. The endpoint requires the unique identifier
        of the filter to be deleted.

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
        """Retrieve the earliest batch of webhook journal entries up to the specified
        count.

        This endpoint is useful for fetching historical webhook data in batches,
        allowing you to process or analyze the earliest entries first.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries by. This
              is an integer value.

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

    def get_earliest_journal_entry(
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
        Retrieve the earliest entry from the webhooks journal for the specified version.
        This endpoint is useful for accessing the oldest records available in the
        journal, which can be helpful for auditing or historical data analysis.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries. It is an
              integer.

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
                    webhook_get_earliest_journal_entry_params.WebhookGetEarliestJournalEntryParams,
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
        Retrieve the earliest batch of webhook journal entries based on the specified
        count. This endpoint is useful for fetching a specific number of the earliest
        entries in the webhook journal for analysis or processing.

        Args:
          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

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

    def get_earliest_local_journal_entry(
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
        This endpoint is useful for accessing the oldest records in the journal, which
        can be helpful for auditing or tracking purposes.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries by. This
              parameter is optional and should be an integer.

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
                    webhook_get_earliest_local_journal_entry_params.WebhookGetEarliestLocalJournalEntryParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_event_subscription(
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

    def get_journal_batch_by_request(
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
        Perform a batch read operation on the webhooks journal for the specified date.
        This endpoint allows you to retrieve multiple entries from the webhooks journal
        in a single request, which can be useful for processing large amounts of data
        efficiently.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=maybe_transform(
                {"inputs": inputs}, webhook_get_journal_batch_by_request_params.WebhookGetJournalBatchByRequestParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_journal_batch_by_request_params.WebhookGetJournalBatchByRequestParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_journal_batch_from_offset(
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
        Retrieve a batch of webhook journal entries starting from a specified offset.
        This endpoint allows you to fetch a specified number of entries, making it
        useful for paginating through large sets of webhook journal data.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to specify the
              portal context for the request.

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
                    webhook_get_journal_batch_from_offset_params.WebhookGetJournalBatchFromOffsetParams,
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
        Retrieve the status of a specific webhook journal entry using its status ID.
        This endpoint is useful for checking the current state of a webhook process,
        such as whether it is pending, in progress, completed, failed, or expired.

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

    def get_journal_subscription(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1:
        """
        Retrieve details of a specific webhook subscription using its unique identifier.
        This endpoint is useful for obtaining information about a particular
        subscription's configuration and status within the HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/webhooks-journal/subscriptions/2026-03/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse1,
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
        """Retrieve the latest batch of webhook journal entries.

        This endpoint allows you
        to specify the number of entries to fetch, providing a way to access recent
        webhook activity within your HubSpot account.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to identify the
              specific portal.

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

    def get_latest_journal_entry(
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
        This endpoint is useful for accessing the most recent webhook events processed
        by your HubSpot account. It allows you to filter the results by the portal ID to
        ensure you are retrieving data relevant to a specific installation.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries. It is an
              integer value.

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
                    webhook_get_latest_journal_entry_params.WebhookGetLatestJournalEntryParams,
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
        """Retrieve the latest batch of webhook journal entries.

        This endpoint is useful
        for accessing the most recent data entries processed by the webhook journal. It
        requires specifying the number of entries to retrieve.

        Args:
          install_portal_id: The ID of the portal installation. This parameter is optional and used to filter
              the journal entries by a specific portal.

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

    def get_latest_local_journal_entry(
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
        This endpoint is useful for accessing the most recent webhook events that have
        been logged, allowing you to process or analyze them as needed.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the latest journal entries. This
              parameter is optional and should be an integer.

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
                    webhook_get_latest_local_journal_entry_params.WebhookGetLatestLocalJournalEntryParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_local_journal_batch_by_request(
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
        """Perform a batch read operation on the webhooks journal.

        This endpoint allows you
        to read multiple entries from the journal in a single request. It requires a
        JSON request body specifying the inputs to be read. The response includes the
        results of the batch read operation, and may return multiple statuses if there
        are errors.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal where the webhooks are installed. This parameter is
              optional and is used to specify the target portal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks-journal/journal-local/2026-03/batch/read",
            body=maybe_transform(
                {"inputs": inputs},
                webhook_get_local_journal_batch_by_request_params.WebhookGetLocalJournalBatchByRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_local_journal_batch_by_request_params.WebhookGetLocalJournalBatchByRequestParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    def get_local_journal_batch_from_offset(
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
        Retrieve a batch of webhook journal entries starting from a specified offset.
        This endpoint allows you to fetch a defined number of entries, facilitating the
        processing of webhook data in manageable chunks.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to specify the
              portal context for the request.

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
                    webhook_get_local_journal_batch_from_offset_params.WebhookGetLocalJournalBatchFromOffsetParams,
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
        Retrieve the status of a specific webhook journal entry using its unique status
        ID. This endpoint is useful for monitoring the progress or completion of webhook
        processing tasks.

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

    def get_next_journal_entries(
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
        Retrieve the next batch of webhook journal entries starting from a specified
        offset. This endpoint is useful for paginating through large sets of webhook
        data, allowing you to continue fetching entries from where you last left off.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. This is
              an optional parameter.

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
                    webhook_get_next_journal_entries_params.WebhookGetNextJournalEntriesParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_next_local_journal_entries(
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
        offset. This endpoint is useful for paginating through webhook journal data in a
        sequential manner, allowing you to fetch entries beyond a given point.

        Args:
          install_portal_id: The ID of the portal where the webhook is installed. This is an integer value.

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
                    webhook_get_next_local_journal_entries_params.WebhookGetNextLocalJournalEntriesParams,
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
        Retrieve details of a specific filter associated with a webhook subscription in
        the HubSpot account. This endpoint is useful for accessing the configuration and
        conditions of a filter by its unique identifier.

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

    def list_event_subscriptions(
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
        """
        Retrieve a list of webhook journal subscriptions for the specified API version.
        This endpoint provides details about each subscription, including actions,
        object types, and associated properties. It is useful for managing and reviewing
        current webhook subscriptions.
        """
        return self._get(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseSubscriptionResponseNoPaging,
        )

    def list_subscription_filters(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListSubscriptionFiltersResponse:
        """
        Retrieve the filters associated with a specific webhook subscription in the
        HubSpot account. This endpoint is useful for obtaining detailed information
        about the filters applied to a given subscription, identified by its
        subscription ID.

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
            cast_to=WebhookListSubscriptionFiltersResponse,
        )

    def update_event_subscription(
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
          active: A boolean indicating whether the subscription is active. If true, the
              subscription is active; if false, it is inactive.

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
                {"active": active}, webhook_update_event_subscription_params.WebhookUpdateEventSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
          target_url: The URL to which webhook events will be sent. It is a string.

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


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create_batch_event_subscriptions(
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
          inputs: An array of SubscriptionBatchUpdateRequest objects, each representing a
              subscription to be updated. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=await async_maybe_transform(
                {"inputs": inputs},
                webhook_create_batch_event_subscriptions_params.WebhookCreateBatchEventSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
        )

    async def create_crm_snapshots(
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
        """Create a batch of CRM object snapshots for the specified portal.

        This endpoint
        allows you to capture the state of CRM objects at a specific point in time,
        which can be useful for auditing or historical analysis. The request requires a
        list of CRM object snapshot requests, each specifying the portal ID, object ID,
        object type ID, and properties to include in the snapshot.

        Args:
          snapshot_requests: An array of CrmObjectSnapshotRequest objects, each representing a request to
              create a snapshot for a specific CRM object. This property is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/snapshots/2026-03/crm",
            body=await async_maybe_transform(
                {"snapshot_requests": snapshot_requests},
                webhook_create_crm_snapshots_params.WebhookCreateCrmSnapshotsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmObjectSnapshotBatchResponse,
        )

    async def create_event_subscription(
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
          active: A boolean indicating whether the subscription is active.

          event_type: A string representing the type of event to subscribe to. Valid values include
              various property changes, creations, deletions, merges, restorations,
              association changes, and event completions.

          event_type_name: A string providing a human-readable name for the event type.

          object_type_id: A string representing the ID of the object type associated with the
              subscription.

          property_name: A string indicating the specific property name related to the event type, if
              applicable.

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
                webhook_create_event_subscription_params.WebhookCreateEventSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
    ) -> SubscriptionResponse1:
        """
        Create a new webhook subscription for the specified portal in the HubSpot
        account. This endpoint allows you to define the subscription details, including
        the types of events you want to subscribe to. The request body must include the
        necessary subscription information as defined by the SubscriptionUpsertRequest
        schema.
        """
        ...

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
        """Create a new filter for a webhook subscription in your HubSpot account.

        This
        endpoint allows you to define specific conditions that a webhook event must meet
        to trigger the subscription. It is useful for managing and customizing the
        behavior of webhook subscriptions based on specific criteria.

        Args:
          filter: Defines a single condition for searching CRM objects, specifying the property to
              filter on, the operator to use (such as equals, greater than, or contains), and
              the value(s) to compare against.

          subscription_id: The unique identifier of the subscription to which the filter will be applied.
              It is an integer formatted as int64.

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

    async def delete_event_subscription(
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
        """Delete a specific webhook journal subscription using its unique identifier.

        This
        operation is useful for managing and cleaning up subscriptions that are no
        longer needed or relevant.

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

    async def delete_journal_subscription_for_portal(
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
        """Delete a webhook journal subscription for a specific portal.

        This operation
        removes the subscription associated with the given portalId, and no content is
        returned upon successful deletion.

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
        """Delete a specific filter associated with a webhook journal subscription.

        This
        operation is useful for managing and cleaning up filters that are no longer
        needed in your subscription setup. The endpoint requires the unique identifier
        of the filter to be deleted.

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
        """Retrieve the earliest batch of webhook journal entries up to the specified
        count.

        This endpoint is useful for fetching historical webhook data in batches,
        allowing you to process or analyze the earliest entries first.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries by. This
              is an integer value.

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

    async def get_earliest_journal_entry(
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
        Retrieve the earliest entry from the webhooks journal for the specified version.
        This endpoint is useful for accessing the oldest records available in the
        journal, which can be helpful for auditing or historical data analysis.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries. It is an
              integer.

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
                    webhook_get_earliest_journal_entry_params.WebhookGetEarliestJournalEntryParams,
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
        Retrieve the earliest batch of webhook journal entries based on the specified
        count. This endpoint is useful for fetching a specific number of the earliest
        entries in the webhook journal for analysis or processing.

        Args:
          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

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

    async def get_earliest_local_journal_entry(
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
        This endpoint is useful for accessing the oldest records in the journal, which
        can be helpful for auditing or tracking purposes.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries by. This
              parameter is optional and should be an integer.

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
                    webhook_get_earliest_local_journal_entry_params.WebhookGetEarliestLocalJournalEntryParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_event_subscription(
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

    async def get_journal_batch_by_request(
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
        Perform a batch read operation on the webhooks journal for the specified date.
        This endpoint allows you to retrieve multiple entries from the webhooks journal
        in a single request, which can be useful for processing large amounts of data
        efficiently.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/journal/2026-03/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, webhook_get_journal_batch_by_request_params.WebhookGetJournalBatchByRequestParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_journal_batch_by_request_params.WebhookGetJournalBatchByRequestParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_journal_batch_from_offset(
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
        Retrieve a batch of webhook journal entries starting from a specified offset.
        This endpoint allows you to fetch a specified number of entries, making it
        useful for paginating through large sets of webhook journal data.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to specify the
              portal context for the request.

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
                    webhook_get_journal_batch_from_offset_params.WebhookGetJournalBatchFromOffsetParams,
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
        Retrieve the status of a specific webhook journal entry using its status ID.
        This endpoint is useful for checking the current state of a webhook process,
        such as whether it is pending, in progress, completed, failed, or expired.

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

    async def get_journal_subscription(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse1:
        """
        Retrieve details of a specific webhook subscription using its unique identifier.
        This endpoint is useful for obtaining information about a particular
        subscription's configuration and status within the HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/webhooks-journal/subscriptions/2026-03/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse1,
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
        """Retrieve the latest batch of webhook journal entries.

        This endpoint allows you
        to specify the number of entries to fetch, providing a way to access recent
        webhook activity within your HubSpot account.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to identify the
              specific portal.

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

    async def get_latest_journal_entry(
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
        This endpoint is useful for accessing the most recent webhook events processed
        by your HubSpot account. It allows you to filter the results by the portal ID to
        ensure you are retrieving data relevant to a specific installation.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries. It is an
              integer value.

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
                    webhook_get_latest_journal_entry_params.WebhookGetLatestJournalEntryParams,
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
        """Retrieve the latest batch of webhook journal entries.

        This endpoint is useful
        for accessing the most recent data entries processed by the webhook journal. It
        requires specifying the number of entries to retrieve.

        Args:
          install_portal_id: The ID of the portal installation. This parameter is optional and used to filter
              the journal entries by a specific portal.

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

    async def get_latest_local_journal_entry(
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
        This endpoint is useful for accessing the most recent webhook events that have
        been logged, allowing you to process or analyze them as needed.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the latest journal entries. This
              parameter is optional and should be an integer.

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
                    webhook_get_latest_local_journal_entry_params.WebhookGetLatestLocalJournalEntryParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_local_journal_batch_by_request(
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
        """Perform a batch read operation on the webhooks journal.

        This endpoint allows you
        to read multiple entries from the journal in a single request. It requires a
        JSON request body specifying the inputs to be read. The response includes the
        results of the batch read operation, and may return multiple statuses if there
        are errors.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal where the webhooks are installed. This parameter is
              optional and is used to specify the target portal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks-journal/journal-local/2026-03/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs},
                webhook_get_local_journal_batch_by_request_params.WebhookGetLocalJournalBatchByRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"install_portal_id": install_portal_id},
                    webhook_get_local_journal_batch_by_request_params.WebhookGetLocalJournalBatchByRequestParams,
                ),
            ),
            cast_to=BatchResponseJournalFetchResponse,
        )

    async def get_local_journal_batch_from_offset(
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
        Retrieve a batch of webhook journal entries starting from a specified offset.
        This endpoint allows you to fetch a defined number of entries, facilitating the
        processing of webhook data in manageable chunks.

        Args:
          install_portal_id: The ID of the portal installation. This is an integer value used to specify the
              portal context for the request.

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
                    webhook_get_local_journal_batch_from_offset_params.WebhookGetLocalJournalBatchFromOffsetParams,
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
        Retrieve the status of a specific webhook journal entry using its unique status
        ID. This endpoint is useful for monitoring the progress or completion of webhook
        processing tasks.

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

    async def get_next_journal_entries(
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
        Retrieve the next batch of webhook journal entries starting from a specified
        offset. This endpoint is useful for paginating through large sets of webhook
        data, allowing you to continue fetching entries from where you last left off.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. This is
              an optional parameter.

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
                    webhook_get_next_journal_entries_params.WebhookGetNextJournalEntriesParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_next_local_journal_entries(
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
        offset. This endpoint is useful for paginating through webhook journal data in a
        sequential manner, allowing you to fetch entries beyond a given point.

        Args:
          install_portal_id: The ID of the portal where the webhook is installed. This is an integer value.

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
                    webhook_get_next_local_journal_entries_params.WebhookGetNextLocalJournalEntriesParams,
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
        Retrieve details of a specific filter associated with a webhook subscription in
        the HubSpot account. This endpoint is useful for accessing the configuration and
        conditions of a filter by its unique identifier.

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

    async def list_event_subscriptions(
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
        """
        Retrieve a list of webhook journal subscriptions for the specified API version.
        This endpoint provides details about each subscription, including actions,
        object types, and associated properties. It is useful for managing and reviewing
        current webhook subscriptions.
        """
        return await self._get(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseSubscriptionResponseNoPaging,
        )

    async def list_subscription_filters(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListSubscriptionFiltersResponse:
        """
        Retrieve the filters associated with a specific webhook subscription in the
        HubSpot account. This endpoint is useful for obtaining detailed information
        about the filters applied to a given subscription, identified by its
        subscription ID.

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
            cast_to=WebhookListSubscriptionFiltersResponse,
        )

    async def update_event_subscription(
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
          active: A boolean indicating whether the subscription is active. If true, the
              subscription is active; if false, it is inactive.

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
                {"active": active}, webhook_update_event_subscription_params.WebhookUpdateEventSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
          target_url: The URL to which webhook events will be sent. It is a string.

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


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_batch_event_subscriptions = to_raw_response_wrapper(
            webhooks.create_batch_event_subscriptions,
        )
        self.create_crm_snapshots = to_raw_response_wrapper(
            webhooks.create_crm_snapshots,
        )
        self.create_event_subscription = to_raw_response_wrapper(
            webhooks.create_event_subscription,
        )
        self.create_journal_subscription = to_raw_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription_filter = to_raw_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.delete_event_subscription = to_raw_response_wrapper(
            webhooks.delete_event_subscription,
        )
        self.delete_journal_subscription = to_raw_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_journal_subscription_for_portal = to_raw_response_wrapper(
            webhooks.delete_journal_subscription_for_portal,
        )
        self.delete_settings = to_raw_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription_filter = to_raw_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal_batch = to_raw_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_journal_entry = to_custom_raw_response_wrapper(
            webhooks.get_earliest_journal_entry,
            BinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = to_raw_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_earliest_local_journal_entry = to_custom_raw_response_wrapper(
            webhooks.get_earliest_local_journal_entry,
            BinaryAPIResponse,
        )
        self.get_event_subscription = to_raw_response_wrapper(
            webhooks.get_event_subscription,
        )
        self.get_journal_batch_by_request = to_raw_response_wrapper(
            webhooks.get_journal_batch_by_request,
        )
        self.get_journal_batch_from_offset = to_raw_response_wrapper(
            webhooks.get_journal_batch_from_offset,
        )
        self.get_journal_status = to_raw_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_journal_subscription = to_raw_response_wrapper(
            webhooks.get_journal_subscription,
        )
        self.get_latest_journal_batch = to_raw_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_journal_entry = to_custom_raw_response_wrapper(
            webhooks.get_latest_journal_entry,
            BinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = to_raw_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_latest_local_journal_entry = to_custom_raw_response_wrapper(
            webhooks.get_latest_local_journal_entry,
            BinaryAPIResponse,
        )
        self.get_local_journal_batch_by_request = to_raw_response_wrapper(
            webhooks.get_local_journal_batch_by_request,
        )
        self.get_local_journal_batch_from_offset = to_raw_response_wrapper(
            webhooks.get_local_journal_batch_from_offset,
        )
        self.get_local_journal_status = to_raw_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_entries = to_custom_raw_response_wrapper(
            webhooks.get_next_journal_entries,
            BinaryAPIResponse,
        )
        self.get_next_local_journal_entries = to_custom_raw_response_wrapper(
            webhooks.get_next_local_journal_entries,
            BinaryAPIResponse,
        )
        self.get_settings = to_raw_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription_filter = to_raw_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.list_event_subscriptions = to_raw_response_wrapper(
            webhooks.list_event_subscriptions,
        )
        self.list_journal_subscriptions = to_raw_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscription_filters = to_raw_response_wrapper(
            webhooks.list_subscription_filters,
        )
        self.update_event_subscription = to_raw_response_wrapper(
            webhooks.update_event_subscription,
        )
        self.update_settings = to_raw_response_wrapper(
            webhooks.update_settings,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_batch_event_subscriptions = async_to_raw_response_wrapper(
            webhooks.create_batch_event_subscriptions,
        )
        self.create_crm_snapshots = async_to_raw_response_wrapper(
            webhooks.create_crm_snapshots,
        )
        self.create_event_subscription = async_to_raw_response_wrapper(
            webhooks.create_event_subscription,
        )
        self.create_journal_subscription = async_to_raw_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription_filter = async_to_raw_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.delete_event_subscription = async_to_raw_response_wrapper(
            webhooks.delete_event_subscription,
        )
        self.delete_journal_subscription = async_to_raw_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_journal_subscription_for_portal = async_to_raw_response_wrapper(
            webhooks.delete_journal_subscription_for_portal,
        )
        self.delete_settings = async_to_raw_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription_filter = async_to_raw_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_journal_entry = async_to_custom_raw_response_wrapper(
            webhooks.get_earliest_journal_entry,
            AsyncBinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_earliest_local_journal_entry = async_to_custom_raw_response_wrapper(
            webhooks.get_earliest_local_journal_entry,
            AsyncBinaryAPIResponse,
        )
        self.get_event_subscription = async_to_raw_response_wrapper(
            webhooks.get_event_subscription,
        )
        self.get_journal_batch_by_request = async_to_raw_response_wrapper(
            webhooks.get_journal_batch_by_request,
        )
        self.get_journal_batch_from_offset = async_to_raw_response_wrapper(
            webhooks.get_journal_batch_from_offset,
        )
        self.get_journal_status = async_to_raw_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_journal_subscription = async_to_raw_response_wrapper(
            webhooks.get_journal_subscription,
        )
        self.get_latest_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_journal_entry = async_to_custom_raw_response_wrapper(
            webhooks.get_latest_journal_entry,
            AsyncBinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = async_to_raw_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_latest_local_journal_entry = async_to_custom_raw_response_wrapper(
            webhooks.get_latest_local_journal_entry,
            AsyncBinaryAPIResponse,
        )
        self.get_local_journal_batch_by_request = async_to_raw_response_wrapper(
            webhooks.get_local_journal_batch_by_request,
        )
        self.get_local_journal_batch_from_offset = async_to_raw_response_wrapper(
            webhooks.get_local_journal_batch_from_offset,
        )
        self.get_local_journal_status = async_to_raw_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_entries = async_to_custom_raw_response_wrapper(
            webhooks.get_next_journal_entries,
            AsyncBinaryAPIResponse,
        )
        self.get_next_local_journal_entries = async_to_custom_raw_response_wrapper(
            webhooks.get_next_local_journal_entries,
            AsyncBinaryAPIResponse,
        )
        self.get_settings = async_to_raw_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription_filter = async_to_raw_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.list_event_subscriptions = async_to_raw_response_wrapper(
            webhooks.list_event_subscriptions,
        )
        self.list_journal_subscriptions = async_to_raw_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscription_filters = async_to_raw_response_wrapper(
            webhooks.list_subscription_filters,
        )
        self.update_event_subscription = async_to_raw_response_wrapper(
            webhooks.update_event_subscription,
        )
        self.update_settings = async_to_raw_response_wrapper(
            webhooks.update_settings,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_batch_event_subscriptions = to_streamed_response_wrapper(
            webhooks.create_batch_event_subscriptions,
        )
        self.create_crm_snapshots = to_streamed_response_wrapper(
            webhooks.create_crm_snapshots,
        )
        self.create_event_subscription = to_streamed_response_wrapper(
            webhooks.create_event_subscription,
        )
        self.create_journal_subscription = to_streamed_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription_filter = to_streamed_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.delete_event_subscription = to_streamed_response_wrapper(
            webhooks.delete_event_subscription,
        )
        self.delete_journal_subscription = to_streamed_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_journal_subscription_for_portal = to_streamed_response_wrapper(
            webhooks.delete_journal_subscription_for_portal,
        )
        self.delete_settings = to_streamed_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription_filter = to_streamed_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal_batch = to_streamed_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_journal_entry = to_custom_streamed_response_wrapper(
            webhooks.get_earliest_journal_entry,
            StreamedBinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = to_streamed_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_earliest_local_journal_entry = to_custom_streamed_response_wrapper(
            webhooks.get_earliest_local_journal_entry,
            StreamedBinaryAPIResponse,
        )
        self.get_event_subscription = to_streamed_response_wrapper(
            webhooks.get_event_subscription,
        )
        self.get_journal_batch_by_request = to_streamed_response_wrapper(
            webhooks.get_journal_batch_by_request,
        )
        self.get_journal_batch_from_offset = to_streamed_response_wrapper(
            webhooks.get_journal_batch_from_offset,
        )
        self.get_journal_status = to_streamed_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_journal_subscription = to_streamed_response_wrapper(
            webhooks.get_journal_subscription,
        )
        self.get_latest_journal_batch = to_streamed_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_journal_entry = to_custom_streamed_response_wrapper(
            webhooks.get_latest_journal_entry,
            StreamedBinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = to_streamed_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_latest_local_journal_entry = to_custom_streamed_response_wrapper(
            webhooks.get_latest_local_journal_entry,
            StreamedBinaryAPIResponse,
        )
        self.get_local_journal_batch_by_request = to_streamed_response_wrapper(
            webhooks.get_local_journal_batch_by_request,
        )
        self.get_local_journal_batch_from_offset = to_streamed_response_wrapper(
            webhooks.get_local_journal_batch_from_offset,
        )
        self.get_local_journal_status = to_streamed_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_entries = to_custom_streamed_response_wrapper(
            webhooks.get_next_journal_entries,
            StreamedBinaryAPIResponse,
        )
        self.get_next_local_journal_entries = to_custom_streamed_response_wrapper(
            webhooks.get_next_local_journal_entries,
            StreamedBinaryAPIResponse,
        )
        self.get_settings = to_streamed_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription_filter = to_streamed_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.list_event_subscriptions = to_streamed_response_wrapper(
            webhooks.list_event_subscriptions,
        )
        self.list_journal_subscriptions = to_streamed_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscription_filters = to_streamed_response_wrapper(
            webhooks.list_subscription_filters,
        )
        self.update_event_subscription = to_streamed_response_wrapper(
            webhooks.update_event_subscription,
        )
        self.update_settings = to_streamed_response_wrapper(
            webhooks.update_settings,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_batch_event_subscriptions = async_to_streamed_response_wrapper(
            webhooks.create_batch_event_subscriptions,
        )
        self.create_crm_snapshots = async_to_streamed_response_wrapper(
            webhooks.create_crm_snapshots,
        )
        self.create_event_subscription = async_to_streamed_response_wrapper(
            webhooks.create_event_subscription,
        )
        self.create_journal_subscription = async_to_streamed_response_wrapper(
            webhooks.create_journal_subscription,
        )
        self.create_subscription_filter = async_to_streamed_response_wrapper(
            webhooks.create_subscription_filter,
        )
        self.delete_event_subscription = async_to_streamed_response_wrapper(
            webhooks.delete_event_subscription,
        )
        self.delete_journal_subscription = async_to_streamed_response_wrapper(
            webhooks.delete_journal_subscription,
        )
        self.delete_journal_subscription_for_portal = async_to_streamed_response_wrapper(
            webhooks.delete_journal_subscription_for_portal,
        )
        self.delete_settings = async_to_streamed_response_wrapper(
            webhooks.delete_settings,
        )
        self.delete_subscription_filter = async_to_streamed_response_wrapper(
            webhooks.delete_subscription_filter,
        )
        self.get_earliest_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_earliest_journal_batch,
        )
        self.get_earliest_journal_entry = async_to_custom_streamed_response_wrapper(
            webhooks.get_earliest_journal_entry,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_earliest_local_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_earliest_local_journal_batch,
        )
        self.get_earliest_local_journal_entry = async_to_custom_streamed_response_wrapper(
            webhooks.get_earliest_local_journal_entry,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_event_subscription = async_to_streamed_response_wrapper(
            webhooks.get_event_subscription,
        )
        self.get_journal_batch_by_request = async_to_streamed_response_wrapper(
            webhooks.get_journal_batch_by_request,
        )
        self.get_journal_batch_from_offset = async_to_streamed_response_wrapper(
            webhooks.get_journal_batch_from_offset,
        )
        self.get_journal_status = async_to_streamed_response_wrapper(
            webhooks.get_journal_status,
        )
        self.get_journal_subscription = async_to_streamed_response_wrapper(
            webhooks.get_journal_subscription,
        )
        self.get_latest_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_latest_journal_batch,
        )
        self.get_latest_journal_entry = async_to_custom_streamed_response_wrapper(
            webhooks.get_latest_journal_entry,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_latest_local_journal_batch = async_to_streamed_response_wrapper(
            webhooks.get_latest_local_journal_batch,
        )
        self.get_latest_local_journal_entry = async_to_custom_streamed_response_wrapper(
            webhooks.get_latest_local_journal_entry,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_local_journal_batch_by_request = async_to_streamed_response_wrapper(
            webhooks.get_local_journal_batch_by_request,
        )
        self.get_local_journal_batch_from_offset = async_to_streamed_response_wrapper(
            webhooks.get_local_journal_batch_from_offset,
        )
        self.get_local_journal_status = async_to_streamed_response_wrapper(
            webhooks.get_local_journal_status,
        )
        self.get_next_journal_entries = async_to_custom_streamed_response_wrapper(
            webhooks.get_next_journal_entries,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_next_local_journal_entries = async_to_custom_streamed_response_wrapper(
            webhooks.get_next_local_journal_entries,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_settings = async_to_streamed_response_wrapper(
            webhooks.get_settings,
        )
        self.get_subscription_filter = async_to_streamed_response_wrapper(
            webhooks.get_subscription_filter,
        )
        self.list_event_subscriptions = async_to_streamed_response_wrapper(
            webhooks.list_event_subscriptions,
        )
        self.list_journal_subscriptions = async_to_streamed_response_wrapper(
            webhooks.list_journal_subscriptions,
        )
        self.list_subscription_filters = async_to_streamed_response_wrapper(
            webhooks.list_subscription_filters,
        )
        self.update_event_subscription = async_to_streamed_response_wrapper(
            webhooks.update_event_subscription,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            webhooks.update_settings,
        )
