# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared_params.filter import Filter
from ....types.shared.filter_response import FilterResponse
from ....types.shared.filter_create_response import FilterCreateResponse
from ....types.webhooks_journal.subscriptions import filter_create_params
from ....types.webhooks_journal.subscriptions.filter_list_response import FilterListResponse

__all__ = ["FiltersResource", "AsyncFiltersResource"]


class FiltersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return FiltersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        filter: Filter,
        subscription_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterCreateResponse:
        """
        Create a new filter for a specific webhook subscription in the HubSpot account.
        This endpoint allows you to define conditions that determine when a webhook
        should be triggered. The filter is associated with a subscription identified by
        its ID, and the request must include the filter details.

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
                filter_create_params.FilterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterCreateResponse,
        )

    def list(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterListResponse:
        """Retrieve the filters associated with a specific webhook subscription.

        This
        endpoint allows you to view the filters applied to a subscription, which can
        help in managing and understanding the conditions set for webhook events.

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
            cast_to=FilterListResponse,
        )

    def delete(
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
        """Remove a specific filter from the webhooks journal subscriptions.

        This operation
        is useful for managing and cleaning up filters that are no longer needed. Once
        deleted, the filter cannot be recovered.

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

    def get(
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
        endpoint allows you to access the details of the filter identified by the
        filterId, which is useful for managing and understanding the conditions applied
        to webhook events.

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


class AsyncFiltersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFiltersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        filter: Filter,
        subscription_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterCreateResponse:
        """
        Create a new filter for a specific webhook subscription in the HubSpot account.
        This endpoint allows you to define conditions that determine when a webhook
        should be triggered. The filter is associated with a subscription identified by
        its ID, and the request must include the filter details.

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
                filter_create_params.FilterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterCreateResponse,
        )

    async def list(
        self,
        subscription_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterListResponse:
        """Retrieve the filters associated with a specific webhook subscription.

        This
        endpoint allows you to view the filters applied to a subscription, which can
        help in managing and understanding the conditions set for webhook events.

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
            cast_to=FilterListResponse,
        )

    async def delete(
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
        """Remove a specific filter from the webhooks journal subscriptions.

        This operation
        is useful for managing and cleaning up filters that are no longer needed. Once
        deleted, the filter cannot be recovered.

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

    async def get(
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
        endpoint allows you to access the details of the filter identified by the
        filterId, which is useful for managing and understanding the conditions applied
        to webhook events.

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


class FiltersResourceWithRawResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.create = to_raw_response_wrapper(
            filters.create,
        )
        self.list = to_raw_response_wrapper(
            filters.list,
        )
        self.delete = to_raw_response_wrapper(
            filters.delete,
        )
        self.get = to_raw_response_wrapper(
            filters.get,
        )


class AsyncFiltersResourceWithRawResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.create = async_to_raw_response_wrapper(
            filters.create,
        )
        self.list = async_to_raw_response_wrapper(
            filters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            filters.delete,
        )
        self.get = async_to_raw_response_wrapper(
            filters.get,
        )


class FiltersResourceWithStreamingResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.create = to_streamed_response_wrapper(
            filters.create,
        )
        self.list = to_streamed_response_wrapper(
            filters.list,
        )
        self.delete = to_streamed_response_wrapper(
            filters.delete,
        )
        self.get = to_streamed_response_wrapper(
            filters.get,
        )


class AsyncFiltersResourceWithStreamingResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.create = async_to_streamed_response_wrapper(
            filters.create,
        )
        self.list = async_to_streamed_response_wrapper(
            filters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            filters.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            filters.get,
        )
