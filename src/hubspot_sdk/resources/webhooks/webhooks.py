# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .webhook_subscriptions.webhook_subscriptions import (
    WebhookSubscriptionsResource,
    AsyncWebhookSubscriptionsResource,
    WebhookSubscriptionsResourceWithRawResponse,
    AsyncWebhookSubscriptionsResourceWithRawResponse,
    WebhookSubscriptionsResourceWithStreamingResponse,
    AsyncWebhookSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def webhook_subscriptions(self) -> WebhookSubscriptionsResource:
        return WebhookSubscriptionsResource(self._client)

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


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def webhook_subscriptions(self) -> AsyncWebhookSubscriptionsResource:
        return AsyncWebhookSubscriptionsResource(self._client)

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


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def webhook_subscriptions(self) -> WebhookSubscriptionsResourceWithRawResponse:
        return WebhookSubscriptionsResourceWithRawResponse(self._webhooks.webhook_subscriptions)


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def webhook_subscriptions(self) -> AsyncWebhookSubscriptionsResourceWithRawResponse:
        return AsyncWebhookSubscriptionsResourceWithRawResponse(self._webhooks.webhook_subscriptions)


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def webhook_subscriptions(self) -> WebhookSubscriptionsResourceWithStreamingResponse:
        return WebhookSubscriptionsResourceWithStreamingResponse(self._webhooks.webhook_subscriptions)


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def webhook_subscriptions(self) -> AsyncWebhookSubscriptionsResourceWithStreamingResponse:
        return AsyncWebhookSubscriptionsResourceWithStreamingResponse(self._webhooks.webhook_subscriptions)
