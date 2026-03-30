# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cms.blogs.authors import batch_get_params, batch_create_params, batch_delete_params, batch_update_params
from .....types.cms.blogs.blog_author_param import BlogAuthorParam

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        inputs: Iterable[BlogAuthorParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Create the Blog Author objects detailed in the request body.

        Args:
          inputs: Blog authors to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/blogs/2026-03/authors/batch/create",
            body=maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Update the Blog Author objects identified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/blogs/2026-03/authors/batch/update",
            body=maybe_transform({"inputs": inputs}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, batch_update_params.BatchUpdateParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the Blog Author objects identified in the request body.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/blogs/2026-03/authors/batch/archive",
            body=maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Retrieve the Blog Author objects identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/blogs/2026-03/authors/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, batch_get_params.BatchGetParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        inputs: Iterable[BlogAuthorParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Create the Blog Author objects detailed in the request body.

        Args:
          inputs: Blog authors to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/blogs/2026-03/authors/batch/create",
            body=await async_maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Update the Blog Author objects identified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/blogs/2026-03/authors/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, batch_update_params.BatchUpdateParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the Blog Author objects identified in the request body.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/blogs/2026-03/authors/batch/archive",
            body=await async_maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve the Blog Author objects identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/blogs/2026-03/authors/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, batch_get_params.BatchGetParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_custom_raw_response_wrapper(
            batch.create,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            batch.update,
            BinaryAPIResponse,
        )
        self.delete = to_raw_response_wrapper(
            batch.delete,
        )
        self.get = to_custom_raw_response_wrapper(
            batch.get,
            BinaryAPIResponse,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_custom_raw_response_wrapper(
            batch.create,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            batch.update,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_raw_response_wrapper(
            batch.delete,
        )
        self.get = async_to_custom_raw_response_wrapper(
            batch.get,
            AsyncBinaryAPIResponse,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_custom_streamed_response_wrapper(
            batch.create,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            batch.update,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_streamed_response_wrapper(
            batch.delete,
        )
        self.get = to_custom_streamed_response_wrapper(
            batch.get,
            StreamedBinaryAPIResponse,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_custom_streamed_response_wrapper(
            batch.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            batch.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_streamed_response_wrapper(
            batch.delete,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            batch.get,
            AsyncStreamedBinaryAPIResponse,
        )
