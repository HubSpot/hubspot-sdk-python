# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.marketing.marketing_events import (
    participation_list_breakdown_by_id_params,
    participation_list_breakdown_by_contact_params,
    participation_list_breakdown_by_external_account_and_event_id_params,
)
from ....types.marketing.attendance_counters import AttendanceCounters
from ....types.marketing.participation_breakdown import ParticipationBreakdown

__all__ = ["ParticipationsResource", "AsyncParticipationsResource"]


class ParticipationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParticipationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ParticipationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParticipationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return ParticipationsResourceWithStreamingResponse(self)

    def get_by_external_account_and_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttendanceCounters:
        """
        Read Marketing event's participations counters by externalAccountId and
        externalEventId pair.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._get(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{external_account_id}/{external_event_id}",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttendanceCounters,
        )

    def get_by_id(
        self,
        marketing_event_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttendanceCounters:
        """
        Read Marketing event's participations counters by internal identifier
        marketingEventId.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{marketing_event_id}",
                marketing_event_id=marketing_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttendanceCounters,
        )

    def list_breakdown_by_contact(
        self,
        contact_identifier: str,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ParticipationBreakdown]:
        """
        Read Contact's participations by identifier - email or internal id.

        Args:
          after: The cursor indicating the position of the last retrieved item.

          limit: The limit for response size. The default value is 10, the max number is 100

          state: The participation state value. It may be REGISTERED, CANCELLED, ATTENDED,
              NO_SHOW

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_identifier:
            raise ValueError(f"Expected a non-empty value for `contact_identifier` but received {contact_identifier!r}")
        return self._get_api_list(
            path_template(
                "/marketing/marketing-events/2026-03/participations/contacts/{contact_identifier}/breakdown",
                contact_identifier=contact_identifier,
            ),
            page=SyncPage[ParticipationBreakdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "state": state,
                    },
                    participation_list_breakdown_by_contact_params.ParticipationListBreakdownByContactParams,
                ),
            ),
            model=ParticipationBreakdown,
        )

    def list_breakdown_by_external_account_and_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        after: str | Omit = omit,
        contact_identifier: str | Omit = omit,
        limit: int | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ParticipationBreakdown]:
        """
        Read Marketing event's participations breakdown with optional filters by
        externalAccountId and externalEventId pair.

        Args:
          after: The cursor indicating the position of the last retrieved item.

          contact_identifier: The identifier of the Contact. It may be email or internal id.

          limit: The limit for response size. The default value is 10, the max number is 100

          state: The participation state value. It may be REGISTERED, CANCELLED, ATTENDED,
              NO_SHOW

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._get_api_list(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{external_account_id}/{external_event_id}/breakdown",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
            ),
            page=SyncPage[ParticipationBreakdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "contact_identifier": contact_identifier,
                        "limit": limit,
                        "state": state,
                    },
                    participation_list_breakdown_by_external_account_and_event_id_params.ParticipationListBreakdownByExternalAccountAndEventIDParams,
                ),
            ),
            model=ParticipationBreakdown,
        )

    def list_breakdown_by_id(
        self,
        marketing_event_id: int,
        *,
        after: str | Omit = omit,
        contact_identifier: str | Omit = omit,
        limit: int | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ParticipationBreakdown]:
        """
        Read Marketing event's participations breakdown with optional filters by
        internal identifier marketingEventId.

        Args:
          after: The cursor indicating the position of the last retrieved item.

          contact_identifier: The identifier of the Contact. It may be email or internal id.

          limit: The limit for response size. The default value is 10, the max number is 100

          state: The participation state value. It may be REGISTERED, CANCELLED, ATTENDED,
              NO_SHOW

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{marketing_event_id}/breakdown",
                marketing_event_id=marketing_event_id,
            ),
            page=SyncPage[ParticipationBreakdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "contact_identifier": contact_identifier,
                        "limit": limit,
                        "state": state,
                    },
                    participation_list_breakdown_by_id_params.ParticipationListBreakdownByIDParams,
                ),
            ),
            model=ParticipationBreakdown,
        )


class AsyncParticipationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParticipationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParticipationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParticipationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncParticipationsResourceWithStreamingResponse(self)

    async def get_by_external_account_and_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttendanceCounters:
        """
        Read Marketing event's participations counters by externalAccountId and
        externalEventId pair.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._get(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{external_account_id}/{external_event_id}",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttendanceCounters,
        )

    async def get_by_id(
        self,
        marketing_event_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttendanceCounters:
        """
        Read Marketing event's participations counters by internal identifier
        marketingEventId.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{marketing_event_id}",
                marketing_event_id=marketing_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttendanceCounters,
        )

    def list_breakdown_by_contact(
        self,
        contact_identifier: str,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ParticipationBreakdown, AsyncPage[ParticipationBreakdown]]:
        """
        Read Contact's participations by identifier - email or internal id.

        Args:
          after: The cursor indicating the position of the last retrieved item.

          limit: The limit for response size. The default value is 10, the max number is 100

          state: The participation state value. It may be REGISTERED, CANCELLED, ATTENDED,
              NO_SHOW

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_identifier:
            raise ValueError(f"Expected a non-empty value for `contact_identifier` but received {contact_identifier!r}")
        return self._get_api_list(
            path_template(
                "/marketing/marketing-events/2026-03/participations/contacts/{contact_identifier}/breakdown",
                contact_identifier=contact_identifier,
            ),
            page=AsyncPage[ParticipationBreakdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "state": state,
                    },
                    participation_list_breakdown_by_contact_params.ParticipationListBreakdownByContactParams,
                ),
            ),
            model=ParticipationBreakdown,
        )

    def list_breakdown_by_external_account_and_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        after: str | Omit = omit,
        contact_identifier: str | Omit = omit,
        limit: int | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ParticipationBreakdown, AsyncPage[ParticipationBreakdown]]:
        """
        Read Marketing event's participations breakdown with optional filters by
        externalAccountId and externalEventId pair.

        Args:
          after: The cursor indicating the position of the last retrieved item.

          contact_identifier: The identifier of the Contact. It may be email or internal id.

          limit: The limit for response size. The default value is 10, the max number is 100

          state: The participation state value. It may be REGISTERED, CANCELLED, ATTENDED,
              NO_SHOW

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._get_api_list(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{external_account_id}/{external_event_id}/breakdown",
                external_account_id=external_account_id,
                external_event_id=external_event_id,
            ),
            page=AsyncPage[ParticipationBreakdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "contact_identifier": contact_identifier,
                        "limit": limit,
                        "state": state,
                    },
                    participation_list_breakdown_by_external_account_and_event_id_params.ParticipationListBreakdownByExternalAccountAndEventIDParams,
                ),
            ),
            model=ParticipationBreakdown,
        )

    def list_breakdown_by_id(
        self,
        marketing_event_id: int,
        *,
        after: str | Omit = omit,
        contact_identifier: str | Omit = omit,
        limit: int | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ParticipationBreakdown, AsyncPage[ParticipationBreakdown]]:
        """
        Read Marketing event's participations breakdown with optional filters by
        internal identifier marketingEventId.

        Args:
          after: The cursor indicating the position of the last retrieved item.

          contact_identifier: The identifier of the Contact. It may be email or internal id.

          limit: The limit for response size. The default value is 10, the max number is 100

          state: The participation state value. It may be REGISTERED, CANCELLED, ATTENDED,
              NO_SHOW

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template(
                "/marketing/marketing-events/2026-03/participations/{marketing_event_id}/breakdown",
                marketing_event_id=marketing_event_id,
            ),
            page=AsyncPage[ParticipationBreakdown],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "contact_identifier": contact_identifier,
                        "limit": limit,
                        "state": state,
                    },
                    participation_list_breakdown_by_id_params.ParticipationListBreakdownByIDParams,
                ),
            ),
            model=ParticipationBreakdown,
        )


