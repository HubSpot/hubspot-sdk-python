# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from .portals import (
    PortalsResource,
    AsyncPortalsResource,
    PortalsResourceWithRawResponse,
    AsyncPortalsResourceWithRawResponse,
    PortalsResourceWithStreamingResponse,
    AsyncPortalsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FeatureFlagsResource", "AsyncFeatureFlagsResource"]


class FeatureFlagsResource(SyncAPIResource):
    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def portals(self) -> PortalsResource:
        return PortalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FeatureFlagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FeatureFlagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeatureFlagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FeatureFlagsResourceWithStreamingResponse(self)


class AsyncFeatureFlagsResource(AsyncAPIResource):
    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def portals(self) -> AsyncPortalsResource:
        return AsyncPortalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFeatureFlagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeatureFlagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeatureFlagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFeatureFlagsResourceWithStreamingResponse(self)


class FeatureFlagsResourceWithRawResponse:
    def __init__(self, feature_flags: FeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._feature_flags.apps)

    @cached_property
    def portals(self) -> PortalsResourceWithRawResponse:
        return PortalsResourceWithRawResponse(self._feature_flags.portals)


class AsyncFeatureFlagsResourceWithRawResponse:
    def __init__(self, feature_flags: AsyncFeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._feature_flags.apps)

    @cached_property
    def portals(self) -> AsyncPortalsResourceWithRawResponse:
        return AsyncPortalsResourceWithRawResponse(self._feature_flags.portals)


class FeatureFlagsResourceWithStreamingResponse:
    def __init__(self, feature_flags: FeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._feature_flags.apps)

    @cached_property
    def portals(self) -> PortalsResourceWithStreamingResponse:
        return PortalsResourceWithStreamingResponse(self._feature_flags.portals)


class AsyncFeatureFlagsResourceWithStreamingResponse:
    def __init__(self, feature_flags: AsyncFeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._feature_flags.apps)

    @cached_property
    def portals(self) -> AsyncPortalsResourceWithStreamingResponse:
        return AsyncPortalsResourceWithStreamingResponse(self._feature_flags.portals)
