# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.scheduler.meetings import (
    basic_list_params,
    basic_get_availability_by_slug_params,
    basic_get_booking_info_by_slug_params,
)
from ....types.scheduler.external_booking_info import ExternalBookingInfo
from ....types.scheduler.external_link_metadata import ExternalLinkMetadata
from ....types.scheduler.external_link_availability_and_busy_times import ExternalLinkAvailabilityAndBusyTimes

__all__ = ["BasicResource", "AsyncBasicResource"]


class BasicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BasicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BasicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BasicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return BasicResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        organizer_user_id: str | Omit = omit,
        type: Literal["GROUP_CALENDAR", "PERSONAL_LINK", "ROUND_ROBIN_CALENDAR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ExternalLinkMetadata]:
        """
        Get a paged list meeting scheduling pages

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/scheduler/2026-03/meetings/meeting-links",
            page=SyncPage[ExternalLinkMetadata],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "name": name,
                        "organizer_user_id": organizer_user_id,
                        "type": type,
                    },
                    basic_list_params.BasicListParams,
                ),
            ),
            model=ExternalLinkMetadata,
        )

    def get_availability_by_slug(
        self,
        slug: str,
        *,
        timezone: str,
        month_offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalLinkAvailabilityAndBusyTimes:
        """
        Get the next availability times for a meeting page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/scheduler/2026-03/meetings/meeting-links/book/availability-page/{slug}", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "timezone": timezone,
                        "month_offset": month_offset,
                    },
                    basic_get_availability_by_slug_params.BasicGetAvailabilityBySlugParams,
                ),
            ),
            cast_to=ExternalLinkAvailabilityAndBusyTimes,
        )

    def get_booking_info_by_slug(
        self,
        slug: str,
        *,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBookingInfo:
        """
        Get details about the initial information necessary for a meeting scheduler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/scheduler/2026-03/meetings/meeting-links/book/{slug}", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"timezone": timezone}, basic_get_booking_info_by_slug_params.BasicGetBookingInfoBySlugParams
                ),
            ),
            cast_to=ExternalBookingInfo,
        )


class AsyncBasicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBasicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBasicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBasicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBasicResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        organizer_user_id: str | Omit = omit,
        type: Literal["GROUP_CALENDAR", "PERSONAL_LINK", "ROUND_ROBIN_CALENDAR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExternalLinkMetadata, AsyncPage[ExternalLinkMetadata]]:
        """
        Get a paged list meeting scheduling pages

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/scheduler/2026-03/meetings/meeting-links",
            page=AsyncPage[ExternalLinkMetadata],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "name": name,
                        "organizer_user_id": organizer_user_id,
                        "type": type,
                    },
                    basic_list_params.BasicListParams,
                ),
            ),
            model=ExternalLinkMetadata,
        )

    async def get_availability_by_slug(
        self,
        slug: str,
        *,
        timezone: str,
        month_offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalLinkAvailabilityAndBusyTimes:
        """
        Get the next availability times for a meeting page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/scheduler/2026-03/meetings/meeting-links/book/availability-page/{slug}", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "timezone": timezone,
                        "month_offset": month_offset,
                    },
                    basic_get_availability_by_slug_params.BasicGetAvailabilityBySlugParams,
                ),
            ),
            cast_to=ExternalLinkAvailabilityAndBusyTimes,
        )

    async def get_booking_info_by_slug(
        self,
        slug: str,
        *,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBookingInfo:
        """
        Get details about the initial information necessary for a meeting scheduler.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/scheduler/2026-03/meetings/meeting-links/book/{slug}", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"timezone": timezone}, basic_get_booking_info_by_slug_params.BasicGetBookingInfoBySlugParams
                ),
            ),
            cast_to=ExternalBookingInfo,
        )


class BasicResourceWithRawResponse:
    def __init__(self, basic: BasicResource) -> None:
        self._basic = basic

        self.list = to_raw_response_wrapper(
            basic.list,
        )
        self.get_availability_by_slug = to_raw_response_wrapper(
            basic.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = to_raw_response_wrapper(
            basic.get_booking_info_by_slug,
        )


class AsyncBasicResourceWithRawResponse:
    def __init__(self, basic: AsyncBasicResource) -> None:
        self._basic = basic

        self.list = async_to_raw_response_wrapper(
            basic.list,
        )
        self.get_availability_by_slug = async_to_raw_response_wrapper(
            basic.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = async_to_raw_response_wrapper(
            basic.get_booking_info_by_slug,
        )


class BasicResourceWithStreamingResponse:
    def __init__(self, basic: BasicResource) -> None:
        self._basic = basic

        self.list = to_streamed_response_wrapper(
            basic.list,
        )
        self.get_availability_by_slug = to_streamed_response_wrapper(
            basic.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = to_streamed_response_wrapper(
            basic.get_booking_info_by_slug,
        )


class AsyncBasicResourceWithStreamingResponse:
    def __init__(self, basic: AsyncBasicResource) -> None:
        self._basic = basic

        self.list = async_to_streamed_response_wrapper(
            basic.list,
        )
        self.get_availability_by_slug = async_to_streamed_response_wrapper(
            basic.get_availability_by_slug,
        )
        self.get_booking_info_by_slug = async_to_streamed_response_wrapper(
            basic.get_booking_info_by_slug,
        )
