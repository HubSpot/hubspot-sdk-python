# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .site_pages.site_pages import (
    SitePagesResource,
    AsyncSitePagesResource,
    SitePagesResourceWithRawResponse,
    AsyncSitePagesResourceWithRawResponse,
    SitePagesResourceWithStreamingResponse,
    AsyncSitePagesResourceWithStreamingResponse,
)
from .landing_pages.landing_pages import (
    LandingPagesResource,
    AsyncLandingPagesResource,
    LandingPagesResourceWithRawResponse,
    AsyncLandingPagesResourceWithRawResponse,
    LandingPagesResourceWithStreamingResponse,
    AsyncLandingPagesResourceWithStreamingResponse,
)

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def landing_pages(self) -> LandingPagesResource:
        return LandingPagesResource(self._client)

    @cached_property
    def site_pages(self) -> SitePagesResource:
        return SitePagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return PagesResourceWithStreamingResponse(self)


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def landing_pages(self) -> AsyncLandingPagesResource:
        return AsyncLandingPagesResource(self._client)

    @cached_property
    def site_pages(self) -> AsyncSitePagesResource:
        return AsyncSitePagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPagesResourceWithStreamingResponse(self)


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

    @cached_property
    def landing_pages(self) -> LandingPagesResourceWithRawResponse:
        return LandingPagesResourceWithRawResponse(self._pages.landing_pages)

    @cached_property
    def site_pages(self) -> SitePagesResourceWithRawResponse:
        return SitePagesResourceWithRawResponse(self._pages.site_pages)


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

    @cached_property
    def landing_pages(self) -> AsyncLandingPagesResourceWithRawResponse:
        return AsyncLandingPagesResourceWithRawResponse(self._pages.landing_pages)

    @cached_property
    def site_pages(self) -> AsyncSitePagesResourceWithRawResponse:
        return AsyncSitePagesResourceWithRawResponse(self._pages.site_pages)


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

    @cached_property
    def landing_pages(self) -> LandingPagesResourceWithStreamingResponse:
        return LandingPagesResourceWithStreamingResponse(self._pages.landing_pages)

    @cached_property
    def site_pages(self) -> SitePagesResourceWithStreamingResponse:
        return SitePagesResourceWithStreamingResponse(self._pages.site_pages)


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

    @cached_property
    def landing_pages(self) -> AsyncLandingPagesResourceWithStreamingResponse:
        return AsyncLandingPagesResourceWithStreamingResponse(self._pages.landing_pages)

    @cached_property
    def site_pages(self) -> AsyncSitePagesResourceWithStreamingResponse:
        return AsyncSitePagesResourceWithStreamingResponse(self._pages.site_pages)
