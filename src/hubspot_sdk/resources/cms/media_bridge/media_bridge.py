# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from .schemas import (
    SchemasResource,
    AsyncSchemasResource,
    SchemasResourceWithRawResponse,
    AsyncSchemasResourceWithRawResponse,
    SchemasResourceWithStreamingResponse,
    AsyncSchemasResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .properties import (
    PropertiesResource,
    AsyncPropertiesResource,
    PropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
    AsyncPropertiesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .integrator_settings import (
    IntegratorSettingsResource,
    AsyncIntegratorSettingsResource,
    IntegratorSettingsResourceWithRawResponse,
    AsyncIntegratorSettingsResourceWithRawResponse,
    IntegratorSettingsResourceWithStreamingResponse,
    AsyncIntegratorSettingsResourceWithStreamingResponse,
)

__all__ = ["MediaBridgeResource", "AsyncMediaBridgeResource"]


class MediaBridgeResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def integrator_settings(self) -> IntegratorSettingsResource:
        return IntegratorSettingsResource(self._client)

    @cached_property
    def properties(self) -> PropertiesResource:
        return PropertiesResource(self._client)

    @cached_property
    def schemas(self) -> SchemasResource:
        return SchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> MediaBridgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MediaBridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaBridgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MediaBridgeResourceWithStreamingResponse(self)


class AsyncMediaBridgeResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def integrator_settings(self) -> AsyncIntegratorSettingsResource:
        return AsyncIntegratorSettingsResource(self._client)

    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        return AsyncPropertiesResource(self._client)

    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        return AsyncSchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMediaBridgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaBridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaBridgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMediaBridgeResourceWithStreamingResponse(self)


class MediaBridgeResourceWithRawResponse:
    def __init__(self, media_bridge: MediaBridgeResource) -> None:
        self._media_bridge = media_bridge

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._media_bridge.events)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._media_bridge.groups)

    @cached_property
    def integrator_settings(self) -> IntegratorSettingsResourceWithRawResponse:
        return IntegratorSettingsResourceWithRawResponse(self._media_bridge.integrator_settings)

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        return PropertiesResourceWithRawResponse(self._media_bridge.properties)

    @cached_property
    def schemas(self) -> SchemasResourceWithRawResponse:
        return SchemasResourceWithRawResponse(self._media_bridge.schemas)


class AsyncMediaBridgeResourceWithRawResponse:
    def __init__(self, media_bridge: AsyncMediaBridgeResource) -> None:
        self._media_bridge = media_bridge

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._media_bridge.events)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._media_bridge.groups)

    @cached_property
    def integrator_settings(self) -> AsyncIntegratorSettingsResourceWithRawResponse:
        return AsyncIntegratorSettingsResourceWithRawResponse(self._media_bridge.integrator_settings)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        return AsyncPropertiesResourceWithRawResponse(self._media_bridge.properties)

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithRawResponse:
        return AsyncSchemasResourceWithRawResponse(self._media_bridge.schemas)


class MediaBridgeResourceWithStreamingResponse:
    def __init__(self, media_bridge: MediaBridgeResource) -> None:
        self._media_bridge = media_bridge

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._media_bridge.events)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._media_bridge.groups)

    @cached_property
    def integrator_settings(self) -> IntegratorSettingsResourceWithStreamingResponse:
        return IntegratorSettingsResourceWithStreamingResponse(self._media_bridge.integrator_settings)

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        return PropertiesResourceWithStreamingResponse(self._media_bridge.properties)

    @cached_property
    def schemas(self) -> SchemasResourceWithStreamingResponse:
        return SchemasResourceWithStreamingResponse(self._media_bridge.schemas)


class AsyncMediaBridgeResourceWithStreamingResponse:
    def __init__(self, media_bridge: AsyncMediaBridgeResource) -> None:
        self._media_bridge = media_bridge

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._media_bridge.events)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._media_bridge.groups)

    @cached_property
    def integrator_settings(self) -> AsyncIntegratorSettingsResourceWithStreamingResponse:
        return AsyncIntegratorSettingsResourceWithStreamingResponse(self._media_bridge.integrator_settings)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        return AsyncPropertiesResourceWithStreamingResponse(self._media_bridge.properties)

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithStreamingResponse:
        return AsyncSchemasResourceWithStreamingResponse(self._media_bridge.schemas)
