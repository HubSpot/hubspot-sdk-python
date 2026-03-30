# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.crm.objects.services import (
    batch_get_params,
    batch_create_params,
    batch_delete_params,
    batch_update_params,
    batch_upsert_params,
)
from .....types.crm.simple_public_object_id_param import SimplePublicObjectIDParam
from .....types.crm.batch_response_simple_public_object import BatchResponseSimplePublicObject
from .....types.crm.simple_public_object_batch_input_param import SimplePublicObjectBatchInputParam
from .....types.crm.batch_response_simple_public_upsert_object import BatchResponseSimplePublicUpsertObject
from .....types.crm.simple_public_object_batch_input_upsert_param import SimplePublicObjectBatchInputUpsertParam
from .....types.crm.simple_public_object_batch_input_for_create_param import SimplePublicObjectBatchInputForCreateParam

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
        inputs: Iterable[SimplePublicObjectBatchInputForCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicObject:
        """
        Create a batch of objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/0-162/batch/create",
            body=maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    def update(
        self,
        *,
        inputs: Iterable[SimplePublicObjectBatchInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicObject:
        """
        Update a batch of objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/0-162/batch/update",
            body=maybe_transform({"inputs": inputs}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    def delete(
        self,
        *,
        inputs: Iterable[SimplePublicObjectIDParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a batch of objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/crm/objects/2026-03/0-162/batch/archive",
            body=maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        inputs: Iterable[SimplePublicObjectIDParam],
        properties: SequenceNotStr[str],
        properties_with_history: SequenceNotStr[str],
        archived: bool | Omit = omit,
        id_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicObject:
        """
        Retrieve records by record ID or include the `idProperty` parameter to retrieve
        records by a custom unique value property.

        Args:
          properties: Key-value pairs for setting properties for the new object.

          properties_with_history: Key-value pairs for setting properties for the new object and their histories.

          archived: Whether to return only results that have been archived.

          id_property: When using a custom unique value property to retrieve records, the name of the
              property. Do not include this parameter if retrieving by record ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/0-162/batch/read",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "properties": properties,
                    "properties_with_history": properties_with_history,
                    "id_property": id_property,
                },
                batch_get_params.BatchGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, batch_get_params.BatchGetParams),
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    def upsert(
        self,
        *,
        inputs: Iterable[SimplePublicObjectBatchInputUpsertParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicUpsertObject:
        """
        Create or update records identified by a unique property value as specified by
        the `idProperty` query param. `idProperty` query param refers to a property
        whose values are unique for the object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/0-162/batch/upsert",
            body=maybe_transform({"inputs": inputs}, batch_upsert_params.BatchUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicUpsertObject,
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
        inputs: Iterable[SimplePublicObjectBatchInputForCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicObject:
        """
        Create a batch of objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/0-162/batch/create",
            body=await async_maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    async def update(
        self,
        *,
        inputs: Iterable[SimplePublicObjectBatchInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicObject:
        """
        Update a batch of objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/0-162/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    async def delete(
        self,
        *,
        inputs: Iterable[SimplePublicObjectIDParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a batch of objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/crm/objects/2026-03/0-162/batch/archive",
            body=await async_maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        inputs: Iterable[SimplePublicObjectIDParam],
        properties: SequenceNotStr[str],
        properties_with_history: SequenceNotStr[str],
        archived: bool | Omit = omit,
        id_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicObject:
        """
        Retrieve records by record ID or include the `idProperty` parameter to retrieve
        records by a custom unique value property.

        Args:
          properties: Key-value pairs for setting properties for the new object.

          properties_with_history: Key-value pairs for setting properties for the new object and their histories.

          archived: Whether to return only results that have been archived.

          id_property: When using a custom unique value property to retrieve records, the name of the
              property. Do not include this parameter if retrieving by record ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/0-162/batch/read",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "properties": properties,
                    "properties_with_history": properties_with_history,
                    "id_property": id_property,
                },
                batch_get_params.BatchGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, batch_get_params.BatchGetParams),
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    async def upsert(
        self,
        *,
        inputs: Iterable[SimplePublicObjectBatchInputUpsertParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSimplePublicUpsertObject:
        """
        Create or update records identified by a unique property value as specified by
        the `idProperty` query param. `idProperty` query param refers to a property
        whose values are unique for the object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/0-162/batch/upsert",
            body=await async_maybe_transform({"inputs": inputs}, batch_upsert_params.BatchUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicUpsertObject,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )
        self.update = to_raw_response_wrapper(
            batch.update,
        )
        self.delete = to_raw_response_wrapper(
            batch.delete,
        )
        self.get = to_raw_response_wrapper(
            batch.get,
        )
        self.upsert = to_raw_response_wrapper(
            batch.upsert,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )
        self.update = async_to_raw_response_wrapper(
            batch.update,
        )
        self.delete = async_to_raw_response_wrapper(
            batch.delete,
        )
        self.get = async_to_raw_response_wrapper(
            batch.get,
        )
        self.upsert = async_to_raw_response_wrapper(
            batch.upsert,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )
        self.update = to_streamed_response_wrapper(
            batch.update,
        )
        self.delete = to_streamed_response_wrapper(
            batch.delete,
        )
        self.get = to_streamed_response_wrapper(
            batch.get,
        )
        self.upsert = to_streamed_response_wrapper(
            batch.upsert,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
        self.update = async_to_streamed_response_wrapper(
            batch.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            batch.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            batch.get,
        )
        self.upsert = async_to_streamed_response_wrapper(
            batch.upsert,
        )
