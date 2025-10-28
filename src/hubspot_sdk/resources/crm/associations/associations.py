# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .v4.v4 import (
    V4Resource,
    AsyncV4Resource,
    V4ResourceWithRawResponse,
    AsyncV4ResourceWithRawResponse,
    V4ResourceWithStreamingResponse,
    AsyncV4ResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .schema.schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)

__all__ = ["AssociationsResource", "AsyncAssociationsResource"]


class AssociationsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def v4(self) -> V4Resource:
        return V4Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AssociationsResourceWithStreamingResponse(self)


class AsyncAssociationsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def v4(self) -> AsyncV4Resource:
        return AsyncV4Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAssociationsResourceWithStreamingResponse(self)


class AssociationsResourceWithRawResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._associations.batch)

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._associations.schema)

    @cached_property
    def v4(self) -> V4ResourceWithRawResponse:
        return V4ResourceWithRawResponse(self._associations.v4)


class AsyncAssociationsResourceWithRawResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._associations.batch)

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._associations.schema)

    @cached_property
    def v4(self) -> AsyncV4ResourceWithRawResponse:
        return AsyncV4ResourceWithRawResponse(self._associations.v4)


class AssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._associations.batch)

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._associations.schema)

    @cached_property
    def v4(self) -> V4ResourceWithStreamingResponse:
        return V4ResourceWithStreamingResponse(self._associations.v4)


class AsyncAssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._associations.batch)

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._associations.schema)

    @cached_property
    def v4(self) -> AsyncV4ResourceWithStreamingResponse:
        return AsyncV4ResourceWithStreamingResponse(self._associations.v4)
