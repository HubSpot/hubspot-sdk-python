# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cms import source_code_extract_async_params
from ..._base_client import make_request_options
from ...types.shared.task_locator import TaskLocator
from ...types.shared.action_response import ActionResponse

__all__ = ["SourceCodeResource", "AsyncSourceCodeResource"]


class SourceCodeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourceCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SourceCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourceCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SourceCodeResourceWithStreamingResponse(self)

    def extract_async(
        self,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """Extract a zip file in the developer file system.

        Extraction status can be
        checked with the `/extract/async/tasks/taskId/status` endpoint below.

        Args:
          path: The file system location where the zip file is to be extracted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/source-code/2026-03/extract/async",
            body=maybe_transform({"path": path}, source_code_extract_async_params.SourceCodeExtractAsyncParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskLocator,
        )

    def get_extraction_status(
        self,
        task_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponse:
        """
        Get the status of an extraction by the `taskId` returned from the initial
        `extract/async` request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/cms/source-code/2026-03/extract/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponse,
        )


class AsyncSourceCodeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourceCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourceCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourceCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSourceCodeResourceWithStreamingResponse(self)

    async def extract_async(
        self,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """Extract a zip file in the developer file system.

        Extraction status can be
        checked with the `/extract/async/tasks/taskId/status` endpoint below.

        Args:
          path: The file system location where the zip file is to be extracted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/source-code/2026-03/extract/async",
            body=await async_maybe_transform(
                {"path": path}, source_code_extract_async_params.SourceCodeExtractAsyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskLocator,
        )

    async def get_extraction_status(
        self,
        task_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponse:
        """
        Get the status of an extraction by the `taskId` returned from the initial
        `extract/async` request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/cms/source-code/2026-03/extract/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponse,
        )


class SourceCodeResourceWithRawResponse:
    def __init__(self, source_code: SourceCodeResource) -> None:
        self._source_code = source_code

        self.extract_async = to_raw_response_wrapper(
            source_code.extract_async,
        )
        self.get_extraction_status = to_raw_response_wrapper(
            source_code.get_extraction_status,
        )


class AsyncSourceCodeResourceWithRawResponse:
    def __init__(self, source_code: AsyncSourceCodeResource) -> None:
        self._source_code = source_code

        self.extract_async = async_to_raw_response_wrapper(
            source_code.extract_async,
        )
        self.get_extraction_status = async_to_raw_response_wrapper(
            source_code.get_extraction_status,
        )


class SourceCodeResourceWithStreamingResponse:
    def __init__(self, source_code: SourceCodeResource) -> None:
        self._source_code = source_code

        self.extract_async = to_streamed_response_wrapper(
            source_code.extract_async,
        )
        self.get_extraction_status = to_streamed_response_wrapper(
            source_code.get_extraction_status,
        )


class AsyncSourceCodeResourceWithStreamingResponse:
    def __init__(self, source_code: AsyncSourceCodeResource) -> None:
        self._source_code = source_code

        self.extract_async = async_to_streamed_response_wrapper(
            source_code.extract_async,
        )
        self.get_extraction_status = async_to_streamed_response_wrapper(
            source_code.get_extraction_status,
        )
