# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.object_schemas import batch_get_params
from ....types.crm.collection_response_object_schema_no_paging import CollectionResponseObjectSchemaNoPaging

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

    def get(
        self,
        *,
        include_association_definitions: bool,
        include_audit_metadata: bool,
        include_property_definitions: bool,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectSchemaNoPaging:
        """
        Retrieve details of multiple custom object schemas by providing a batch request
        with specified inputs. This operation allows you to fetch schema information,
        including properties and associations, for multiple custom objects in a single
        API call.

        Args:
          include_association_definitions: Indicates whether to include association definitions in the response.

          include_audit_metadata: Indicates whether to include audit metadata in the response.

          include_property_definitions: Indicates whether to include property definitions in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm-object-schemas/2026-03/schemas/batch/read",
            body=maybe_transform(
                {
                    "include_association_definitions": include_association_definitions,
                    "include_audit_metadata": include_audit_metadata,
                    "include_property_definitions": include_property_definitions,
                    "inputs": inputs,
                },
                batch_get_params.BatchGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseObjectSchemaNoPaging,
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

    async def get(
        self,
        *,
        include_association_definitions: bool,
        include_audit_metadata: bool,
        include_property_definitions: bool,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectSchemaNoPaging:
        """
        Retrieve details of multiple custom object schemas by providing a batch request
        with specified inputs. This operation allows you to fetch schema information,
        including properties and associations, for multiple custom objects in a single
        API call.

        Args:
          include_association_definitions: Indicates whether to include association definitions in the response.

          include_audit_metadata: Indicates whether to include audit metadata in the response.

          include_property_definitions: Indicates whether to include property definitions in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm-object-schemas/2026-03/schemas/batch/read",
            body=await async_maybe_transform(
                {
                    "include_association_definitions": include_association_definitions,
                    "include_audit_metadata": include_audit_metadata,
                    "include_property_definitions": include_property_definitions,
                    "inputs": inputs,
                },
                batch_get_params.BatchGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseObjectSchemaNoPaging,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.get = to_raw_response_wrapper(
            batch.get,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.get = async_to_raw_response_wrapper(
            batch.get,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.get = to_streamed_response_wrapper(
            batch.get,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.get = async_to_streamed_response_wrapper(
            batch.get,
        )
