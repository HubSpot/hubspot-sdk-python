# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .multi_language import (
    MultiLanguageResource,
    AsyncMultiLanguageResource,
    MultiLanguageResourceWithRawResponse,
    AsyncMultiLanguageResourceWithRawResponse,
    MultiLanguageResourceWithStreamingResponse,
    AsyncMultiLanguageResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cms.blogs import setting_list_params, setting_list_revisions_params
from .....types.cms.blogs.blog import Blog
from .....types.cms.blogs.blog_version import BlogVersion
from .....types.cms.blogs.version_blog import VersionBlog

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def multi_language(self) -> MultiLanguageResource:
        return MultiLanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Blog]:
        """Get the list of blogs.

        Results can be limited and filtered by creation or
        updated date.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/blog-settings/2026-03/settings",
            page=SyncPage[Blog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    setting_list_params.SettingListParams,
                ),
            ),
            model=Blog,
        )

    def get(
        self,
        blog_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Blog:
        """
        Retrieve a specific blog by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return self._get(
            path_template("/cms/blog-settings/2026-03/settings/{blog_id}", blog_id=blog_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Blog,
        )

    def get_revision(
        self,
        revision_id: str,
        *,
        blog_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlogVersion:
        """
        Get a specific blog revision.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            path_template(
                "/cms/blog-settings/2026-03/settings/{blog_id}/revisions/{revision_id}",
                blog_id=blog_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogVersion,
        )

    def list_revisions(
        self,
        blog_id: str,
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
    ) -> SyncPage[VersionBlog]:
        """Get the list of blog revisions.

        Results can be limited and filtered by creation
        or updated date.

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
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return self._get_api_list(
            path_template("/cms/blog-settings/2026-03/settings/{blog_id}/revisions", blog_id=blog_id),
            page=SyncPage[VersionBlog],
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
                    setting_list_revisions_params.SettingListRevisionsParams,
                ),
            ),
            model=VersionBlog,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResource:
        return AsyncMultiLanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Blog, AsyncPage[Blog]]:
        """Get the list of blogs.

        Results can be limited and filtered by creation or
        updated date.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/blog-settings/2026-03/settings",
            page=AsyncPage[Blog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    setting_list_params.SettingListParams,
                ),
            ),
            model=Blog,
        )

    async def get(
        self,
        blog_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Blog:
        """
        Retrieve a specific blog by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return await self._get(
            path_template("/cms/blog-settings/2026-03/settings/{blog_id}", blog_id=blog_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Blog,
        )

    async def get_revision(
        self,
        revision_id: str,
        *,
        blog_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlogVersion:
        """
        Get a specific blog revision.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            path_template(
                "/cms/blog-settings/2026-03/settings/{blog_id}/revisions/{revision_id}",
                blog_id=blog_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogVersion,
        )

    def list_revisions(
        self,
        blog_id: str,
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
    ) -> AsyncPaginator[VersionBlog, AsyncPage[VersionBlog]]:
        """Get the list of blog revisions.

        Results can be limited and filtered by creation
        or updated date.

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
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return self._get_api_list(
            path_template("/cms/blog-settings/2026-03/settings/{blog_id}/revisions", blog_id=blog_id),
            page=AsyncPage[VersionBlog],
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
                    setting_list_revisions_params.SettingListRevisionsParams,
                ),
            ),
            model=VersionBlog,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.list = to_raw_response_wrapper(
            settings.list,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )
        self.get_revision = to_raw_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = to_raw_response_wrapper(
            settings.list_revisions,
        )

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithRawResponse:
        return MultiLanguageResourceWithRawResponse(self._settings.multi_language)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.list = async_to_raw_response_wrapper(
            settings.list,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )
        self.get_revision = async_to_raw_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = async_to_raw_response_wrapper(
            settings.list_revisions,
        )

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithRawResponse:
        return AsyncMultiLanguageResourceWithRawResponse(self._settings.multi_language)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.list = to_streamed_response_wrapper(
            settings.list,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )
        self.get_revision = to_streamed_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = to_streamed_response_wrapper(
            settings.list_revisions,
        )

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithStreamingResponse:
        return MultiLanguageResourceWithStreamingResponse(self._settings.multi_language)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.list = async_to_streamed_response_wrapper(
            settings.list,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
        self.get_revision = async_to_streamed_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = async_to_streamed_response_wrapper(
            settings.list_revisions,
        )

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithStreamingResponse:
        return AsyncMultiLanguageResourceWithStreamingResponse(self._settings.multi_language)
