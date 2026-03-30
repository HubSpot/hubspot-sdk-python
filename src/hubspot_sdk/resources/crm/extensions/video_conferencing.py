# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.extensions import video_conferencing_update_params
from ....types.crm.extensions.external_settings import ExternalSettings

__all__ = ["VideoConferencingResource", "AsyncVideoConferencingResource"]


class VideoConferencingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoConferencingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VideoConferencingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoConferencingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return VideoConferencingResourceWithStreamingResponse(self)

    def update(
        self,
        app_id: int,
        *,
        create_meeting_url: str,
        delete_meeting_url: str | Omit = omit,
        fetch_accounts_uri: str | Omit = omit,
        update_meeting_url: str | Omit = omit,
        user_verify_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalSettings:
        """
        Create or update video conference extension settings for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            path_template("/crm/extensions/videoconferencing/2026-03/settings/{app_id}", app_id=app_id),
            body=maybe_transform(
                {
                    "create_meeting_url": create_meeting_url,
                    "delete_meeting_url": delete_meeting_url,
                    "fetch_accounts_uri": fetch_accounts_uri,
                    "update_meeting_url": update_meeting_url,
                    "user_verify_url": user_verify_url,
                },
                video_conferencing_update_params.VideoConferencingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalSettings,
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
        Delete video conference extension settings for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/extensions/videoconferencing/2026-03/settings/{app_id}", app_id=app_id),
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
    ) -> ExternalSettings:
        """
        Fetch video conference extension settings for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/crm/extensions/videoconferencing/2026-03/settings/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalSettings,
        )


class AsyncVideoConferencingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoConferencingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoConferencingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoConferencingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncVideoConferencingResourceWithStreamingResponse(self)

    async def update(
        self,
        app_id: int,
        *,
        create_meeting_url: str,
        delete_meeting_url: str | Omit = omit,
        fetch_accounts_uri: str | Omit = omit,
        update_meeting_url: str | Omit = omit,
        user_verify_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalSettings:
        """
        Create or update video conference extension settings for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            path_template("/crm/extensions/videoconferencing/2026-03/settings/{app_id}", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "create_meeting_url": create_meeting_url,
                    "delete_meeting_url": delete_meeting_url,
                    "fetch_accounts_uri": fetch_accounts_uri,
                    "update_meeting_url": update_meeting_url,
                    "user_verify_url": user_verify_url,
                },
                video_conferencing_update_params.VideoConferencingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalSettings,
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
        Delete video conference extension settings for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/extensions/videoconferencing/2026-03/settings/{app_id}", app_id=app_id),
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
    ) -> ExternalSettings:
        """
        Fetch video conference extension settings for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/crm/extensions/videoconferencing/2026-03/settings/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalSettings,
        )


class VideoConferencingResourceWithRawResponse:
    def __init__(self, video_conferencing: VideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

        self.update = to_raw_response_wrapper(
            video_conferencing.update,
        )
        self.delete = to_raw_response_wrapper(
            video_conferencing.delete,
        )
        self.get = to_raw_response_wrapper(
            video_conferencing.get,
        )


class AsyncVideoConferencingResourceWithRawResponse:
    def __init__(self, video_conferencing: AsyncVideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

        self.update = async_to_raw_response_wrapper(
            video_conferencing.update,
        )
        self.delete = async_to_raw_response_wrapper(
            video_conferencing.delete,
        )
        self.get = async_to_raw_response_wrapper(
            video_conferencing.get,
        )


class VideoConferencingResourceWithStreamingResponse:
    def __init__(self, video_conferencing: VideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

        self.update = to_streamed_response_wrapper(
            video_conferencing.update,
        )
        self.delete = to_streamed_response_wrapper(
            video_conferencing.delete,
        )
        self.get = to_streamed_response_wrapper(
            video_conferencing.get,
        )


class AsyncVideoConferencingResourceWithStreamingResponse:
    def __init__(self, video_conferencing: AsyncVideoConferencingResource) -> None:
        self._video_conferencing = video_conferencing

        self.update = async_to_streamed_response_wrapper(
            video_conferencing.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            video_conferencing.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            video_conferencing.get,
        )
