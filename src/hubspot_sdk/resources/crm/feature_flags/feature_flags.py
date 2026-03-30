# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.crm import feature_flag_update_params, feature_flag_list_portals_params
from ...._base_client import make_request_options
from ....types.crm.flags_for_app_response import FlagsForAppResponse
from ....types.crm.portal_flag_state_response import PortalFlagStateResponse
from ....types.crm.portal_flag_state_batch_response import PortalFlagStateBatchResponse

__all__ = ["FeatureFlagsResource", "AsyncFeatureFlagsResource"]


class FeatureFlagsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> FeatureFlagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FeatureFlagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeatureFlagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FeatureFlagsResourceWithStreamingResponse(self)

    def update(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        flag_state: Literal["ABSENT", "OFF", "ON"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateResponse:
        """
        Specify an account-level flag state for a specific HubSpot account.

        Args:
          flag_state: The state that the given flag should be in for this portal

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._put(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/{portal_id}",
                app_id=app_id,
                flag_name=flag_name,
                portal_id=portal_id,
            ),
            body=maybe_transform({"flag_state": flag_state}, feature_flag_update_params.FeatureFlagUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateResponse,
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
    ) -> PortalFlagStateResponse:
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
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/{portal_id}",
                app_id=app_id,
                flag_name=flag_name,
                portal_id=portal_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateResponse,
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
    ) -> PortalFlagStateResponse:
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
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/{portal_id}",
                app_id=app_id,
                flag_name=flag_name,
                portal_id=portal_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateResponse,
        )

    def list_all(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagsForAppResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/feature-flags/2026-03/{app_id}/flags/all", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagsForAppResponse,
        )

    def list_portals(
        self,
        flag_name: str,
        *,
        app_id: int,
        limit: int | Omit = omit,
        start_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateBatchResponse:
        """
        Retrieve a list of HubSpot accounts with an account-level flag setting for the
        specified app. No request body is included.

        Args:
          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._get(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals", app_id=app_id, flag_name=flag_name
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "start_portal_id": start_portal_id,
                    },
                    feature_flag_list_portals_params.FeatureFlagListPortalsParams,
                ),
            ),
            cast_to=PortalFlagStateBatchResponse,
        )


class AsyncFeatureFlagsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFeatureFlagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeatureFlagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeatureFlagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFeatureFlagsResourceWithStreamingResponse(self)

    async def update(
        self,
        portal_id: int,
        *,
        app_id: int,
        flag_name: str,
        flag_state: Literal["ABSENT", "OFF", "ON"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateResponse:
        """
        Specify an account-level flag state for a specific HubSpot account.

        Args:
          flag_state: The state that the given flag should be in for this portal

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._put(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/{portal_id}",
                app_id=app_id,
                flag_name=flag_name,
                portal_id=portal_id,
            ),
            body=await async_maybe_transform(
                {"flag_state": flag_state}, feature_flag_update_params.FeatureFlagUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateResponse,
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
    ) -> PortalFlagStateResponse:
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
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/{portal_id}",
                app_id=app_id,
                flag_name=flag_name,
                portal_id=portal_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateResponse,
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
    ) -> PortalFlagStateResponse:
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
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals/{portal_id}",
                app_id=app_id,
                flag_name=flag_name,
                portal_id=portal_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalFlagStateResponse,
        )

    async def list_all(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagsForAppResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/feature-flags/2026-03/{app_id}/flags/all", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagsForAppResponse,
        )

    async def list_portals(
        self,
        flag_name: str,
        *,
        app_id: int,
        limit: int | Omit = omit,
        start_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalFlagStateBatchResponse:
        """
        Retrieve a list of HubSpot accounts with an account-level flag setting for the
        specified app. No request body is included.

        Args:
          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._get(
            path_template(
                "/feature-flags/2026-03/{app_id}/flags/{flag_name}/portals", app_id=app_id, flag_name=flag_name
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "start_portal_id": start_portal_id,
                    },
                    feature_flag_list_portals_params.FeatureFlagListPortalsParams,
                ),
            ),
            cast_to=PortalFlagStateBatchResponse,
        )


class FeatureFlagsResourceWithRawResponse:
    def __init__(self, feature_flags: FeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

        self.update = to_raw_response_wrapper(
            feature_flags.update,
        )
        self.delete = to_raw_response_wrapper(
            feature_flags.delete,
        )
        self.get = to_raw_response_wrapper(
            feature_flags.get,
        )
        self.list_all = to_raw_response_wrapper(
            feature_flags.list_all,
        )
        self.list_portals = to_raw_response_wrapper(
            feature_flags.list_portals,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._feature_flags.batch)


class AsyncFeatureFlagsResourceWithRawResponse:
    def __init__(self, feature_flags: AsyncFeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

        self.update = async_to_raw_response_wrapper(
            feature_flags.update,
        )
        self.delete = async_to_raw_response_wrapper(
            feature_flags.delete,
        )
        self.get = async_to_raw_response_wrapper(
            feature_flags.get,
        )
        self.list_all = async_to_raw_response_wrapper(
            feature_flags.list_all,
        )
        self.list_portals = async_to_raw_response_wrapper(
            feature_flags.list_portals,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._feature_flags.batch)


class FeatureFlagsResourceWithStreamingResponse:
    def __init__(self, feature_flags: FeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

        self.update = to_streamed_response_wrapper(
            feature_flags.update,
        )
        self.delete = to_streamed_response_wrapper(
            feature_flags.delete,
        )
        self.get = to_streamed_response_wrapper(
            feature_flags.get,
        )
        self.list_all = to_streamed_response_wrapper(
            feature_flags.list_all,
        )
        self.list_portals = to_streamed_response_wrapper(
            feature_flags.list_portals,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._feature_flags.batch)


class AsyncFeatureFlagsResourceWithStreamingResponse:
    def __init__(self, feature_flags: AsyncFeatureFlagsResource) -> None:
        self._feature_flags = feature_flags

        self.update = async_to_streamed_response_wrapper(
            feature_flags.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            feature_flags.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            feature_flags.get,
        )
        self.list_all = async_to_streamed_response_wrapper(
            feature_flags.list_all,
        )
        self.list_portals = async_to_streamed_response_wrapper(
            feature_flags.list_portals,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._feature_flags.batch)
