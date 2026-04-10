# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.conversations import visitor_identification_generate_token_params
from ...types.conversations.identification_token_response import IdentificationTokenResponse

__all__ = ["VisitorIdentificationResource", "AsyncVisitorIdentificationResource"]


class VisitorIdentificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VisitorIdentificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VisitorIdentificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VisitorIdentificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return VisitorIdentificationResourceWithStreamingResponse(self)

    def generate_token(
        self,
        *,
        email: str,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentificationTokenResponse:
        """
        Generate an identification token for a website visitor who has been
        authenticated using your own system. An identification token returned from this
        API can be used to pass information about your already-authenticated visitor to
        the chat widget, so that it treats the visitor as a known contact. This allows
        support agents to recognize and assist the visitor more effectively.

        Args:
          email: The email of the visitor that you wish to identify

          first_name: The first name of the visitor that you wish to identify. This value will only be
              set in HubSpot for new contacts and existing contacts where first name is
              unknown. Optional.

          last_name: The last name of the visitor that you wish to identify. This value will only be
              set in HubSpot for new contacts and existing contacts where last name is
              unknown. Optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/visitor-identification/2026-03/tokens/create",
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                visitor_identification_generate_token_params.VisitorIdentificationGenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentificationTokenResponse,
        )


class AsyncVisitorIdentificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVisitorIdentificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVisitorIdentificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVisitorIdentificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncVisitorIdentificationResourceWithStreamingResponse(self)

    async def generate_token(
        self,
        *,
        email: str,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentificationTokenResponse:
        """
        Generate an identification token for a website visitor who has been
        authenticated using your own system. An identification token returned from this
        API can be used to pass information about your already-authenticated visitor to
        the chat widget, so that it treats the visitor as a known contact. This allows
        support agents to recognize and assist the visitor more effectively.

        Args:
          email: The email of the visitor that you wish to identify

          first_name: The first name of the visitor that you wish to identify. This value will only be
              set in HubSpot for new contacts and existing contacts where first name is
              unknown. Optional.

          last_name: The last name of the visitor that you wish to identify. This value will only be
              set in HubSpot for new contacts and existing contacts where last name is
              unknown. Optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/visitor-identification/2026-03/tokens/create",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                visitor_identification_generate_token_params.VisitorIdentificationGenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentificationTokenResponse,
        )


class VisitorIdentificationResourceWithRawResponse:
    def __init__(self, visitor_identification: VisitorIdentificationResource) -> None:
        self._visitor_identification = visitor_identification

        self.generate_token = to_raw_response_wrapper(
            visitor_identification.generate_token,
        )


class AsyncVisitorIdentificationResourceWithRawResponse:
    def __init__(self, visitor_identification: AsyncVisitorIdentificationResource) -> None:
        self._visitor_identification = visitor_identification

        self.generate_token = async_to_raw_response_wrapper(
            visitor_identification.generate_token,
        )


class VisitorIdentificationResourceWithStreamingResponse:
    def __init__(self, visitor_identification: VisitorIdentificationResource) -> None:
        self._visitor_identification = visitor_identification

        self.generate_token = to_streamed_response_wrapper(
            visitor_identification.generate_token,
        )


class AsyncVisitorIdentificationResourceWithStreamingResponse:
    def __init__(self, visitor_identification: AsyncVisitorIdentificationResource) -> None:
        self._visitor_identification = visitor_identification

        self.generate_token = async_to_streamed_response_wrapper(
            visitor_identification.generate_token,
        )
