# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from .a_b_tests import (
    ABTestsResource,
    AsyncABTestsResource,
    ABTestsResourceWithRawResponse,
    AsyncABTestsResourceWithRawResponse,
    ABTestsResourceWithStreamingResponse,
    AsyncABTestsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.cms import page_list_site_page_revisions_params, page_list_landing_page_revisions_params
from ....pagination import SyncPage, AsyncPage
from .landing_pages import (
    LandingPagesResource,
    AsyncLandingPagesResource,
    LandingPagesResourceWithRawResponse,
    AsyncLandingPagesResourceWithRawResponse,
    LandingPagesResourceWithStreamingResponse,
    AsyncLandingPagesResourceWithStreamingResponse,
)
from .website_pages import (
    WebsitePagesResource,
    AsyncWebsitePagesResource,
    WebsitePagesResourceWithRawResponse,
    AsyncWebsitePagesResourceWithRawResponse,
    WebsitePagesResourceWithStreamingResponse,
    AsyncWebsitePagesResourceWithStreamingResponse,
)
from .multi_language import (
    MultiLanguageResource,
    AsyncMultiLanguageResource,
    MultiLanguageResourceWithRawResponse,
    AsyncMultiLanguageResourceWithRawResponse,
    MultiLanguageResourceWithStreamingResponse,
    AsyncMultiLanguageResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cms.pages_page import PagesPage
from ....types.cms.page_version import PageVersion

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def a_b_tests(self) -> ABTestsResource:
        return ABTestsResource(self._client)

    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def landing_pages(self) -> LandingPagesResource:
        return LandingPagesResource(self._client)

    @cached_property
    def multi_language(self) -> MultiLanguageResource:
        return MultiLanguageResource(self._client)

    @cached_property
    def website_pages(self) -> WebsitePagesResource:
        return WebsitePagesResource(self._client)

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

    def get_landing_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageVersion:
        """
        Retrieve a previous version of a landing page, specified by page ID and revision
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            path_template(
                "/cms/pages/2026-03/landing-pages/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageVersion,
        )

    def get_site_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageVersion:
        """
        Retrieve a previous version of a website page by the revision ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            path_template(
                "/cms/pages/2026-03/site-pages/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageVersion,
        )

    def list_landing_page_revisions(
        self,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PageVersion]:
        """
        Retrieve all the previous versions of a landing page, specified by page ID.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            path_template("/cms/pages/2026-03/landing-pages/{object_id}/revisions", object_id=object_id),
            page=SyncPage[PageVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    page_list_landing_page_revisions_params.PageListLandingPageRevisionsParams,
                ),
            ),
            model=PageVersion,
        )

    def list_site_page_revisions(
        self,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PageVersion]:
        """
        Retrieves all the previous versions of a website page, specified by page ID.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            path_template("/cms/pages/2026-03/site-pages/{object_id}/revisions", object_id=object_id),
            page=SyncPage[PageVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    page_list_site_page_revisions_params.PageListSitePageRevisionsParams,
                ),
            ),
            model=PageVersion,
        )

    def reset_site_page_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Discards any edits and resets the draft to match the live version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/cms/pages/2026-03/site-pages/{object_id}/draft/reset", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def restore_landing_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Restores a previous version of a landing page, specified by page ID and revision
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._post(
            path_template(
                "/cms/pages/2026-03/landing-pages/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )

    def restore_landing_page_revision_to_draft(
        self,
        revision_id: int,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Specify a previous version of a landing page to set as the page draft.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            path_template(
                "/cms/pages/2026-03/landing-pages/{object_id}/revisions/{revision_id}/restore-to-draft",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )

    def restore_site_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Restores a website page to a previous version, specified by page ID and version
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._post(
            path_template(
                "/cms/pages/2026-03/site-pages/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )

    def restore_site_page_revision_to_draft(
        self,
        revision_id: int,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Takes a specified version of a website page and sets it as the new draft version
        of the page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            path_template(
                "/cms/pages/2026-03/site-pages/{object_id}/revisions/{revision_id}/restore-to-draft",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def a_b_tests(self) -> AsyncABTestsResource:
        return AsyncABTestsResource(self._client)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def landing_pages(self) -> AsyncLandingPagesResource:
        return AsyncLandingPagesResource(self._client)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResource:
        return AsyncMultiLanguageResource(self._client)

    @cached_property
    def website_pages(self) -> AsyncWebsitePagesResource:
        return AsyncWebsitePagesResource(self._client)

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

    async def get_landing_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageVersion:
        """
        Retrieve a previous version of a landing page, specified by page ID and revision
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            path_template(
                "/cms/pages/2026-03/landing-pages/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageVersion,
        )

    async def get_site_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageVersion:
        """
        Retrieve a previous version of a website page by the revision ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            path_template(
                "/cms/pages/2026-03/site-pages/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageVersion,
        )

    def list_landing_page_revisions(
        self,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PageVersion, AsyncPage[PageVersion]]:
        """
        Retrieve all the previous versions of a landing page, specified by page ID.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            path_template("/cms/pages/2026-03/landing-pages/{object_id}/revisions", object_id=object_id),
            page=AsyncPage[PageVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    page_list_landing_page_revisions_params.PageListLandingPageRevisionsParams,
                ),
            ),
            model=PageVersion,
        )

    def list_site_page_revisions(
        self,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PageVersion, AsyncPage[PageVersion]]:
        """
        Retrieves all the previous versions of a website page, specified by page ID.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            path_template("/cms/pages/2026-03/site-pages/{object_id}/revisions", object_id=object_id),
            page=AsyncPage[PageVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    page_list_site_page_revisions_params.PageListSitePageRevisionsParams,
                ),
            ),
            model=PageVersion,
        )

    async def reset_site_page_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Discards any edits and resets the draft to match the live version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/cms/pages/2026-03/site-pages/{object_id}/draft/reset", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def restore_landing_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Restores a previous version of a landing page, specified by page ID and revision
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._post(
            path_template(
                "/cms/pages/2026-03/landing-pages/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )

    async def restore_landing_page_revision_to_draft(
        self,
        revision_id: int,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Specify a previous version of a landing page to set as the page draft.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            path_template(
                "/cms/pages/2026-03/landing-pages/{object_id}/revisions/{revision_id}/restore-to-draft",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )

    async def restore_site_page_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Restores a website page to a previous version, specified by page ID and version
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._post(
            path_template(
                "/cms/pages/2026-03/site-pages/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )

    async def restore_site_page_revision_to_draft(
        self,
        revision_id: int,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PagesPage:
        """
        Takes a specified version of a website page and sets it as the new draft version
        of the page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            path_template(
                "/cms/pages/2026-03/site-pages/{object_id}/revisions/{revision_id}/restore-to-draft",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesPage,
        )


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.get_landing_page_revision = to_raw_response_wrapper(
            pages.get_landing_page_revision,
        )
        self.get_site_page_revision = to_raw_response_wrapper(
            pages.get_site_page_revision,
        )
        self.list_landing_page_revisions = to_raw_response_wrapper(
            pages.list_landing_page_revisions,
        )
        self.list_site_page_revisions = to_raw_response_wrapper(
            pages.list_site_page_revisions,
        )
        self.reset_site_page_draft = to_raw_response_wrapper(
            pages.reset_site_page_draft,
        )
        self.restore_landing_page_revision = to_raw_response_wrapper(
            pages.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = to_raw_response_wrapper(
            pages.restore_landing_page_revision_to_draft,
        )
        self.restore_site_page_revision = to_raw_response_wrapper(
            pages.restore_site_page_revision,
        )
        self.restore_site_page_revision_to_draft = to_raw_response_wrapper(
            pages.restore_site_page_revision_to_draft,
        )

    @cached_property
    def a_b_tests(self) -> ABTestsResourceWithRawResponse:
        return ABTestsResourceWithRawResponse(self._pages.a_b_tests)

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._pages.batch)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._pages.folders)

    @cached_property
    def landing_pages(self) -> LandingPagesResourceWithRawResponse:
        return LandingPagesResourceWithRawResponse(self._pages.landing_pages)

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithRawResponse:
        return MultiLanguageResourceWithRawResponse(self._pages.multi_language)

    @cached_property
    def website_pages(self) -> WebsitePagesResourceWithRawResponse:
        return WebsitePagesResourceWithRawResponse(self._pages.website_pages)


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.get_landing_page_revision = async_to_raw_response_wrapper(
            pages.get_landing_page_revision,
        )
        self.get_site_page_revision = async_to_raw_response_wrapper(
            pages.get_site_page_revision,
        )
        self.list_landing_page_revisions = async_to_raw_response_wrapper(
            pages.list_landing_page_revisions,
        )
        self.list_site_page_revisions = async_to_raw_response_wrapper(
            pages.list_site_page_revisions,
        )
        self.reset_site_page_draft = async_to_raw_response_wrapper(
            pages.reset_site_page_draft,
        )
        self.restore_landing_page_revision = async_to_raw_response_wrapper(
            pages.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = async_to_raw_response_wrapper(
            pages.restore_landing_page_revision_to_draft,
        )
        self.restore_site_page_revision = async_to_raw_response_wrapper(
            pages.restore_site_page_revision,
        )
        self.restore_site_page_revision_to_draft = async_to_raw_response_wrapper(
            pages.restore_site_page_revision_to_draft,
        )

    @cached_property
    def a_b_tests(self) -> AsyncABTestsResourceWithRawResponse:
        return AsyncABTestsResourceWithRawResponse(self._pages.a_b_tests)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._pages.batch)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._pages.folders)

    @cached_property
    def landing_pages(self) -> AsyncLandingPagesResourceWithRawResponse:
        return AsyncLandingPagesResourceWithRawResponse(self._pages.landing_pages)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithRawResponse:
        return AsyncMultiLanguageResourceWithRawResponse(self._pages.multi_language)

    @cached_property
    def website_pages(self) -> AsyncWebsitePagesResourceWithRawResponse:
        return AsyncWebsitePagesResourceWithRawResponse(self._pages.website_pages)


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.get_landing_page_revision = to_streamed_response_wrapper(
            pages.get_landing_page_revision,
        )
        self.get_site_page_revision = to_streamed_response_wrapper(
            pages.get_site_page_revision,
        )
        self.list_landing_page_revisions = to_streamed_response_wrapper(
            pages.list_landing_page_revisions,
        )
        self.list_site_page_revisions = to_streamed_response_wrapper(
            pages.list_site_page_revisions,
        )
        self.reset_site_page_draft = to_streamed_response_wrapper(
            pages.reset_site_page_draft,
        )
        self.restore_landing_page_revision = to_streamed_response_wrapper(
            pages.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = to_streamed_response_wrapper(
            pages.restore_landing_page_revision_to_draft,
        )
        self.restore_site_page_revision = to_streamed_response_wrapper(
            pages.restore_site_page_revision,
        )
        self.restore_site_page_revision_to_draft = to_streamed_response_wrapper(
            pages.restore_site_page_revision_to_draft,
        )

    @cached_property
    def a_b_tests(self) -> ABTestsResourceWithStreamingResponse:
        return ABTestsResourceWithStreamingResponse(self._pages.a_b_tests)

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._pages.batch)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._pages.folders)

    @cached_property
    def landing_pages(self) -> LandingPagesResourceWithStreamingResponse:
        return LandingPagesResourceWithStreamingResponse(self._pages.landing_pages)

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithStreamingResponse:
        return MultiLanguageResourceWithStreamingResponse(self._pages.multi_language)

    @cached_property
    def website_pages(self) -> WebsitePagesResourceWithStreamingResponse:
        return WebsitePagesResourceWithStreamingResponse(self._pages.website_pages)


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.get_landing_page_revision = async_to_streamed_response_wrapper(
            pages.get_landing_page_revision,
        )
        self.get_site_page_revision = async_to_streamed_response_wrapper(
            pages.get_site_page_revision,
        )
        self.list_landing_page_revisions = async_to_streamed_response_wrapper(
            pages.list_landing_page_revisions,
        )
        self.list_site_page_revisions = async_to_streamed_response_wrapper(
            pages.list_site_page_revisions,
        )
        self.reset_site_page_draft = async_to_streamed_response_wrapper(
            pages.reset_site_page_draft,
        )
        self.restore_landing_page_revision = async_to_streamed_response_wrapper(
            pages.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = async_to_streamed_response_wrapper(
            pages.restore_landing_page_revision_to_draft,
        )
        self.restore_site_page_revision = async_to_streamed_response_wrapper(
            pages.restore_site_page_revision,
        )
        self.restore_site_page_revision_to_draft = async_to_streamed_response_wrapper(
            pages.restore_site_page_revision_to_draft,
        )

    @cached_property
    def a_b_tests(self) -> AsyncABTestsResourceWithStreamingResponse:
        return AsyncABTestsResourceWithStreamingResponse(self._pages.a_b_tests)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._pages.batch)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._pages.folders)

    @cached_property
    def landing_pages(self) -> AsyncLandingPagesResourceWithStreamingResponse:
        return AsyncLandingPagesResourceWithStreamingResponse(self._pages.landing_pages)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithStreamingResponse:
        return AsyncMultiLanguageResourceWithStreamingResponse(self._pages.multi_language)

    @cached_property
    def website_pages(self) -> AsyncWebsitePagesResourceWithStreamingResponse:
        return AsyncWebsitePagesResourceWithStreamingResponse(self._pages.website_pages)
