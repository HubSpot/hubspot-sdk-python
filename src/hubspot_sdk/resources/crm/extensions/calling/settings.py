# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.crm.extensions.calling import setting_create_params, setting_update_params
from .....types.webhooks.settings_response import SettingsResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        name: str,
        url: str,
        height: int | Omit = omit,
        is_ready: bool | Omit = omit,
        supports_custom_objects: bool | Omit = omit,
        supports_inbound_calling: bool | Omit = omit,
        uses_calling_window: bool | Omit = omit,
        uses_remote: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "height": height,
                    "is_ready": is_ready,
                    "supports_custom_objects": supports_custom_objects,
                    "supports_inbound_calling": supports_inbound_calling,
                    "uses_calling_window": uses_calling_window,
                    "uses_remote": uses_remote,
                    "width": width,
                },
                setting_create_params.SettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    def update(
        self,
        app_id: int,
        *,
        height: int | Omit = omit,
        is_ready: bool | Omit = omit,
        name: str | Omit = omit,
        supports_custom_objects: bool | Omit = omit,
        supports_inbound_calling: bool | Omit = omit,
        url: str | Omit = omit,
        uses_calling_window: bool | Omit = omit,
        uses_remote: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            body=maybe_transform(
                {
                    "height": height,
                    "is_ready": is_ready,
                    "name": name,
                    "supports_custom_objects": supports_custom_objects,
                    "supports_inbound_calling": supports_inbound_calling,
                    "url": url,
                    "uses_calling_window": uses_calling_window,
                    "uses_remote": uses_remote,
                    "width": width,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    def delete(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        name: str,
        url: str,
        height: int | Omit = omit,
        is_ready: bool | Omit = omit,
        supports_custom_objects: bool | Omit = omit,
        supports_inbound_calling: bool | Omit = omit,
        uses_calling_window: bool | Omit = omit,
        uses_remote: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "height": height,
                    "is_ready": is_ready,
                    "supports_custom_objects": supports_custom_objects,
                    "supports_inbound_calling": supports_inbound_calling,
                    "uses_calling_window": uses_calling_window,
                    "uses_remote": uses_remote,
                    "width": width,
                },
                setting_create_params.SettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    async def update(
        self,
        app_id: int,
        *,
        height: int | Omit = omit,
        is_ready: bool | Omit = omit,
        name: str | Omit = omit,
        supports_custom_objects: bool | Omit = omit,
        supports_inbound_calling: bool | Omit = omit,
        url: str | Omit = omit,
        uses_calling_window: bool | Omit = omit,
        uses_remote: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            body=await async_maybe_transform(
                {
                    "height": height,
                    "is_ready": is_ready,
                    "name": name,
                    "supports_custom_objects": supports_custom_objects,
                    "supports_inbound_calling": supports_inbound_calling,
                    "url": url,
                    "uses_calling_window": uses_calling_window,
                    "uses_remote": uses_remote,
                    "width": width,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    async def delete(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.create = to_raw_response_wrapper(
            settings.create,
        )
        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.delete = to_raw_response_wrapper(
            settings.delete,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.create = async_to_raw_response_wrapper(
            settings.create,
        )
        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.delete = async_to_raw_response_wrapper(
            settings.delete,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.create = to_streamed_response_wrapper(
            settings.create,
        )
        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = to_streamed_response_wrapper(
            settings.delete,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.create = async_to_streamed_response_wrapper(
            settings.create,
        )
        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            settings.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
