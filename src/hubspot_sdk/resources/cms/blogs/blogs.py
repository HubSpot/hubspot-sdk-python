# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .authors import (
    AuthorsResource,
    AsyncAuthorsResource,
    AuthorsResourceWithRawResponse,
    AsyncAuthorsResourceWithRawResponse,
    AuthorsResourceWithStreamingResponse,
    AsyncAuthorsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .posts.posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BlogsResource", "AsyncBlogsResource"]


class BlogsResource(SyncAPIResource):
    @cached_property
    def authors(self) -> AuthorsResource:
        return AuthorsResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BlogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BlogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BlogsResourceWithStreamingResponse(self)


class AsyncBlogsResource(AsyncAPIResource):
    @cached_property
    def authors(self) -> AsyncAuthorsResource:
        return AsyncAuthorsResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBlogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBlogsResourceWithStreamingResponse(self)


class BlogsResourceWithRawResponse:
    def __init__(self, blogs: BlogsResource) -> None:
        self._blogs = blogs

    @cached_property
    def authors(self) -> AuthorsResourceWithRawResponse:
        return AuthorsResourceWithRawResponse(self._blogs.authors)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._blogs.posts)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._blogs.tags)


class AsyncBlogsResourceWithRawResponse:
    def __init__(self, blogs: AsyncBlogsResource) -> None:
        self._blogs = blogs

    @cached_property
    def authors(self) -> AsyncAuthorsResourceWithRawResponse:
        return AsyncAuthorsResourceWithRawResponse(self._blogs.authors)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._blogs.posts)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._blogs.tags)


class BlogsResourceWithStreamingResponse:
    def __init__(self, blogs: BlogsResource) -> None:
        self._blogs = blogs

    @cached_property
    def authors(self) -> AuthorsResourceWithStreamingResponse:
        return AuthorsResourceWithStreamingResponse(self._blogs.authors)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._blogs.posts)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._blogs.tags)


class AsyncBlogsResourceWithStreamingResponse:
    def __init__(self, blogs: AsyncBlogsResource) -> None:
        self._blogs = blogs

    @cached_property
    def authors(self) -> AsyncAuthorsResourceWithStreamingResponse:
        return AsyncAuthorsResourceWithStreamingResponse(self._blogs.authors)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._blogs.posts)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._blogs.tags)
