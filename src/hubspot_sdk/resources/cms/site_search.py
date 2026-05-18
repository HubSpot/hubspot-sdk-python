# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cms import site_search_get_indexed_data_params
from ..._base_client import make_request_options
from ...types.cms.indexed_data import IndexedData

__all__ = ["SiteSearchResource", "AsyncSiteSearchResource"]


class SiteSearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SiteSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SiteSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SiteSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SiteSearchResourceWithStreamingResponse(self)

    def get_indexed_data(
        self,
        content_id: str,
        *,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexedData:
        """
        Return all indexed data for an asset (e.g., page, blog post, HubDB table),
        specified by ID. This is useful when debugging why a particular asset is not
        returned from a custom search.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not content_id:
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return self._get(
            path_template("/cms/site-search/2026-03/indexed-data/{content_id}", content_id=content_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"type": type}, site_search_get_indexed_data_params.SiteSearchGetIndexedDataParams
                ),
            ),
            cast_to=IndexedData,
        )


class AsyncSiteSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSiteSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSiteSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSiteSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSiteSearchResourceWithStreamingResponse(self)

    async def get_indexed_data(
        self,
        content_id: str,
        *,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexedData:
        """
        Return all indexed data for an asset (e.g., page, blog post, HubDB table),
        specified by ID. This is useful when debugging why a particular asset is not
        returned from a custom search.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not content_id:
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return await self._get(
            path_template("/cms/site-search/2026-03/indexed-data/{content_id}", content_id=content_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, site_search_get_indexed_data_params.SiteSearchGetIndexedDataParams
                ),
            ),
            cast_to=IndexedData,
        )


class SiteSearchResourceWithRawResponse:
    def __init__(self, site_search: SiteSearchResource) -> None:
        self._site_search = site_search

        self.get_indexed_data = to_raw_response_wrapper(
            site_search.get_indexed_data,
        )


class AsyncSiteSearchResourceWithRawResponse:
    def __init__(self, site_search: AsyncSiteSearchResource) -> None:
        self._site_search = site_search

        self.get_indexed_data = async_to_raw_response_wrapper(
            site_search.get_indexed_data,
        )


class SiteSearchResourceWithStreamingResponse:
    def __init__(self, site_search: SiteSearchResource) -> None:
        self._site_search = site_search

        self.get_indexed_data = to_streamed_response_wrapper(
            site_search.get_indexed_data,
        )


class AsyncSiteSearchResourceWithStreamingResponse:
    def __init__(self, site_search: AsyncSiteSearchResource) -> None:
        self._site_search = site_search

        self.get_indexed_data = async_to_streamed_response_wrapper(
            site_search.get_indexed_data,
        )
