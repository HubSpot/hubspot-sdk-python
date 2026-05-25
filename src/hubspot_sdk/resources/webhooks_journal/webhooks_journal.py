# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .snapshots import (
    SnapshotsResource,
    AsyncSnapshotsResource,
    SnapshotsResourceWithRawResponse,
    AsyncSnapshotsResourceWithRawResponse,
    SnapshotsResourceWithStreamingResponse,
    AsyncSnapshotsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .journal.journal import (
    JournalResource,
    AsyncJournalResource,
    JournalResourceWithRawResponse,
    AsyncJournalResourceWithRawResponse,
    JournalResourceWithStreamingResponse,
    AsyncJournalResourceWithStreamingResponse,
)
from .journal_local.journal_local import (
    JournalLocalResource,
    AsyncJournalLocalResource,
    JournalLocalResourceWithRawResponse,
    AsyncJournalLocalResourceWithRawResponse,
    JournalLocalResourceWithStreamingResponse,
    AsyncJournalLocalResourceWithStreamingResponse,
)
from .subscriptions.subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["WebhooksJournalResource", "AsyncWebhooksJournalResource"]


class WebhooksJournalResource(SyncAPIResource):
    @cached_property
    def journal(self) -> JournalResource:
        return JournalResource(self._client)

    @cached_property
    def journal_local(self) -> JournalLocalResource:
        return JournalLocalResource(self._client)

    @cached_property
    def snapshots(self) -> SnapshotsResource:
        return SnapshotsResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebhooksJournalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksJournalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksJournalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return WebhooksJournalResourceWithStreamingResponse(self)


class AsyncWebhooksJournalResource(AsyncAPIResource):
    @cached_property
    def journal(self) -> AsyncJournalResource:
        return AsyncJournalResource(self._client)

    @cached_property
    def journal_local(self) -> AsyncJournalLocalResource:
        return AsyncJournalLocalResource(self._client)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResource:
        return AsyncSnapshotsResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksJournalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksJournalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksJournalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncWebhooksJournalResourceWithStreamingResponse(self)


class WebhooksJournalResourceWithRawResponse:
    def __init__(self, webhooks_journal: WebhooksJournalResource) -> None:
        self._webhooks_journal = webhooks_journal

    @cached_property
    def journal(self) -> JournalResourceWithRawResponse:
        return JournalResourceWithRawResponse(self._webhooks_journal.journal)

    @cached_property
    def journal_local(self) -> JournalLocalResourceWithRawResponse:
        return JournalLocalResourceWithRawResponse(self._webhooks_journal.journal_local)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self._webhooks_journal.snapshots)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._webhooks_journal.subscriptions)


class AsyncWebhooksJournalResourceWithRawResponse:
    def __init__(self, webhooks_journal: AsyncWebhooksJournalResource) -> None:
        self._webhooks_journal = webhooks_journal

    @cached_property
    def journal(self) -> AsyncJournalResourceWithRawResponse:
        return AsyncJournalResourceWithRawResponse(self._webhooks_journal.journal)

    @cached_property
    def journal_local(self) -> AsyncJournalLocalResourceWithRawResponse:
        return AsyncJournalLocalResourceWithRawResponse(self._webhooks_journal.journal_local)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self._webhooks_journal.snapshots)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._webhooks_journal.subscriptions)


class WebhooksJournalResourceWithStreamingResponse:
    def __init__(self, webhooks_journal: WebhooksJournalResource) -> None:
        self._webhooks_journal = webhooks_journal

    @cached_property
    def journal(self) -> JournalResourceWithStreamingResponse:
        return JournalResourceWithStreamingResponse(self._webhooks_journal.journal)

    @cached_property
    def journal_local(self) -> JournalLocalResourceWithStreamingResponse:
        return JournalLocalResourceWithStreamingResponse(self._webhooks_journal.journal_local)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self._webhooks_journal.snapshots)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._webhooks_journal.subscriptions)


class AsyncWebhooksJournalResourceWithStreamingResponse:
    def __init__(self, webhooks_journal: AsyncWebhooksJournalResource) -> None:
        self._webhooks_journal = webhooks_journal

    @cached_property
    def journal(self) -> AsyncJournalResourceWithStreamingResponse:
        return AsyncJournalResourceWithStreamingResponse(self._webhooks_journal.journal)

    @cached_property
    def journal_local(self) -> AsyncJournalLocalResourceWithStreamingResponse:
        return AsyncJournalLocalResourceWithStreamingResponse(self._webhooks_journal.journal_local)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self._webhooks_journal.snapshots)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._webhooks_journal.subscriptions)
