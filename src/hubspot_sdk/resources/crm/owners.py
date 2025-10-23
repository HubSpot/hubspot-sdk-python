# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.crm import owner_get_params, owner_list_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.crm.public_owner import PublicOwner

__all__ = ["OwnersResource", "AsyncOwnersResource"]


class OwnersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OwnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OwnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return OwnersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        email: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicOwner]:
        """
        Retrieve a paginated list of owners available in the account.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results (optional).

          archived: Whether to return only results that have been archived.

          email: Filter by email address (optional).

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v3/owners/",
            page=SyncPage[PublicOwner],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "email": email,
                        "limit": limit,
                    },
                    owner_list_params.OwnerListParams,
                ),
            ),
            model=PublicOwner,
        )

    def get(
        self,
        owner_id: int,
        *,
        archived: bool | Omit = omit,
        id_property: Literal["id", "userId"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicOwner:
        """
        Retrieve details of a specific owner using either their 'id' or 'userId'.

        Args:
          archived: Whether to return only results that have been archived.

          id_property: Specifies whether to use 'id' or 'userId' as the identifier for the owner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v3/owners/{owner_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "id_property": id_property,
                    },
                    owner_get_params.OwnerGetParams,
                ),
            ),
            cast_to=PublicOwner,
        )


class AsyncOwnersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOwnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOwnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncOwnersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        email: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicOwner, AsyncPage[PublicOwner]]:
        """
        Retrieve a paginated list of owners available in the account.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results (optional).

          archived: Whether to return only results that have been archived.

          email: Filter by email address (optional).

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v3/owners/",
            page=AsyncPage[PublicOwner],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "email": email,
                        "limit": limit,
                    },
                    owner_list_params.OwnerListParams,
                ),
            ),
            model=PublicOwner,
        )

    async def get(
        self,
        owner_id: int,
        *,
        archived: bool | Omit = omit,
        id_property: Literal["id", "userId"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicOwner:
        """
        Retrieve details of a specific owner using either their 'id' or 'userId'.

        Args:
          archived: Whether to return only results that have been archived.

          id_property: Specifies whether to use 'id' or 'userId' as the identifier for the owner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v3/owners/{owner_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "id_property": id_property,
                    },
                    owner_get_params.OwnerGetParams,
                ),
            ),
            cast_to=PublicOwner,
        )


class OwnersResourceWithRawResponse:
    def __init__(self, owners: OwnersResource) -> None:
        self._owners = owners

        self.list = to_raw_response_wrapper(
            owners.list,
        )
        self.get = to_raw_response_wrapper(
            owners.get,
        )


class AsyncOwnersResourceWithRawResponse:
    def __init__(self, owners: AsyncOwnersResource) -> None:
        self._owners = owners

        self.list = async_to_raw_response_wrapper(
            owners.list,
        )
        self.get = async_to_raw_response_wrapper(
            owners.get,
        )


class OwnersResourceWithStreamingResponse:
    def __init__(self, owners: OwnersResource) -> None:
        self._owners = owners

        self.list = to_streamed_response_wrapper(
            owners.list,
        )
        self.get = to_streamed_response_wrapper(
            owners.get,
        )


class AsyncOwnersResourceWithStreamingResponse:
    def __init__(self, owners: AsyncOwnersResource) -> None:
        self._owners = owners

        self.list = async_to_streamed_response_wrapper(
            owners.list,
        )
        self.get = async_to_streamed_response_wrapper(
            owners.get,
        )
