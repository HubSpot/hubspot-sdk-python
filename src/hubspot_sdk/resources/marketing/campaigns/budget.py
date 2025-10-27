# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.marketing.campaigns import budget_create_params, budget_update_params
from ....types.marketing.public_budget_item import PublicBudgetItem
from ....types.marketing.public_budget_totals import PublicBudgetTotals

__all__ = ["BudgetResource", "AsyncBudgetResource"]


class BudgetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BudgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BudgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BudgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BudgetResourceWithStreamingResponse(self)

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
    ) -> PublicBudgetItem:
        """
        Add a new budget item to the campaign

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._post(
            f"/marketing/v3/campaigns/{campaign_guid}/budget",
            body=maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetItem,
        )

    def update(
        self,
        budget_id: int,
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
    ) -> PublicBudgetItem:
        """
        Update a specific budget item by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._put(
            f"/marketing/v3/campaigns/{campaign_guid}/budget/{budget_id}",
            body=maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetItem,
        )

    def delete(
        self,
        budget_id: int,
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
        Delete a specific budget item by ID

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
            f"/marketing/v3/campaigns/{campaign_guid}/budget/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        budget_id: int,
        *,
        campaign_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBudgetItem:
        """
        Get a specific budget item by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/budget/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetItem,
        )

    def get_totals(
        self,
        campaign_guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBudgetTotals:
        """
        Retrieve detailed information about the budget and spend items for a specified
        campaign, including the total budget, total spend, and remaining budget. Budget
        and Spend items may be returned in any order, but the order field specifies
        their sequence based on the creation date. The item with order 0 is the oldest,
        and items with higher order values are newer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/budget/totals",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetTotals,
        )


class AsyncBudgetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBudgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBudgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBudgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBudgetResourceWithStreamingResponse(self)

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
    ) -> PublicBudgetItem:
        """
        Add a new budget item to the campaign

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._post(
            f"/marketing/v3/campaigns/{campaign_guid}/budget",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetItem,
        )

    async def update(
        self,
        budget_id: int,
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
    ) -> PublicBudgetItem:
        """
        Update a specific budget item by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._put(
            f"/marketing/v3/campaigns/{campaign_guid}/budget/{budget_id}",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "name": name,
                    "order": order,
                    "description": description,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetItem,
        )

    async def delete(
        self,
        budget_id: int,
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
        Delete a specific budget item by ID

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
            f"/marketing/v3/campaigns/{campaign_guid}/budget/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        budget_id: int,
        *,
        campaign_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBudgetItem:
        """
        Get a specific budget item by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/budget/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetItem,
        )

    async def get_totals(
        self,
        campaign_guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBudgetTotals:
        """
        Retrieve detailed information about the budget and spend items for a specified
        campaign, including the total budget, total spend, and remaining budget. Budget
        and Spend items may be returned in any order, but the order field specifies
        their sequence based on the creation date. The item with order 0 is the oldest,
        and items with higher order values are newer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        return await self._get(
            f"/marketing/v3/campaigns/{campaign_guid}/budget/totals",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBudgetTotals,
        )


class BudgetResourceWithRawResponse:
    def __init__(self, budget: BudgetResource) -> None:
        self._budget = budget

        self.create = to_raw_response_wrapper(
            budget.create,
        )
        self.update = to_raw_response_wrapper(
            budget.update,
        )
        self.delete = to_raw_response_wrapper(
            budget.delete,
        )
        self.get = to_raw_response_wrapper(
            budget.get,
        )
        self.get_totals = to_raw_response_wrapper(
            budget.get_totals,
        )


class AsyncBudgetResourceWithRawResponse:
    def __init__(self, budget: AsyncBudgetResource) -> None:
        self._budget = budget

        self.create = async_to_raw_response_wrapper(
            budget.create,
        )
        self.update = async_to_raw_response_wrapper(
            budget.update,
        )
        self.delete = async_to_raw_response_wrapper(
            budget.delete,
        )
        self.get = async_to_raw_response_wrapper(
            budget.get,
        )
        self.get_totals = async_to_raw_response_wrapper(
            budget.get_totals,
        )


class BudgetResourceWithStreamingResponse:
    def __init__(self, budget: BudgetResource) -> None:
        self._budget = budget

        self.create = to_streamed_response_wrapper(
            budget.create,
        )
        self.update = to_streamed_response_wrapper(
            budget.update,
        )
        self.delete = to_streamed_response_wrapper(
            budget.delete,
        )
        self.get = to_streamed_response_wrapper(
            budget.get,
        )
        self.get_totals = to_streamed_response_wrapper(
            budget.get_totals,
        )


class AsyncBudgetResourceWithStreamingResponse:
    def __init__(self, budget: AsyncBudgetResource) -> None:
        self._budget = budget

        self.create = async_to_streamed_response_wrapper(
            budget.create,
        )
        self.update = async_to_streamed_response_wrapper(
            budget.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            budget.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            budget.get,
        )
        self.get_totals = async_to_streamed_response_wrapper(
            budget.get_totals,
        )
