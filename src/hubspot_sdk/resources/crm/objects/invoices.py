# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.crm.objects import (
    invoice_get_params,
    invoice_list_params,
    invoice_create_params,
    invoice_delete_params,
    invoice_search_params,
    invoice_update_params,
    invoice_upsert_params,
)
from ....types.crm.filter_group_param import FilterGroupParam
from ....types.crm.simple_public_object_id_param import SimplePublicObjectIDParam
from ....types.crm.batch_response_simple_public_object import BatchResponseSimplePublicObject
from ....types.crm.simple_public_object_batch_input_param import SimplePublicObjectBatchInputParam
from ....types.crm.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from ....types.crm.batch_response_simple_public_upsert_object import BatchResponseSimplePublicUpsertObject
from ....types.crm.simple_public_object_batch_input_upsert_param import SimplePublicObjectBatchInputUpsertParam
from ....types.crm.simple_public_object_batch_input_for_create_param import SimplePublicObjectBatchInputForCreateParam
from ....types.crm.collection_response_with_total_simple_public_object import (
    CollectionResponseWithTotalSimplePublicObject,
)

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

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
        Create multiple invoices at once by providing a batch of invoice data, and
        receive a response with details of the created invoices, including their IDs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/invoices/batch/create",
            body=maybe_transform({"inputs": inputs}, invoice_create_params.InvoiceCreateParams),
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
        Update multiple invoices in a single request using either their internal IDs or
        unique property values. This endpoint allows for efficient batch processing of
        invoice updates, ensuring that changes are applied consistently across multiple
        records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/invoices/batch/update",
            body=maybe_transform({"inputs": inputs}, invoice_update_params.InvoiceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[SimplePublicObjectWithAssociations]:
        """Read a page of invoices.

        Control what is returned via the `properties` query
        param.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          limit: The maximum number of results to display per page.

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored. Usage of this parameter will reduce
              the maximum number of objects that can be read by a single request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/objects/2026-03/invoices",
            page=SyncPage[SimplePublicObjectWithAssociations],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associations": associations,
                        "limit": limit,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
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
        """Archive multiple invoices by their IDs in a single request.

        This operation moves
        the specified invoices to the archive, making them inactive but retrievable for
        future reference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/crm/objects/2026-03/invoices/batch/archive",
            body=maybe_transform({"inputs": inputs}, invoice_delete_params.InvoiceDeleteParams),
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
            "/crm/objects/2026-03/invoices/batch/read",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "properties": properties,
                    "properties_with_history": properties_with_history,
                    "id_property": id_property,
                },
                invoice_get_params.InvoiceGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, invoice_get_params.InvoiceGetParams),
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    def search(
        self,
        *,
        after: str,
        filter_groups: Iterable[FilterGroupParam],
        limit: int,
        properties: SequenceNotStr[str],
        sorts: SequenceNotStr[str],
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Execute a search for invoices based on filter criteria, sorting options, and
        properties to include in the response. This endpoint supports pagination and
        allows for complex queries using multiple filter groups.

        Args:
          after: A paging cursor token for retrieving subsequent pages.

          filter_groups: Up to 6 groups of filters defining additional query criteria.

          limit: The maximum results to return, up to 200 objects.

          properties: A list of property names to include in the response.

          sorts: Specifies sorting order based on object properties.

          query: The search query string, up to 3000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/invoices/search",
            body=maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                invoice_search_params.InvoiceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
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
            "/crm/objects/2026-03/invoices/batch/upsert",
            body=maybe_transform({"inputs": inputs}, invoice_upsert_params.InvoiceUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicUpsertObject,
        )


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

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
        Create multiple invoices at once by providing a batch of invoice data, and
        receive a response with details of the created invoices, including their IDs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/invoices/batch/create",
            body=await async_maybe_transform({"inputs": inputs}, invoice_create_params.InvoiceCreateParams),
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
        Update multiple invoices in a single request using either their internal IDs or
        unique property values. This endpoint allows for efficient batch processing of
        invoice updates, ensuring that changes are applied consistently across multiple
        records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/invoices/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, invoice_update_params.InvoiceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SimplePublicObjectWithAssociations, AsyncPage[SimplePublicObjectWithAssociations]]:
        """Read a page of invoices.

        Control what is returned via the `properties` query
        param.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          limit: The maximum number of results to display per page.

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored. Usage of this parameter will reduce
              the maximum number of objects that can be read by a single request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/objects/2026-03/invoices",
            page=AsyncPage[SimplePublicObjectWithAssociations],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associations": associations,
                        "limit": limit,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
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
        """Archive multiple invoices by their IDs in a single request.

        This operation moves
        the specified invoices to the archive, making them inactive but retrievable for
        future reference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/crm/objects/2026-03/invoices/batch/archive",
            body=await async_maybe_transform({"inputs": inputs}, invoice_delete_params.InvoiceDeleteParams),
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
            "/crm/objects/2026-03/invoices/batch/read",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "properties": properties,
                    "properties_with_history": properties_with_history,
                    "id_property": id_property,
                },
                invoice_get_params.InvoiceGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, invoice_get_params.InvoiceGetParams),
            ),
            cast_to=BatchResponseSimplePublicObject,
        )

    async def search(
        self,
        *,
        after: str,
        filter_groups: Iterable[FilterGroupParam],
        limit: int,
        properties: SequenceNotStr[str],
        sorts: SequenceNotStr[str],
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Execute a search for invoices based on filter criteria, sorting options, and
        properties to include in the response. This endpoint supports pagination and
        allows for complex queries using multiple filter groups.

        Args:
          after: A paging cursor token for retrieving subsequent pages.

          filter_groups: Up to 6 groups of filters defining additional query criteria.

          limit: The maximum results to return, up to 200 objects.

          properties: A list of property names to include in the response.

          sorts: Specifies sorting order based on object properties.

          query: The search query string, up to 3000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/invoices/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                invoice_search_params.InvoiceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
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
            "/crm/objects/2026-03/invoices/batch/upsert",
            body=await async_maybe_transform({"inputs": inputs}, invoice_upsert_params.InvoiceUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSimplePublicUpsertObject,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_raw_response_wrapper(
            invoices.create,
        )
        self.update = to_raw_response_wrapper(
            invoices.update,
        )
        self.list = to_raw_response_wrapper(
            invoices.list,
        )
        self.delete = to_raw_response_wrapper(
            invoices.delete,
        )
        self.get = to_raw_response_wrapper(
            invoices.get,
        )
        self.search = to_raw_response_wrapper(
            invoices.search,
        )
        self.upsert = to_raw_response_wrapper(
            invoices.upsert,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_raw_response_wrapper(
            invoices.create,
        )
        self.update = async_to_raw_response_wrapper(
            invoices.update,
        )
        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )
        self.delete = async_to_raw_response_wrapper(
            invoices.delete,
        )
        self.get = async_to_raw_response_wrapper(
            invoices.get,
        )
        self.search = async_to_raw_response_wrapper(
            invoices.search,
        )
        self.upsert = async_to_raw_response_wrapper(
            invoices.upsert,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.update = to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.delete = to_streamed_response_wrapper(
            invoices.delete,
        )
        self.get = to_streamed_response_wrapper(
            invoices.get,
        )
        self.search = to_streamed_response_wrapper(
            invoices.search,
        )
        self.upsert = to_streamed_response_wrapper(
            invoices.upsert,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.update = async_to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            invoices.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            invoices.get,
        )
        self.search = async_to_streamed_response_wrapper(
            invoices.search,
        )
        self.upsert = async_to_streamed_response_wrapper(
            invoices.upsert,
        )
