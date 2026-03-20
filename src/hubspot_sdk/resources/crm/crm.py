# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .objects.objects import (
    ObjectsResource,
    AsyncObjectsResource,
    ObjectsResourceWithRawResponse,
    AsyncObjectsResourceWithRawResponse,
    ObjectsResourceWithStreamingResponse,
    AsyncObjectsResourceWithStreamingResponse,
)

__all__ = ["CrmResource", "AsyncCrmResource"]


class CrmResource(SyncAPIResource):
    @cached_property
    def objects(self) -> ObjectsResource:
        return ObjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CrmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CrmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CrmResourceWithStreamingResponse(self)


class AsyncCrmResource(AsyncAPIResource):
    @cached_property
    def objects(self) -> AsyncObjectsResource:
        return AsyncObjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCrmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCrmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCrmResourceWithStreamingResponse(self)


class CrmResourceWithRawResponse:
    def __init__(self, crm: CrmResource) -> None:
        self._crm = crm

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        return ObjectsResourceWithRawResponse(self._crm.objects)


class AsyncCrmResourceWithRawResponse:
    def __init__(self, crm: AsyncCrmResource) -> None:
        self._crm = crm

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        return AsyncObjectsResourceWithRawResponse(self._crm.objects)


class CrmResourceWithStreamingResponse:
    def __init__(self, crm: CrmResource) -> None:
        self._crm = crm

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        return ObjectsResourceWithStreamingResponse(self._crm.objects)


class AsyncCrmResourceWithStreamingResponse:
    def __init__(self, crm: AsyncCrmResource) -> None:
        self._crm = crm

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        return AsyncObjectsResourceWithStreamingResponse(self._crm.objects)
