# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.marketing.marketing_events import (
    subscriber_state_record_by_id_params,
    subscriber_state_record_by_email_params,
)
from ....types.marketing.marketing_event_subscriber_param import MarketingEventSubscriberParam
from ....types.marketing.marketing_event_email_subscriber_param import MarketingEventEmailSubscriberParam

__all__ = ["SubscriberStateResource", "AsyncSubscriberStateResource"]


class SubscriberStateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriberStateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubscriberStateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriberStateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SubscriberStateResourceWithStreamingResponse(self)

    def record_by_email(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        external_account_id: str,
        inputs: Iterable[MarketingEventEmailSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Record a subscriber state between multiple HubSpot contacts and a marketing
        event, using contact email addresses. Note that the contact must already exist
        in HubSpot; a contact will not be created. The contactProperties field is used
        only when creating a new contact. These properties will not update existing
        contacts.

        Args:
          inputs: List of marketing event details to create or update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/{subscriber_state}/email-upsert",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=maybe_transform(
                {"inputs": inputs}, subscriber_state_record_by_email_params.SubscriberStateRecordByEmailParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    subscriber_state_record_by_email_params.SubscriberStateRecordByEmailParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def record_by_id(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        external_account_id: str,
        inputs: Iterable[MarketingEventSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Record a subscriber state between multiple HubSpot contacts and a marketing
        event, using HubSpot contact IDs. Note that the contact must already exist in
        HubSpot; a contact will not be created.

        Args:
          inputs: List of HubSpot contacts to subscribe to the marketing event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/{subscriber_state}/upsert",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=maybe_transform(
                {"inputs": inputs}, subscriber_state_record_by_id_params.SubscriberStateRecordByIDParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    subscriber_state_record_by_id_params.SubscriberStateRecordByIDParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSubscriberStateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriberStateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriberStateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriberStateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSubscriberStateResourceWithStreamingResponse(self)

    async def record_by_email(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        external_account_id: str,
        inputs: Iterable[MarketingEventEmailSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Record a subscriber state between multiple HubSpot contacts and a marketing
        event, using contact email addresses. Note that the contact must already exist
        in HubSpot; a contact will not be created. The contactProperties field is used
        only when creating a new contact. These properties will not update existing
        contacts.

        Args:
          inputs: List of marketing event details to create or update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/{subscriber_state}/email-upsert",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=await async_maybe_transform(
                {"inputs": inputs}, subscriber_state_record_by_email_params.SubscriberStateRecordByEmailParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    subscriber_state_record_by_email_params.SubscriberStateRecordByEmailParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def record_by_id(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        external_account_id: str,
        inputs: Iterable[MarketingEventSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Record a subscriber state between multiple HubSpot contacts and a marketing
        event, using HubSpot contact IDs. Note that the contact must already exist in
        HubSpot; a contact will not be created.

        Args:
          inputs: List of HubSpot contacts to subscribe to the marketing event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}/{subscriber_state}/upsert",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=await async_maybe_transform(
                {"inputs": inputs}, subscriber_state_record_by_id_params.SubscriberStateRecordByIDParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    subscriber_state_record_by_id_params.SubscriberStateRecordByIDParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SubscriberStateResourceWithRawResponse:
    def __init__(self, subscriber_state: SubscriberStateResource) -> None:
        self._subscriber_state = subscriber_state

        self.record_by_email = to_custom_raw_response_wrapper(
            subscriber_state.record_by_email,
            BinaryAPIResponse,
        )
        self.record_by_id = to_custom_raw_response_wrapper(
            subscriber_state.record_by_id,
            BinaryAPIResponse,
        )


class AsyncSubscriberStateResourceWithRawResponse:
    def __init__(self, subscriber_state: AsyncSubscriberStateResource) -> None:
        self._subscriber_state = subscriber_state

        self.record_by_email = async_to_custom_raw_response_wrapper(
            subscriber_state.record_by_email,
            AsyncBinaryAPIResponse,
        )
        self.record_by_id = async_to_custom_raw_response_wrapper(
            subscriber_state.record_by_id,
            AsyncBinaryAPIResponse,
        )


class SubscriberStateResourceWithStreamingResponse:
    def __init__(self, subscriber_state: SubscriberStateResource) -> None:
        self._subscriber_state = subscriber_state

        self.record_by_email = to_custom_streamed_response_wrapper(
            subscriber_state.record_by_email,
            StreamedBinaryAPIResponse,
        )
        self.record_by_id = to_custom_streamed_response_wrapper(
            subscriber_state.record_by_id,
            StreamedBinaryAPIResponse,
        )


class AsyncSubscriberStateResourceWithStreamingResponse:
    def __init__(self, subscriber_state: AsyncSubscriberStateResource) -> None:
        self._subscriber_state = subscriber_state

        self.record_by_email = async_to_custom_streamed_response_wrapper(
            subscriber_state.record_by_email,
            AsyncStreamedBinaryAPIResponse,
        )
        self.record_by_id = async_to_custom_streamed_response_wrapper(
            subscriber_state.record_by_id,
            AsyncStreamedBinaryAPIResponse,
        )
