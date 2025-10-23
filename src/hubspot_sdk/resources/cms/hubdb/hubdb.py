# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tables import (
    TablesResource,
    AsyncTablesResource,
    TablesResourceWithRawResponse,
    AsyncTablesResourceWithRawResponse,
    TablesResourceWithStreamingResponse,
    AsyncTablesResourceWithStreamingResponse,
)
from .rows.rows import (
    RowsResource,
    AsyncRowsResource,
    RowsResourceWithRawResponse,
    AsyncRowsResourceWithRawResponse,
    RowsResourceWithStreamingResponse,
    AsyncRowsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["HubdbResource", "AsyncHubdbResource"]


class HubdbResource(SyncAPIResource):
    @cached_property
    def rows(self) -> RowsResource:
        return RowsResource(self._client)

    @cached_property
    def tables(self) -> TablesResource:
        return TablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> HubdbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return HubdbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HubdbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return HubdbResourceWithStreamingResponse(self)


class AsyncHubdbResource(AsyncAPIResource):
    @cached_property
    def rows(self) -> AsyncRowsResource:
        return AsyncRowsResource(self._client)

    @cached_property
    def tables(self) -> AsyncTablesResource:
        return AsyncTablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHubdbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHubdbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHubdbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncHubdbResourceWithStreamingResponse(self)


class HubdbResourceWithRawResponse:
    def __init__(self, hubdb: HubdbResource) -> None:
        self._hubdb = hubdb

    @cached_property
    def rows(self) -> RowsResourceWithRawResponse:
        return RowsResourceWithRawResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> TablesResourceWithRawResponse:
        return TablesResourceWithRawResponse(self._hubdb.tables)


class AsyncHubdbResourceWithRawResponse:
    def __init__(self, hubdb: AsyncHubdbResource) -> None:
        self._hubdb = hubdb

    @cached_property
    def rows(self) -> AsyncRowsResourceWithRawResponse:
        return AsyncRowsResourceWithRawResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> AsyncTablesResourceWithRawResponse:
        return AsyncTablesResourceWithRawResponse(self._hubdb.tables)


class HubdbResourceWithStreamingResponse:
    def __init__(self, hubdb: HubdbResource) -> None:
        self._hubdb = hubdb

    @cached_property
    def rows(self) -> RowsResourceWithStreamingResponse:
        return RowsResourceWithStreamingResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> TablesResourceWithStreamingResponse:
        return TablesResourceWithStreamingResponse(self._hubdb.tables)


class AsyncHubdbResourceWithStreamingResponse:
    def __init__(self, hubdb: AsyncHubdbResource) -> None:
        self._hubdb = hubdb

    @cached_property
    def rows(self) -> AsyncRowsResourceWithStreamingResponse:
        return AsyncRowsResourceWithStreamingResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> AsyncTablesResourceWithStreamingResponse:
        return AsyncTablesResourceWithStreamingResponse(self._hubdb.tables)
