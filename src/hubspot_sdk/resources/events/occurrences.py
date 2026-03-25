# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.events import occurrence_list_params
from ...types.events.external_unified_event import ExternalUnifiedEvent
from ...types.events.visible_external_event_type_names import VisibleExternalEventTypeNames

__all__ = ["OccurrencesResource", "AsyncOccurrencesResource"]


class OccurrencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OccurrencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OccurrencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OccurrencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return OccurrencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        event_type: str | Omit = omit,
        limit: int | Omit = omit,
        object_id: int | Omit = omit,
        object_property: occurrence_list_params.ObjectProperty | Omit = omit,
        object_type: str | Omit = omit,
        occurred_after: Union[str, datetime] | Omit = omit,
        occurred_before: Union[str, datetime] | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        property: occurrence_list_params.Property | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ExternalUnifiedEvent]:
        """Retrieve event occurrences for the specified time frame.

        This endpoint allows
        filtering by various parameters such as object type, event type, and occurrence
        time. It supports pagination and sorting of results.

        Args:
          id: An array of event IDs to filter by.

          after: A cursor token for pagination. Use the value from the previous response's
              paging.next.after field.

          before: A cursor token to retrieve results before a specific point.

          event_type: The type of event to filter by.

          limit: The maximum number of results to display per page.

          object_id: The unique identifier of the object associated with the events.

          object_type: The type of object associated with the events.

          occurred_after: Filter events that occurred after this date-time.

          occurred_before: Filter events that occurred before this date-time.

          properties: An array of property names to include in the response.

          sort: An array of fields to sort the results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/event-occurrences/2026-03",
            page=SyncPage[ExternalUnifiedEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "event_type": event_type,
                        "limit": limit,
                        "object_id": object_id,
                        "object_property": object_property,
                        "object_type": object_type,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "properties": properties,
                        "property": property,
                        "sort": sort,
                    },
                    occurrence_list_params.OccurrenceListParams,
                ),
            ),
            model=ExternalUnifiedEvent,
        )

    def list_event_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibleExternalEventTypeNames:
        """
        Retrieve a list of visible external event type names for the specified event
        occurrences in March 2026. This endpoint is useful for identifying the types of
        events that are available for analysis or reporting within your HubSpot account.
        """
        return self._get(
            "/events/event-occurrences/2026-03/event-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibleExternalEventTypeNames,
        )


class AsyncOccurrencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOccurrencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOccurrencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOccurrencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncOccurrencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        event_type: str | Omit = omit,
        limit: int | Omit = omit,
        object_id: int | Omit = omit,
        object_property: occurrence_list_params.ObjectProperty | Omit = omit,
        object_type: str | Omit = omit,
        occurred_after: Union[str, datetime] | Omit = omit,
        occurred_before: Union[str, datetime] | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        property: occurrence_list_params.Property | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExternalUnifiedEvent, AsyncPage[ExternalUnifiedEvent]]:
        """Retrieve event occurrences for the specified time frame.

        This endpoint allows
        filtering by various parameters such as object type, event type, and occurrence
        time. It supports pagination and sorting of results.

        Args:
          id: An array of event IDs to filter by.

          after: A cursor token for pagination. Use the value from the previous response's
              paging.next.after field.

          before: A cursor token to retrieve results before a specific point.

          event_type: The type of event to filter by.

          limit: The maximum number of results to display per page.

          object_id: The unique identifier of the object associated with the events.

          object_type: The type of object associated with the events.

          occurred_after: Filter events that occurred after this date-time.

          occurred_before: Filter events that occurred before this date-time.

          properties: An array of property names to include in the response.

          sort: An array of fields to sort the results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/event-occurrences/2026-03",
            page=AsyncPage[ExternalUnifiedEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "event_type": event_type,
                        "limit": limit,
                        "object_id": object_id,
                        "object_property": object_property,
                        "object_type": object_type,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "properties": properties,
                        "property": property,
                        "sort": sort,
                    },
                    occurrence_list_params.OccurrenceListParams,
                ),
            ),
            model=ExternalUnifiedEvent,
        )

    async def list_event_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibleExternalEventTypeNames:
        """
        Retrieve a list of visible external event type names for the specified event
        occurrences in March 2026. This endpoint is useful for identifying the types of
        events that are available for analysis or reporting within your HubSpot account.
        """
        return await self._get(
            "/events/event-occurrences/2026-03/event-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisibleExternalEventTypeNames,
        )


class OccurrencesResourceWithRawResponse:
    def __init__(self, occurrences: OccurrencesResource) -> None:
        self._occurrences = occurrences

        self.list = to_raw_response_wrapper(
            occurrences.list,
        )
        self.list_event_types = to_raw_response_wrapper(
            occurrences.list_event_types,
        )


class AsyncOccurrencesResourceWithRawResponse:
    def __init__(self, occurrences: AsyncOccurrencesResource) -> None:
        self._occurrences = occurrences

        self.list = async_to_raw_response_wrapper(
            occurrences.list,
        )
        self.list_event_types = async_to_raw_response_wrapper(
            occurrences.list_event_types,
        )


class OccurrencesResourceWithStreamingResponse:
    def __init__(self, occurrences: OccurrencesResource) -> None:
        self._occurrences = occurrences

        self.list = to_streamed_response_wrapper(
            occurrences.list,
        )
        self.list_event_types = to_streamed_response_wrapper(
            occurrences.list_event_types,
        )


class AsyncOccurrencesResourceWithStreamingResponse:
    def __init__(self, occurrences: AsyncOccurrencesResource) -> None:
        self._occurrences = occurrences

        self.list = async_to_streamed_response_wrapper(
            occurrences.list,
        )
        self.list_event_types = async_to_streamed_response_wrapper(
            occurrences.list_event_types,
        )
