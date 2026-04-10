# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

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
from ....types.automation.actions import callback_complete_params, callback_complete_batch_params
from ....types.automation.callback_completion_batch_request_param import CallbackCompletionBatchRequestParam

__all__ = ["CallbacksResource", "AsyncCallbacksResource"]


class CallbacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallbacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CallbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallbacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return CallbacksResourceWithStreamingResponse(self)

    def complete(
        self,
        callback_id: str,
        *,
        output_fields: Dict[str, str],
        typed_outputs: object,
        failure_reason_type: str | Omit = omit,
        request_context: callback_complete_params.RequestContext | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a specific blocked action execution by ID.

        Args:
          output_fields: Contains the output fields associated with the callback, with each field
              represented as a key-value pair.

          typed_outputs: Holds the typed outputs related to the callback, structured as an object.

          failure_reason_type: Indicates the reason for the failure of a callback completion.

          request_context: Specifies the context in which the request is made, which can be one of several
              predefined contexts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not callback_id:
            raise ValueError(f"Expected a non-empty value for `callback_id` but received {callback_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/automation/actions/callbacks/2026-03/{callback_id}/complete", callback_id=callback_id),
            body=maybe_transform(
                {
                    "output_fields": output_fields,
                    "typed_outputs": typed_outputs,
                    "failure_reason_type": failure_reason_type,
                    "request_context": request_context,
                },
                callback_complete_params.CallbackCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def complete_batch(
        self,
        *,
        inputs: Iterable[CallbackCompletionBatchRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a batch of blocked action executions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/automation/actions/callbacks/2026-03/complete",
            body=maybe_transform({"inputs": inputs}, callback_complete_batch_params.CallbackCompleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCallbacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallbacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallbacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCallbacksResourceWithStreamingResponse(self)

    async def complete(
        self,
        callback_id: str,
        *,
        output_fields: Dict[str, str],
        typed_outputs: object,
        failure_reason_type: str | Omit = omit,
        request_context: callback_complete_params.RequestContext | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a specific blocked action execution by ID.

        Args:
          output_fields: Contains the output fields associated with the callback, with each field
              represented as a key-value pair.

          typed_outputs: Holds the typed outputs related to the callback, structured as an object.

          failure_reason_type: Indicates the reason for the failure of a callback completion.

          request_context: Specifies the context in which the request is made, which can be one of several
              predefined contexts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not callback_id:
            raise ValueError(f"Expected a non-empty value for `callback_id` but received {callback_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/automation/actions/callbacks/2026-03/{callback_id}/complete", callback_id=callback_id),
            body=await async_maybe_transform(
                {
                    "output_fields": output_fields,
                    "typed_outputs": typed_outputs,
                    "failure_reason_type": failure_reason_type,
                    "request_context": request_context,
                },
                callback_complete_params.CallbackCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def complete_batch(
        self,
        *,
        inputs: Iterable[CallbackCompletionBatchRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a batch of blocked action executions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/automation/actions/callbacks/2026-03/complete",
            body=await async_maybe_transform(
                {"inputs": inputs}, callback_complete_batch_params.CallbackCompleteBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CallbacksResourceWithRawResponse:
    def __init__(self, callbacks: CallbacksResource) -> None:
        self._callbacks = callbacks

        self.complete = to_raw_response_wrapper(
            callbacks.complete,
        )
        self.complete_batch = to_raw_response_wrapper(
            callbacks.complete_batch,
        )


class AsyncCallbacksResourceWithRawResponse:
    def __init__(self, callbacks: AsyncCallbacksResource) -> None:
        self._callbacks = callbacks

        self.complete = async_to_raw_response_wrapper(
            callbacks.complete,
        )
        self.complete_batch = async_to_raw_response_wrapper(
            callbacks.complete_batch,
        )


class CallbacksResourceWithStreamingResponse:
    def __init__(self, callbacks: CallbacksResource) -> None:
        self._callbacks = callbacks

        self.complete = to_streamed_response_wrapper(
            callbacks.complete,
        )
        self.complete_batch = to_streamed_response_wrapper(
            callbacks.complete_batch,
        )


class AsyncCallbacksResourceWithStreamingResponse:
    def __init__(self, callbacks: AsyncCallbacksResource) -> None:
        self._callbacks = callbacks

        self.complete = async_to_streamed_response_wrapper(
            callbacks.complete,
        )
        self.complete_batch = async_to_streamed_response_wrapper(
            callbacks.complete_batch,
        )
