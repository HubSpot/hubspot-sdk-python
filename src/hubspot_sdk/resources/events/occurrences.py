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

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OccurrencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OccurrencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
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
        """Retrieve a list of event type names.

        You may use these event types to query the
        API for event occurrences of a desired type.

        Note: the `get_types` method is only supported in the Python SDK version
        `12.0.0-beta.1` or later.
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

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOccurrencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOccurrencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
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
        """Retrieve a list of event type names.

        You may use these event types to query the
        API for event occurrences of a desired type.

        Note: the `get_types` method is only supported in the Python SDK version
        `12.0.0-beta.1` or later.
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
