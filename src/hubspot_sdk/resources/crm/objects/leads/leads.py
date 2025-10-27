# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
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
from .....pagination import SyncPage, AsyncPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.crm.objects import (
    lead_get_params,
    lead_list_params,
    lead_create_params,
    lead_search_params,
    lead_update_params,
)
from .....types.crm.filter_group_param import FilterGroupParam
from .....types.crm.simple_public_object import SimplePublicObject
from .....types.crm.public_associations_for_object_param import PublicAssociationsForObjectParam
from .....types.crm.created_response_simple_public_object import CreatedResponseSimplePublicObject
from .....types.crm.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from .....types.crm.collection_response_with_total_simple_public_object import (
    CollectionResponseWithTotalSimplePublicObject,
)

__all__ = ["LeadsResource", "AsyncLeadsResource"]


class LeadsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> LeadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LeadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return LeadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        properties: Dict[str, str],
        associations: Iterable[PublicAssociationsForObjectParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponseSimplePublicObject:
        """
        Create a lead with the given properties and return a copy of the object,
        including the ID. Documentation and examples for creating standard leads is
        provided.

        Args:
          properties: Key-value pairs for setting properties for the new object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/leads",
            body=maybe_transform(
                {
                    "properties": properties,
                    "associations": associations,
                },
                lead_create_params.LeadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponseSimplePublicObject,
        )

    def update(
        self,
        leads_id: str,
        *,
        properties: Dict[str, str],
        id_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Perform a partial update of an Object identified by `{leadsId}`or optionally a
        unique property value as specified by the `idProperty` query param. `{leadsId}`
        refers to the internal object ID by default, and the `idProperty` query param
        refers to a property whose values are unique for the object. Provided property
        values will be overwritten. Read-only and non-existent properties will result in
        an error. Properties values can be cleared by passing an empty string.

        Args:
          properties: Key value pairs representing the properties of the object.

          id_property: The name of a property whose values are unique for this object

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not leads_id:
            raise ValueError(f"Expected a non-empty value for `leads_id` but received {leads_id!r}")
        return self._patch(
            f"/crm/v3/objects/leads/{leads_id}",
            body=maybe_transform({"properties": properties}, lead_update_params.LeadUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id_property": id_property}, lead_update_params.LeadUpdateParams),
            ),
            cast_to=SimplePublicObject,
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
        """Read a page of leads.

        Control what is returned via the `properties` query param.

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
              the maximum number of leads that can be read by a single request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v3/objects/leads",
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
                    lead_list_params.LeadListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
        )

    def delete(
        self,
        leads_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move an Object identified by `{leadsId}` to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not leads_id:
            raise ValueError(f"Expected a non-empty value for `leads_id` but received {leads_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/objects/leads/{leads_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        leads_id: str,
        *,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        id_property: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """Read an Object identified by `{leadsId}`.

        `{leadsId}` refers to the internal
        object ID by default, or optionally any unique property value as specified by
        the `idProperty` query param. Control what is returned via the `properties`
        query param.

        Args:
          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          id_property: The name of a property whose values are unique for this object

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not leads_id:
            raise ValueError(f"Expected a non-empty value for `leads_id` but received {leads_id!r}")
        return self._get(
            f"/crm/v3/objects/leads/{leads_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "associations": associations,
                        "id_property": id_property,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    lead_get_params.LeadGetParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    def search(
        self,
        *,
        after: str | Omit = omit,
        filter_groups: Iterable[FilterGroupParam] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        sorts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Args:
          after: A paging cursor token for retrieving subsequent pages.

          filter_groups: Up to 6 groups of filters defining additional query criteria.

          limit: The maximum results to return, up to 200 objects.

          properties: A list of property names to include in the response.

          query: The search query string, up to 3000 characters.

          sorts: Specifies sorting order based on object properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/leads/search",
            body=maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "query": query,
                    "sorts": sorts,
                },
                lead_search_params.LeadSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class AsyncLeadsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLeadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncLeadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        properties: Dict[str, str],
        associations: Iterable[PublicAssociationsForObjectParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponseSimplePublicObject:
        """
        Create a lead with the given properties and return a copy of the object,
        including the ID. Documentation and examples for creating standard leads is
        provided.

        Args:
          properties: Key-value pairs for setting properties for the new object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/leads",
            body=await async_maybe_transform(
                {
                    "properties": properties,
                    "associations": associations,
                },
                lead_create_params.LeadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponseSimplePublicObject,
        )

    async def update(
        self,
        leads_id: str,
        *,
        properties: Dict[str, str],
        id_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Perform a partial update of an Object identified by `{leadsId}`or optionally a
        unique property value as specified by the `idProperty` query param. `{leadsId}`
        refers to the internal object ID by default, and the `idProperty` query param
        refers to a property whose values are unique for the object. Provided property
        values will be overwritten. Read-only and non-existent properties will result in
        an error. Properties values can be cleared by passing an empty string.

        Args:
          properties: Key value pairs representing the properties of the object.

          id_property: The name of a property whose values are unique for this object

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not leads_id:
            raise ValueError(f"Expected a non-empty value for `leads_id` but received {leads_id!r}")
        return await self._patch(
            f"/crm/v3/objects/leads/{leads_id}",
            body=await async_maybe_transform({"properties": properties}, lead_update_params.LeadUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id_property": id_property}, lead_update_params.LeadUpdateParams),
            ),
            cast_to=SimplePublicObject,
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
        """Read a page of leads.

        Control what is returned via the `properties` query param.

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
              the maximum number of leads that can be read by a single request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v3/objects/leads",
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
                    lead_list_params.LeadListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
        )

    async def delete(
        self,
        leads_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move an Object identified by `{leadsId}` to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not leads_id:
            raise ValueError(f"Expected a non-empty value for `leads_id` but received {leads_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/objects/leads/{leads_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        leads_id: str,
        *,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        id_property: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """Read an Object identified by `{leadsId}`.

        `{leadsId}` refers to the internal
        object ID by default, or optionally any unique property value as specified by
        the `idProperty` query param. Control what is returned via the `properties`
        query param.

        Args:
          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          id_property: The name of a property whose values are unique for this object

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not leads_id:
            raise ValueError(f"Expected a non-empty value for `leads_id` but received {leads_id!r}")
        return await self._get(
            f"/crm/v3/objects/leads/{leads_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "associations": associations,
                        "id_property": id_property,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    lead_get_params.LeadGetParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    async def search(
        self,
        *,
        after: str | Omit = omit,
        filter_groups: Iterable[FilterGroupParam] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        sorts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Args:
          after: A paging cursor token for retrieving subsequent pages.

          filter_groups: Up to 6 groups of filters defining additional query criteria.

          limit: The maximum results to return, up to 200 objects.

          properties: A list of property names to include in the response.

          query: The search query string, up to 3000 characters.

          sorts: Specifies sorting order based on object properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/leads/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "query": query,
                    "sorts": sorts,
                },
                lead_search_params.LeadSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class LeadsResourceWithRawResponse:
    def __init__(self, leads: LeadsResource) -> None:
        self._leads = leads

        self.create = to_raw_response_wrapper(
            leads.create,
        )
        self.update = to_raw_response_wrapper(
            leads.update,
        )
        self.list = to_raw_response_wrapper(
            leads.list,
        )
        self.delete = to_raw_response_wrapper(
            leads.delete,
        )
        self.get = to_raw_response_wrapper(
            leads.get,
        )
        self.search = to_raw_response_wrapper(
            leads.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._leads.batch)


class AsyncLeadsResourceWithRawResponse:
    def __init__(self, leads: AsyncLeadsResource) -> None:
        self._leads = leads

        self.create = async_to_raw_response_wrapper(
            leads.create,
        )
        self.update = async_to_raw_response_wrapper(
            leads.update,
        )
        self.list = async_to_raw_response_wrapper(
            leads.list,
        )
        self.delete = async_to_raw_response_wrapper(
            leads.delete,
        )
        self.get = async_to_raw_response_wrapper(
            leads.get,
        )
        self.search = async_to_raw_response_wrapper(
            leads.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._leads.batch)


class LeadsResourceWithStreamingResponse:
    def __init__(self, leads: LeadsResource) -> None:
        self._leads = leads

        self.create = to_streamed_response_wrapper(
            leads.create,
        )
        self.update = to_streamed_response_wrapper(
            leads.update,
        )
        self.list = to_streamed_response_wrapper(
            leads.list,
        )
        self.delete = to_streamed_response_wrapper(
            leads.delete,
        )
        self.get = to_streamed_response_wrapper(
            leads.get,
        )
        self.search = to_streamed_response_wrapper(
            leads.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._leads.batch)


class AsyncLeadsResourceWithStreamingResponse:
    def __init__(self, leads: AsyncLeadsResource) -> None:
        self._leads = leads

        self.create = async_to_streamed_response_wrapper(
            leads.create,
        )
        self.update = async_to_streamed_response_wrapper(
            leads.update,
        )
        self.list = async_to_streamed_response_wrapper(
            leads.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            leads.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            leads.get,
        )
        self.search = async_to_streamed_response_wrapper(
            leads.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._leads.batch)
