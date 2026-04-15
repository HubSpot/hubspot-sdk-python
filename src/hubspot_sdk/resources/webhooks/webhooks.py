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
        """Create a batch of CRM object snapshots for a specified portal.

        This endpoint
        allows you to capture the current state of CRM objects by submitting a batch
        request with the necessary object details. It is useful for tracking changes or
        maintaining historical records of CRM data.

        Args:
          snapshot_requests: An array of CrmObjectSnapshotRequest objects, each representing a request to
              capture a snapshot of a specific CRM object. This property is required.

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
          active: A boolean indicating whether the subscription is active. This field is required.

          event_type: A string representing the type of event to subscribe to. Valid values include
              various object changes such as 'contact.propertyChange', 'deal.creation', and
              'conversation.newMessage'.

          event_type_name: A string that provides a human-readable name for the event type. This is
              optional.

          object_type_id: A string representing the identifier of the object type for which the
              subscription is being created. This is optional.

          property_name: A string indicating the name of the property that triggers the event. This is
              optional and used when subscribing to property change events.

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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        """Create a new filter for a webhook subscription in the HubSpot account.

        This
        endpoint allows you to define conditions that determine when a webhook event
        should be triggered for a specific subscription. The request body must include
        the subscription ID and the filter details.

        Args:
          filter: Defines a single condition for searching CRM objects, specifying the property to
              filter on, the operator to use (such as equals, greater than, or contains), and
              the value(s) to compare against.

          subscription_id: The unique identifier of the subscription to which the filter will be applied.
              It is an integer in int64 format.

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
        longer needed.

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
        removes the subscription associated with the given portalId, effectively
        stopping any webhook events from being sent to the portal.

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
        """Remove a specific filter from your webhook journal subscriptions.

        This operation
        is useful when you need to clean up or modify the filters applied to your
        webhook subscriptions. The filter identified by the filterId will be permanently
        deleted.

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
        allowing you to process or analyze them as needed.

        Args:
          install_portal_id: The ID of the portal installation for which to fetch the journal entries. This
              is an optional parameter.

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
        Retrieve the earliest entry from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the initial entries in the journal, which
        can be helpful for debugging or auditing purposes.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries. This is an
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
        Retrieve the earliest batch of webhook journal entries up to a specified count.
        This endpoint is useful for accessing the oldest records available in the
        webhook journal, allowing you to process or analyze historical webhook data.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. It is
              an integer value.

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
        This endpoint is useful for accessing the oldest available data in the journal,
        which can be used for historical analysis or troubleshooting.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the earliest journal entry. This
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
        """Read a batch of webhook journal entries for the specified portal.

        This endpoint
        allows you to retrieve detailed information about webhook events processed by
        your HubSpot account. It is useful for auditing and tracking webhook activity.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal from which to retrieve webhook journal entries. This is an
              integer value.

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
        This endpoint allows you to specify the number of entries to retrieve, helping
        you manage and paginate through large sets of webhook data efficiently.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. This
              parameter is optional and is used to specify which portal's data to retrieve.

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
        Retrieve the status of a specific webhook journal entry using its unique status
        ID. This endpoint is useful for monitoring the progress or outcome of a webhook
        operation, providing insights into whether it is pending, in progress,
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
        Retrieve details of a specific webhook journal subscription using its unique
        identifier. This endpoint is useful for obtaining information about a particular
        subscription, such as its actions, object types, and associated properties.

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
        """
        Retrieve the latest batch of webhook journal entries up to a specified count.
        This endpoint is useful for fetching the most recent webhook events processed by
        your HubSpot account. The response includes details about each event, and you
        can specify the number of entries to retrieve.

        Args:
          install_portal_id: The ID of the portal installation. This parameter is optional and can be used to
              filter results by a specific portal.

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
        Retrieve the latest entry from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the most recent webhook data available in
        the journal.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the latest journal entry. It is an
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
        """
        Retrieve the latest batch of webhook journal entries up to a specified count.
        This endpoint is useful for fetching the most recent webhook events processed by
        the system. It requires authentication and supports various security schemes.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. It is
              an optional integer parameter.

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
        """Retrieve the latest entries from the webhooks journal.

        This endpoint is useful
        for accessing the most recent webhook data for analysis or troubleshooting. It
        supports filtering by the installPortalId to narrow down results to a specific
        portal.

        Args:
          install_portal_id: An integer representing the ID of the portal to filter the webhook journal
              entries.

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
        to retrieve a batch of journal entries by providing the necessary input data. It
        is useful for processing large volumes of webhook data efficiently.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal where the webhook is installed. This parameter is optional
              and is used to specify the portal context for the operation.

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
        This endpoint is useful for fetching sequential batches of data, allowing you to
        paginate through large sets of webhook journal entries efficiently.

        Args:
          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

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
        ID. This endpoint is useful for checking the progress or result of a webhook
        operation, such as whether it is pending, in progress, completed, failed, or
        expired.

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
        Retrieve the next set of webhook journal entries starting from a specified
        offset. This endpoint is useful for paginating through webhook journal entries
        in a HubSpot account. It allows you to continue fetching entries from where the
        last request left off, using the offset parameter.

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
        """Retrieve the next set of journal entries starting from a specified offset.

        This
        endpoint is useful for paginating through webhook journal entries in a
        sequential manner. It requires specifying the offset from which the next entries
        should be fetched.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries by. This is an
              optional parameter.

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
        """Retrieve a specific filter associated with a webhook journal subscription.

        This
        endpoint allows you to access detailed information about the filter identified
        by the filterId path parameter. It is useful for managing and reviewing filter
        configurations within your webhook subscriptions.

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
        """Retrieve a list of webhook journal subscriptions for the specified version.

        This
        endpoint allows you to view all active subscriptions without pagination. It is
        useful for managing and auditing webhook subscriptions in your HubSpot account.
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
        """Retrieve the filters associated with a specific webhook subscription.

        This
        endpoint is useful for obtaining detailed information about the filters applied
        to a subscription, which can help in managing and understanding the data flow
        through your webhook integrations.

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
        """Create a batch of CRM object snapshots for a specified portal.

        This endpoint
        allows you to capture the current state of CRM objects by submitting a batch
        request with the necessary object details. It is useful for tracking changes or
        maintaining historical records of CRM data.

        Args:
          snapshot_requests: An array of CrmObjectSnapshotRequest objects, each representing a request to
              capture a snapshot of a specific CRM object. This property is required.

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
          active: A boolean indicating whether the subscription is active. This field is required.

          event_type: A string representing the type of event to subscribe to. Valid values include
              various object changes such as 'contact.propertyChange', 'deal.creation', and
              'conversation.newMessage'.

          event_type_name: A string that provides a human-readable name for the event type. This is
              optional.

          object_type_id: A string representing the identifier of the object type for which the
              subscription is being created. This is optional.

          property_name: A string indicating the name of the property that triggers the event. This is
              optional and used when subscribing to property change events.

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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        Create a new subscription in the webhooks journal for the specified version.
        This endpoint allows you to define the subscription details, including actions
        and object types, to manage webhook events effectively. It requires a valid
        request body with the subscription details.
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
        """Create a new filter for a webhook subscription in the HubSpot account.

        This
        endpoint allows you to define conditions that determine when a webhook event
        should be triggered for a specific subscription. The request body must include
        the subscription ID and the filter details.

        Args:
          filter: Defines a single condition for searching CRM objects, specifying the property to
              filter on, the operator to use (such as equals, greater than, or contains), and
              the value(s) to compare against.

          subscription_id: The unique identifier of the subscription to which the filter will be applied.
              It is an integer in int64 format.

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
        longer needed.

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
        removes the subscription associated with the given portalId, effectively
        stopping any webhook events from being sent to the portal.

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
        """Remove a specific filter from your webhook journal subscriptions.

        This operation
        is useful when you need to clean up or modify the filters applied to your
        webhook subscriptions. The filter identified by the filterId will be permanently
        deleted.

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
        allowing you to process or analyze them as needed.

        Args:
          install_portal_id: The ID of the portal installation for which to fetch the journal entries. This
              is an optional parameter.

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
        Retrieve the earliest entry from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the initial entries in the journal, which
        can be helpful for debugging or auditing purposes.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries. This is an
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
        Retrieve the earliest batch of webhook journal entries up to a specified count.
        This endpoint is useful for accessing the oldest records available in the
        webhook journal, allowing you to process or analyze historical webhook data.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. It is
              an integer value.

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
        This endpoint is useful for accessing the oldest available data in the journal,
        which can be used for historical analysis or troubleshooting.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the earliest journal entry. This
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
        """Read a batch of webhook journal entries for the specified portal.

        This endpoint
        allows you to retrieve detailed information about webhook events processed by
        your HubSpot account. It is useful for auditing and tracking webhook activity.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal from which to retrieve webhook journal entries. This is an
              integer value.

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
        This endpoint allows you to specify the number of entries to retrieve, helping
        you manage and paginate through large sets of webhook data efficiently.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. This
              parameter is optional and is used to specify which portal's data to retrieve.

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
        Retrieve the status of a specific webhook journal entry using its unique status
        ID. This endpoint is useful for monitoring the progress or outcome of a webhook
        operation, providing insights into whether it is pending, in progress,
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
        Retrieve details of a specific webhook journal subscription using its unique
        identifier. This endpoint is useful for obtaining information about a particular
        subscription, such as its actions, object types, and associated properties.

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
        """
        Retrieve the latest batch of webhook journal entries up to a specified count.
        This endpoint is useful for fetching the most recent webhook events processed by
        your HubSpot account. The response includes details about each event, and you
        can specify the number of entries to retrieve.

        Args:
          install_portal_id: The ID of the portal installation. This parameter is optional and can be used to
              filter results by a specific portal.

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
        Retrieve the latest entry from the webhooks journal for the specified portal.
        This endpoint is useful for accessing the most recent webhook data available in
        the journal.

        Args:
          install_portal_id: The ID of the portal for which to retrieve the latest journal entry. It is an
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
        """
        Retrieve the latest batch of webhook journal entries up to a specified count.
        This endpoint is useful for fetching the most recent webhook events processed by
        the system. It requires authentication and supports various security schemes.

        Args:
          install_portal_id: The ID of the portal installation to filter the webhook journal entries. It is
              an optional integer parameter.

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
        """Retrieve the latest entries from the webhooks journal.

        This endpoint is useful
        for accessing the most recent webhook data for analysis or troubleshooting. It
        supports filtering by the installPortalId to narrow down results to a specific
        portal.

        Args:
          install_portal_id: An integer representing the ID of the portal to filter the webhook journal
              entries.

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
        to retrieve a batch of journal entries by providing the necessary input data. It
        is useful for processing large volumes of webhook data efficiently.

        Args:
          inputs: Strings to input.

          install_portal_id: The ID of the portal where the webhook is installed. This parameter is optional
              and is used to specify the portal context for the operation.

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
        This endpoint is useful for fetching sequential batches of data, allowing you to
        paginate through large sets of webhook journal entries efficiently.

        Args:
          install_portal_id: The ID of the portal where the webhooks are installed. This is an integer value.

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
        ID. This endpoint is useful for checking the progress or result of a webhook
        operation, such as whether it is pending, in progress, completed, failed, or
        expired.

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
        Retrieve the next set of webhook journal entries starting from a specified
        offset. This endpoint is useful for paginating through webhook journal entries
        in a HubSpot account. It allows you to continue fetching entries from where the
        last request left off, using the offset parameter.

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
        """Retrieve the next set of journal entries starting from a specified offset.

        This
        endpoint is useful for paginating through webhook journal entries in a
        sequential manner. It requires specifying the offset from which the next entries
        should be fetched.

        Args:
          install_portal_id: The ID of the portal installation to filter the journal entries by. This is an
              optional parameter.

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
        """Retrieve a specific filter associated with a webhook journal subscription.

        This
        endpoint allows you to access detailed information about the filter identified
        by the filterId path parameter. It is useful for managing and reviewing filter
        configurations within your webhook subscriptions.

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
        """Retrieve a list of webhook journal subscriptions for the specified version.

        This
        endpoint allows you to view all active subscriptions without pagination. It is
        useful for managing and auditing webhook subscriptions in your HubSpot account.
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
        """Retrieve the filters associated with a specific webhook subscription.

        This
        endpoint is useful for obtaining detailed information about the filters applied
        to a subscription, which can help in managing and understanding the data flow
        through your webhook integrations.

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
