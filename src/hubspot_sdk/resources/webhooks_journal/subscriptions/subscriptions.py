# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, overload

import httpx

from .filters import (
    FiltersResource,
    AsyncFiltersResource,
    FiltersResourceWithRawResponse,
    AsyncFiltersResourceWithRawResponse,
    FiltersResourceWithStreamingResponse,
    AsyncFiltersResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.webhooks_journal import subscription_create_params
from ....types.webhooks_journal.subscription_response import SubscriptionResponse
from ....types.webhooks_journal.collection_response_subscription_response_no_paging import (
    CollectionResponseSubscriptionResponseNoPaging,
)

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def filters(self) -> FiltersResource:
        return FiltersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        object_ids: Iterable[int],
        object_type_id: str,
        portal_id: int,
        properties: SequenceNotStr[str],
        subscription_type: Literal["OBJECT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        associated_object_type_ids: SequenceNotStr[str],
        object_ids: Iterable[int],
        object_type_id: str,
        portal_id: int,
        subscription_type: Literal["ASSOCIATION"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        event_type_id: str,
        properties: SequenceNotStr[str],
        subscription_type: Literal["APP_LIFECYCLE_EVENT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        list_ids: Iterable[int],
        object_ids: Iterable[int],
        portal_id: int,
        subscription_type: Literal["LIST_MEMBERSHIP"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        object_type_id: str,
        portal_id: int,
        subscription_type: Literal["GDPR_PRIVACY_DELETION"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["actions", "object_ids", "object_type_id", "portal_id", "properties", "subscription_type"],
        ["actions", "associated_object_type_ids", "object_ids", "object_type_id", "portal_id", "subscription_type"],
        ["event_type_id", "properties", "subscription_type"],
        ["actions", "list_ids", "object_ids", "portal_id", "subscription_type"],
        ["actions", "object_type_id", "portal_id", "subscription_type"],
    )
    def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ]
        | Omit = omit,
        object_ids: Iterable[int] | Omit = omit,
        object_type_id: str | Omit = omit,
        portal_id: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        subscription_type: Literal["OBJECT"]
        | Literal["ASSOCIATION"]
        | Literal["APP_LIFECYCLE_EVENT"]
        | Literal["LIST_MEMBERSHIP"]
        | Literal["GDPR_PRIVACY_DELETION"],
        associated_object_type_ids: SequenceNotStr[str] | Omit = omit,
        event_type_id: str | Omit = omit,
        list_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        return self._post(
            "/webhooks-journal/subscriptions/2026-03",
            body=maybe_transform(
                {
                    "actions": actions,
                    "object_ids": object_ids,
                    "object_type_id": object_type_id,
                    "portal_id": portal_id,
                    "properties": properties,
                    "subscription_type": subscription_type,
                    "associated_object_type_ids": associated_object_type_ids,
                    "event_type_id": event_type_id,
                    "list_ids": list_ids,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    def list(
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
        useful for monitoring and managing webhook subscriptions in your HubSpot
        account.
        """
        return self._get(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseSubscriptionResponseNoPaging,
        )

    def delete(
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
        longer needed in your HubSpot account.

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

    def delete_for_portal(
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
        removes the subscription associated with the given portalId, ensuring that no
        further webhook events are sent for this portal. Use this endpoint to manage and
        clean up subscriptions that are no longer needed.

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

    def get(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Retrieve details of a specific webhook subscription using its unique identifier.
        This endpoint is useful for obtaining information about a particular
        subscription, such as its actions, object type, and associated properties.

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
            cast_to=SubscriptionResponse,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def filters(self) -> AsyncFiltersResource:
        return AsyncFiltersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        object_ids: Iterable[int],
        object_type_id: str,
        portal_id: int,
        properties: SequenceNotStr[str],
        subscription_type: Literal["OBJECT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        associated_object_type_ids: SequenceNotStr[str],
        object_ids: Iterable[int],
        object_type_id: str,
        portal_id: int,
        subscription_type: Literal["ASSOCIATION"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        event_type_id: str,
        properties: SequenceNotStr[str],
        subscription_type: Literal["APP_LIFECYCLE_EVENT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        list_ids: Iterable[int],
        object_ids: Iterable[int],
        portal_id: int,
        subscription_type: Literal["LIST_MEMBERSHIP"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ],
        object_type_id: str,
        portal_id: int,
        subscription_type: Literal["GDPR_PRIVACY_DELETION"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create a new subscription in the Webhooks Journal for the specified version.
        This endpoint allows you to define the subscription details by providing the
        necessary information in the request body. It supports various types of
        subscriptions, including object, association, event, app lifecycle event, list
        membership, and GDPR privacy deletion. Ensure that all required fields are
        included in the request to successfully create a subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["actions", "object_ids", "object_type_id", "portal_id", "properties", "subscription_type"],
        ["actions", "associated_object_type_ids", "object_ids", "object_type_id", "portal_id", "subscription_type"],
        ["event_type_id", "properties", "subscription_type"],
        ["actions", "list_ids", "object_ids", "portal_id", "subscription_type"],
        ["actions", "object_type_id", "portal_id", "subscription_type"],
    )
    async def create(
        self,
        *,
        actions: List[
            Literal[
                "CREATE",
                "UPDATE",
                "DELETE",
                "MERGE",
                "RESTORE",
                "ASSOCIATION_ADDED",
                "ASSOCIATION_REMOVED",
                "SNAPSHOT",
                "APP_INSTALL",
                "APP_UNINSTALL",
                "ADDED_TO_LIST",
                "REMOVED_FROM_LIST",
                "GDPR_DELETE",
            ]
        ]
        | Omit = omit,
        object_ids: Iterable[int] | Omit = omit,
        object_type_id: str | Omit = omit,
        portal_id: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        subscription_type: Literal["OBJECT"]
        | Literal["ASSOCIATION"]
        | Literal["APP_LIFECYCLE_EVENT"]
        | Literal["LIST_MEMBERSHIP"]
        | Literal["GDPR_PRIVACY_DELETION"],
        associated_object_type_ids: SequenceNotStr[str] | Omit = omit,
        event_type_id: str | Omit = omit,
        list_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        return await self._post(
            "/webhooks-journal/subscriptions/2026-03",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "object_ids": object_ids,
                    "object_type_id": object_type_id,
                    "portal_id": portal_id,
                    "properties": properties,
                    "subscription_type": subscription_type,
                    "associated_object_type_ids": associated_object_type_ids,
                    "event_type_id": event_type_id,
                    "list_ids": list_ids,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    async def list(
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
        useful for monitoring and managing webhook subscriptions in your HubSpot
        account.
        """
        return await self._get(
            "/webhooks-journal/subscriptions/2026-03",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseSubscriptionResponseNoPaging,
        )

    async def delete(
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
        longer needed in your HubSpot account.

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

    async def delete_for_portal(
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
        removes the subscription associated with the given portalId, ensuring that no
        further webhook events are sent for this portal. Use this endpoint to manage and
        clean up subscriptions that are no longer needed.

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

    async def get(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Retrieve details of a specific webhook subscription using its unique identifier.
        This endpoint is useful for obtaining information about a particular
        subscription, such as its actions, object type, and associated properties.

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
            cast_to=SubscriptionResponse,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.delete_for_portal = to_raw_response_wrapper(
            subscriptions.delete_for_portal,
        )
        self.get = to_raw_response_wrapper(
            subscriptions.get,
        )

    @cached_property
    def filters(self) -> FiltersResourceWithRawResponse:
        return FiltersResourceWithRawResponse(self._subscriptions.filters)


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.delete_for_portal = async_to_raw_response_wrapper(
            subscriptions.delete_for_portal,
        )
        self.get = async_to_raw_response_wrapper(
            subscriptions.get,
        )

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithRawResponse:
        return AsyncFiltersResourceWithRawResponse(self._subscriptions.filters)


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.delete_for_portal = to_streamed_response_wrapper(
            subscriptions.delete_for_portal,
        )
        self.get = to_streamed_response_wrapper(
            subscriptions.get,
        )

    @cached_property
    def filters(self) -> FiltersResourceWithStreamingResponse:
        return FiltersResourceWithStreamingResponse(self._subscriptions.filters)


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.delete_for_portal = async_to_streamed_response_wrapper(
            subscriptions.delete_for_portal,
        )
        self.get = async_to_streamed_response_wrapper(
            subscriptions.get,
        )

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithStreamingResponse:
        return AsyncFiltersResourceWithStreamingResponse(self._subscriptions.filters)
