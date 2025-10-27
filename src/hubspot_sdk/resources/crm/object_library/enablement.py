# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.object_type_enablement_public_response import ObjectTypeEnablementPublicResponse
from ....types.crm.portal_object_type_enablement_public_response import PortalObjectTypeEnablementPublicResponse

__all__ = ["EnablementResource", "AsyncEnablementResource"]


class EnablementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnablementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnablementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnablementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EnablementResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalObjectTypeEnablementPublicResponse:
        """Returns all objects in the object library and their enablement status"""
        return self._get(
            "/crm/v3/object-library/enablement",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalObjectTypeEnablementPublicResponse,
        )

    def get(
        self,
        object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectTypeEnablementPublicResponse:
        """
        Returns an object and its enablement status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return self._get(
            f"/crm/v3/object-library/enablement/{object_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTypeEnablementPublicResponse,
        )


class AsyncEnablementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnablementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnablementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnablementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEnablementResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalObjectTypeEnablementPublicResponse:
        """Returns all objects in the object library and their enablement status"""
        return await self._get(
            "/crm/v3/object-library/enablement",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalObjectTypeEnablementPublicResponse,
        )

    async def get(
        self,
        object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectTypeEnablementPublicResponse:
        """
        Returns an object and its enablement status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return await self._get(
            f"/crm/v3/object-library/enablement/{object_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTypeEnablementPublicResponse,
        )


class EnablementResourceWithRawResponse:
    def __init__(self, enablement: EnablementResource) -> None:
        self._enablement = enablement

        self.list = to_raw_response_wrapper(
            enablement.list,
        )
        self.get = to_raw_response_wrapper(
            enablement.get,
        )


class AsyncEnablementResourceWithRawResponse:
    def __init__(self, enablement: AsyncEnablementResource) -> None:
        self._enablement = enablement

        self.list = async_to_raw_response_wrapper(
            enablement.list,
        )
        self.get = async_to_raw_response_wrapper(
            enablement.get,
        )


class EnablementResourceWithStreamingResponse:
    def __init__(self, enablement: EnablementResource) -> None:
        self._enablement = enablement

        self.list = to_streamed_response_wrapper(
            enablement.list,
        )
        self.get = to_streamed_response_wrapper(
            enablement.get,
        )


class AsyncEnablementResourceWithStreamingResponse:
    def __init__(self, enablement: AsyncEnablementResource) -> None:
        self._enablement = enablement

        self.list = async_to_streamed_response_wrapper(
            enablement.list,
        )
        self.get = async_to_streamed_response_wrapper(
            enablement.get,
        )
