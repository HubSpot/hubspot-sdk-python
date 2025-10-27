# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform
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
from .....types.crm.associated_id import AssociatedID
from .....types.crm.objects.partner_services import association_list_params
from .....types.crm.simple_public_object_with_associations import SimplePublicObjectWithAssociations

__all__ = ["AssociationsResource", "AsyncAssociationsResource"]


class AssociationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AssociationsResourceWithStreamingResponse(self)

    def update(
        self,
        association_type: str,
        *,
        partner_service_id: str,
        to_object_type: str,
        to_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """
        Associate a partner service with another object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        if not association_type:
            raise ValueError(f"Expected a non-empty value for `association_type` but received {association_type!r}")
        return self._put(
            f"/crm/v3/objects/partner_services/{partner_service_id}/associations/{to_object_type}/{to_object_id}/{association_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    def list(
        self,
        to_object_type: str,
        *,
        partner_service_id: str,
        after: str | Omit = omit,
        include_fa: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[AssociatedID]:
        """
        List associations of a partner service by type

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
            f"/crm/v3/objects/partner_services/{partner_service_id}/associations/{to_object_type}",
            page=SyncPage[AssociatedID],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_fa": include_fa,
                        "limit": limit,
                    },
                    association_list_params.AssociationListParams,
                ),
            ),
            model=AssociatedID,
        )

    def delete(
        self,
        association_type: str,
        *,
        partner_service_id: str,
        to_object_type: str,
        to_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an association between two partner services

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        if not association_type:
            raise ValueError(f"Expected a non-empty value for `association_type` but received {association_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/objects/partner_services/{partner_service_id}/associations/{to_object_type}/{to_object_id}/{association_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAssociationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAssociationsResourceWithStreamingResponse(self)

    async def update(
        self,
        association_type: str,
        *,
        partner_service_id: str,
        to_object_type: str,
        to_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """
        Associate a partner service with another object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        if not association_type:
            raise ValueError(f"Expected a non-empty value for `association_type` but received {association_type!r}")
        return await self._put(
            f"/crm/v3/objects/partner_services/{partner_service_id}/associations/{to_object_type}/{to_object_id}/{association_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    def list(
        self,
        to_object_type: str,
        *,
        partner_service_id: str,
        after: str | Omit = omit,
        include_fa: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssociatedID, AsyncPage[AssociatedID]]:
        """
        List associations of a partner service by type

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
            f"/crm/v3/objects/partner_services/{partner_service_id}/associations/{to_object_type}",
            page=AsyncPage[AssociatedID],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_fa": include_fa,
                        "limit": limit,
                    },
                    association_list_params.AssociationListParams,
                ),
            ),
            model=AssociatedID,
        )

    async def delete(
        self,
        association_type: str,
        *,
        partner_service_id: str,
        to_object_type: str,
        to_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an association between two partner services

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partner_service_id:
            raise ValueError(f"Expected a non-empty value for `partner_service_id` but received {partner_service_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        if not association_type:
            raise ValueError(f"Expected a non-empty value for `association_type` but received {association_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/objects/partner_services/{partner_service_id}/associations/{to_object_type}/{to_object_id}/{association_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AssociationsResourceWithRawResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

        self.update = to_raw_response_wrapper(
            associations.update,
        )
        self.list = to_raw_response_wrapper(
            associations.list,
        )
        self.delete = to_raw_response_wrapper(
            associations.delete,
        )


class AsyncAssociationsResourceWithRawResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

        self.update = async_to_raw_response_wrapper(
            associations.update,
        )
        self.list = async_to_raw_response_wrapper(
            associations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            associations.delete,
        )


class AssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

        self.update = to_streamed_response_wrapper(
            associations.update,
        )
        self.list = to_streamed_response_wrapper(
            associations.list,
        )
        self.delete = to_streamed_response_wrapper(
            associations.delete,
        )


class AsyncAssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

        self.update = async_to_streamed_response_wrapper(
            associations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            associations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            associations.delete,
        )
