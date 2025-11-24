# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.conversations import actor_get_params, actor_batch_read_params
from ...types.conversations.public_actor import PublicActor
from ...types.conversations.batch_response_public_actor import BatchResponsePublicActor

__all__ = ["ActorsResource", "AsyncActorsResource"]


class ActorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ActorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ActorsResourceWithStreamingResponse(self)

    def batch_read(
        self,
        *,
        inputs: SequenceNotStr[str],
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicActor:
        """
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conversations/v3/conversations/actors/batch/read",
            body=maybe_transform({"inputs": inputs}, actor_batch_read_params.ActorBatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"property": property}, actor_batch_read_params.ActorBatchReadParams),
            ),
            cast_to=BatchResponsePublicActor,
        )

    def get(
        self,
        actor_id: str,
        *,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActor:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not actor_id:
            raise ValueError(f"Expected a non-empty value for `actor_id` but received {actor_id!r}")
        return cast(
            PublicActor,
            self._get(
                f"/conversations/v3/conversations/actors/{actor_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"property": property}, actor_get_params.ActorGetParams),
                ),
                cast_to=cast(Any, PublicActor),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncActorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncActorsResourceWithStreamingResponse(self)

    async def batch_read(
        self,
        *,
        inputs: SequenceNotStr[str],
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicActor:
        """
        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conversations/v3/conversations/actors/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, actor_batch_read_params.ActorBatchReadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"property": property}, actor_batch_read_params.ActorBatchReadParams),
            ),
            cast_to=BatchResponsePublicActor,
        )

    async def get(
        self,
        actor_id: str,
        *,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActor:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not actor_id:
            raise ValueError(f"Expected a non-empty value for `actor_id` but received {actor_id!r}")
        return cast(
            PublicActor,
            await self._get(
                f"/conversations/v3/conversations/actors/{actor_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"property": property}, actor_get_params.ActorGetParams),
                ),
                cast_to=cast(Any, PublicActor),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ActorsResourceWithRawResponse:
    def __init__(self, actors: ActorsResource) -> None:
        self._actors = actors

        self.batch_read = to_raw_response_wrapper(
            actors.batch_read,
        )
        self.get = to_raw_response_wrapper(
            actors.get,
        )


class AsyncActorsResourceWithRawResponse:
    def __init__(self, actors: AsyncActorsResource) -> None:
        self._actors = actors

        self.batch_read = async_to_raw_response_wrapper(
            actors.batch_read,
        )
        self.get = async_to_raw_response_wrapper(
            actors.get,
        )


class ActorsResourceWithStreamingResponse:
    def __init__(self, actors: ActorsResource) -> None:
        self._actors = actors

        self.batch_read = to_streamed_response_wrapper(
            actors.batch_read,
        )
        self.get = to_streamed_response_wrapper(
            actors.get,
        )


class AsyncActorsResourceWithStreamingResponse:
    def __init__(self, actors: AsyncActorsResource) -> None:
        self._actors = actors

        self.batch_read = async_to_streamed_response_wrapper(
            actors.batch_read,
        )
        self.get = async_to_streamed_response_wrapper(
            actors.get,
        )
