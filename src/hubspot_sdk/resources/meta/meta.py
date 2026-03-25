# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .origins.origins import (
    OriginsResource,
    AsyncOriginsResource,
    OriginsResourceWithRawResponse,
    AsyncOriginsResourceWithRawResponse,
    OriginsResourceWithStreamingResponse,
    AsyncOriginsResourceWithStreamingResponse,
)

__all__ = ["MetaResource", "AsyncMetaResource"]


class MetaResource(SyncAPIResource):
    @cached_property
    def origins(self) -> OriginsResource:
        return OriginsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MetaResourceWithStreamingResponse(self)


class AsyncMetaResource(AsyncAPIResource):
    @cached_property
    def origins(self) -> AsyncOriginsResource:
        return AsyncOriginsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMetaResourceWithStreamingResponse(self)


class MetaResourceWithRawResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

    @cached_property
    def origins(self) -> OriginsResourceWithRawResponse:
        return OriginsResourceWithRawResponse(self._meta.origins)


class AsyncMetaResourceWithRawResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

    @cached_property
    def origins(self) -> AsyncOriginsResourceWithRawResponse:
        return AsyncOriginsResourceWithRawResponse(self._meta.origins)


class MetaResourceWithStreamingResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

    @cached_property
    def origins(self) -> OriginsResourceWithStreamingResponse:
        return OriginsResourceWithStreamingResponse(self._meta.origins)


class AsyncMetaResourceWithStreamingResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

    @cached_property
    def origins(self) -> AsyncOriginsResourceWithStreamingResponse:
        return AsyncOriginsResourceWithStreamingResponse(self._meta.origins)
