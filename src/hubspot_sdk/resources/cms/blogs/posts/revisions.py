# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cms.blogs.posts import revision_get_previous_versions_params

__all__ = ["RevisionsResource", "AsyncRevisionsResource"]


class RevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return RevisionsResourceWithStreamingResponse(self)

    def get_previous_version(
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
    ) -> BinaryAPIResponse:
        """
        Retrieve a previous version of a blog post.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/cms/blogs/2026-03/posts/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_previous_versions(
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
    ) -> BinaryAPIResponse:
        """
        Retrieve all the previous versions of a blog post.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/cms/blogs/2026-03/posts/{object_id}/revisions", object_id=object_id),
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
                    revision_get_previous_versions_params.RevisionGetPreviousVersionsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def restore_previous_version(
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
    ) -> BinaryAPIResponse:
        """
        Restores a blog post to one of its previous versions.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/cms/blogs/2026-03/posts/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def restore_previous_version_to_draft(
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
    ) -> BinaryAPIResponse:
        """
        Takes a specified version of a blog post, sets it as the new draft version of
        the blog post.

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
            path_template(
                "/cms/blogs/2026-03/posts/{object_id}/revisions/{revision_id}/restore-to-draft",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncRevisionsResourceWithStreamingResponse(self)

    async def get_previous_version(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve a previous version of a blog post.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/cms/blogs/2026-03/posts/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_previous_versions(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve all the previous versions of a blog post.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/cms/blogs/2026-03/posts/{object_id}/revisions", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    revision_get_previous_versions_params.RevisionGetPreviousVersionsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def restore_previous_version(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Restores a blog post to one of its previous versions.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/cms/blogs/2026-03/posts/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def restore_previous_version_to_draft(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Takes a specified version of a blog post, sets it as the new draft version of
        the blog post.

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
            path_template(
                "/cms/blogs/2026-03/posts/{object_id}/revisions/{revision_id}/restore-to-draft",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class RevisionsResourceWithRawResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.get_previous_version = to_custom_raw_response_wrapper(
            revisions.get_previous_version,
            BinaryAPIResponse,
        )
        self.get_previous_versions = to_custom_raw_response_wrapper(
            revisions.get_previous_versions,
            BinaryAPIResponse,
        )
        self.restore_previous_version = to_custom_raw_response_wrapper(
            revisions.restore_previous_version,
            BinaryAPIResponse,
        )
        self.restore_previous_version_to_draft = to_custom_raw_response_wrapper(
            revisions.restore_previous_version_to_draft,
            BinaryAPIResponse,
        )


class AsyncRevisionsResourceWithRawResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.get_previous_version = async_to_custom_raw_response_wrapper(
            revisions.get_previous_version,
            AsyncBinaryAPIResponse,
        )
        self.get_previous_versions = async_to_custom_raw_response_wrapper(
            revisions.get_previous_versions,
            AsyncBinaryAPIResponse,
        )
        self.restore_previous_version = async_to_custom_raw_response_wrapper(
            revisions.restore_previous_version,
            AsyncBinaryAPIResponse,
        )
        self.restore_previous_version_to_draft = async_to_custom_raw_response_wrapper(
            revisions.restore_previous_version_to_draft,
            AsyncBinaryAPIResponse,
        )


class RevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.get_previous_version = to_custom_streamed_response_wrapper(
            revisions.get_previous_version,
            StreamedBinaryAPIResponse,
        )
        self.get_previous_versions = to_custom_streamed_response_wrapper(
            revisions.get_previous_versions,
            StreamedBinaryAPIResponse,
        )
        self.restore_previous_version = to_custom_streamed_response_wrapper(
            revisions.restore_previous_version,
            StreamedBinaryAPIResponse,
        )
        self.restore_previous_version_to_draft = to_custom_streamed_response_wrapper(
            revisions.restore_previous_version_to_draft,
            StreamedBinaryAPIResponse,
        )


class AsyncRevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.get_previous_version = async_to_custom_streamed_response_wrapper(
            revisions.get_previous_version,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_previous_versions = async_to_custom_streamed_response_wrapper(
            revisions.get_previous_versions,
            AsyncStreamedBinaryAPIResponse,
        )
        self.restore_previous_version = async_to_custom_streamed_response_wrapper(
            revisions.restore_previous_version,
            AsyncStreamedBinaryAPIResponse,
        )
        self.restore_previous_version_to_draft = async_to_custom_streamed_response_wrapper(
            revisions.restore_previous_version_to_draft,
            AsyncStreamedBinaryAPIResponse,
        )
