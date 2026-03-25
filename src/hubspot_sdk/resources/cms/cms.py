# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .blogs.blogs import (
    BlogsResource,
    AsyncBlogsResource,
    BlogsResourceWithRawResponse,
    AsyncBlogsResourceWithRawResponse,
    BlogsResourceWithStreamingResponse,
    AsyncBlogsResourceWithStreamingResponse,
)

__all__ = ["CmsResource", "AsyncCmsResource"]


class CmsResource(SyncAPIResource):
    @cached_property
    def blogs(self) -> BlogsResource:
        return BlogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CmsResourceWithStreamingResponse(self)


class AsyncCmsResource(AsyncAPIResource):
    @cached_property
    def blogs(self) -> AsyncBlogsResource:
        return AsyncBlogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCmsResourceWithStreamingResponse(self)


class CmsResourceWithRawResponse:
    def __init__(self, cms: CmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> BlogsResourceWithRawResponse:
        return BlogsResourceWithRawResponse(self._cms.blogs)


class AsyncCmsResourceWithRawResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> AsyncBlogsResourceWithRawResponse:
        return AsyncBlogsResourceWithRawResponse(self._cms.blogs)


class CmsResourceWithStreamingResponse:
    def __init__(self, cms: CmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> BlogsResourceWithStreamingResponse:
        return BlogsResourceWithStreamingResponse(self._cms.blogs)


class AsyncCmsResourceWithStreamingResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> AsyncBlogsResourceWithStreamingResponse:
        return AsyncBlogsResourceWithStreamingResponse(self._cms.blogs)
