# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.crm import timeline_create_event_params, timeline_create_project_type_params
from ...._base_client import make_request_options
from ....types.crm.timeline_event_i_frame_param import TimelineEventIFrameParam
from ....types.crm.app_event_resolution_response import AppEventResolutionResponse

__all__ = ["TimelineResource", "AsyncTimelineResource"]


class TimelineResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> TimelineResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TimelineResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimelineResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return TimelineResourceWithStreamingResponse(self)

    def create_event(
        self,
        *,
        id: str,
        event_type_name: str,
        properties: Dict[str, str],
        domain: str | Omit = omit,
        email: str | Omit = omit,
        extra_data: object | Omit = omit,
        object_id: str | Omit = omit,
        object_type_fully_qualified_name: str | Omit = omit,
        timeline_i_frame: TimelineEventIFrameParam | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        utk: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a single instance of event data to a specified event type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/integrators/timeline/2026-03/events",
            body=maybe_transform(
                {
                    "id": id,
                    "event_type_name": event_type_name,
                    "properties": properties,
                    "domain": domain,
                    "email": email,
                    "extra_data": extra_data,
                    "object_id": object_id,
                    "object_type_fully_qualified_name": object_type_fully_qualified_name,
                    "timeline_i_frame": timeline_i_frame,
                    "timestamp": timestamp,
                    "utk": utk,
                },
                timeline_create_event_params.TimelineCreateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_project_type(
        self,
        *,
        developer_symbol: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppEventResolutionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integrators/timeline/2026-03/types/projects",
            body=maybe_transform(
                {
                    "developer_symbol": developer_symbol,
                    "project_name": project_name,
                },
                timeline_create_project_type_params.TimelineCreateProjectTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppEventResolutionResponse,
        )


class AsyncTimelineResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTimelineResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimelineResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimelineResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTimelineResourceWithStreamingResponse(self)

    async def create_event(
        self,
        *,
        id: str,
        event_type_name: str,
        properties: Dict[str, str],
        domain: str | Omit = omit,
        email: str | Omit = omit,
        extra_data: object | Omit = omit,
        object_id: str | Omit = omit,
        object_type_fully_qualified_name: str | Omit = omit,
        timeline_i_frame: TimelineEventIFrameParam | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        utk: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a single instance of event data to a specified event type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/integrators/timeline/2026-03/events",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "event_type_name": event_type_name,
                    "properties": properties,
                    "domain": domain,
                    "email": email,
                    "extra_data": extra_data,
                    "object_id": object_id,
                    "object_type_fully_qualified_name": object_type_fully_qualified_name,
                    "timeline_i_frame": timeline_i_frame,
                    "timestamp": timestamp,
                    "utk": utk,
                },
                timeline_create_event_params.TimelineCreateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_project_type(
        self,
        *,
        developer_symbol: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppEventResolutionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integrators/timeline/2026-03/types/projects",
            body=await async_maybe_transform(
                {
                    "developer_symbol": developer_symbol,
                    "project_name": project_name,
                },
                timeline_create_project_type_params.TimelineCreateProjectTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppEventResolutionResponse,
        )


class TimelineResourceWithRawResponse:
    def __init__(self, timeline: TimelineResource) -> None:
        self._timeline = timeline

        self.create_event = to_raw_response_wrapper(
            timeline.create_event,
        )
        self.create_project_type = to_raw_response_wrapper(
            timeline.create_project_type,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._timeline.batch)


class AsyncTimelineResourceWithRawResponse:
    def __init__(self, timeline: AsyncTimelineResource) -> None:
        self._timeline = timeline

        self.create_event = async_to_raw_response_wrapper(
            timeline.create_event,
        )
        self.create_project_type = async_to_raw_response_wrapper(
            timeline.create_project_type,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._timeline.batch)


class TimelineResourceWithStreamingResponse:
    def __init__(self, timeline: TimelineResource) -> None:
        self._timeline = timeline

        self.create_event = to_streamed_response_wrapper(
            timeline.create_event,
        )
        self.create_project_type = to_streamed_response_wrapper(
            timeline.create_project_type,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._timeline.batch)


class AsyncTimelineResourceWithStreamingResponse:
    def __init__(self, timeline: AsyncTimelineResource) -> None:
        self._timeline = timeline

        self.create_event = async_to_streamed_response_wrapper(
            timeline.create_event,
        )
        self.create_project_type = async_to_streamed_response_wrapper(
            timeline.create_project_type,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._timeline.batch)
