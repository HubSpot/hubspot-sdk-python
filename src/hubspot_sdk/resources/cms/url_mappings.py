# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.cms import url_mapping_create_params
from ..._base_client import make_request_options

__all__ = ["URLMappingsResource", "AsyncURLMappingsResource"]


class URLMappingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return URLMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return URLMappingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        created: Union[str, datetime],
        destination: str,
        is_match_full_url: bool,
        is_match_query_string: bool,
        is_only_after_not_found: bool,
        is_pattern: bool,
        is_protocol_agnostic: bool,
        is_trailing_slash_optional: bool,
        precedence: int,
        redirect_style: int,
        route_prefix: str,
        updated: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Create a new URL mapping in your HubSpot account.

        This endpoint allows you to
        define URL redirections and mappings, which can be useful for managing site
        navigation and SEO. The request body must include all required properties of the
        UrlMapping schema.

        Args:
          id: The unique ID of this URL redirect.

          created: The date and time when the URL mapping was initially created.

          destination: The destination URL, where the target URL should be redirected if it matches the
              `routePrefix`.

          is_match_full_url: Whether the `routePrefix` should match on the entire URL, including the domain.

          is_match_query_string: Whether the `routePrefix` should match on the entire URL path, including the
              query string.

          is_only_after_not_found: Whether the URL redirect mapping should apply only if a live page on the URL
              isn't found. If False, the URL redirect mapping will take precedence over any
              existing page.

          is_pattern: Whether the `routePrefix` should match based on pattern.

          is_protocol_agnostic: Whether the `routePrefix` should match both HTTP and HTTPS protocols.

          is_trailing_slash_optional: Whether a trailing slash will be ignored.

          precedence: Used to prioritize URL redirection. If a given URL matches more than one
              redirect, the one with the **lower** precedence will be used.

          redirect_style: The type of redirect to create. Options include: 301 (permanent), 302
              (temporary), or 305 (proxy). Find more details
              [here](https://knowledge.hubspot.com/cos-general/how-to-redirect-a-hubspot-page).

          route_prefix: The target incoming URL, path, or pattern to match for redirection.

          updated: The date and time when the URL mapping was last modified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/url-mappings/2026-03/url-mappings",
            body=maybe_transform(
                {
                    "id": id,
                    "created": created,
                    "destination": destination,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "updated": updated,
                },
                url_mapping_create_params.URLMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Retrieve a list of URL mappings from the HubSpot account.

        This endpoint provides
        access to URL mapping configurations, which can be used to manage and redirect
        URLs within the HubSpot CMS. It is useful for understanding how URLs are
        structured and redirected in your content management setup.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/url-mappings/2026-03/url-mappings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific URL mapping in your HubSpot account using its unique
        identifier. This operation will remove the URL mapping permanently, and it
        requires appropriate write and delete permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Retrieve a specific URL mapping by its unique identifier.

        This endpoint is
        useful for obtaining details about a particular URL mapping configuration within
        your HubSpot account. It requires the ID of the URL mapping as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncURLMappingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncURLMappingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        created: Union[str, datetime],
        destination: str,
        is_match_full_url: bool,
        is_match_query_string: bool,
        is_only_after_not_found: bool,
        is_pattern: bool,
        is_protocol_agnostic: bool,
        is_trailing_slash_optional: bool,
        precedence: int,
        redirect_style: int,
        route_prefix: str,
        updated: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Create a new URL mapping in your HubSpot account.

        This endpoint allows you to
        define URL redirections and mappings, which can be useful for managing site
        navigation and SEO. The request body must include all required properties of the
        UrlMapping schema.

        Args:
          id: The unique ID of this URL redirect.

          created: The date and time when the URL mapping was initially created.

          destination: The destination URL, where the target URL should be redirected if it matches the
              `routePrefix`.

          is_match_full_url: Whether the `routePrefix` should match on the entire URL, including the domain.

          is_match_query_string: Whether the `routePrefix` should match on the entire URL path, including the
              query string.

          is_only_after_not_found: Whether the URL redirect mapping should apply only if a live page on the URL
              isn't found. If False, the URL redirect mapping will take precedence over any
              existing page.

          is_pattern: Whether the `routePrefix` should match based on pattern.

          is_protocol_agnostic: Whether the `routePrefix` should match both HTTP and HTTPS protocols.

          is_trailing_slash_optional: Whether a trailing slash will be ignored.

          precedence: Used to prioritize URL redirection. If a given URL matches more than one
              redirect, the one with the **lower** precedence will be used.

          redirect_style: The type of redirect to create. Options include: 301 (permanent), 302
              (temporary), or 305 (proxy). Find more details
              [here](https://knowledge.hubspot.com/cos-general/how-to-redirect-a-hubspot-page).

          route_prefix: The target incoming URL, path, or pattern to match for redirection.

          updated: The date and time when the URL mapping was last modified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/url-mappings/2026-03/url-mappings",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "created": created,
                    "destination": destination,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "updated": updated,
                },
                url_mapping_create_params.URLMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Retrieve a list of URL mappings from the HubSpot account.

        This endpoint provides
        access to URL mapping configurations, which can be used to manage and redirect
        URLs within the HubSpot CMS. It is useful for understanding how URLs are
        structured and redirected in your content management setup.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/url-mappings/2026-03/url-mappings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific URL mapping in your HubSpot account using its unique
        identifier. This operation will remove the URL mapping permanently, and it
        requires appropriate write and delete permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Retrieve a specific URL mapping by its unique identifier.

        This endpoint is
        useful for obtaining details about a particular URL mapping configuration within
        your HubSpot account. It requires the ID of the URL mapping as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class URLMappingsResourceWithRawResponse:
    def __init__(self, url_mappings: URLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = to_custom_raw_response_wrapper(
            url_mappings.create,
            BinaryAPIResponse,
        )
        self.list = to_custom_raw_response_wrapper(
            url_mappings.list,
            BinaryAPIResponse,
        )
        self.delete = to_raw_response_wrapper(
            url_mappings.delete,
        )
        self.get = to_custom_raw_response_wrapper(
            url_mappings.get,
            BinaryAPIResponse,
        )


class AsyncURLMappingsResourceWithRawResponse:
    def __init__(self, url_mappings: AsyncURLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = async_to_custom_raw_response_wrapper(
            url_mappings.create,
            AsyncBinaryAPIResponse,
        )
        self.list = async_to_custom_raw_response_wrapper(
            url_mappings.list,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_raw_response_wrapper(
            url_mappings.delete,
        )
        self.get = async_to_custom_raw_response_wrapper(
            url_mappings.get,
            AsyncBinaryAPIResponse,
        )


class URLMappingsResourceWithStreamingResponse:
    def __init__(self, url_mappings: URLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = to_custom_streamed_response_wrapper(
            url_mappings.create,
            StreamedBinaryAPIResponse,
        )
        self.list = to_custom_streamed_response_wrapper(
            url_mappings.list,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_streamed_response_wrapper(
            url_mappings.delete,
        )
        self.get = to_custom_streamed_response_wrapper(
            url_mappings.get,
            StreamedBinaryAPIResponse,
        )


class AsyncURLMappingsResourceWithStreamingResponse:
    def __init__(self, url_mappings: AsyncURLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = async_to_custom_streamed_response_wrapper(
            url_mappings.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list = async_to_custom_streamed_response_wrapper(
            url_mappings.list,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_streamed_response_wrapper(
            url_mappings.delete,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            url_mappings.get,
            AsyncStreamedBinaryAPIResponse,
        )
