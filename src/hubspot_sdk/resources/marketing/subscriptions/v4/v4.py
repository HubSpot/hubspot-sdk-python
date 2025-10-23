# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .links import (
    LinksResource,
    AsyncLinksResource,
    LinksResourceWithRawResponse,
    AsyncLinksResourceWithRawResponse,
    LinksResourceWithStreamingResponse,
    AsyncLinksResourceWithStreamingResponse,
)
from .statuses import (
    StatusesResource,
    AsyncStatusesResource,
    StatusesResourceWithRawResponse,
    AsyncStatusesResourceWithRawResponse,
    StatusesResourceWithStreamingResponse,
    AsyncStatusesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from .definitions import (
    DefinitionsResource,
    AsyncDefinitionsResource,
    DefinitionsResourceWithRawResponse,
    AsyncDefinitionsResourceWithRawResponse,
    DefinitionsResourceWithStreamingResponse,
    AsyncDefinitionsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V4Resource", "AsyncV4Resource"]


class V4Resource(SyncAPIResource):
    @cached_property
    def definitions(self) -> DefinitionsResource:
        return DefinitionsResource(self._client)

    @cached_property
    def links(self) -> LinksResource:
        return LinksResource(self._client)

    @cached_property
    def statuses(self) -> StatusesResource:
        return StatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return V4ResourceWithStreamingResponse(self)


class AsyncV4Resource(AsyncAPIResource):
    @cached_property
    def definitions(self) -> AsyncDefinitionsResource:
        return AsyncDefinitionsResource(self._client)

    @cached_property
    def links(self) -> AsyncLinksResource:
        return AsyncLinksResource(self._client)

    @cached_property
    def statuses(self) -> AsyncStatusesResource:
        return AsyncStatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncV4ResourceWithStreamingResponse(self)


class V4ResourceWithRawResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

    @cached_property
    def definitions(self) -> DefinitionsResourceWithRawResponse:
        return DefinitionsResourceWithRawResponse(self._v4.definitions)

    @cached_property
    def links(self) -> LinksResourceWithRawResponse:
        return LinksResourceWithRawResponse(self._v4.links)

    @cached_property
    def statuses(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self._v4.statuses)


class AsyncV4ResourceWithRawResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

    @cached_property
    def definitions(self) -> AsyncDefinitionsResourceWithRawResponse:
        return AsyncDefinitionsResourceWithRawResponse(self._v4.definitions)

    @cached_property
    def links(self) -> AsyncLinksResourceWithRawResponse:
        return AsyncLinksResourceWithRawResponse(self._v4.links)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self._v4.statuses)


class V4ResourceWithStreamingResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

    @cached_property
    def definitions(self) -> DefinitionsResourceWithStreamingResponse:
        return DefinitionsResourceWithStreamingResponse(self._v4.definitions)

    @cached_property
    def links(self) -> LinksResourceWithStreamingResponse:
        return LinksResourceWithStreamingResponse(self._v4.links)

    @cached_property
    def statuses(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self._v4.statuses)


class AsyncV4ResourceWithStreamingResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

    @cached_property
    def definitions(self) -> AsyncDefinitionsResourceWithStreamingResponse:
        return AsyncDefinitionsResourceWithStreamingResponse(self._v4.definitions)

    @cached_property
    def links(self) -> AsyncLinksResourceWithStreamingResponse:
        return AsyncLinksResourceWithStreamingResponse(self._v4.links)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self._v4.statuses)
