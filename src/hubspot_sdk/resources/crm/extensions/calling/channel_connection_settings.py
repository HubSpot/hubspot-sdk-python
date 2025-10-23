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
from .....types.crm.extensions.calling import (
    channel_connection_setting_create_params,
    channel_connection_setting_update_params,
)
from .....types.crm.extensions.channel_connection_settings_response import ChannelConnectionSettingsResponse

__all__ = ["ChannelConnectionSettingsResource", "AsyncChannelConnectionSettingsResource"]


class ChannelConnectionSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelConnectionSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChannelConnectionSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelConnectionSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ChannelConnectionSettingsResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        is_ready: bool,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Configure
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#create-channel-connection-settings)
        for the app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                channel_connection_setting_create_params.ChannelConnectionSettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    def update(
        self,
        app_id: int,
        *,
        is_ready: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Update existing
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#manage-the-webhook-settings-for-channel-connection)
        for your app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                channel_connection_setting_update_params.ChannelConnectionSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
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
        Delete the
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#delete-existing-channel-connection-settings)
        for the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
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
    ) -> ChannelConnectionSettingsResponse:
        """
        Retrieve the settings related to the app's
        [channel connection](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#fetch-existing-channel-connection-settings).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )


class AsyncChannelConnectionSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelConnectionSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelConnectionSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelConnectionSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncChannelConnectionSettingsResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        is_ready: bool,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Configure
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#create-channel-connection-settings)
        for the app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=await async_maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                channel_connection_setting_create_params.ChannelConnectionSettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    async def update(
        self,
        app_id: int,
        *,
        is_ready: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Update existing
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#manage-the-webhook-settings-for-channel-connection)
        for your app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=await async_maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                channel_connection_setting_update_params.ChannelConnectionSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
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
        Delete the
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#delete-existing-channel-connection-settings)
        for the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
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
    ) -> ChannelConnectionSettingsResponse:
        """
        Retrieve the settings related to the app's
        [channel connection](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#fetch-existing-channel-connection-settings).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )


class ChannelConnectionSettingsResourceWithRawResponse:
    def __init__(self, channel_connection_settings: ChannelConnectionSettingsResource) -> None:
        self._channel_connection_settings = channel_connection_settings

        self.create = to_raw_response_wrapper(
            channel_connection_settings.create,
        )
        self.update = to_raw_response_wrapper(
            channel_connection_settings.update,
        )
        self.delete = to_raw_response_wrapper(
            channel_connection_settings.delete,
        )
        self.get = to_raw_response_wrapper(
            channel_connection_settings.get,
        )


class AsyncChannelConnectionSettingsResourceWithRawResponse:
    def __init__(self, channel_connection_settings: AsyncChannelConnectionSettingsResource) -> None:
        self._channel_connection_settings = channel_connection_settings

        self.create = async_to_raw_response_wrapper(
            channel_connection_settings.create,
        )
        self.update = async_to_raw_response_wrapper(
            channel_connection_settings.update,
        )
        self.delete = async_to_raw_response_wrapper(
            channel_connection_settings.delete,
        )
        self.get = async_to_raw_response_wrapper(
            channel_connection_settings.get,
        )


class ChannelConnectionSettingsResourceWithStreamingResponse:
    def __init__(self, channel_connection_settings: ChannelConnectionSettingsResource) -> None:
        self._channel_connection_settings = channel_connection_settings

        self.create = to_streamed_response_wrapper(
            channel_connection_settings.create,
        )
        self.update = to_streamed_response_wrapper(
            channel_connection_settings.update,
        )
        self.delete = to_streamed_response_wrapper(
            channel_connection_settings.delete,
        )
        self.get = to_streamed_response_wrapper(
            channel_connection_settings.get,
        )


class AsyncChannelConnectionSettingsResourceWithStreamingResponse:
    def __init__(self, channel_connection_settings: AsyncChannelConnectionSettingsResource) -> None:
        self._channel_connection_settings = channel_connection_settings

        self.create = async_to_streamed_response_wrapper(
            channel_connection_settings.create,
        )
        self.update = async_to_streamed_response_wrapper(
            channel_connection_settings.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            channel_connection_settings.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            channel_connection_settings.get,
        )
