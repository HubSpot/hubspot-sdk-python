# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.app_webhooks import (
    app_webhook_update_settings_params,
    app_webhook_create_subscription_params,
    app_webhook_update_subscription_params,
    app_webhook_batch_update_subscriptions_params,
)
from ...types.crm.extensions.settings_response import SettingsResponse
from ...types.app_webhooks.subscription_response import SubscriptionResponse
from ...types.app_webhooks.throttling_settings_param import ThrottlingSettingsParam
from ...types.app_webhooks.subscription_list_response import SubscriptionListResponse
from ...types.app_webhooks.batch_response_subscription_response import BatchResponseSubscriptionResponse
from ...types.app_webhooks.subscription_batch_update_request_param import SubscriptionBatchUpdateRequestParam

__all__ = ["AppWebhooksResource", "AsyncAppWebhooksResource"]


class AppWebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AppWebhooksResourceWithStreamingResponse(self)

    def batch_update_subscriptions(
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/app-webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=maybe_transform(
                {"inputs": inputs},
                app_webhook_batch_update_subscriptions_params.AppWebhookBatchUpdateSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
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
        """Args:
          active: Determines if the subscription is active or paused.

        Defaults to false.

          event_type: Type of event to listen for. Can be one of `create`, `delete`,
              `deletedForPrivacy`, or `propertyChange`.

          property_name: The internal name of the property to monitor for changes. Only applies when
              `eventType` is `propertyChange`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/app-webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
            body=maybe_transform(
                {
                    "active": active,
                    "event_type": event_type,
                    "event_type_name": event_type_name,
                    "object_type_id": object_type_id,
                    "property_name": property_name,
                },
                app_webhook_create_subscription_params.AppWebhookCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/app-webhooks/2026-03/{app_id}/settings", app_id=app_id),
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/app-webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/app-webhooks/2026-03/{app_id}/settings", app_id=app_id),
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template(
                "/app-webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/app-webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
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
        Args:
          target_url: A publicly available URL for HubSpot to call where event payloads will be
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            path_template("/app-webhooks/2026-03/{app_id}/settings", app_id=app_id),
            body=maybe_transform(
                {
                    "target_url": target_url,
                    "throttling": throttling,
                },
                app_webhook_update_settings_params.AppWebhookUpdateSettingsParams,
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
        Args:
          active: Determines if the subscription is active or paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template(
                "/app-webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            body=maybe_transform(
                {"active": active}, app_webhook_update_subscription_params.AppWebhookUpdateSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )


class AsyncAppWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAppWebhooksResourceWithStreamingResponse(self)

    async def batch_update_subscriptions(
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/app-webhooks/2026-03/{app_id}/subscriptions/batch/update", app_id=app_id),
            body=await async_maybe_transform(
                {"inputs": inputs},
                app_webhook_batch_update_subscriptions_params.AppWebhookBatchUpdateSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
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
        """Args:
          active: Determines if the subscription is active or paused.

        Defaults to false.

          event_type: Type of event to listen for. Can be one of `create`, `delete`,
              `deletedForPrivacy`, or `propertyChange`.

          property_name: The internal name of the property to monitor for changes. Only applies when
              `eventType` is `propertyChange`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/app-webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "event_type": event_type,
                    "event_type_name": event_type_name,
                    "object_type_id": object_type_id,
                    "property_name": property_name,
                },
                app_webhook_create_subscription_params.AppWebhookCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/app-webhooks/2026-03/{app_id}/settings", app_id=app_id),
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/app-webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/app-webhooks/2026-03/{app_id}/settings", app_id=app_id),
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template(
                "/app-webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/app-webhooks/2026-03/{app_id}/subscriptions", app_id=app_id),
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
        Args:
          target_url: A publicly available URL for HubSpot to call where event payloads will be
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            path_template("/app-webhooks/2026-03/{app_id}/settings", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "target_url": target_url,
                    "throttling": throttling,
                },
                app_webhook_update_settings_params.AppWebhookUpdateSettingsParams,
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
        Args:
          active: Determines if the subscription is active or paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template(
                "/app-webhooks/2026-03/{app_id}/subscriptions/{subscription_id}",
                app_id=app_id,
                subscription_id=subscription_id,
            ),
            body=await async_maybe_transform(
                {"active": active}, app_webhook_update_subscription_params.AppWebhookUpdateSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )


class AppWebhooksResourceWithRawResponse:
    def __init__(self, app_webhooks: AppWebhooksResource) -> None:
        self._app_webhooks = app_webhooks

        self.batch_update_subscriptions = to_raw_response_wrapper(
            app_webhooks.batch_update_subscriptions,
        )
        self.create_subscription = to_raw_response_wrapper(
            app_webhooks.create_subscription,
        )
        self.delete_settings = to_raw_response_wrapper(
            app_webhooks.delete_settings,
        )
        self.delete_subscription = to_raw_response_wrapper(
            app_webhooks.delete_subscription,
        )
        self.get_settings = to_raw_response_wrapper(
            app_webhooks.get_settings,
        )
        self.get_subscription = to_raw_response_wrapper(
            app_webhooks.get_subscription,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            app_webhooks.list_subscriptions,
        )
        self.update_settings = to_raw_response_wrapper(
            app_webhooks.update_settings,
        )
        self.update_subscription = to_raw_response_wrapper(
            app_webhooks.update_subscription,
        )


class AsyncAppWebhooksResourceWithRawResponse:
    def __init__(self, app_webhooks: AsyncAppWebhooksResource) -> None:
        self._app_webhooks = app_webhooks

        self.batch_update_subscriptions = async_to_raw_response_wrapper(
            app_webhooks.batch_update_subscriptions,
        )
        self.create_subscription = async_to_raw_response_wrapper(
            app_webhooks.create_subscription,
        )
        self.delete_settings = async_to_raw_response_wrapper(
            app_webhooks.delete_settings,
        )
        self.delete_subscription = async_to_raw_response_wrapper(
            app_webhooks.delete_subscription,
        )
        self.get_settings = async_to_raw_response_wrapper(
            app_webhooks.get_settings,
        )
        self.get_subscription = async_to_raw_response_wrapper(
            app_webhooks.get_subscription,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            app_webhooks.list_subscriptions,
        )
        self.update_settings = async_to_raw_response_wrapper(
            app_webhooks.update_settings,
        )
        self.update_subscription = async_to_raw_response_wrapper(
            app_webhooks.update_subscription,
        )


class AppWebhooksResourceWithStreamingResponse:
    def __init__(self, app_webhooks: AppWebhooksResource) -> None:
        self._app_webhooks = app_webhooks

        self.batch_update_subscriptions = to_streamed_response_wrapper(
            app_webhooks.batch_update_subscriptions,
        )
        self.create_subscription = to_streamed_response_wrapper(
            app_webhooks.create_subscription,
        )
        self.delete_settings = to_streamed_response_wrapper(
            app_webhooks.delete_settings,
        )
        self.delete_subscription = to_streamed_response_wrapper(
            app_webhooks.delete_subscription,
        )
        self.get_settings = to_streamed_response_wrapper(
            app_webhooks.get_settings,
        )
        self.get_subscription = to_streamed_response_wrapper(
            app_webhooks.get_subscription,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            app_webhooks.list_subscriptions,
        )
        self.update_settings = to_streamed_response_wrapper(
            app_webhooks.update_settings,
        )
        self.update_subscription = to_streamed_response_wrapper(
            app_webhooks.update_subscription,
        )


class AsyncAppWebhooksResourceWithStreamingResponse:
    def __init__(self, app_webhooks: AsyncAppWebhooksResource) -> None:
        self._app_webhooks = app_webhooks

        self.batch_update_subscriptions = async_to_streamed_response_wrapper(
            app_webhooks.batch_update_subscriptions,
        )
        self.create_subscription = async_to_streamed_response_wrapper(
            app_webhooks.create_subscription,
        )
        self.delete_settings = async_to_streamed_response_wrapper(
            app_webhooks.delete_settings,
        )
        self.delete_subscription = async_to_streamed_response_wrapper(
            app_webhooks.delete_subscription,
        )
        self.get_settings = async_to_streamed_response_wrapper(
            app_webhooks.get_settings,
        )
        self.get_subscription = async_to_streamed_response_wrapper(
            app_webhooks.get_subscription,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            app_webhooks.list_subscriptions,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            app_webhooks.update_settings,
        )
        self.update_subscription = async_to_streamed_response_wrapper(
            app_webhooks.update_subscription,
        )
