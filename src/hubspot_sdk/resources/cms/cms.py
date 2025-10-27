# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .audit_logs import (
    AuditLogsResource,
    AsyncAuditLogsResource,
    AuditLogsResourceWithRawResponse,
    AsyncAuditLogsResourceWithRawResponse,
    AuditLogsResourceWithStreamingResponse,
    AsyncAuditLogsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .blogs.blogs import (
    BlogsResource,
    AsyncBlogsResource,
    BlogsResourceWithRawResponse,
    AsyncBlogsResourceWithRawResponse,
    BlogsResourceWithStreamingResponse,
    AsyncBlogsResourceWithStreamingResponse,
)
from .hubdb.hubdb import (
    HubdbResource,
    AsyncHubdbResource,
    HubdbResourceWithRawResponse,
    AsyncHubdbResourceWithRawResponse,
    HubdbResourceWithStreamingResponse,
    AsyncHubdbResourceWithStreamingResponse,
)
from .pages.pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)
from .site_search import (
    SiteSearchResource,
    AsyncSiteSearchResource,
    SiteSearchResourceWithRawResponse,
    AsyncSiteSearchResourceWithRawResponse,
    SiteSearchResourceWithStreamingResponse,
    AsyncSiteSearchResourceWithStreamingResponse,
)
from .source_code import (
    SourceCodeResource,
    AsyncSourceCodeResource,
    SourceCodeResourceWithRawResponse,
    AsyncSourceCodeResourceWithRawResponse,
    SourceCodeResourceWithStreamingResponse,
    AsyncSourceCodeResourceWithStreamingResponse,
)
from .url_redirects import (
    URLRedirectsResource,
    AsyncURLRedirectsResource,
    URLRedirectsResourceWithRawResponse,
    AsyncURLRedirectsResourceWithRawResponse,
    URLRedirectsResourceWithStreamingResponse,
    AsyncURLRedirectsResourceWithStreamingResponse,
)
from .media_bridge.media_bridge import (
    MediaBridgeResource,
    AsyncMediaBridgeResource,
    MediaBridgeResourceWithRawResponse,
    AsyncMediaBridgeResourceWithRawResponse,
    MediaBridgeResourceWithStreamingResponse,
    AsyncMediaBridgeResourceWithStreamingResponse,
)

__all__ = ["CmsResource", "AsyncCmsResource"]


class CmsResource(SyncAPIResource):
    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        return AuditLogsResource(self._client)

    @cached_property
    def blogs(self) -> BlogsResource:
        return BlogsResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def hubdb(self) -> HubdbResource:
        return HubdbResource(self._client)

    @cached_property
    def media_bridge(self) -> MediaBridgeResource:
        return MediaBridgeResource(self._client)

    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def site_search(self) -> SiteSearchResource:
        return SiteSearchResource(self._client)

    @cached_property
    def source_code(self) -> SourceCodeResource:
        return SourceCodeResource(self._client)

    @cached_property
    def url_redirects(self) -> URLRedirectsResource:
        return URLRedirectsResource(self._client)

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
    def audit_logs(self) -> AsyncAuditLogsResource:
        return AsyncAuditLogsResource(self._client)

    @cached_property
    def blogs(self) -> AsyncBlogsResource:
        return AsyncBlogsResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def hubdb(self) -> AsyncHubdbResource:
        return AsyncHubdbResource(self._client)

    @cached_property
    def media_bridge(self) -> AsyncMediaBridgeResource:
        return AsyncMediaBridgeResource(self._client)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def site_search(self) -> AsyncSiteSearchResource:
        return AsyncSiteSearchResource(self._client)

    @cached_property
    def source_code(self) -> AsyncSourceCodeResource:
        return AsyncSourceCodeResource(self._client)

    @cached_property
    def url_redirects(self) -> AsyncURLRedirectsResource:
        return AsyncURLRedirectsResource(self._client)

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
    def audit_logs(self) -> AuditLogsResourceWithRawResponse:
        return AuditLogsResourceWithRawResponse(self._cms.audit_logs)

    @cached_property
    def blogs(self) -> BlogsResourceWithRawResponse:
        return BlogsResourceWithRawResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._cms.domains)

    @cached_property
    def hubdb(self) -> HubdbResourceWithRawResponse:
        return HubdbResourceWithRawResponse(self._cms.hubdb)

    @cached_property
    def media_bridge(self) -> MediaBridgeResourceWithRawResponse:
        return MediaBridgeResourceWithRawResponse(self._cms.media_bridge)

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._cms.pages)

    @cached_property
    def site_search(self) -> SiteSearchResourceWithRawResponse:
        return SiteSearchResourceWithRawResponse(self._cms.site_search)

    @cached_property
    def source_code(self) -> SourceCodeResourceWithRawResponse:
        return SourceCodeResourceWithRawResponse(self._cms.source_code)

    @cached_property
    def url_redirects(self) -> URLRedirectsResourceWithRawResponse:
        return URLRedirectsResourceWithRawResponse(self._cms.url_redirects)


class AsyncCmsResourceWithRawResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithRawResponse:
        return AsyncAuditLogsResourceWithRawResponse(self._cms.audit_logs)

    @cached_property
    def blogs(self) -> AsyncBlogsResourceWithRawResponse:
        return AsyncBlogsResourceWithRawResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._cms.domains)

    @cached_property
    def hubdb(self) -> AsyncHubdbResourceWithRawResponse:
        return AsyncHubdbResourceWithRawResponse(self._cms.hubdb)

    @cached_property
    def media_bridge(self) -> AsyncMediaBridgeResourceWithRawResponse:
        return AsyncMediaBridgeResourceWithRawResponse(self._cms.media_bridge)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._cms.pages)

    @cached_property
    def site_search(self) -> AsyncSiteSearchResourceWithRawResponse:
        return AsyncSiteSearchResourceWithRawResponse(self._cms.site_search)

    @cached_property
    def source_code(self) -> AsyncSourceCodeResourceWithRawResponse:
        return AsyncSourceCodeResourceWithRawResponse(self._cms.source_code)

    @cached_property
    def url_redirects(self) -> AsyncURLRedirectsResourceWithRawResponse:
        return AsyncURLRedirectsResourceWithRawResponse(self._cms.url_redirects)


class CmsResourceWithStreamingResponse:
    def __init__(self, cms: CmsResource) -> None:
        self._cms = cms

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithStreamingResponse:
        return AuditLogsResourceWithStreamingResponse(self._cms.audit_logs)

    @cached_property
    def blogs(self) -> BlogsResourceWithStreamingResponse:
        return BlogsResourceWithStreamingResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._cms.domains)

    @cached_property
    def hubdb(self) -> HubdbResourceWithStreamingResponse:
        return HubdbResourceWithStreamingResponse(self._cms.hubdb)

    @cached_property
    def media_bridge(self) -> MediaBridgeResourceWithStreamingResponse:
        return MediaBridgeResourceWithStreamingResponse(self._cms.media_bridge)

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._cms.pages)

    @cached_property
    def site_search(self) -> SiteSearchResourceWithStreamingResponse:
        return SiteSearchResourceWithStreamingResponse(self._cms.site_search)

    @cached_property
    def source_code(self) -> SourceCodeResourceWithStreamingResponse:
        return SourceCodeResourceWithStreamingResponse(self._cms.source_code)

    @cached_property
    def url_redirects(self) -> URLRedirectsResourceWithStreamingResponse:
        return URLRedirectsResourceWithStreamingResponse(self._cms.url_redirects)


class AsyncCmsResourceWithStreamingResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        return AsyncAuditLogsResourceWithStreamingResponse(self._cms.audit_logs)

    @cached_property
    def blogs(self) -> AsyncBlogsResourceWithStreamingResponse:
        return AsyncBlogsResourceWithStreamingResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._cms.domains)

    @cached_property
    def hubdb(self) -> AsyncHubdbResourceWithStreamingResponse:
        return AsyncHubdbResourceWithStreamingResponse(self._cms.hubdb)

    @cached_property
    def media_bridge(self) -> AsyncMediaBridgeResourceWithStreamingResponse:
        return AsyncMediaBridgeResourceWithStreamingResponse(self._cms.media_bridge)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._cms.pages)

    @cached_property
    def site_search(self) -> AsyncSiteSearchResourceWithStreamingResponse:
        return AsyncSiteSearchResourceWithStreamingResponse(self._cms.site_search)

    @cached_property
    def source_code(self) -> AsyncSourceCodeResourceWithStreamingResponse:
        return AsyncSourceCodeResourceWithStreamingResponse(self._cms.source_code)

    @cached_property
    def url_redirects(self) -> AsyncURLRedirectsResourceWithStreamingResponse:
        return AsyncURLRedirectsResourceWithStreamingResponse(self._cms.url_redirects)
