# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .datasource import (
    DatasourceResource,
    AsyncDatasourceResource,
    DatasourceResourceWithRawResponse,
    AsyncDatasourceResourceWithRawResponse,
    DatasourceResourceWithStreamingResponse,
    AsyncDatasourceResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DataStudioResource", "AsyncDataStudioResource"]


class DataStudioResource(SyncAPIResource):
    @cached_property
    def datasource(self) -> DatasourceResource:
        return DatasourceResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataStudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DataStudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataStudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return DataStudioResourceWithStreamingResponse(self)


class AsyncDataStudioResource(AsyncAPIResource):
    @cached_property
    def datasource(self) -> AsyncDatasourceResource:
        return AsyncDatasourceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataStudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataStudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataStudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDataStudioResourceWithStreamingResponse(self)


class DataStudioResourceWithRawResponse:
    def __init__(self, data_studio: DataStudioResource) -> None:
        self._data_studio = data_studio

    @cached_property
    def datasource(self) -> DatasourceResourceWithRawResponse:
        return DatasourceResourceWithRawResponse(self._data_studio.datasource)


class AsyncDataStudioResourceWithRawResponse:
    def __init__(self, data_studio: AsyncDataStudioResource) -> None:
        self._data_studio = data_studio

    @cached_property
    def datasource(self) -> AsyncDatasourceResourceWithRawResponse:
        return AsyncDatasourceResourceWithRawResponse(self._data_studio.datasource)


class DataStudioResourceWithStreamingResponse:
    def __init__(self, data_studio: DataStudioResource) -> None:
        self._data_studio = data_studio

    @cached_property
    def datasource(self) -> DatasourceResourceWithStreamingResponse:
        return DatasourceResourceWithStreamingResponse(self._data_studio.datasource)


class AsyncDataStudioResourceWithStreamingResponse:
    def __init__(self, data_studio: AsyncDataStudioResource) -> None:
        self._data_studio = data_studio

    @cached_property
    def datasource(self) -> AsyncDatasourceResourceWithStreamingResponse:
        return AsyncDatasourceResourceWithStreamingResponse(self._data_studio.datasource)
