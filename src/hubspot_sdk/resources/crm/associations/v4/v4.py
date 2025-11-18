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
from .report import (
    ReportResource,
    AsyncReportResource,
    ReportResourceWithRawResponse,
    AsyncReportResourceWithRawResponse,
    ReportResourceWithStreamingResponse,
    AsyncReportResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.crm.associations import v4_merge_params
from .....types.crm.simple_public_object import SimplePublicObject

__all__ = ["V4Resource", "AsyncV4Resource"]


class V4Resource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def report(self) -> ReportResource:
        return ReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> V4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return V4ResourceWithStreamingResponse(self)

    def merge(
        self,
        object_type: str,
        *,
        object_id_to_merge: str,
        primary_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Merge two CRM objects of the specified type into one.

        Args:
          object_id_to_merge: The unique identifier of the CRM object that will be merged into the primary
              object.

          primary_object_id: The unique identifier of the CRM object that will remain after the merge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/crm/v4/objects/{object_type}/merge",
            body=maybe_transform(
                {
                    "object_id_to_merge": object_id_to_merge,
                    "primary_object_id": primary_object_id,
                },
                v4_merge_params.V4MergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObject,
        )


class AsyncV4Resource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def report(self) -> AsyncReportResource:
        return AsyncReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncV4ResourceWithStreamingResponse(self)

    async def merge(
        self,
        object_type: str,
        *,
        object_id_to_merge: str,
        primary_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Merge two CRM objects of the specified type into one.

        Args:
          object_id_to_merge: The unique identifier of the CRM object that will be merged into the primary
              object.

          primary_object_id: The unique identifier of the CRM object that will remain after the merge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/crm/v4/objects/{object_type}/merge",
            body=await async_maybe_transform(
                {
                    "object_id_to_merge": object_id_to_merge,
                    "primary_object_id": primary_object_id,
                },
                v4_merge_params.V4MergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObject,
        )


class V4ResourceWithRawResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.merge = to_raw_response_wrapper(
            v4.merge,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._v4.batch)

    @cached_property
    def report(self) -> ReportResourceWithRawResponse:
        return ReportResourceWithRawResponse(self._v4.report)


class AsyncV4ResourceWithRawResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.merge = async_to_raw_response_wrapper(
            v4.merge,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._v4.batch)

    @cached_property
    def report(self) -> AsyncReportResourceWithRawResponse:
        return AsyncReportResourceWithRawResponse(self._v4.report)


class V4ResourceWithStreamingResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.merge = to_streamed_response_wrapper(
            v4.merge,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._v4.batch)

    @cached_property
    def report(self) -> ReportResourceWithStreamingResponse:
        return ReportResourceWithStreamingResponse(self._v4.report)


class AsyncV4ResourceWithStreamingResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.merge = async_to_streamed_response_wrapper(
            v4.merge,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._v4.batch)

    @cached_property
    def report(self) -> AsyncReportResourceWithStreamingResponse:
        return AsyncReportResourceWithStreamingResponse(self._v4.report)
