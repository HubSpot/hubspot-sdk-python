# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.marketing.events import (
    attendance_create_by_event_id_and_email_params,
    attendance_create_by_event_id_and_contact_id_params,
    attendance_create_by_external_event_id_and_email_params,
    attendance_create_by_external_event_id_and_contact_id_params,
)
from ....types.marketing.marketing_event_subscriber_param import MarketingEventSubscriberParam
from ....types.marketing.batch_response_subscriber_vid_response import BatchResponseSubscriberVidResponse
from ....types.marketing.marketing_event_email_subscriber_param import MarketingEventEmailSubscriberParam
from ....types.marketing.batch_response_subscriber_email_response import BatchResponseSubscriberEmailResponse

__all__ = ["AttendanceResource", "AsyncAttendanceResource"]


class AttendanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttendanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AttendanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttendanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AttendanceResourceWithStreamingResponse(self)

    def create_by_event_id_and_contact_id(
        self,
        subscriber_state: str,
        *,
        object_id: str,
        inputs: Iterable[MarketingEventSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberVidResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their HubSpot contact IDs.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

        Args:
          inputs: List of HubSpot contacts to subscribe to the marketing event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/{object_id}/attendance/{subscriber_state}/create",
                object_id=object_id,
                subscriber_state=subscriber_state,
            ),
            body=maybe_transform(
                {"inputs": inputs},
                attendance_create_by_event_id_and_contact_id_params.AttendanceCreateByEventIDAndContactIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriberVidResponse,
        )

    def create_by_event_id_and_email(
        self,
        subscriber_state: str,
        *,
        object_id: str,
        inputs: Iterable[MarketingEventEmailSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberEmailResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their email addresses.

        If a contact does not exist, it will be automatically created. The
        contactProperties field is used exclusively for creating new contacts and will
        not update properties of existing contacts.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

        Args:
          inputs: List of marketing event details to create or update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/{object_id}/attendance/{subscriber_state}/email-create",
                object_id=object_id,
                subscriber_state=subscriber_state,
            ),
            body=maybe_transform(
                {"inputs": inputs},
                attendance_create_by_event_id_and_email_params.AttendanceCreateByEventIDAndEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriberEmailResponse,
        )

    def create_by_external_event_id_and_contact_id(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        inputs: Iterable[MarketingEventSubscriberParam],
        external_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberVidResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their HubSpot contact IDs.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

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
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/attendance/{external_event_id}/{subscriber_state}/create",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=maybe_transform(
                {"inputs": inputs},
                attendance_create_by_external_event_id_and_contact_id_params.AttendanceCreateByExternalEventIDAndContactIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    attendance_create_by_external_event_id_and_contact_id_params.AttendanceCreateByExternalEventIDAndContactIDParams,
                ),
            ),
            cast_to=BatchResponseSubscriberVidResponse,
        )

    def create_by_external_event_id_and_email(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        inputs: Iterable[MarketingEventEmailSubscriberParam],
        external_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberEmailResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their email addresses.

        If a contact does not exist, it will be automatically created. The
        contactProperties field is used exclusively for creating new contacts and will
        not update properties of existing contacts.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

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
        return self._post(
            path_template(
                "/marketing/marketing-events/2026-03/attendance/{external_event_id}/{subscriber_state}/email-create",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=maybe_transform(
                {"inputs": inputs},
                attendance_create_by_external_event_id_and_email_params.AttendanceCreateByExternalEventIDAndEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    attendance_create_by_external_event_id_and_email_params.AttendanceCreateByExternalEventIDAndEmailParams,
                ),
            ),
            cast_to=BatchResponseSubscriberEmailResponse,
        )


class AsyncAttendanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttendanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttendanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttendanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAttendanceResourceWithStreamingResponse(self)

    async def create_by_event_id_and_contact_id(
        self,
        subscriber_state: str,
        *,
        object_id: str,
        inputs: Iterable[MarketingEventSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberVidResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their HubSpot contact IDs.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

        Args:
          inputs: List of HubSpot contacts to subscribe to the marketing event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/{object_id}/attendance/{subscriber_state}/create",
                object_id=object_id,
                subscriber_state=subscriber_state,
            ),
            body=await async_maybe_transform(
                {"inputs": inputs},
                attendance_create_by_event_id_and_contact_id_params.AttendanceCreateByEventIDAndContactIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriberVidResponse,
        )

    async def create_by_event_id_and_email(
        self,
        subscriber_state: str,
        *,
        object_id: str,
        inputs: Iterable[MarketingEventEmailSubscriberParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberEmailResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their email addresses.

        If a contact does not exist, it will be automatically created. The
        contactProperties field is used exclusively for creating new contacts and will
        not update properties of existing contacts.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

        Args:
          inputs: List of marketing event details to create or update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not subscriber_state:
            raise ValueError(f"Expected a non-empty value for `subscriber_state` but received {subscriber_state!r}")
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/{object_id}/attendance/{subscriber_state}/email-create",
                object_id=object_id,
                subscriber_state=subscriber_state,
            ),
            body=await async_maybe_transform(
                {"inputs": inputs},
                attendance_create_by_event_id_and_email_params.AttendanceCreateByEventIDAndEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriberEmailResponse,
        )

    async def create_by_external_event_id_and_contact_id(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        inputs: Iterable[MarketingEventSubscriberParam],
        external_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberVidResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their HubSpot contact IDs.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

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
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/attendance/{external_event_id}/{subscriber_state}/create",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=await async_maybe_transform(
                {"inputs": inputs},
                attendance_create_by_external_event_id_and_contact_id_params.AttendanceCreateByExternalEventIDAndContactIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    attendance_create_by_external_event_id_and_contact_id_params.AttendanceCreateByExternalEventIDAndContactIDParams,
                ),
            ),
            cast_to=BatchResponseSubscriberVidResponse,
        )

    async def create_by_external_event_id_and_email(
        self,
        subscriber_state: str,
        *,
        external_event_id: str,
        inputs: Iterable[MarketingEventEmailSubscriberParam],
        external_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriberEmailResponse:
        """
        Records the participation of multiple HubSpot contacts in a Marketing Event
        using their email addresses.

        If a contact does not exist, it will be automatically created. The
        contactProperties field is used exclusively for creating new contacts and will
        not update properties of existing contacts.

        Additional Functionality:

        - Adds a timeline event to the contacts.

        Allowed Properties: For the state "attend":

        - joinedAt
        - leftAt

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
        return await self._post(
            path_template(
                "/marketing/marketing-events/2026-03/attendance/{external_event_id}/{subscriber_state}/email-create",
                external_event_id=external_event_id,
                subscriber_state=subscriber_state,
            ),
            body=await async_maybe_transform(
                {"inputs": inputs},
                attendance_create_by_external_event_id_and_email_params.AttendanceCreateByExternalEventIDAndEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    attendance_create_by_external_event_id_and_email_params.AttendanceCreateByExternalEventIDAndEmailParams,
                ),
            ),
            cast_to=BatchResponseSubscriberEmailResponse,
        )


class AttendanceResourceWithRawResponse:
    def __init__(self, attendance: AttendanceResource) -> None:
        self._attendance = attendance

        self.create_by_event_id_and_contact_id = to_raw_response_wrapper(
            attendance.create_by_event_id_and_contact_id,
        )
        self.create_by_event_id_and_email = to_raw_response_wrapper(
            attendance.create_by_event_id_and_email,
        )
        self.create_by_external_event_id_and_contact_id = to_raw_response_wrapper(
            attendance.create_by_external_event_id_and_contact_id,
        )
        self.create_by_external_event_id_and_email = to_raw_response_wrapper(
            attendance.create_by_external_event_id_and_email,
        )


class AsyncAttendanceResourceWithRawResponse:
    def __init__(self, attendance: AsyncAttendanceResource) -> None:
        self._attendance = attendance

        self.create_by_event_id_and_contact_id = async_to_raw_response_wrapper(
            attendance.create_by_event_id_and_contact_id,
        )
        self.create_by_event_id_and_email = async_to_raw_response_wrapper(
            attendance.create_by_event_id_and_email,
        )
        self.create_by_external_event_id_and_contact_id = async_to_raw_response_wrapper(
            attendance.create_by_external_event_id_and_contact_id,
        )
        self.create_by_external_event_id_and_email = async_to_raw_response_wrapper(
            attendance.create_by_external_event_id_and_email,
        )


class AttendanceResourceWithStreamingResponse:
    def __init__(self, attendance: AttendanceResource) -> None:
        self._attendance = attendance

        self.create_by_event_id_and_contact_id = to_streamed_response_wrapper(
            attendance.create_by_event_id_and_contact_id,
        )
        self.create_by_event_id_and_email = to_streamed_response_wrapper(
            attendance.create_by_event_id_and_email,
        )
        self.create_by_external_event_id_and_contact_id = to_streamed_response_wrapper(
            attendance.create_by_external_event_id_and_contact_id,
        )
        self.create_by_external_event_id_and_email = to_streamed_response_wrapper(
            attendance.create_by_external_event_id_and_email,
        )


class AsyncAttendanceResourceWithStreamingResponse:
    def __init__(self, attendance: AsyncAttendanceResource) -> None:
        self._attendance = attendance

        self.create_by_event_id_and_contact_id = async_to_streamed_response_wrapper(
            attendance.create_by_event_id_and_contact_id,
        )
        self.create_by_event_id_and_email = async_to_streamed_response_wrapper(
            attendance.create_by_event_id_and_email,
        )
        self.create_by_external_event_id_and_contact_id = async_to_streamed_response_wrapper(
            attendance.create_by_external_event_id_and_contact_id,
        )
        self.create_by_external_event_id_and_email = async_to_streamed_response_wrapper(
            attendance.create_by_external_event_id_and_email,
        )
