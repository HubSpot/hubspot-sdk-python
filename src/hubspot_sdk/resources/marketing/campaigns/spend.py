# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.marketing.campaigns import spend_create_params, spend_update_params
from ....types.marketing.public_spend_item import PublicSpendItem

__all__ = ["SpendResource", "AsyncSpendResource"]


class SpendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SpendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SpendResourceWithStreamingResponse(self)

    def create(
        self,
        campaign_guid: str,
        *,
        amount: float,
        name: str,
        order: int,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSpendItem:
        """
        Create a new campaign spend item

        Args:
          amount: The monetary value of the spend item.

          name: The name of the spend item.

          order: The sequence number indicating the order of the spend item.

          description: A brief description of the spend item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._post(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}/spend", campaign_guid=campaign_guid),
            body=maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                spend_create_params.SpendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSpendItem,
        )

    def update(
        self,
        spend_id: int,
        *,
        campaign_guid: str,
        amount: float,
        name: str,
        order: int,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSpendItem:
        """
        Update a specific campaign spend item by ID

        Args:
          amount: The monetary value of the spend item.

          name: The name of the spend item.

          order: The sequence number indicating the order of the spend item.

          description: A brief description of the spend item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._put(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/spend/{spend_id}",
                campaign_guid=campaign_guid,
                spend_id=spend_id,
            ),
            body=maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                spend_update_params.SpendUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSpendItem,
        )

    def delete(
        self,
        spend_id: int,
        *,
        campaign_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific campaign spend item by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/spend/{spend_id}",
                campaign_guid=campaign_guid,
                spend_id=spend_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        spend_id: int,
        *,
        campaign_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSpendItem:
        """
        Read a campaign spend item by its spendId

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/spend/{spend_id}",
                campaign_guid=campaign_guid,
                spend_id=spend_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSpendItem,
        )


class AsyncSpendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSpendResourceWithStreamingResponse(self)

    async def create(
        self,
        campaign_guid: str,
        *,
        amount: float,
        name: str,
        order: int,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSpendItem:
        """
        Create a new campaign spend item

        Args:
          amount: The monetary value of the spend item.

          name: The name of the spend item.

          order: The sequence number indicating the order of the spend item.

          description: A brief description of the spend item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._post(
            path_template("/marketing/campaigns/2026-03/{campaign_guid}/spend", campaign_guid=campaign_guid),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                spend_create_params.SpendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSpendItem,
        )

    async def update(
        self,
        spend_id: int,
        *,
        campaign_guid: str,
        amount: float,
        name: str,
        order: int,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSpendItem:
        """
        Update a specific campaign spend item by ID

        Args:
          amount: The monetary value of the spend item.

          name: The name of the spend item.

          order: The sequence number indicating the order of the spend item.

          description: A brief description of the spend item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._put(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/spend/{spend_id}",
                campaign_guid=campaign_guid,
                spend_id=spend_id,
            ),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                spend_update_params.SpendUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSpendItem,
        )

    async def delete(
        self,
        spend_id: int,
        *,
        campaign_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific campaign spend item by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/spend/{spend_id}",
                campaign_guid=campaign_guid,
                spend_id=spend_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        spend_id: int,
        *,
        campaign_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSpendItem:
        """
        Read a campaign spend item by its spendId

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/spend/{spend_id}",
                campaign_guid=campaign_guid,
                spend_id=spend_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSpendItem,
        )


class SpendResourceWithRawResponse:
    def __init__(self, spend: SpendResource) -> None:
        self._spend = spend

        self.create = to_raw_response_wrapper(
            spend.create,
        )
        self.update = to_raw_response_wrapper(
            spend.update,
        )
        self.delete = to_raw_response_wrapper(
            spend.delete,
        )
        self.get = to_raw_response_wrapper(
            spend.get,
        )


class AsyncSpendResourceWithRawResponse:
    def __init__(self, spend: AsyncSpendResource) -> None:
        self._spend = spend

        self.create = async_to_raw_response_wrapper(
            spend.create,
        )
        self.update = async_to_raw_response_wrapper(
            spend.update,
        )
        self.delete = async_to_raw_response_wrapper(
            spend.delete,
        )
        self.get = async_to_raw_response_wrapper(
            spend.get,
        )


class SpendResourceWithStreamingResponse:
    def __init__(self, spend: SpendResource) -> None:
        self._spend = spend

        self.create = to_streamed_response_wrapper(
            spend.create,
        )
        self.update = to_streamed_response_wrapper(
            spend.update,
        )
        self.delete = to_streamed_response_wrapper(
            spend.delete,
        )
        self.get = to_streamed_response_wrapper(
            spend.get,
        )


class AsyncSpendResourceWithStreamingResponse:
    def __init__(self, spend: AsyncSpendResource) -> None:
        self._spend = spend

        self.create = async_to_streamed_response_wrapper(
            spend.create,
        )
        self.update = async_to_streamed_response_wrapper(
            spend.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            spend.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            spend.get,
        )
