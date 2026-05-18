# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncPage, AsyncPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cms.pages_page import PagesPage
from .....types.cms.page_version import PageVersion
from .....types.cms.pages.landing_pages import revision_list_landing_page_revisions_params

__all__ = ["RevisionsResource", "AsyncRevisionsResource"]


class RevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return RevisionsResourceWithStreamingResponse(self)

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
                    revision_list_landing_page_revisions_params.RevisionListLandingPageRevisionsParams,
                ),
            ),
            model=PageVersion,
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


class AsyncRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncRevisionsResourceWithStreamingResponse(self)

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
                    revision_list_landing_page_revisions_params.RevisionListLandingPageRevisionsParams,
                ),
            ),
            model=PageVersion,
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


class RevisionsResourceWithRawResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.get_landing_page_revision = to_raw_response_wrapper(
            revisions.get_landing_page_revision,
        )
        self.list_landing_page_revisions = to_raw_response_wrapper(
            revisions.list_landing_page_revisions,
        )
        self.restore_landing_page_revision = to_raw_response_wrapper(
            revisions.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = to_raw_response_wrapper(
            revisions.restore_landing_page_revision_to_draft,
        )


class AsyncRevisionsResourceWithRawResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.get_landing_page_revision = async_to_raw_response_wrapper(
            revisions.get_landing_page_revision,
        )
        self.list_landing_page_revisions = async_to_raw_response_wrapper(
            revisions.list_landing_page_revisions,
        )
        self.restore_landing_page_revision = async_to_raw_response_wrapper(
            revisions.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = async_to_raw_response_wrapper(
            revisions.restore_landing_page_revision_to_draft,
        )


class RevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.get_landing_page_revision = to_streamed_response_wrapper(
            revisions.get_landing_page_revision,
        )
        self.list_landing_page_revisions = to_streamed_response_wrapper(
            revisions.list_landing_page_revisions,
        )
        self.restore_landing_page_revision = to_streamed_response_wrapper(
            revisions.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = to_streamed_response_wrapper(
            revisions.restore_landing_page_revision_to_draft,
        )


class AsyncRevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.get_landing_page_revision = async_to_streamed_response_wrapper(
            revisions.get_landing_page_revision,
        )
        self.list_landing_page_revisions = async_to_streamed_response_wrapper(
            revisions.list_landing_page_revisions,
        )
        self.restore_landing_page_revision = async_to_streamed_response_wrapper(
            revisions.restore_landing_page_revision,
        )
        self.restore_landing_page_revision_to_draft = async_to_streamed_response_wrapper(
            revisions.restore_landing_page_revision_to_draft,
        )
