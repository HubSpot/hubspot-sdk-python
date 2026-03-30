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
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
    partner_service_get_params,
    partner_service_list_params,
    partner_service_search_params,
    partner_service_update_params,
)
from .....types.crm.filter_group_param import FilterGroupParam
from .....types.crm.simple_public_object import SimplePublicObject
from .....types.crm.multi_associated_object_with_label import MultiAssociatedObjectWithLabel
from .....types.crm.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from .....types.crm.collection_response_with_total_simple_public_object import (
    CollectionResponseWithTotalSimplePublicObject,
)

__all__ = ["PartnerServicesResource", "AsyncPartnerServicesResource"]


class PartnerServicesResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> PartnerServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PartnerServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartnerServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PartnerServicesResourceWithStreamingResponse(self)

    def update(
        self,
        partner_service_id: str,
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
        Perform a partial update of an Object identified by `{partnerServiceId}`or
        optionally a unique property value as specified by the `idProperty` query param.
        `{partnerServiceId}` refers to the internal object ID by default, and the
        `idProperty` query param refers to a property whose values are unique for the
        object. Provided property values will be overwritten. Read-only and non-existent
        properties will result in an error. Properties values can be cleared by passing
        an empty string.

        Args:
          properties: Key value pairs representing the properties of the object.

          id_property: The name of a property whose values are unique for this object type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        return self._patch(
            path_template(
                "/crm/objects/2026-03/partner_services/{partner_service_id}", partner_service_id=partner_service_id
            ),
            body=maybe_transform({"properties": properties}, partner_service_update_params.PartnerServiceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"id_property": id_property}, partner_service_update_params.PartnerServiceUpdateParams
                ),
            ),
            cast_to=SimplePublicObject,
        )

    def list(
        self,
        to_object_type: str,
        *,
        partner_service_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[MultiAssociatedObjectWithLabel]:
        """
        Retrieve a list of associations for a specific partner service, filtered by the
        type of associated object.

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
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._get_api_list(
            path_template(
                "/crm/objects/2026-03/partner_services/{partner_service_id}/associations/{to_object_type}",
                partner_service_id=partner_service_id,
                to_object_type=to_object_type,
            ),
            page=SyncPage[MultiAssociatedObjectWithLabel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    partner_service_list_params.PartnerServiceListParams,
                ),
            ),
            model=MultiAssociatedObjectWithLabel,
        )

    def get(
        self,
        partner_service_id: str,
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
        """Read an Object identified by `{partnerServiceId}`.

        `{partnerServiceId}` refers
        to the internal object ID by default, or optionally any unique property value as
        specified by the `idProperty` query param. Control what is returned via the
        `properties` query param.

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
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        return self._get(
            path_template(
                "/crm/objects/2026-03/partner_services/{partner_service_id}", partner_service_id=partner_service_id
            ),
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
                    partner_service_get_params.PartnerServiceGetParams,
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
        Execute a search query to find partner services based on defined filters,
        properties, and sorting options. This endpoint allows you to retrieve a
        collection of partner services that match the specified search criteria.

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
            "/crm/objects/2026-03/partner_services/search",
            body=maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                partner_service_search_params.PartnerServiceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class AsyncPartnerServicesResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPartnerServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPartnerServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartnerServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPartnerServicesResourceWithStreamingResponse(self)

    async def update(
        self,
        partner_service_id: str,
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
        Perform a partial update of an Object identified by `{partnerServiceId}`or
        optionally a unique property value as specified by the `idProperty` query param.
        `{partnerServiceId}` refers to the internal object ID by default, and the
        `idProperty` query param refers to a property whose values are unique for the
        object. Provided property values will be overwritten. Read-only and non-existent
        properties will result in an error. Properties values can be cleared by passing
        an empty string.

        Args:
          properties: Key value pairs representing the properties of the object.

          id_property: The name of a property whose values are unique for this object type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        return await self._patch(
            path_template(
                "/crm/objects/2026-03/partner_services/{partner_service_id}", partner_service_id=partner_service_id
            ),
            body=await async_maybe_transform(
                {"properties": properties}, partner_service_update_params.PartnerServiceUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id_property": id_property}, partner_service_update_params.PartnerServiceUpdateParams
                ),
            ),
            cast_to=SimplePublicObject,
        )

    def list(
        self,
        to_object_type: str,
        *,
        partner_service_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MultiAssociatedObjectWithLabel, AsyncPage[MultiAssociatedObjectWithLabel]]:
        """
        Retrieve a list of associations for a specific partner service, filtered by the
        type of associated object.

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
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._get_api_list(
            path_template(
                "/crm/objects/2026-03/partner_services/{partner_service_id}/associations/{to_object_type}",
                partner_service_id=partner_service_id,
                to_object_type=to_object_type,
            ),
            page=AsyncPage[MultiAssociatedObjectWithLabel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    partner_service_list_params.PartnerServiceListParams,
                ),
            ),
            model=MultiAssociatedObjectWithLabel,
        )

    async def get(
        self,
        partner_service_id: str,
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
        """Read an Object identified by `{partnerServiceId}`.

        `{partnerServiceId}` refers
        to the internal object ID by default, or optionally any unique property value as
        specified by the `idProperty` query param. Control what is returned via the
        `properties` query param.

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
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        return await self._get(
            path_template(
                "/crm/objects/2026-03/partner_services/{partner_service_id}", partner_service_id=partner_service_id
            ),
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
                    partner_service_get_params.PartnerServiceGetParams,
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
        Execute a search query to find partner services based on defined filters,
        properties, and sorting options. This endpoint allows you to retrieve a
        collection of partner services that match the specified search criteria.

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
            "/crm/objects/2026-03/partner_services/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                partner_service_search_params.PartnerServiceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class PartnerServicesResourceWithRawResponse:
    def __init__(self, partner_services: PartnerServicesResource) -> None:
        self._partner_services = partner_services

        self.update = to_raw_response_wrapper(
            partner_services.update,
        )
        self.list = to_raw_response_wrapper(
            partner_services.list,
        )
        self.get = to_raw_response_wrapper(
            partner_services.get,
        )
        self.search = to_raw_response_wrapper(
            partner_services.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._partner_services.batch)


class AsyncPartnerServicesResourceWithRawResponse:
    def __init__(self, partner_services: AsyncPartnerServicesResource) -> None:
        self._partner_services = partner_services

        self.update = async_to_raw_response_wrapper(
            partner_services.update,
        )
        self.list = async_to_raw_response_wrapper(
            partner_services.list,
        )
        self.get = async_to_raw_response_wrapper(
            partner_services.get,
        )
        self.search = async_to_raw_response_wrapper(
            partner_services.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._partner_services.batch)


class PartnerServicesResourceWithStreamingResponse:
    def __init__(self, partner_services: PartnerServicesResource) -> None:
        self._partner_services = partner_services

        self.update = to_streamed_response_wrapper(
            partner_services.update,
        )
        self.list = to_streamed_response_wrapper(
            partner_services.list,
        )
        self.get = to_streamed_response_wrapper(
            partner_services.get,
        )
        self.search = to_streamed_response_wrapper(
            partner_services.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._partner_services.batch)


class AsyncPartnerServicesResourceWithStreamingResponse:
    def __init__(self, partner_services: AsyncPartnerServicesResource) -> None:
        self._partner_services = partner_services

        self.update = async_to_streamed_response_wrapper(
            partner_services.update,
        )
        self.list = async_to_streamed_response_wrapper(
            partner_services.list,
        )
        self.get = async_to_streamed_response_wrapper(
            partner_services.get,
        )
        self.search = async_to_streamed_response_wrapper(
            partner_services.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._partner_services.batch)
