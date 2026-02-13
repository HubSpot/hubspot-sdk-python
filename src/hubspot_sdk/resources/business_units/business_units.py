# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.business_units import business_unit_get_by_user_id_params
from ...types.business_units.collection_response_public_business_unit_no_paging import (
    CollectionResponsePublicBusinessUnitNoPaging,
)

__all__ = ["BusinessUnitsResource", "AsyncBusinessUnitsResource"]


class BusinessUnitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BusinessUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BusinessUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BusinessUnitsResourceWithStreamingResponse(self)

    def get_by_user_id(
        self,
        user_id: str,
        *,
        name: SequenceNotStr[str] | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicBusinessUnitNoPaging:
        """Get Business Units identified by `userId`.

        The `userId` refers to the user’s ID.

        Args:
          name: The names of Business Units to retrieve. If empty or not provided, then all
              associated Business Units will be returned.

          properties: The names of properties to optionally include in the response body. The only
              valid value is `logoMetadata`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/business-units/v3/business-units/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "properties": properties,
                    },
                    business_unit_get_by_user_id_params.BusinessUnitGetByUserIDParams,
                ),
            ),
            cast_to=CollectionResponsePublicBusinessUnitNoPaging,
        )


class AsyncBusinessUnitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBusinessUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBusinessUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBusinessUnitsResourceWithStreamingResponse(self)

    async def get_by_user_id(
        self,
        user_id: str,
        *,
        name: SequenceNotStr[str] | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicBusinessUnitNoPaging:
        """Get Business Units identified by `userId`.

        The `userId` refers to the user’s ID.

        Args:
          name: The names of Business Units to retrieve. If empty or not provided, then all
              associated Business Units will be returned.

          properties: The names of properties to optionally include in the response body. The only
              valid value is `logoMetadata`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/business-units/v3/business-units/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "properties": properties,
                    },
                    business_unit_get_by_user_id_params.BusinessUnitGetByUserIDParams,
                ),
            ),
            cast_to=CollectionResponsePublicBusinessUnitNoPaging,
        )


class BusinessUnitsResourceWithRawResponse:
    def __init__(self, business_units: BusinessUnitsResource) -> None:
        self._business_units = business_units

        self.get_by_user_id = to_raw_response_wrapper(
            business_units.get_by_user_id,
        )


class AsyncBusinessUnitsResourceWithRawResponse:
    def __init__(self, business_units: AsyncBusinessUnitsResource) -> None:
        self._business_units = business_units

        self.get_by_user_id = async_to_raw_response_wrapper(
            business_units.get_by_user_id,
        )


class BusinessUnitsResourceWithStreamingResponse:
    def __init__(self, business_units: BusinessUnitsResource) -> None:
        self._business_units = business_units

        self.get_by_user_id = to_streamed_response_wrapper(
            business_units.get_by_user_id,
        )


class AsyncBusinessUnitsResourceWithStreamingResponse:
    def __init__(self, business_units: AsyncBusinessUnitsResource) -> None:
        self._business_units = business_units

        self.get_by_user_id = async_to_streamed_response_wrapper(
            business_units.get_by_user_id,
        )
