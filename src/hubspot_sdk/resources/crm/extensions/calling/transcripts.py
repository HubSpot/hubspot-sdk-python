# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.crm.extensions.calling import transcript_create_params, transcript_create_inbound_call_params
from .....types.crm.extensions.calling.transcript_response import TranscriptResponse
from .....types.crm.extensions.formatted_phone_number_param import FormattedPhoneNumberParam
from .....types.crm.extensions.calling.transcript_create_response import TranscriptCreateResponse
from .....types.crm.extensions.completed_third_party_call_response import CompletedThirdPartyCallResponse
from .....types.crm.extensions.calling.transcript_create_utterance_param import TranscriptCreateUtteranceParam

__all__ = ["TranscriptsResource", "AsyncTranscriptsResource"]


class TranscriptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranscriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TranscriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return TranscriptsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        engagement_id: int,
        transcript_create_utterances: Iterable[TranscriptCreateUtteranceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/extensions/calling/2026-03/transcripts",
            body=maybe_transform(
                {
                    "engagement_id": engagement_id,
                    "transcript_create_utterances": transcript_create_utterances,
                },
                transcript_create_params.TranscriptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranscriptCreateResponse,
        )

    def delete(
        self,
        transcript_id: str,
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
        if not transcript_id:
            raise ValueError(f"Expected a non-empty value for `transcript_id` but received {transcript_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/extensions/calling/2026-03/transcripts/{transcript_id}", transcript_id=transcript_id),
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
                transcript_create_inbound_call_params.TranscriptCreateInboundCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletedThirdPartyCallResponse,
        )

    def get(
        self,
        transcript_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcript_id:
            raise ValueError(f"Expected a non-empty value for `transcript_id` but received {transcript_id!r}")
        return self._get(
            path_template("/crm/extensions/calling/2026-03/transcripts/{transcript_id}", transcript_id=transcript_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranscriptResponse,
        )


class AsyncTranscriptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranscriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranscriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTranscriptsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        engagement_id: int,
        transcript_create_utterances: Iterable[TranscriptCreateUtteranceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/extensions/calling/2026-03/transcripts",
            body=await async_maybe_transform(
                {
                    "engagement_id": engagement_id,
                    "transcript_create_utterances": transcript_create_utterances,
                },
                transcript_create_params.TranscriptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranscriptCreateResponse,
        )

    async def delete(
        self,
        transcript_id: str,
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
        if not transcript_id:
            raise ValueError(f"Expected a non-empty value for `transcript_id` but received {transcript_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/extensions/calling/2026-03/transcripts/{transcript_id}", transcript_id=transcript_id),
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
                transcript_create_inbound_call_params.TranscriptCreateInboundCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletedThirdPartyCallResponse,
        )

    async def get(
        self,
        transcript_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcript_id:
            raise ValueError(f"Expected a non-empty value for `transcript_id` but received {transcript_id!r}")
        return await self._get(
            path_template("/crm/extensions/calling/2026-03/transcripts/{transcript_id}", transcript_id=transcript_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranscriptResponse,
        )


class TranscriptsResourceWithRawResponse:
    def __init__(self, transcripts: TranscriptsResource) -> None:
        self._transcripts = transcripts

        self.create = to_raw_response_wrapper(
            transcripts.create,
        )
        self.delete = to_raw_response_wrapper(
            transcripts.delete,
        )
        self.create_inbound_call = to_raw_response_wrapper(
            transcripts.create_inbound_call,
        )
        self.get = to_raw_response_wrapper(
            transcripts.get,
        )


class AsyncTranscriptsResourceWithRawResponse:
    def __init__(self, transcripts: AsyncTranscriptsResource) -> None:
        self._transcripts = transcripts

        self.create = async_to_raw_response_wrapper(
            transcripts.create,
        )
        self.delete = async_to_raw_response_wrapper(
            transcripts.delete,
        )
        self.create_inbound_call = async_to_raw_response_wrapper(
            transcripts.create_inbound_call,
        )
        self.get = async_to_raw_response_wrapper(
            transcripts.get,
        )


class TranscriptsResourceWithStreamingResponse:
    def __init__(self, transcripts: TranscriptsResource) -> None:
        self._transcripts = transcripts

        self.create = to_streamed_response_wrapper(
            transcripts.create,
        )
        self.delete = to_streamed_response_wrapper(
            transcripts.delete,
        )
        self.create_inbound_call = to_streamed_response_wrapper(
            transcripts.create_inbound_call,
        )
        self.get = to_streamed_response_wrapper(
            transcripts.get,
        )


class AsyncTranscriptsResourceWithStreamingResponse:
    def __init__(self, transcripts: AsyncTranscriptsResource) -> None:
        self._transcripts = transcripts

        self.create = async_to_streamed_response_wrapper(
            transcripts.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            transcripts.delete,
        )
        self.create_inbound_call = async_to_streamed_response_wrapper(
            transcripts.create_inbound_call,
        )
        self.get = async_to_streamed_response_wrapper(
            transcripts.get,
        )
