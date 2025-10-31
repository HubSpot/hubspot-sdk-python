# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.feature_flags import portal_update_params, portal_batch_delete_params, portal_batch_upsert_params
from ....types.crm.feature_flags.portal_get_response import PortalGetResponse
from ....types.crm.feature_flags.portal_delete_response import PortalDeleteResponse
from ....types.crm.feature_flags.portal_update_response import PortalUpdateResponse
from ....types.crm.feature_flags.portal_batch_delete_response import PortalBatchDeleteResponse
from ....types.crm.feature_flags.portal_batch_upsert_response import PortalBatchUpsertResponse

__all__ = ["PortalsResource", "AsyncPortalsResource"]


class PortalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PortalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PortalsResourceWithStreamingResponse(self)

    def update(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        flag_state: Literal["OFF", "ON", "ABSENT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalUpdateResponse:
        """
        Specify an account-level flag state for a specific HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._put(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/{portal_id}",
            body=maybe_transform({"flag_state": flag_state}, portal_update_params.PortalUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalUpdateResponse,
        )

    def delete(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalDeleteResponse:
        """Delete an account-level flag state for a specific HubSpot account.

        No request
        body is included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._delete(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/{portal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalDeleteResponse,
        )

    def batch_delete(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalBatchDeleteResponse:
        """Delete an account-level flag state for multiple HubSpot accounts at once.

        Use
        this endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._post(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/batch/delete",
            body=maybe_transform({"portal_ids": portal_ids}, portal_batch_delete_params.PortalBatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalBatchDeleteResponse,
        )

    def batch_upsert(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_states: Iterable[portal_batch_upsert_params.PortalState],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalBatchUpsertResponse:
        """Set the portal flag state for multiple HubSpot accounts at once.

        Use this
        endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._post(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/batch/upsert",
            body=maybe_transform({"portal_states": portal_states}, portal_batch_upsert_params.PortalBatchUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalBatchUpsertResponse,
        )

    def get(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalGetResponse:
        """
        Retrieve the account-level flag state of a specific HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._get(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/{portal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalGetResponse,
        )


class AsyncPortalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPortalsResourceWithStreamingResponse(self)

    async def update(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        flag_state: Literal["OFF", "ON", "ABSENT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalUpdateResponse:
        """
        Specify an account-level flag state for a specific HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._put(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/{portal_id}",
            body=await async_maybe_transform({"flag_state": flag_state}, portal_update_params.PortalUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalUpdateResponse,
        )

    async def delete(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalDeleteResponse:
        """Delete an account-level flag state for a specific HubSpot account.

        No request
        body is included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._delete(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/{portal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalDeleteResponse,
        )

    async def batch_delete(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalBatchDeleteResponse:
        """Delete an account-level flag state for multiple HubSpot accounts at once.

        Use
        this endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._post(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/batch/delete",
            body=await async_maybe_transform(
                {"portal_ids": portal_ids}, portal_batch_delete_params.PortalBatchDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalBatchDeleteResponse,
        )

    async def batch_upsert(
        self,
        flag_name: str,
        *,
        app_id: int,
        portal_states: Iterable[portal_batch_upsert_params.PortalState],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalBatchUpsertResponse:
        """Set the portal flag state for multiple HubSpot accounts at once.

        Use this
        endpoint to manage flag exposure for groups of HubSpot accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._post(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/batch/upsert",
            body=await async_maybe_transform(
                {"portal_states": portal_states}, portal_batch_upsert_params.PortalBatchUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalBatchUpsertResponse,
        )

    async def get(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalGetResponse:
        """
        Retrieve the account-level flag state of a specific HubSpot account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._get(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals/{portal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalGetResponse,
        )


class PortalsResourceWithRawResponse:
    def __init__(self, portals: PortalsResource) -> None:
        self._portals = portals

        self.update = to_raw_response_wrapper(
            portals.update,
        )
        self.delete = to_raw_response_wrapper(
            portals.delete,
        )
        self.batch_delete = to_raw_response_wrapper(
            portals.batch_delete,
        )
        self.batch_upsert = to_raw_response_wrapper(
            portals.batch_upsert,
        )
        self.get = to_raw_response_wrapper(
            portals.get,
        )


class AsyncPortalsResourceWithRawResponse:
    def __init__(self, portals: AsyncPortalsResource) -> None:
        self._portals = portals

        self.update = async_to_raw_response_wrapper(
            portals.update,
        )
        self.delete = async_to_raw_response_wrapper(
            portals.delete,
        )
        self.batch_delete = async_to_raw_response_wrapper(
            portals.batch_delete,
        )
        self.batch_upsert = async_to_raw_response_wrapper(
            portals.batch_upsert,
        )
        self.get = async_to_raw_response_wrapper(
            portals.get,
        )


class PortalsResourceWithStreamingResponse:
    def __init__(self, portals: PortalsResource) -> None:
        self._portals = portals

        self.update = to_streamed_response_wrapper(
            portals.update,
        )
        self.delete = to_streamed_response_wrapper(
            portals.delete,
        )
        self.batch_delete = to_streamed_response_wrapper(
            portals.batch_delete,
        )
        self.batch_upsert = to_streamed_response_wrapper(
            portals.batch_upsert,
        )
        self.get = to_streamed_response_wrapper(
            portals.get,
        )


class AsyncPortalsResourceWithStreamingResponse:
    def __init__(self, portals: AsyncPortalsResource) -> None:
        self._portals = portals

        self.update = async_to_streamed_response_wrapper(
            portals.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            portals.delete,
        )
        self.batch_delete = async_to_streamed_response_wrapper(
            portals.batch_delete,
        )
        self.batch_upsert = async_to_streamed_response_wrapper(
            portals.batch_upsert,
        )
        self.get = async_to_streamed_response_wrapper(
            portals.get,
        )
