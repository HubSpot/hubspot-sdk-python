# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .send import (
    SendResource,
    AsyncSendResource,
    SendResourceWithRawResponse,
    AsyncSendResourceWithRawResponse,
    SendResourceWithStreamingResponse,
    AsyncSendResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .definitions import (
    DefinitionsResource,
    AsyncDefinitionsResource,
    DefinitionsResourceWithRawResponse,
    AsyncDefinitionsResourceWithRawResponse,
    DefinitionsResourceWithStreamingResponse,
    AsyncDefinitionsResourceWithStreamingResponse,
)
from .occurrences import (
    OccurrencesResource,
    AsyncOccurrencesResource,
    OccurrencesResourceWithRawResponse,
    AsyncOccurrencesResourceWithRawResponse,
    OccurrencesResourceWithStreamingResponse,
    AsyncOccurrencesResourceWithStreamingResponse,
)

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def definitions(self) -> DefinitionsResource:
        return DefinitionsResource(self._client)

    @cached_property
    def occurrences(self) -> OccurrencesResource:
        return OccurrencesResource(self._client)

    @cached_property
    def send(self) -> SendResource:
        return SendResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def definitions(self) -> AsyncDefinitionsResource:
        return AsyncDefinitionsResource(self._client)

    @cached_property
    def occurrences(self) -> AsyncOccurrencesResource:
        return AsyncOccurrencesResource(self._client)

    @cached_property
    def send(self) -> AsyncSendResource:
        return AsyncSendResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def definitions(self) -> DefinitionsResourceWithRawResponse:
        return DefinitionsResourceWithRawResponse(self._events.definitions)

    @cached_property
    def occurrences(self) -> OccurrencesResourceWithRawResponse:
        return OccurrencesResourceWithRawResponse(self._events.occurrences)

    @cached_property
    def send(self) -> SendResourceWithRawResponse:
        return SendResourceWithRawResponse(self._events.send)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def definitions(self) -> AsyncDefinitionsResourceWithRawResponse:
        return AsyncDefinitionsResourceWithRawResponse(self._events.definitions)

    @cached_property
    def occurrences(self) -> AsyncOccurrencesResourceWithRawResponse:
        return AsyncOccurrencesResourceWithRawResponse(self._events.occurrences)

    @cached_property
    def send(self) -> AsyncSendResourceWithRawResponse:
        return AsyncSendResourceWithRawResponse(self._events.send)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def definitions(self) -> DefinitionsResourceWithStreamingResponse:
        return DefinitionsResourceWithStreamingResponse(self._events.definitions)

    @cached_property
    def occurrences(self) -> OccurrencesResourceWithStreamingResponse:
        return OccurrencesResourceWithStreamingResponse(self._events.occurrences)

    @cached_property
    def send(self) -> SendResourceWithStreamingResponse:
        return SendResourceWithStreamingResponse(self._events.send)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def definitions(self) -> AsyncDefinitionsResourceWithStreamingResponse:
        return AsyncDefinitionsResourceWithStreamingResponse(self._events.definitions)

    @cached_property
    def occurrences(self) -> AsyncOccurrencesResourceWithStreamingResponse:
        return AsyncOccurrencesResourceWithStreamingResponse(self._events.occurrences)

    @cached_property
    def send(self) -> AsyncSendResourceWithStreamingResponse:
        return AsyncSendResourceWithStreamingResponse(self._events.send)
