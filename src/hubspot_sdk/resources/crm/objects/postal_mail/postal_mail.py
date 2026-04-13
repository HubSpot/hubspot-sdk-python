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
from ....._utils import path_template, maybe_transform, async_maybe_transform
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
    postal_mail_get_params,
    postal_mail_list_params,
    postal_mail_create_params,
    postal_mail_search_params,
    postal_mail_update_params,
)
from .....types.crm.filter_group_param import FilterGroupParam
from .....types.crm.simple_public_object import SimplePublicObject
from .....types.crm.public_associations_for_object_param import PublicAssociationsForObjectParam
from .....types.crm.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from .....types.crm.collection_response_with_total_simple_public_object import (
    CollectionResponseWithTotalSimplePublicObject,
)

__all__ = ["PostalMailResource", "AsyncPostalMailResource"]


class PostalMailResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostalMailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PostalMailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostalMailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return PostalMailResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        associations: Iterable[PublicAssociationsForObjectParam],
        properties: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Create a postal mail object with the given properties and return a copy of the
        object, including the ID.

        Args:
          properties: Key-value pairs for setting properties for the new object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/objects/2026-03/postal_mail",
            body=maybe_transform(
                {
                    "associations": associations,
                    "properties": properties,
                },
                postal_mail_create_params.PostalMailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObject,
        )

    def update(
        self,
        postal_mail_id: str,
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
        Args:
          properties: Key value pairs representing the properties of the object.

          id_property: The name of a property whose values are unique for this object type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not postal_mail_id:
            raise ValueError(f"Expected a non-empty value for `postal_mail_id` but received {postal_mail_id!r}")
        return self._patch(
            path_template("/crm/objects/2026-03/postal_mail/{postal_mail_id}", postal_mail_id=postal_mail_id),
            body=maybe_transform({"properties": properties}, postal_mail_update_params.PostalMailUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id_property": id_property}, postal_mail_update_params.PostalMailUpdateParams),
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
        """
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
            "/crm/objects/2026-03/postal_mail",
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
                    postal_mail_list_params.PostalMailListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
        )

    def delete(
        self,
        postal_mail_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move the postal mail object with the ID `{postalMailId}` to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not postal_mail_id:
            raise ValueError(f"Expected a non-empty value for `postal_mail_id` but received {postal_mail_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/objects/2026-03/postal_mail/{postal_mail_id}", postal_mail_id=postal_mail_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        postal_mail_id: str,
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
        """
        Args:
          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          id_property: The name of a property whose values are unique for this object type

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
        if not postal_mail_id:
            raise ValueError(f"Expected a non-empty value for `postal_mail_id` but received {postal_mail_id!r}")
        return self._get(
            path_template("/crm/objects/2026-03/postal_mail/{postal_mail_id}", postal_mail_id=postal_mail_id),
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
                    postal_mail_get_params.PostalMailGetParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
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
        Search for postal mail objects using specific criteria in the request.

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
            "/crm/objects/2026-03/postal_mail/search",
            body=maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                postal_mail_search_params.PostalMailSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class AsyncPostalMailResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostalMailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostalMailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostalMailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPostalMailResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        associations: Iterable[PublicAssociationsForObjectParam],
        properties: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Create a postal mail object with the given properties and return a copy of the
        object, including the ID.

        Args:
          properties: Key-value pairs for setting properties for the new object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/objects/2026-03/postal_mail",
            body=await async_maybe_transform(
                {
                    "associations": associations,
                    "properties": properties,
                },
                postal_mail_create_params.PostalMailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObject,
        )

    async def update(
        self,
        postal_mail_id: str,
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
        Args:
          properties: Key value pairs representing the properties of the object.

          id_property: The name of a property whose values are unique for this object type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not postal_mail_id:
            raise ValueError(f"Expected a non-empty value for `postal_mail_id` but received {postal_mail_id!r}")
        return await self._patch(
            path_template("/crm/objects/2026-03/postal_mail/{postal_mail_id}", postal_mail_id=postal_mail_id),
            body=await async_maybe_transform(
                {"properties": properties}, postal_mail_update_params.PostalMailUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id_property": id_property}, postal_mail_update_params.PostalMailUpdateParams
                ),
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
        """
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
            "/crm/objects/2026-03/postal_mail",
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
                    postal_mail_list_params.PostalMailListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
        )

    async def delete(
        self,
        postal_mail_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move the postal mail object with the ID `{postalMailId}` to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not postal_mail_id:
            raise ValueError(f"Expected a non-empty value for `postal_mail_id` but received {postal_mail_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/objects/2026-03/postal_mail/{postal_mail_id}", postal_mail_id=postal_mail_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        postal_mail_id: str,
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
        """
        Args:
          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          id_property: The name of a property whose values are unique for this object type

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
        if not postal_mail_id:
            raise ValueError(f"Expected a non-empty value for `postal_mail_id` but received {postal_mail_id!r}")
        return await self._get(
            path_template("/crm/objects/2026-03/postal_mail/{postal_mail_id}", postal_mail_id=postal_mail_id),
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
                    postal_mail_get_params.PostalMailGetParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
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
        Search for postal mail objects using specific criteria in the request.

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
            "/crm/objects/2026-03/postal_mail/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                postal_mail_search_params.PostalMailSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class PostalMailResourceWithRawResponse:
    def __init__(self, postal_mail: PostalMailResource) -> None:
        self._postal_mail = postal_mail

        self.create = to_raw_response_wrapper(
            postal_mail.create,
        )
        self.update = to_raw_response_wrapper(
            postal_mail.update,
        )
        self.list = to_raw_response_wrapper(
            postal_mail.list,
        )
        self.delete = to_raw_response_wrapper(
            postal_mail.delete,
        )
        self.get = to_raw_response_wrapper(
            postal_mail.get,
        )
        self.search = to_raw_response_wrapper(
            postal_mail.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._postal_mail.batch)


class AsyncPostalMailResourceWithRawResponse:
    def __init__(self, postal_mail: AsyncPostalMailResource) -> None:
        self._postal_mail = postal_mail

        self.create = async_to_raw_response_wrapper(
            postal_mail.create,
        )
        self.update = async_to_raw_response_wrapper(
            postal_mail.update,
        )
        self.list = async_to_raw_response_wrapper(
            postal_mail.list,
        )
        self.delete = async_to_raw_response_wrapper(
            postal_mail.delete,
        )
        self.get = async_to_raw_response_wrapper(
            postal_mail.get,
        )
        self.search = async_to_raw_response_wrapper(
            postal_mail.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._postal_mail.batch)


class PostalMailResourceWithStreamingResponse:
    def __init__(self, postal_mail: PostalMailResource) -> None:
        self._postal_mail = postal_mail

        self.create = to_streamed_response_wrapper(
            postal_mail.create,
        )
        self.update = to_streamed_response_wrapper(
            postal_mail.update,
        )
        self.list = to_streamed_response_wrapper(
            postal_mail.list,
        )
        self.delete = to_streamed_response_wrapper(
            postal_mail.delete,
        )
        self.get = to_streamed_response_wrapper(
            postal_mail.get,
        )
        self.search = to_streamed_response_wrapper(
            postal_mail.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._postal_mail.batch)


class AsyncPostalMailResourceWithStreamingResponse:
    def __init__(self, postal_mail: AsyncPostalMailResource) -> None:
        self._postal_mail = postal_mail

        self.create = async_to_streamed_response_wrapper(
            postal_mail.create,
        )
        self.update = async_to_streamed_response_wrapper(
            postal_mail.update,
        )
        self.list = async_to_streamed_response_wrapper(
            postal_mail.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            postal_mail.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            postal_mail.get,
        )
        self.search = async_to_streamed_response_wrapper(
            postal_mail.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._postal_mail.batch)
