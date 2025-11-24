# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.conversations import thread_get_params, thread_list_params, thread_update_params
from ...types.conversations.public_thread import PublicThread

__all__ = ["ThreadsResource", "AsyncThreadsResource"]


class ThreadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ThreadsResourceWithStreamingResponse(self)

    def update(
        self,
        thread_id: int,
        *,
        query_archived: bool | Omit = omit,
        body_archived: bool | Omit = omit,
        status: Literal["CLOSED", "OPEN"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicThread:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/conversations/v3/conversations/threads/{thread_id}",
            body=maybe_transform(
                {
                    "body_archived": body_archived,
                    "status": status,
                },
                thread_update_params.ThreadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query_archived": query_archived}, thread_update_params.ThreadUpdateParams),
            ),
            cast_to=PublicThread,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associated_contact_id: int | Omit = omit,
        association: List[Literal["TICKET"]] | Omit = omit,
        inbox_id: Iterable[int] | Omit = omit,
        latest_message_timestamp_after: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        thread_status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicThread]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/threads",
            page=SyncPage[PublicThread],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associated_contact_id": associated_contact_id,
                        "association": association,
                        "inbox_id": inbox_id,
                        "latest_message_timestamp_after": latest_message_timestamp_after,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "thread_status": thread_status,
                    },
                    thread_list_params.ThreadListParams,
                ),
            ),
            model=PublicThread,
        )

    def delete(
        self,
        thread_id: int,
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
            f"/conversations/v3/conversations/threads/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        thread_id: int,
        *,
        archived: bool | Omit = omit,
        association: List[Literal["TICKET"]] | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicThread:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/conversations/v3/conversations/threads/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "association": association,
                        "property": property,
                    },
                    thread_get_params.ThreadGetParams,
                ),
            ),
            cast_to=PublicThread,
        )


class AsyncThreadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncThreadsResourceWithStreamingResponse(self)

    async def update(
        self,
        thread_id: int,
        *,
        query_archived: bool | Omit = omit,
        body_archived: bool | Omit = omit,
        status: Literal["CLOSED", "OPEN"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicThread:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/conversations/v3/conversations/threads/{thread_id}",
            body=await async_maybe_transform(
                {
                    "body_archived": body_archived,
                    "status": status,
                },
                thread_update_params.ThreadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_archived": query_archived}, thread_update_params.ThreadUpdateParams
                ),
            ),
            cast_to=PublicThread,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associated_contact_id: int | Omit = omit,
        association: List[Literal["TICKET"]] | Omit = omit,
        inbox_id: Iterable[int] | Omit = omit,
        latest_message_timestamp_after: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        thread_status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicThread, AsyncPage[PublicThread]]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conversations/v3/conversations/threads",
            page=AsyncPage[PublicThread],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associated_contact_id": associated_contact_id,
                        "association": association,
                        "inbox_id": inbox_id,
                        "latest_message_timestamp_after": latest_message_timestamp_after,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "thread_status": thread_status,
                    },
                    thread_list_params.ThreadListParams,
                ),
            ),
            model=PublicThread,
        )

    async def delete(
        self,
        thread_id: int,
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
            f"/conversations/v3/conversations/threads/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        thread_id: int,
        *,
        archived: bool | Omit = omit,
        association: List[Literal["TICKET"]] | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicThread:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/conversations/v3/conversations/threads/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "association": association,
                        "property": property,
                    },
                    thread_get_params.ThreadGetParams,
                ),
            ),
            cast_to=PublicThread,
        )


class ThreadsResourceWithRawResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.update = to_raw_response_wrapper(
            threads.update,
        )
        self.list = to_raw_response_wrapper(
            threads.list,
        )
        self.delete = to_raw_response_wrapper(
            threads.delete,
        )
        self.get = to_raw_response_wrapper(
            threads.get,
        )


class AsyncThreadsResourceWithRawResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.update = async_to_raw_response_wrapper(
            threads.update,
        )
        self.list = async_to_raw_response_wrapper(
            threads.list,
        )
        self.delete = async_to_raw_response_wrapper(
            threads.delete,
        )
        self.get = async_to_raw_response_wrapper(
            threads.get,
        )


class ThreadsResourceWithStreamingResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.update = to_streamed_response_wrapper(
            threads.update,
        )
        self.list = to_streamed_response_wrapper(
            threads.list,
        )
        self.delete = to_streamed_response_wrapper(
            threads.delete,
        )
        self.get = to_streamed_response_wrapper(
            threads.get,
        )


class AsyncThreadsResourceWithStreamingResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.update = async_to_streamed_response_wrapper(
            threads.update,
        )
        self.list = async_to_streamed_response_wrapper(
            threads.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            threads.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            threads.get,
        )
