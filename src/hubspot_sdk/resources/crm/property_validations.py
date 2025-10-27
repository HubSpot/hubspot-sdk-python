# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.crm.collection_response_public_property_validation_rule_no_paging import (
    CollectionResponsePublicPropertyValidationRuleNoPaging,
)
from ...types.crm.collection_response_public_property_validation_rule_map_no_paging import (
    CollectionResponsePublicPropertyValidationRuleMapNoPaging,
)

__all__ = ["PropertyValidationsResource", "AsyncPropertyValidationsResource"]


class PropertyValidationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PropertyValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PropertyValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertyValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PropertyValidationsResourceWithStreamingResponse(self)

    def list(
        self,
        object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleMapNoPaging:
        """
        Read all properties with validation rules for a given object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return self._get(
            f"/crm/v3/property-validations/{object_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleMapNoPaging,
        )

    def get(
        self,
        property_name: str,
        *,
        object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleNoPaging:
        """
        Read a property's validation rules identified by {propertyName}.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return self._get(
            f"/crm/v3/property-validations/{object_type_id}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleNoPaging,
        )


class AsyncPropertyValidationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPropertyValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertyValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertyValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPropertyValidationsResourceWithStreamingResponse(self)

    async def list(
        self,
        object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleMapNoPaging:
        """
        Read all properties with validation rules for a given object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return await self._get(
            f"/crm/v3/property-validations/{object_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleMapNoPaging,
        )

    async def get(
        self,
        property_name: str,
        *,
        object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleNoPaging:
        """
        Read a property's validation rules identified by {propertyName}.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return await self._get(
            f"/crm/v3/property-validations/{object_type_id}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleNoPaging,
        )


class PropertyValidationsResourceWithRawResponse:
    def __init__(self, property_validations: PropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = to_raw_response_wrapper(
            property_validations.list,
        )
        self.get = to_raw_response_wrapper(
            property_validations.get,
        )


class AsyncPropertyValidationsResourceWithRawResponse:
    def __init__(self, property_validations: AsyncPropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = async_to_raw_response_wrapper(
            property_validations.list,
        )
        self.get = async_to_raw_response_wrapper(
            property_validations.get,
        )


class PropertyValidationsResourceWithStreamingResponse:
    def __init__(self, property_validations: PropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = to_streamed_response_wrapper(
            property_validations.list,
        )
        self.get = to_streamed_response_wrapper(
            property_validations.get,
        )


class AsyncPropertyValidationsResourceWithStreamingResponse:
    def __init__(self, property_validations: AsyncPropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = async_to_streamed_response_wrapper(
            property_validations.list,
        )
        self.get = async_to_streamed_response_wrapper(
            property_validations.get,
        )
