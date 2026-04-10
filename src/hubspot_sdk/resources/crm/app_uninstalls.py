# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["AppUninstallsResource", "AsyncAppUninstallsResource"]


class AppUninstallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppUninstallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppUninstallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppUninstallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AppUninstallsResourceWithStreamingResponse(self)

    def uninstall(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Use this endpoint to uninstall your app from a customer's HubSpot account.

        If
        successful, this endpoint will return a 204 and the customer will receive an
        email notification that the developer has uninstall the app from their account.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/appinstalls/2026-03/external-install",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAppUninstallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppUninstallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppUninstallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppUninstallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAppUninstallsResourceWithStreamingResponse(self)

    async def uninstall(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Use this endpoint to uninstall your app from a customer's HubSpot account.

        If
        successful, this endpoint will return a 204 and the customer will receive an
        email notification that the developer has uninstall the app from their account.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/appinstalls/2026-03/external-install",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AppUninstallsResourceWithRawResponse:
    def __init__(self, app_uninstalls: AppUninstallsResource) -> None:
        self._app_uninstalls = app_uninstalls

        self.uninstall = to_raw_response_wrapper(
            app_uninstalls.uninstall,
        )


class AsyncAppUninstallsResourceWithRawResponse:
    def __init__(self, app_uninstalls: AsyncAppUninstallsResource) -> None:
        self._app_uninstalls = app_uninstalls

        self.uninstall = async_to_raw_response_wrapper(
            app_uninstalls.uninstall,
        )


class AppUninstallsResourceWithStreamingResponse:
    def __init__(self, app_uninstalls: AppUninstallsResource) -> None:
        self._app_uninstalls = app_uninstalls

        self.uninstall = to_streamed_response_wrapper(
            app_uninstalls.uninstall,
        )


class AsyncAppUninstallsResourceWithStreamingResponse:
    def __init__(self, app_uninstalls: AsyncAppUninstallsResource) -> None:
        self._app_uninstalls = app_uninstalls

        self.uninstall = async_to_streamed_response_wrapper(
            app_uninstalls.uninstall,
        )
