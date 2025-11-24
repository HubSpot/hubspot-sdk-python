# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.crm.feature_flags import app_update_params, app_list_portals_params
from ....types.crm.flag_response import FlagResponse
from ....types.crm.portal_flag_state_batch_response import PortalFlagStateBatchResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def update(
        self,
        flag_name: str,
        *,
        app_id: int,
        default_state: Literal["ABSENT", "OFF", "ON"],
        override_state: Literal["ABSENT", "OFF", "ON"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagResponse:
        """Set a feature flag for an app.

        For example, update the `hs-hide-crm-cards`
        flag's `defaultState` to `ON` to hide classic CRM cards from new installs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._put(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}",
            body=maybe_transform(
                {
                    "default_state": default_state,
                    "override_state": override_state,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagResponse,
        )

    def delete(
        self,
        flag_name: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagResponse:
        """Delete a feature flag in an app.

        For example, delete the `hs-release-app-cards`
        flag after all accounts have been migrated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._delete(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagResponse,
        )

    def get(
        self,
        flag_name: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagResponse:
        """Retrieve the current status of the app's feature flags.

        No request body is
        included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._get(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagResponse,
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
          limit: The maximum number of results to return in a single request.

          start_portal_id: The initial account ID for listing, enabling pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return self._get(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals",
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
                    app_list_portals_params.AppListPortalsParams,
                ),
            ),
            cast_to=PortalFlagStateBatchResponse,
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def update(
        self,
        flag_name: str,
        *,
        app_id: int,
        default_state: Literal["ABSENT", "OFF", "ON"],
        override_state: Literal["ABSENT", "OFF", "ON"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagResponse:
        """Set a feature flag for an app.

        For example, update the `hs-hide-crm-cards`
        flag's `defaultState` to `ON` to hide classic CRM cards from new installs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._put(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}",
            body=await async_maybe_transform(
                {
                    "default_state": default_state,
                    "override_state": override_state,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagResponse,
        )

    async def delete(
        self,
        flag_name: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagResponse:
        """Delete a feature flag in an app.

        For example, delete the `hs-release-app-cards`
        flag after all accounts have been migrated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._delete(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagResponse,
        )

    async def get(
        self,
        flag_name: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlagResponse:
        """Retrieve the current status of the app's feature flags.

        No request body is
        included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._get(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlagResponse,
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
          limit: The maximum number of results to return in a single request.

          start_portal_id: The initial account ID for listing, enabling pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flag_name:
            raise ValueError(f"Expected a non-empty value for `flag_name` but received {flag_name!r}")
        return await self._get(
            f"/feature-flags/v3/{app_id}/flags/{flag_name}/portals",
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
                    app_list_portals_params.AppListPortalsParams,
                ),
            ),
            cast_to=PortalFlagStateBatchResponse,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.update = to_raw_response_wrapper(
            apps.update,
        )
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.get = to_raw_response_wrapper(
            apps.get,
        )
        self.list_portals = to_raw_response_wrapper(
            apps.list_portals,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.update = async_to_raw_response_wrapper(
            apps.update,
        )
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.get = async_to_raw_response_wrapper(
            apps.get,
        )
        self.list_portals = async_to_raw_response_wrapper(
            apps.list_portals,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.update = to_streamed_response_wrapper(
            apps.update,
        )
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = to_streamed_response_wrapper(
            apps.get,
        )
        self.list_portals = to_streamed_response_wrapper(
            apps.list_portals,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.update = async_to_streamed_response_wrapper(
            apps.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            apps.get,
        )
        self.list_portals = async_to_streamed_response_wrapper(
            apps.list_portals,
        )
