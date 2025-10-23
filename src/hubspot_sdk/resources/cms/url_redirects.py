# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cms import url_redirect_list_params, url_redirect_create_params, url_redirect_update_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cms.url_mapping import URLMapping

__all__ = ["URLRedirectsResource", "AsyncURLRedirectsResource"]


class URLRedirectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLRedirectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return URLRedirectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLRedirectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return URLRedirectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        destination: str,
        redirect_style: int,
        route_prefix: str,
        is_match_full_url: bool | Omit = omit,
        is_match_query_string: bool | Omit = omit,
        is_only_after_not_found: bool | Omit = omit,
        is_pattern: bool | Omit = omit,
        is_protocol_agnostic: bool | Omit = omit,
        is_trailing_slash_optional: bool | Omit = omit,
        precedence: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Creates and configures a new URL redirect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/url-redirects/",
            body=maybe_transform(
                {
                    "destination": destination,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                },
                url_redirect_create_params.URLRedirectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    def update(
        self,
        url_redirect_id: str,
        *,
        id: str,
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
        created: Union[str, datetime] | Omit = omit,
        updated: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Updates the settings for an existing URL redirect.

        Args:
          id: The unique ID of this URL redirect.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return self._patch(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            body=maybe_transform(
                {
                    "id": id,
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
                    "created": created,
                    "updated": updated,
                },
                url_redirect_update_params.URLRedirectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[URLMapping]:
        """Returns all existing URL redirects.

        Results can be limited and filtered by
        creation or updated date.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          created_after: Only return redirects created after this date.

          created_at: Only return redirects created on exactly this date.

          created_before: Only return redirects created before this date.

          limit: Maximum number of result per page

          updated_after: Only return redirects last updated after this date.

          updated_at: Only return redirects last updated on exactly this date.

          updated_before: Only return redirects last updated before this date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/url-redirects/",
            page=SyncPage[URLMapping],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    url_redirect_list_params.URLRedirectListParams,
                ),
            ),
            model=URLMapping,
        )

    def delete(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete one existing redirect, so it is no longer mapped.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Returns the details for a single existing URL redirect by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return self._get(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )


class AsyncURLRedirectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLRedirectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLRedirectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLRedirectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncURLRedirectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        destination: str,
        redirect_style: int,
        route_prefix: str,
        is_match_full_url: bool | Omit = omit,
        is_match_query_string: bool | Omit = omit,
        is_only_after_not_found: bool | Omit = omit,
        is_pattern: bool | Omit = omit,
        is_protocol_agnostic: bool | Omit = omit,
        is_trailing_slash_optional: bool | Omit = omit,
        precedence: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Creates and configures a new URL redirect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/url-redirects/",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                },
                url_redirect_create_params.URLRedirectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    async def update(
        self,
        url_redirect_id: str,
        *,
        id: str,
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
        created: Union[str, datetime] | Omit = omit,
        updated: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Updates the settings for an existing URL redirect.

        Args:
          id: The unique ID of this URL redirect.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return await self._patch(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
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
                    "created": created,
                    "updated": updated,
                },
                url_redirect_update_params.URLRedirectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[URLMapping, AsyncPage[URLMapping]]:
        """Returns all existing URL redirects.

        Results can be limited and filtered by
        creation or updated date.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          created_after: Only return redirects created after this date.

          created_at: Only return redirects created on exactly this date.

          created_before: Only return redirects created before this date.

          limit: Maximum number of result per page

          updated_after: Only return redirects last updated after this date.

          updated_at: Only return redirects last updated on exactly this date.

          updated_before: Only return redirects last updated before this date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/url-redirects/",
            page=AsyncPage[URLMapping],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    url_redirect_list_params.URLRedirectListParams,
                ),
            ),
            model=URLMapping,
        )

    async def delete(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete one existing redirect, so it is no longer mapped.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Returns the details for a single existing URL redirect by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return await self._get(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )


class URLRedirectsResourceWithRawResponse:
    def __init__(self, url_redirects: URLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = to_raw_response_wrapper(
            url_redirects.create,
        )
        self.update = to_raw_response_wrapper(
            url_redirects.update,
        )
        self.list = to_raw_response_wrapper(
            url_redirects.list,
        )
        self.delete = to_raw_response_wrapper(
            url_redirects.delete,
        )
        self.read = to_raw_response_wrapper(
            url_redirects.read,
        )


class AsyncURLRedirectsResourceWithRawResponse:
    def __init__(self, url_redirects: AsyncURLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = async_to_raw_response_wrapper(
            url_redirects.create,
        )
        self.update = async_to_raw_response_wrapper(
            url_redirects.update,
        )
        self.list = async_to_raw_response_wrapper(
            url_redirects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            url_redirects.delete,
        )
        self.read = async_to_raw_response_wrapper(
            url_redirects.read,
        )


class URLRedirectsResourceWithStreamingResponse:
    def __init__(self, url_redirects: URLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = to_streamed_response_wrapper(
            url_redirects.create,
        )
        self.update = to_streamed_response_wrapper(
            url_redirects.update,
        )
        self.list = to_streamed_response_wrapper(
            url_redirects.list,
        )
        self.delete = to_streamed_response_wrapper(
            url_redirects.delete,
        )
        self.read = to_streamed_response_wrapper(
            url_redirects.read,
        )


class AsyncURLRedirectsResourceWithStreamingResponse:
    def __init__(self, url_redirects: AsyncURLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = async_to_streamed_response_wrapper(
            url_redirects.create,
        )
        self.update = async_to_streamed_response_wrapper(
            url_redirects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            url_redirects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            url_redirects.delete,
        )
        self.read = async_to_streamed_response_wrapper(
            url_redirects.read,
        )
