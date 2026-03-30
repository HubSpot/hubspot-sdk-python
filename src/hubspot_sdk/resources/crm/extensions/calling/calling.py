# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .transcripts import (
    TranscriptsResource,
    AsyncTranscriptsResource,
    TranscriptsResourceWithRawResponse,
    AsyncTranscriptsResourceWithRawResponse,
    TranscriptsResourceWithStreamingResponse,
    AsyncTranscriptsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.crm.extensions import (
    calling_create_params,
    calling_update_params,
    calling_mark_ready_params,
    calling_create_inbound_call_params,
)
from .....types.crm.extensions.recording_settings_response import RecordingSettingsResponse
from .....types.crm.extensions.formatted_phone_number_param import FormattedPhoneNumberParam
from .....types.crm.extensions.completed_third_party_call_response import CompletedThirdPartyCallResponse

__all__ = ["CallingResource", "AsyncCallingResource"]


class CallingResource(SyncAPIResource):
    @cached_property
    def transcripts(self) -> TranscriptsResource:
        return TranscriptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CallingResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Create new recording settings for a specific app using the provided app ID.

        Args:
          url_to_retrieve_authed_recording: The URL used to access authenticated call recordings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/recording", app_id=app_id),
            body=maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_create_params.CallingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    def update(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Update the recording settings for a specific app using the provided app ID.

        Args:
          url_to_retrieve_authed_recording: The URL used to access authenticated call recordings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/recording", app_id=app_id),
            body=maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_update_params.CallingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
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
        Delete the channel connection settings associated with the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/channel-connection", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_inbound_call(
        self,
        *,
        create_engagement: bool,
        engagement_properties: Dict[str, str],
        external_call_id: str,
        final_call_status: Literal[
            "BUSY",
            "CALLING_CRM_USER",
            "CANCELED",
            "COMPLETED",
            "CONNECTING",
            "FAILED",
            "HOLD",
            "IN_PROGRESS",
            "MISSED",
            "NO_ANSWER",
            "QUEUED",
            "RINGING",
            "UNKNOWN",
        ],
        from_number: FormattedPhoneNumberParam,
        potential_recipient_user_ids: Iterable[int],
        to_number: FormattedPhoneNumberParam,
        call_started_timestamp: Union[str, datetime] | Omit = omit,
        duration_seconds: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletedThirdPartyCallResponse:
        """
        Args:
          create_engagement: Indicates whether an engagement should be created for the call.

          engagement_properties: Contains additional properties related to the engagement.

          external_call_id: The unique identifier for the call from an external system.

          final_call_status: The final status of the call, with accepted values including: BUSY,
              CALLING_CRM_USER, CANCELED, COMPLETED, CONNECTING, FAILED, HOLD, IN_PROGRESS,
              MISSED, NO_ANSWER, QUEUED, RINGING, UNKNOWN.

          call_started_timestamp: The timestamp indicating when the call started, formatted as a date-time string.

          duration_seconds: The duration of the call in seconds.

          user_id: The ID of the user associated with the call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/extensions/calling/2026-03/inbound-call",
            body=maybe_transform(
                {
                    "create_engagement": create_engagement,
                    "engagement_properties": engagement_properties,
                    "external_call_id": external_call_id,
                    "final_call_status": final_call_status,
                    "from_number": from_number,
                    "potential_recipient_user_ids": potential_recipient_user_ids,
                    "to_number": to_number,
                    "call_started_timestamp": call_started_timestamp,
                    "duration_seconds": duration_seconds,
                    "user_id": user_id,
                },
                calling_create_inbound_call_params.CallingCreateInboundCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletedThirdPartyCallResponse,
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
    ) -> RecordingSettingsResponse:
        """
        Retrieve the current recording settings for a specific app using the provided
        app ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/recording", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    def mark_ready(
        self,
        *,
        engagement_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint is used to mark a call recording as ready.

        It requires the
        engagementId to identify the specific recording.

        Args:
          engagement_id: The unique identifier for the engagement associated with the call recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/crm/extensions/calling/2026-03/recordings/ready",
            body=maybe_transform({"engagement_id": engagement_id}, calling_mark_ready_params.CallingMarkReadyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCallingResource(AsyncAPIResource):
    @cached_property
    def transcripts(self) -> AsyncTranscriptsResource:
        return AsyncTranscriptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCallingResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Create new recording settings for a specific app using the provided app ID.

        Args:
          url_to_retrieve_authed_recording: The URL used to access authenticated call recordings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/recording", app_id=app_id),
            body=await async_maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_create_params.CallingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    async def update(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Update the recording settings for a specific app using the provided app ID.

        Args:
          url_to_retrieve_authed_recording: The URL used to access authenticated call recordings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/recording", app_id=app_id),
            body=await async_maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_update_params.CallingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
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
        Delete the channel connection settings associated with the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/channel-connection", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_inbound_call(
        self,
        *,
        create_engagement: bool,
        engagement_properties: Dict[str, str],
        external_call_id: str,
        final_call_status: Literal[
            "BUSY",
            "CALLING_CRM_USER",
            "CANCELED",
            "COMPLETED",
            "CONNECTING",
            "FAILED",
            "HOLD",
            "IN_PROGRESS",
            "MISSED",
            "NO_ANSWER",
            "QUEUED",
            "RINGING",
            "UNKNOWN",
        ],
        from_number: FormattedPhoneNumberParam,
        potential_recipient_user_ids: Iterable[int],
        to_number: FormattedPhoneNumberParam,
        call_started_timestamp: Union[str, datetime] | Omit = omit,
        duration_seconds: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletedThirdPartyCallResponse:
        """
        Args:
          create_engagement: Indicates whether an engagement should be created for the call.

          engagement_properties: Contains additional properties related to the engagement.

          external_call_id: The unique identifier for the call from an external system.

          final_call_status: The final status of the call, with accepted values including: BUSY,
              CALLING_CRM_USER, CANCELED, COMPLETED, CONNECTING, FAILED, HOLD, IN_PROGRESS,
              MISSED, NO_ANSWER, QUEUED, RINGING, UNKNOWN.

          call_started_timestamp: The timestamp indicating when the call started, formatted as a date-time string.

          duration_seconds: The duration of the call in seconds.

          user_id: The ID of the user associated with the call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/extensions/calling/2026-03/inbound-call",
            body=await async_maybe_transform(
                {
                    "create_engagement": create_engagement,
                    "engagement_properties": engagement_properties,
                    "external_call_id": external_call_id,
                    "final_call_status": final_call_status,
                    "from_number": from_number,
                    "potential_recipient_user_ids": potential_recipient_user_ids,
                    "to_number": to_number,
                    "call_started_timestamp": call_started_timestamp,
                    "duration_seconds": duration_seconds,
                    "user_id": user_id,
                },
                calling_create_inbound_call_params.CallingCreateInboundCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletedThirdPartyCallResponse,
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
    ) -> RecordingSettingsResponse:
        """
        Retrieve the current recording settings for a specific app using the provided
        app ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/crm/extensions/calling/2026-03/{app_id}/settings/recording", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    async def mark_ready(
        self,
        *,
        engagement_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint is used to mark a call recording as ready.

        It requires the
        engagementId to identify the specific recording.

        Args:
          engagement_id: The unique identifier for the engagement associated with the call recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/crm/extensions/calling/2026-03/recordings/ready",
            body=await async_maybe_transform(
                {"engagement_id": engagement_id}, calling_mark_ready_params.CallingMarkReadyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CallingResourceWithRawResponse:
    def __init__(self, calling: CallingResource) -> None:
        self._calling = calling

        self.create = to_raw_response_wrapper(
            calling.create,
        )
        self.update = to_raw_response_wrapper(
            calling.update,
        )
        self.delete = to_raw_response_wrapper(
            calling.delete,
        )
        self.create_inbound_call = to_raw_response_wrapper(
            calling.create_inbound_call,
        )
        self.get = to_raw_response_wrapper(
            calling.get,
        )
        self.mark_ready = to_raw_response_wrapper(
            calling.mark_ready,
        )

    @cached_property
    def transcripts(self) -> TranscriptsResourceWithRawResponse:
        return TranscriptsResourceWithRawResponse(self._calling.transcripts)


class AsyncCallingResourceWithRawResponse:
    def __init__(self, calling: AsyncCallingResource) -> None:
        self._calling = calling

        self.create = async_to_raw_response_wrapper(
            calling.create,
        )
        self.update = async_to_raw_response_wrapper(
            calling.update,
        )
        self.delete = async_to_raw_response_wrapper(
            calling.delete,
        )
        self.create_inbound_call = async_to_raw_response_wrapper(
            calling.create_inbound_call,
        )
        self.get = async_to_raw_response_wrapper(
            calling.get,
        )
        self.mark_ready = async_to_raw_response_wrapper(
            calling.mark_ready,
        )

    @cached_property
    def transcripts(self) -> AsyncTranscriptsResourceWithRawResponse:
        return AsyncTranscriptsResourceWithRawResponse(self._calling.transcripts)


class CallingResourceWithStreamingResponse:
    def __init__(self, calling: CallingResource) -> None:
        self._calling = calling

        self.create = to_streamed_response_wrapper(
            calling.create,
        )
        self.update = to_streamed_response_wrapper(
            calling.update,
        )
        self.delete = to_streamed_response_wrapper(
            calling.delete,
        )
        self.create_inbound_call = to_streamed_response_wrapper(
            calling.create_inbound_call,
        )
        self.get = to_streamed_response_wrapper(
            calling.get,
        )
        self.mark_ready = to_streamed_response_wrapper(
            calling.mark_ready,
        )

    @cached_property
    def transcripts(self) -> TranscriptsResourceWithStreamingResponse:
        return TranscriptsResourceWithStreamingResponse(self._calling.transcripts)


class AsyncCallingResourceWithStreamingResponse:
    def __init__(self, calling: AsyncCallingResource) -> None:
        self._calling = calling

        self.create = async_to_streamed_response_wrapper(
            calling.create,
        )
        self.update = async_to_streamed_response_wrapper(
            calling.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            calling.delete,
        )
        self.create_inbound_call = async_to_streamed_response_wrapper(
            calling.create_inbound_call,
        )
        self.get = async_to_streamed_response_wrapper(
            calling.get,
        )
        self.mark_ready = async_to_streamed_response_wrapper(
            calling.mark_ready,
        )

    @cached_property
    def transcripts(self) -> AsyncTranscriptsResourceWithStreamingResponse:
        return AsyncTranscriptsResourceWithStreamingResponse(self._calling.transcripts)
