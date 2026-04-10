# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .labels import (
    LabelsResource,
    AsyncLabelsResource,
    LabelsResourceWithRawResponse,
    AsyncLabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
    AsyncLabelsResourceWithStreamingResponse,
)
from .limits import (
    LimitsResource,
    AsyncLimitsResource,
    LimitsResourceWithRawResponse,
    AsyncLimitsResourceWithRawResponse,
    LimitsResourceWithStreamingResponse,
    AsyncLimitsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AssociationsSchemaResource", "AsyncAssociationsSchemaResource"]


class AssociationsSchemaResource(SyncAPIResource):
    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def limits(self) -> LimitsResource:
        return LimitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssociationsSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssociationsSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociationsSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AssociationsSchemaResourceWithStreamingResponse(self)


class AsyncAssociationsSchemaResource(AsyncAPIResource):
    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def limits(self) -> AsyncLimitsResource:
        return AsyncLimitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssociationsSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssociationsSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociationsSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAssociationsSchemaResourceWithStreamingResponse(self)


class AssociationsSchemaResourceWithRawResponse:
    def __init__(self, associations_schema: AssociationsSchemaResource) -> None:
        self._associations_schema = associations_schema

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._associations_schema.labels)

    @cached_property
    def limits(self) -> LimitsResourceWithRawResponse:
        return LimitsResourceWithRawResponse(self._associations_schema.limits)


class AsyncAssociationsSchemaResourceWithRawResponse:
    def __init__(self, associations_schema: AsyncAssociationsSchemaResource) -> None:
        self._associations_schema = associations_schema

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._associations_schema.labels)

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithRawResponse:
        return AsyncLimitsResourceWithRawResponse(self._associations_schema.limits)


class AssociationsSchemaResourceWithStreamingResponse:
    def __init__(self, associations_schema: AssociationsSchemaResource) -> None:
        self._associations_schema = associations_schema

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._associations_schema.labels)

    @cached_property
    def limits(self) -> LimitsResourceWithStreamingResponse:
        return LimitsResourceWithStreamingResponse(self._associations_schema.limits)


class AsyncAssociationsSchemaResourceWithStreamingResponse:
    def __init__(self, associations_schema: AsyncAssociationsSchemaResource) -> None:
        self._associations_schema = associations_schema

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._associations_schema.labels)

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithStreamingResponse:
        return AsyncLimitsResourceWithStreamingResponse(self._associations_schema.limits)