class ParticipationsResourceWithRawResponse:
    def __init__(self, participations: ParticipationsResource) -> None:
        self._participations = participations

        self.get_by_external_account_and_event_id = to_raw_response_wrapper(
            participations.get_by_external_account_and_event_id,
        )
        self.get_by_id = to_raw_response_wrapper(
            participations.get_by_id,
        )
        self.list_breakdown_by_contact = to_raw_response_wrapper(
            participations.list_breakdown_by_contact,
        )
        self.list_breakdown_by_external_account_and_event_id = to_raw_response_wrapper(
            participations.list_breakdown_by_external_account_and_event_id,
        )
        self.list_breakdown_by_id = to_raw_response_wrapper(
            participations.list_breakdown_by_id,
        )


class AsyncParticipationsResourceWithRawResponse:
    def __init__(self, participations: AsyncParticipationsResource) -> None:
        self._participations = participations

        self.get_by_external_account_and_event_id = async_to_raw_response_wrapper(
            participations.get_by_external_account_and_event_id,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            participations.get_by_id,
        )
        self.list_breakdown_by_contact = async_to_raw_response_wrapper(
            participations.list_breakdown_by_contact,
        )
        self.list_breakdown_by_external_account_and_event_id = async_to_raw_response_wrapper(
            participations.list_breakdown_by_external_account_and_event_id,
        )
        self.list_breakdown_by_id = async_to_raw_response_wrapper(
            participations.list_breakdown_by_id,
        )


class ParticipationsResourceWithStreamingResponse:
    def __init__(self, participations: ParticipationsResource) -> None:
        self._participations = participations

        self.get_by_external_account_and_event_id = to_streamed_response_wrapper(
            participations.get_by_external_account_and_event_id,
        )
        self.get_by_id = to_streamed_response_wrapper(
            participations.get_by_id,
        )
        self.list_breakdown_by_contact = to_streamed_response_wrapper(
            participations.list_breakdown_by_contact,
        )
        self.list_breakdown_by_external_account_and_event_id = to_streamed_response_wrapper(
            participations.list_breakdown_by_external_account_and_event_id,
        )
        self.list_breakdown_by_id = to_streamed_response_wrapper(
            participations.list_breakdown_by_id,
        )


class AsyncParticipationsResourceWithStreamingResponse:
    def __init__(self, participations: AsyncParticipationsResource) -> None:
        self._participations = participations

        self.get_by_external_account_and_event_id = async_to_streamed_response_wrapper(
            participations.get_by_external_account_and_event_id,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            participations.get_by_id,
        )
        self.list_breakdown_by_contact = async_to_streamed_response_wrapper(
            participations.list_breakdown_by_contact,
        )
        self.list_breakdown_by_external_account_and_event_id = async_to_streamed_response_wrapper(
            participations.list_breakdown_by_external_account_and_event_id,
        )
        self.list_breakdown_by_id = async_to_streamed_response_wrapper(
            participations.list_breakdown_by_id,
        )
