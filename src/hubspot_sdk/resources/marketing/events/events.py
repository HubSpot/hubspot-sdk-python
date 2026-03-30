# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from . import events_ as events
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .attendance import (
    AttendanceResource,
    AsyncAttendanceResource,
    AttendanceResourceWithRawResponse,
    AsyncAttendanceResourceWithRawResponse,
    AttendanceResourceWithStreamingResponse,
    AsyncAttendanceResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from .participations import (
    ParticipationsResource,
    AsyncParticipationsResource,
    ParticipationsResourceWithRawResponse,
    AsyncParticipationsResourceWithRawResponse,
    ParticipationsResourceWithStreamingResponse,
    AsyncParticipationsResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from .subscriber_state import (
    SubscriberStateResource,
    AsyncSubscriberStateResource,
    SubscriberStateResourceWithRawResponse,
    AsyncSubscriberStateResourceWithRawResponse,
    SubscriberStateResourceWithStreamingResponse,
    AsyncSubscriberStateResourceWithStreamingResponse,
)
from .list_associations import (
    ListAssociationsResource,
    AsyncListAssociationsResource,
    ListAssociationsResourceWithRawResponse,
    AsyncListAssociationsResourceWithRawResponse,
    ListAssociationsResourceWithStreamingResponse,
    AsyncListAssociationsResourceWithStreamingResponse,
)
from ....types.marketing import (
    event_list_params,
    event_create_params,
    event_update_params,
    event_delete_batch_params,
    event_update_batch_params,
    event_upsert_batch_params,
    event_get_by_external_event_id_params,
    event_delete_by_external_event_id_params,
    event_search_by_external_event_id_params,
    event_update_by_external_event_id_params,
    event_upsert_by_external_event_id_params,
    event_delete_batch_by_external_event_id_params,
)
from ....types.shared_params.property_value import PropertyValue
from ....types.marketing.marketing_event_default_response import MarketingEventDefaultResponse
from ....types.marketing.marketing_event_public_read_response import MarketingEventPublicReadResponse
from ....types.marketing.marketing_event_create_request_params import MarketingEventCreateRequestParams
from ....types.marketing.marketing_event_public_default_response import MarketingEventPublicDefaultResponse
from ....types.marketing.marketing_event_public_read_response_v2 import MarketingEventPublicReadResponseV2
from ....types.marketing.marketing_event_public_default_response_v2 import MarketingEventPublicDefaultResponseV2
from ....types.marketing.marketing_event_external_unique_identifier_param import (
    MarketingEventExternalUniqueIdentifierParam,
)
from ....types.marketing.marketing_event_public_update_request_full_v2_param import (
    MarketingEventPublicUpdateRequestFullV2Param,
)
from ....types.marketing.marketing_event_public_object_id_delete_request_param import (
    MarketingEventPublicObjectIDDeleteRequestParam,
)
from ....types.marketing.batch_response_marketing_event_public_default_response import (
    BatchResponseMarketingEventPublicDefaultResponse,
)
from ....types.marketing.batch_response_marketing_event_public_default_response_v2 import (
    BatchResponseMarketingEventPublicDefaultResponseV2,
)
from ....types.marketing.collection_response_search_public_response_wrapper_no_paging import (
    CollectionResponseSearchPublicResponseWrapperNoPaging,
)
from ....types.marketing.collection_response_with_total_marketing_event_identifiers_response import (
    CollectionResponseWithTotalMarketingEventIdentifiersResponse,
)

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def attendance(self) -> AttendanceResource:
        return AttendanceResource(self._client)

    @cached_property
    def events(self) -> events.EventsResource:
        return events.EventsResource(self._client)

    @cached_property
    def list_associations(self) -> ListAssociationsResource:
        return ListAssociationsResource(self._client)

    @cached_property
    def participations(self) -> ParticipationsResource:
        return ParticipationsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def subscriber_state(self) -> SubscriberStateResource:
        return SubscriberStateResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        custom_properties: Iterable[PropertyValue],
        event_name: str,
        event_organizer: str,
        external_account_id: str,
        external_event_id: str,
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_completed: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventDefaultResponse:
        """
        Creates a new marketing event in HubSpot

        Args:
          custom_properties: A list of PropertyValues. These can be whatever kind of property names and
              values you want. However, they must already exist on the HubSpot account's
              definition of the MarketingEvent Object. If they don't they will be filtered out
              and not set. In order to do this you'll need to create a new PropertyGroup on
              the HubSpot account's MarketingEvent object for your specific app and create the
              Custom Property you want to track on that HubSpot account. Do not create any new
              default properties on the MarketingEvent object as that will apply to all
              HubSpot accounts.

          event_name: The name of the marketing event.

          event_organizer: The name of the organizer of the marketing event.

          external_account_id: The accountId that is associated with this marketing event in the external event
              application.

          external_event_id: The id of the marketing event in the external event application.

          end_date_time: The end date and time of the marketing event.

          event_cancelled: Indicates if the marketing event has been cancelled. Defaults to `false`

          event_completed: Indicates if the marketing event has been completed. Defaults to `false`

          event_description: The description of the marketing event.

          event_type: Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`,
              `WORKSHOP`

          event_url: A URL in the external event application where the marketing event can be
              managed.

          start_date_time: The start date and time of the marketing event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/marketing-events/2026-03/events",
            body=maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "external_account_id": external_account_id,
                    "external_event_id": external_event_id,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_completed": event_completed,
                    "event_description": event_description,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventDefaultResponse,
        )

    def update(
        self,
        object_id: str,
        *,
        custom_properties: Iterable[PropertyValue],
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_name: str | Omit = omit,
        event_organizer: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicDefaultResponseV2:
        """
        Updates the details of an existing Marketing Event identified by its objectId,
        if it exists.

        Args:
          end_date_time: The end date and time of the marketing event

          event_cancelled: Indicates if the marketing event has been cancelled

          event_description: The description of the marketing event

          event_name: The name of the marketing event

          event_organizer: The name of the organizer of the marketing event

          event_type: The type of the marketing event

          event_url: A URL in the external event application where the marketing event can be managed

          start_date_time: The start date and time of the marketing event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            path_template("/marketing/marketing-events/2026-03/{object_id}", object_id=object_id),
            body=maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_description": event_description,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventPublicDefaultResponseV2,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[MarketingEventPublicReadResponseV2]:
        """
        Args:
          after: The cursor indicating the position of the last retrieved item.

          limit: The limit for response size. The default value is 10, the max number is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/marketing/marketing-events/2026-03",
            page=SyncPage[MarketingEventPublicReadResponseV2],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=MarketingEventPublicReadResponseV2,
        )

    def delete(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the existing Marketing Event with the specified objectId, if it exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/marketing/marketing-events/2026-03/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_batch(
        self,
        *,
        inputs: Iterable[MarketingEventPublicObjectIDDeleteRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Deletes multiple Marketing Events from the portal based on their objectId, if
        they exist.

        Responses: 204: Returned if all specified Marketing Events were successfully
        deleted. 207: Returned if some objectIds did not correspond to any existing
        Marketing Events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/marketing/marketing-events/2026-03/batch/archive",
            body=maybe_transform({"inputs": inputs}, event_delete_batch_params.EventDeleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete_batch_by_external_event_id(
        self,
        *,
        inputs: Iterable[MarketingEventExternalUniqueIdentifierParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Deletes multiple Marketing Events based on externalAccountId, externalEventId,
        and appId.

        Only Marketing Events created by the same apps will be deleted; events from
        other apps cannot be removed by this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/marketing/marketing-events/2026-03/events/delete",
            body=maybe_transform(
                {"inputs": inputs},
                event_delete_batch_by_external_event_id_params.EventDeleteBatchByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete_by_external_event_id(
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
    ) -> None:
        """
        Deletes the existing Marketing Event with the specified externalAccountId,
        externalEventId, if it exists.

        Only Marketing Events created by the same app can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}", external_event_id=external_event_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    event_delete_by_external_event_id_params.EventDeleteByExternalEventIDParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicReadResponseV2:
        """
        Returns the details of a Marketing Event with the specified objectId, if it
        exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            path_template("/marketing/marketing-events/2026-03/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventPublicReadResponseV2,
        )

    def get_by_external_event_id(
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
    ) -> MarketingEventPublicReadResponse:
        """
        Returns the details of a Marketing Event with the specified externalAccountId,
        externalEventId, if it exists.

        Only Marketing Events created by the same app making the request can be
        retrieved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._get(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}", external_event_id=external_event_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    event_get_by_external_event_id_params.EventGetByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventPublicReadResponse,
        )

    def search_by_external_event_id(
        self,
        *,
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseSearchPublicResponseWrapperNoPaging:
        """
        Retrieves Marketing Events where the externalEventId matches the value provided
        in the request, limited to events created by the app making the request.

        Marketing Events created by other apps will not be included in the results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/marketing/marketing-events/2026-03/events/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"q": q}, event_search_by_external_event_id_params.EventSearchByExternalEventIDParams
                ),
            ),
            cast_to=CollectionResponseSearchPublicResponseWrapperNoPaging,
        )

    def search_identifiers_by_external_event_id(
        self,
        external_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalMarketingEventIdentifiersResponse:
        """
        This endpoint searches the portal for all Marketing Events whose externalEventId
        matches the value provided in the request.

        It retrieves the objectId and additional event details for each matching
        Marketing Event.

        Since multiple Marketing Events can have the same externalEventId, the endpoint
        returns all matching results.

        Note: Marketing Events become searchable by externalEventId a few minutes after
        creation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._get(
            path_template(
                "/marketing/marketing-events/2026-03/{external_event_id}/identifiers",
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalMarketingEventIdentifiersResponse,
        )

    def update_batch(
        self,
        *,
        inputs: Iterable[MarketingEventPublicUpdateRequestFullV2Param],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseMarketingEventPublicDefaultResponseV2:
        """
        Updates multiple Marketing Events on the portal based on their objectId, if they
        exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/marketing-events/2026-03/batch/update",
            body=maybe_transform({"inputs": inputs}, event_update_batch_params.EventUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseMarketingEventPublicDefaultResponseV2,
        )

    def update_by_external_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        custom_properties: Iterable[PropertyValue],
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_completed: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_name: str | Omit = omit,
        event_organizer: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicDefaultResponse:
        """
        Updates the details of an existing Marketing Event identified by its
        externalAccountId, externalEventId if it exists.

        Only Marketing Events created by the same app can be updated.

        Args:
          custom_properties: A list of PropertyValues. These can be whatever kind of property names and
              values you want. However, they must already exist on the HubSpot account's
              definition of the MarketingEvent Object. If they don't they will be filtered out
              and not set. In order to do this you'll need to create a new PropertyGroup on
              the HubSpot account's MarketingEvent object for your specific app and create the
              Custom Property you want to track on that HubSpot account. Do not create any new
              default properties on the MarketingEvent object as that will apply to all
              HubSpot accounts.

          end_date_time: The end date and time of the marketing event.

          event_cancelled: Indicates if the marketing event has been cancelled. Defaults to `false`

          event_completed: Indicates if the marketing event has been completed. Defaults to `false`

          event_description: The description of the marketing event.

          event_name: The name of the marketing event.

          event_organizer: The name of the organizer of the marketing event.

          event_type: Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`,
              `WORKSHOP`

          event_url: A URL in the external event application where the marketing event can be
              managed.

          start_date_time: The start date and time of the marketing event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._patch(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}", external_event_id=external_event_id
            ),
            body=maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_completed": event_completed,
                    "event_description": event_description,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_update_by_external_event_id_params.EventUpdateByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external_account_id": external_account_id},
                    event_update_by_external_event_id_params.EventUpdateByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventPublicDefaultResponse,
        )

    def upsert_batch(
        self,
        *,
        inputs: Iterable[MarketingEventCreateRequestParams],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseMarketingEventPublicDefaultResponse:
        """Upserts multiple Marketing Events.

        If a Marketing Event with the specified ID
        already exists, it will be updated; otherwise, a new event will be created.

        Only Marketing Events originally created by the same app can be updated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/marketing-events/2026-03/events/upsert",
            body=maybe_transform({"inputs": inputs}, event_upsert_batch_params.EventUpsertBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseMarketingEventPublicDefaultResponse,
        )

    def upsert_by_external_event_id(
        self,
        path_external_event_id: str,
        *,
        custom_properties: Iterable[PropertyValue],
        event_name: str,
        event_organizer: str,
        external_account_id: str,
        body_external_event_id: str,
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_completed: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicDefaultResponse:
        """
        Upserts a marketing event If there is an existing marketing event with the
        specified ID, it will be updated; otherwise a new event will be created.

        Args:
          custom_properties: A list of PropertyValues. These can be whatever kind of property names and
              values you want. However, they must already exist on the HubSpot account's
              definition of the MarketingEvent Object. If they don't they will be filtered out
              and not set. In order to do this you'll need to create a new PropertyGroup on
              the HubSpot account's MarketingEvent object for your specific app and create the
              Custom Property you want to track on that HubSpot account. Do not create any new
              default properties on the MarketingEvent object as that will apply to all
              HubSpot accounts.

          event_name: The name of the marketing event.

          event_organizer: The name of the organizer of the marketing event.

          external_account_id: The accountId that is associated with this marketing event in the external event
              application.

          body_external_event_id: The id of the marketing event in the external event application.

          end_date_time: The end date and time of the marketing event.

          event_cancelled: Indicates if the marketing event has been cancelled. Defaults to `false`

          event_completed: Indicates if the marketing event has been completed. Defaults to `false`

          event_description: The description of the marketing event.

          event_type: Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`,
              `WORKSHOP`

          event_url: A URL in the external event application where the marketing event can be
              managed.

          start_date_time: The start date and time of the marketing event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_external_event_id:
            raise ValueError(
                f"Expected a non-empty value for `path_external_event_id` but received {path_external_event_id!r}"
            )
        return self._put(
            path_template(
                "/marketing/marketing-events/2026-03/events/{path_external_event_id}",
                path_external_event_id=path_external_event_id,
            ),
            body=maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "external_account_id": external_account_id,
                    "body_external_event_id": body_external_event_id,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_completed": event_completed,
                    "event_description": event_description,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_upsert_by_external_event_id_params.EventUpsertByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventPublicDefaultResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def attendance(self) -> AsyncAttendanceResource:
        return AsyncAttendanceResource(self._client)

    @cached_property
    def events(self) -> events.AsyncEventsResource:
        return events.AsyncEventsResource(self._client)

    @cached_property
    def list_associations(self) -> AsyncListAssociationsResource:
        return AsyncListAssociationsResource(self._client)

    @cached_property
    def participations(self) -> AsyncParticipationsResource:
        return AsyncParticipationsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def subscriber_state(self) -> AsyncSubscriberStateResource:
        return AsyncSubscriberStateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        custom_properties: Iterable[PropertyValue],
        event_name: str,
        event_organizer: str,
        external_account_id: str,
        external_event_id: str,
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_completed: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventDefaultResponse:
        """
        Creates a new marketing event in HubSpot

        Args:
          custom_properties: A list of PropertyValues. These can be whatever kind of property names and
              values you want. However, they must already exist on the HubSpot account's
              definition of the MarketingEvent Object. If they don't they will be filtered out
              and not set. In order to do this you'll need to create a new PropertyGroup on
              the HubSpot account's MarketingEvent object for your specific app and create the
              Custom Property you want to track on that HubSpot account. Do not create any new
              default properties on the MarketingEvent object as that will apply to all
              HubSpot accounts.

          event_name: The name of the marketing event.

          event_organizer: The name of the organizer of the marketing event.

          external_account_id: The accountId that is associated with this marketing event in the external event
              application.

          external_event_id: The id of the marketing event in the external event application.

          end_date_time: The end date and time of the marketing event.

          event_cancelled: Indicates if the marketing event has been cancelled. Defaults to `false`

          event_completed: Indicates if the marketing event has been completed. Defaults to `false`

          event_description: The description of the marketing event.

          event_type: Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`,
              `WORKSHOP`

          event_url: A URL in the external event application where the marketing event can be
              managed.

          start_date_time: The start date and time of the marketing event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/marketing-events/2026-03/events",
            body=await async_maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "external_account_id": external_account_id,
                    "external_event_id": external_event_id,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_completed": event_completed,
                    "event_description": event_description,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventDefaultResponse,
        )

    async def update(
        self,
        object_id: str,
        *,
        custom_properties: Iterable[PropertyValue],
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_name: str | Omit = omit,
        event_organizer: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicDefaultResponseV2:
        """
        Updates the details of an existing Marketing Event identified by its objectId,
        if it exists.

        Args:
          end_date_time: The end date and time of the marketing event

          event_cancelled: Indicates if the marketing event has been cancelled

          event_description: The description of the marketing event

          event_name: The name of the marketing event

          event_organizer: The name of the organizer of the marketing event

          event_type: The type of the marketing event

          event_url: A URL in the external event application where the marketing event can be managed

          start_date_time: The start date and time of the marketing event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            path_template("/marketing/marketing-events/2026-03/{object_id}", object_id=object_id),
            body=await async_maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_description": event_description,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventPublicDefaultResponseV2,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MarketingEventPublicReadResponseV2, AsyncPage[MarketingEventPublicReadResponseV2]]:
        """
        Args:
          after: The cursor indicating the position of the last retrieved item.

          limit: The limit for response size. The default value is 10, the max number is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/marketing/marketing-events/2026-03",
            page=AsyncPage[MarketingEventPublicReadResponseV2],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=MarketingEventPublicReadResponseV2,
        )

    async def delete(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the existing Marketing Event with the specified objectId, if it exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/marketing/marketing-events/2026-03/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_batch(
        self,
        *,
        inputs: Iterable[MarketingEventPublicObjectIDDeleteRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Deletes multiple Marketing Events from the portal based on their objectId, if
        they exist.

        Responses: 204: Returned if all specified Marketing Events were successfully
        deleted. 207: Returned if some objectIds did not correspond to any existing
        Marketing Events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/marketing/marketing-events/2026-03/batch/archive",
            body=await async_maybe_transform({"inputs": inputs}, event_delete_batch_params.EventDeleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete_batch_by_external_event_id(
        self,
        *,
        inputs: Iterable[MarketingEventExternalUniqueIdentifierParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Deletes multiple Marketing Events based on externalAccountId, externalEventId,
        and appId.

        Only Marketing Events created by the same apps will be deleted; events from
        other apps cannot be removed by this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/marketing/marketing-events/2026-03/events/delete",
            body=await async_maybe_transform(
                {"inputs": inputs},
                event_delete_batch_by_external_event_id_params.EventDeleteBatchByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete_by_external_event_id(
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
    ) -> None:
        """
        Deletes the existing Marketing Event with the specified externalAccountId,
        externalEventId, if it exists.

        Only Marketing Events created by the same app can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}", external_event_id=external_event_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    event_delete_by_external_event_id_params.EventDeleteByExternalEventIDParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicReadResponseV2:
        """
        Returns the details of a Marketing Event with the specified objectId, if it
        exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            path_template("/marketing/marketing-events/2026-03/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventPublicReadResponseV2,
        )

    async def get_by_external_event_id(
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
    ) -> MarketingEventPublicReadResponse:
        """
        Returns the details of a Marketing Event with the specified externalAccountId,
        externalEventId, if it exists.

        Only Marketing Events created by the same app making the request can be
        retrieved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._get(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}", external_event_id=external_event_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    event_get_by_external_event_id_params.EventGetByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventPublicReadResponse,
        )

    async def search_by_external_event_id(
        self,
        *,
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseSearchPublicResponseWrapperNoPaging:
        """
        Retrieves Marketing Events where the externalEventId matches the value provided
        in the request, limited to events created by the app making the request.

        Marketing Events created by other apps will not be included in the results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/marketing/marketing-events/2026-03/events/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"q": q}, event_search_by_external_event_id_params.EventSearchByExternalEventIDParams
                ),
            ),
            cast_to=CollectionResponseSearchPublicResponseWrapperNoPaging,
        )

    async def search_identifiers_by_external_event_id(
        self,
        external_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalMarketingEventIdentifiersResponse:
        """
        This endpoint searches the portal for all Marketing Events whose externalEventId
        matches the value provided in the request.

        It retrieves the objectId and additional event details for each matching
        Marketing Event.

        Since multiple Marketing Events can have the same externalEventId, the endpoint
        returns all matching results.

        Note: Marketing Events become searchable by externalEventId a few minutes after
        creation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._get(
            path_template(
                "/marketing/marketing-events/2026-03/{external_event_id}/identifiers",
                external_event_id=external_event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalMarketingEventIdentifiersResponse,
        )

    async def update_batch(
        self,
        *,
        inputs: Iterable[MarketingEventPublicUpdateRequestFullV2Param],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseMarketingEventPublicDefaultResponseV2:
        """
        Updates multiple Marketing Events on the portal based on their objectId, if they
        exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/marketing-events/2026-03/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, event_update_batch_params.EventUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseMarketingEventPublicDefaultResponseV2,
        )

    async def update_by_external_event_id(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        custom_properties: Iterable[PropertyValue],
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_completed: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_name: str | Omit = omit,
        event_organizer: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicDefaultResponse:
        """
        Updates the details of an existing Marketing Event identified by its
        externalAccountId, externalEventId if it exists.

        Only Marketing Events created by the same app can be updated.

        Args:
          custom_properties: A list of PropertyValues. These can be whatever kind of property names and
              values you want. However, they must already exist on the HubSpot account's
              definition of the MarketingEvent Object. If they don't they will be filtered out
              and not set. In order to do this you'll need to create a new PropertyGroup on
              the HubSpot account's MarketingEvent object for your specific app and create the
              Custom Property you want to track on that HubSpot account. Do not create any new
              default properties on the MarketingEvent object as that will apply to all
              HubSpot accounts.

          end_date_time: The end date and time of the marketing event.

          event_cancelled: Indicates if the marketing event has been cancelled. Defaults to `false`

          event_completed: Indicates if the marketing event has been completed. Defaults to `false`

          event_description: The description of the marketing event.

          event_name: The name of the marketing event.

          event_organizer: The name of the organizer of the marketing event.

          event_type: Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`,
              `WORKSHOP`

          event_url: A URL in the external event application where the marketing event can be
              managed.

          start_date_time: The start date and time of the marketing event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._patch(
            path_template(
                "/marketing/marketing-events/2026-03/events/{external_event_id}", external_event_id=external_event_id
            ),
            body=await async_maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_completed": event_completed,
                    "event_description": event_description,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_update_by_external_event_id_params.EventUpdateByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external_account_id": external_account_id},
                    event_update_by_external_event_id_params.EventUpdateByExternalEventIDParams,
                ),
            ),
            cast_to=MarketingEventPublicDefaultResponse,
        )

    async def upsert_batch(
        self,
        *,
        inputs: Iterable[MarketingEventCreateRequestParams],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseMarketingEventPublicDefaultResponse:
        """Upserts multiple Marketing Events.

        If a Marketing Event with the specified ID
        already exists, it will be updated; otherwise, a new event will be created.

        Only Marketing Events originally created by the same app can be updated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/marketing-events/2026-03/events/upsert",
            body=await async_maybe_transform({"inputs": inputs}, event_upsert_batch_params.EventUpsertBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseMarketingEventPublicDefaultResponse,
        )

    async def upsert_by_external_event_id(
        self,
        path_external_event_id: str,
        *,
        custom_properties: Iterable[PropertyValue],
        event_name: str,
        event_organizer: str,
        external_account_id: str,
        body_external_event_id: str,
        end_date_time: Union[str, datetime] | Omit = omit,
        event_cancelled: bool | Omit = omit,
        event_completed: bool | Omit = omit,
        event_description: str | Omit = omit,
        event_type: str | Omit = omit,
        event_url: str | Omit = omit,
        start_date_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketingEventPublicDefaultResponse:
        """
        Upserts a marketing event If there is an existing marketing event with the
        specified ID, it will be updated; otherwise a new event will be created.

        Args:
          custom_properties: A list of PropertyValues. These can be whatever kind of property names and
              values you want. However, they must already exist on the HubSpot account's
              definition of the MarketingEvent Object. If they don't they will be filtered out
              and not set. In order to do this you'll need to create a new PropertyGroup on
              the HubSpot account's MarketingEvent object for your specific app and create the
              Custom Property you want to track on that HubSpot account. Do not create any new
              default properties on the MarketingEvent object as that will apply to all
              HubSpot accounts.

          event_name: The name of the marketing event.

          event_organizer: The name of the organizer of the marketing event.

          external_account_id: The accountId that is associated with this marketing event in the external event
              application.

          body_external_event_id: The id of the marketing event in the external event application.

          end_date_time: The end date and time of the marketing event.

          event_cancelled: Indicates if the marketing event has been cancelled. Defaults to `false`

          event_completed: Indicates if the marketing event has been completed. Defaults to `false`

          event_description: The description of the marketing event.

          event_type: Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`,
              `WORKSHOP`

          event_url: A URL in the external event application where the marketing event can be
              managed.

          start_date_time: The start date and time of the marketing event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_external_event_id:
            raise ValueError(
                f"Expected a non-empty value for `path_external_event_id` but received {path_external_event_id!r}"
            )
        return await self._put(
            path_template(
                "/marketing/marketing-events/2026-03/events/{path_external_event_id}",
                path_external_event_id=path_external_event_id,
            ),
            body=await async_maybe_transform(
                {
                    "custom_properties": custom_properties,
                    "event_name": event_name,
                    "event_organizer": event_organizer,
                    "external_account_id": external_account_id,
                    "body_external_event_id": body_external_event_id,
                    "end_date_time": end_date_time,
                    "event_cancelled": event_cancelled,
                    "event_completed": event_completed,
                    "event_description": event_description,
                    "event_type": event_type,
                    "event_url": event_url,
                    "start_date_time": start_date_time,
                },
                event_upsert_by_external_event_id_params.EventUpsertByExternalEventIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketingEventPublicDefaultResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )
        self.update = to_raw_response_wrapper(
            events.update,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.delete = to_raw_response_wrapper(
            events.delete,
        )
        self.delete_batch = to_custom_raw_response_wrapper(
            events.delete_batch,
            BinaryAPIResponse,
        )
        self.delete_batch_by_external_event_id = to_custom_raw_response_wrapper(
            events.delete_batch_by_external_event_id,
            BinaryAPIResponse,
        )
        self.delete_by_external_event_id = to_raw_response_wrapper(
            events.delete_by_external_event_id,
        )
        self.get = to_raw_response_wrapper(
            events.get,
        )
        self.get_by_external_event_id = to_raw_response_wrapper(
            events.get_by_external_event_id,
        )
        self.search_by_external_event_id = to_raw_response_wrapper(
            events.search_by_external_event_id,
        )
        self.search_identifiers_by_external_event_id = to_raw_response_wrapper(
            events.search_identifiers_by_external_event_id,
        )
        self.update_batch = to_raw_response_wrapper(
            events.update_batch,
        )
        self.update_by_external_event_id = to_raw_response_wrapper(
            events.update_by_external_event_id,
        )
        self.upsert_batch = to_raw_response_wrapper(
            events.upsert_batch,
        )
        self.upsert_by_external_event_id = to_raw_response_wrapper(
            events.upsert_by_external_event_id,
        )

    @cached_property
    def attendance(self) -> AttendanceResourceWithRawResponse:
        return AttendanceResourceWithRawResponse(self._events.attendance)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        return events.EventsResourceWithRawResponse(self._events.events)

    @cached_property
    def list_associations(self) -> ListAssociationsResourceWithRawResponse:
        return ListAssociationsResourceWithRawResponse(self._events.list_associations)

    @cached_property
    def participations(self) -> ParticipationsResourceWithRawResponse:
        return ParticipationsResourceWithRawResponse(self._events.participations)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._events.settings)

    @cached_property
    def subscriber_state(self) -> SubscriberStateResourceWithRawResponse:
        return SubscriberStateResourceWithRawResponse(self._events.subscriber_state)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )
        self.update = async_to_raw_response_wrapper(
            events.update,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.delete = async_to_raw_response_wrapper(
            events.delete,
        )
        self.delete_batch = async_to_custom_raw_response_wrapper(
            events.delete_batch,
            AsyncBinaryAPIResponse,
        )
        self.delete_batch_by_external_event_id = async_to_custom_raw_response_wrapper(
            events.delete_batch_by_external_event_id,
            AsyncBinaryAPIResponse,
        )
        self.delete_by_external_event_id = async_to_raw_response_wrapper(
            events.delete_by_external_event_id,
        )
        self.get = async_to_raw_response_wrapper(
            events.get,
        )
        self.get_by_external_event_id = async_to_raw_response_wrapper(
            events.get_by_external_event_id,
        )
        self.search_by_external_event_id = async_to_raw_response_wrapper(
            events.search_by_external_event_id,
        )
        self.search_identifiers_by_external_event_id = async_to_raw_response_wrapper(
            events.search_identifiers_by_external_event_id,
        )
        self.update_batch = async_to_raw_response_wrapper(
            events.update_batch,
        )
        self.update_by_external_event_id = async_to_raw_response_wrapper(
            events.update_by_external_event_id,
        )
        self.upsert_batch = async_to_raw_response_wrapper(
            events.upsert_batch,
        )
        self.upsert_by_external_event_id = async_to_raw_response_wrapper(
            events.upsert_by_external_event_id,
        )

    @cached_property
    def attendance(self) -> AsyncAttendanceResourceWithRawResponse:
        return AsyncAttendanceResourceWithRawResponse(self._events.attendance)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        return events.AsyncEventsResourceWithRawResponse(self._events.events)

    @cached_property
    def list_associations(self) -> AsyncListAssociationsResourceWithRawResponse:
        return AsyncListAssociationsResourceWithRawResponse(self._events.list_associations)

    @cached_property
    def participations(self) -> AsyncParticipationsResourceWithRawResponse:
        return AsyncParticipationsResourceWithRawResponse(self._events.participations)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._events.settings)

    @cached_property
    def subscriber_state(self) -> AsyncSubscriberStateResourceWithRawResponse:
        return AsyncSubscriberStateResourceWithRawResponse(self._events.subscriber_state)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )
        self.update = to_streamed_response_wrapper(
            events.update,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.delete = to_streamed_response_wrapper(
            events.delete,
        )
        self.delete_batch = to_custom_streamed_response_wrapper(
            events.delete_batch,
            StreamedBinaryAPIResponse,
        )
        self.delete_batch_by_external_event_id = to_custom_streamed_response_wrapper(
            events.delete_batch_by_external_event_id,
            StreamedBinaryAPIResponse,
        )
        self.delete_by_external_event_id = to_streamed_response_wrapper(
            events.delete_by_external_event_id,
        )
        self.get = to_streamed_response_wrapper(
            events.get,
        )
        self.get_by_external_event_id = to_streamed_response_wrapper(
            events.get_by_external_event_id,
        )
        self.search_by_external_event_id = to_streamed_response_wrapper(
            events.search_by_external_event_id,
        )
        self.search_identifiers_by_external_event_id = to_streamed_response_wrapper(
            events.search_identifiers_by_external_event_id,
        )
        self.update_batch = to_streamed_response_wrapper(
            events.update_batch,
        )
        self.update_by_external_event_id = to_streamed_response_wrapper(
            events.update_by_external_event_id,
        )
        self.upsert_batch = to_streamed_response_wrapper(
            events.upsert_batch,
        )
        self.upsert_by_external_event_id = to_streamed_response_wrapper(
            events.upsert_by_external_event_id,
        )

    @cached_property
    def attendance(self) -> AttendanceResourceWithStreamingResponse:
        return AttendanceResourceWithStreamingResponse(self._events.attendance)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        return events.EventsResourceWithStreamingResponse(self._events.events)

    @cached_property
    def list_associations(self) -> ListAssociationsResourceWithStreamingResponse:
        return ListAssociationsResourceWithStreamingResponse(self._events.list_associations)

    @cached_property
    def participations(self) -> ParticipationsResourceWithStreamingResponse:
        return ParticipationsResourceWithStreamingResponse(self._events.participations)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._events.settings)

    @cached_property
    def subscriber_state(self) -> SubscriberStateResourceWithStreamingResponse:
        return SubscriberStateResourceWithStreamingResponse(self._events.subscriber_state)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
        self.update = async_to_streamed_response_wrapper(
            events.update,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            events.delete,
        )
        self.delete_batch = async_to_custom_streamed_response_wrapper(
            events.delete_batch,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete_batch_by_external_event_id = async_to_custom_streamed_response_wrapper(
            events.delete_batch_by_external_event_id,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete_by_external_event_id = async_to_streamed_response_wrapper(
            events.delete_by_external_event_id,
        )
        self.get = async_to_streamed_response_wrapper(
            events.get,
        )
        self.get_by_external_event_id = async_to_streamed_response_wrapper(
            events.get_by_external_event_id,
        )
        self.search_by_external_event_id = async_to_streamed_response_wrapper(
            events.search_by_external_event_id,
        )
        self.search_identifiers_by_external_event_id = async_to_streamed_response_wrapper(
            events.search_identifiers_by_external_event_id,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            events.update_batch,
        )
        self.update_by_external_event_id = async_to_streamed_response_wrapper(
            events.update_by_external_event_id,
        )
        self.upsert_batch = async_to_streamed_response_wrapper(
            events.upsert_batch,
        )
        self.upsert_by_external_event_id = async_to_streamed_response_wrapper(
            events.upsert_by_external_event_id,
        )

    @cached_property
    def attendance(self) -> AsyncAttendanceResourceWithStreamingResponse:
        return AsyncAttendanceResourceWithStreamingResponse(self._events.attendance)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        return events.AsyncEventsResourceWithStreamingResponse(self._events.events)

    @cached_property
    def list_associations(self) -> AsyncListAssociationsResourceWithStreamingResponse:
        return AsyncListAssociationsResourceWithStreamingResponse(self._events.list_associations)

    @cached_property
    def participations(self) -> AsyncParticipationsResourceWithStreamingResponse:
        return AsyncParticipationsResourceWithStreamingResponse(self._events.participations)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._events.settings)

    @cached_property
    def subscriber_state(self) -> AsyncSubscriberStateResourceWithStreamingResponse:
        return AsyncSubscriberStateResourceWithStreamingResponse(self._events.subscriber_state)
