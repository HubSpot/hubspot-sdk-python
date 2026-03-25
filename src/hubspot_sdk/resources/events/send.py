# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.events import (
    send_send_event_params,
    send_send_event_batch_params,
    send_list_event_definitions_params,
    send_create_event_definition_params,
    send_update_event_definition_params,
    send_create_event_definition_property_params,
    send_update_event_definition_property_params,
)
from ...types.events.property import Property
from ...types.events.option_input_param import OptionInputParam
from ...types.events.external_behavioral_event_type_definition import ExternalBehavioralEventTypeDefinition
from ...types.events.behavioral_event_http_completion_request_param import BehavioralEventHTTPCompletionRequestParam
from ...types.events.external_behavioral_event_property_create_param import ExternalBehavioralEventPropertyCreateParam
from ...types.events.external_object_resolution_mapping_request_param import ExternalObjectResolutionMappingRequestParam

__all__ = ["SendResource", "AsyncSendResource"]


class SendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SendResourceWithStreamingResponse(self)

    def create_event_definition(
        self,
        *,
        include_default_properties: bool,
        label: str,
        property_definitions: Iterable[ExternalBehavioralEventPropertyCreateParam],
        custom_matching_id: ExternalObjectResolutionMappingRequestParam | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        primary_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBehavioralEventTypeDefinition:
        """
        Args:
          label: Human readable label for the event for display in HubSpot's UI.

          property_definitions: List of custom properties on event

          description: A description of the event that will be shown as help text in HubSpot.

          name: Internal event name, which must be used when referencing the event from the API.
              If a name is not supplied, one will be generated based on the label. The name
              does not include the `pe<PORTAL_ID>_` prefix used when sending event
              completions.

          primary_object: The object type to associate this event to. Can be one of `CONTACT`, `COMPANY`,
              `DEAL`, `TICKET`. If no value is supplied, will default to `CONTACT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/events/custom/2026-03/event-definitions",
            body=maybe_transform(
                {
                    "include_default_properties": include_default_properties,
                    "label": label,
                    "property_definitions": property_definitions,
                    "custom_matching_id": custom_matching_id,
                    "description": description,
                    "name": name,
                    "primary_object": primary_object,
                },
                send_create_event_definition_params.SendCreateEventDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    def create_event_definition_property(
        self,
        event_name: str,
        *,
        label: str,
        type: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        options: Iterable[OptionInputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """Args:
          label: Human readable label for the property.

        Used in HubSpot UI

          type: The data type of the property. Can be one of the following: [string, number,
              enumeration, datetime]

          description: A description of the property that will be shown as help text in HubSpot.

          name: Internal property name, which must be used when referencing the property from
              the API

          options: A list of available options for the property if it is an enumeration. NOTE: This
              field is only applicable for enumerated properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return self._post(
            path_template("/events/custom/2026-03/event-definitions/{event_name}/property", event_name=event_name),
            body=maybe_transform(
                {
                    "label": label,
                    "type": type,
                    "description": description,
                    "name": name,
                    "options": options,
                },
                send_create_event_definition_property_params.SendCreateEventDefinitionPropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    def delete_event_definition(
        self,
        event_name: str,
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
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/events/custom/2026-03/event-definitions/{event_name}", event_name=event_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_event_definition_property(
        self,
        property_name: str,
        *,
        event_name: str,
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
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/events/custom/2026-03/event-definitions/{event_name}/property/{property_name}",
                event_name=event_name,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_event_definition(
        self,
        event_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBehavioralEventTypeDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return self._get(
            path_template("/events/custom/2026-03/event-definitions/{event_name}", event_name=event_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    def list_event_definitions(
        self,
        *,
        after: str | Omit = omit,
        include_properties: bool | Omit = omit,
        limit: int | Omit = omit,
        search_string: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ExternalBehavioralEventTypeDefinition]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/custom/2026-03/event-definitions",
            page=SyncPage[ExternalBehavioralEventTypeDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_properties": include_properties,
                        "limit": limit,
                        "search_string": search_string,
                        "sort_order": sort_order,
                    },
                    send_list_event_definitions_params.SendListEventDefinitionsParams,
                ),
            ),
            model=ExternalBehavioralEventTypeDefinition,
        )

    def send_event(
        self,
        *,
        event_name: str,
        properties: Dict[str, str],
        email: str | Omit = omit,
        object_id: str | Omit = omit,
        occurred_at: Union[str, datetime] | Omit = omit,
        utk: str | Omit = omit,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Args:
          event_name: The event's fully qualified name.

        This value (formatted as `pe{HubID}_{name}`)
              can be retrieved through the
              [event definitions API](https://developers.hubspot.com/docs/reference/api/analytics-and-events/custom-events/custom-event-definitions#get-%2Fevents%2Fv3%2Fevent-definitions)
              or in
              [HubSpot's UI](https://knowledge.hubspot.com/reports/create-custom-behavioral-events-with-the-code-wizard#find-internal-name).

          properties: The event properties to update. Takes the format of key-value pairs (property
              internal name and property value). Learn more about
              [HubSpot's default event properties](https://developers.hubspot.com/docs/guides/api/analytics-and-events/custom-events/custom-event-definitions#hubspot-s-default-event-properties).

          email: The visitor's email address. Used for associating the event data with a CRM
              record.

          object_id: The ID of the record for which the event occurred (e.g., contact ID or visitor
              ID).

          occurred_at: The time when this event occurred. If this isn't set, the current time will be
              used.

          utk: The visitor's usertoken. Used for associating the event data with a CRM record.

          uuid: Include a universally unique identifier to assign a unique ID to the event
              occurrence. Can be useful for matching data between HubSpot and other external
              systems.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/events/custom/2026-03/send",
            body=maybe_transform(
                {
                    "event_name": event_name,
                    "properties": properties,
                    "email": email,
                    "object_id": object_id,
                    "occurred_at": occurred_at,
                    "utk": utk,
                    "uuid": uuid,
                },
                send_send_event_params.SendSendEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_event_batch(
        self,
        *,
        inputs: Iterable[BehavioralEventHTTPCompletionRequestParam],
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
        return self._post(
            "/events/custom/2026-03/send/batch",
            body=maybe_transform({"inputs": inputs}, send_send_event_batch_params.SendSendEventBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_event_definition(
        self,
        event_name: str,
        *,
        description: str | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBehavioralEventTypeDefinition:
        """
        Args:
          description: A description of the event that will be shown as help text in HubSpot.

          label: Human readable label for the event. Used in HubSpot UI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return self._patch(
            path_template("/events/custom/2026-03/event-definitions/{event_name}", event_name=event_name),
            body=maybe_transform(
                {
                    "description": description,
                    "label": label,
                },
                send_update_event_definition_params.SendUpdateEventDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    def update_event_definition_property(
        self,
        property_name: str,
        *,
        event_name: str,
        description: str | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Args:
          description: A description of the property that will be shown as help text in HubSpot.

          label: Human readable label for the property. Used in HubSpot UI

          options: A list of available options for the property if it is an enumeration. NOTE: This
              field is only applicable for enumerated properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return self._patch(
            path_template(
                "/events/custom/2026-03/event-definitions/{event_name}/property/{property_name}",
                event_name=event_name,
                property_name=property_name,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "label": label,
                    "options": options,
                },
                send_update_event_definition_property_params.SendUpdateEventDefinitionPropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )


class AsyncSendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSendResourceWithStreamingResponse(self)

    async def create_event_definition(
        self,
        *,
        include_default_properties: bool,
        label: str,
        property_definitions: Iterable[ExternalBehavioralEventPropertyCreateParam],
        custom_matching_id: ExternalObjectResolutionMappingRequestParam | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        primary_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBehavioralEventTypeDefinition:
        """
        Args:
          label: Human readable label for the event for display in HubSpot's UI.

          property_definitions: List of custom properties on event

          description: A description of the event that will be shown as help text in HubSpot.

          name: Internal event name, which must be used when referencing the event from the API.
              If a name is not supplied, one will be generated based on the label. The name
              does not include the `pe<PORTAL_ID>_` prefix used when sending event
              completions.

          primary_object: The object type to associate this event to. Can be one of `CONTACT`, `COMPANY`,
              `DEAL`, `TICKET`. If no value is supplied, will default to `CONTACT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/events/custom/2026-03/event-definitions",
            body=await async_maybe_transform(
                {
                    "include_default_properties": include_default_properties,
                    "label": label,
                    "property_definitions": property_definitions,
                    "custom_matching_id": custom_matching_id,
                    "description": description,
                    "name": name,
                    "primary_object": primary_object,
                },
                send_create_event_definition_params.SendCreateEventDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    async def create_event_definition_property(
        self,
        event_name: str,
        *,
        label: str,
        type: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        options: Iterable[OptionInputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """Args:
          label: Human readable label for the property.

        Used in HubSpot UI

          type: The data type of the property. Can be one of the following: [string, number,
              enumeration, datetime]

          description: A description of the property that will be shown as help text in HubSpot.

          name: Internal property name, which must be used when referencing the property from
              the API

          options: A list of available options for the property if it is an enumeration. NOTE: This
              field is only applicable for enumerated properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return await self._post(
            path_template("/events/custom/2026-03/event-definitions/{event_name}/property", event_name=event_name),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "type": type,
                    "description": description,
                    "name": name,
                    "options": options,
                },
                send_create_event_definition_property_params.SendCreateEventDefinitionPropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    async def delete_event_definition(
        self,
        event_name: str,
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
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/events/custom/2026-03/event-definitions/{event_name}", event_name=event_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_event_definition_property(
        self,
        property_name: str,
        *,
        event_name: str,
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
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/events/custom/2026-03/event-definitions/{event_name}/property/{property_name}",
                event_name=event_name,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_event_definition(
        self,
        event_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBehavioralEventTypeDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return await self._get(
            path_template("/events/custom/2026-03/event-definitions/{event_name}", event_name=event_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    def list_event_definitions(
        self,
        *,
        after: str | Omit = omit,
        include_properties: bool | Omit = omit,
        limit: int | Omit = omit,
        search_string: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExternalBehavioralEventTypeDefinition, AsyncPage[ExternalBehavioralEventTypeDefinition]]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/custom/2026-03/event-definitions",
            page=AsyncPage[ExternalBehavioralEventTypeDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_properties": include_properties,
                        "limit": limit,
                        "search_string": search_string,
                        "sort_order": sort_order,
                    },
                    send_list_event_definitions_params.SendListEventDefinitionsParams,
                ),
            ),
            model=ExternalBehavioralEventTypeDefinition,
        )

    async def send_event(
        self,
        *,
        event_name: str,
        properties: Dict[str, str],
        email: str | Omit = omit,
        object_id: str | Omit = omit,
        occurred_at: Union[str, datetime] | Omit = omit,
        utk: str | Omit = omit,
        uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Args:
          event_name: The event's fully qualified name.

        This value (formatted as `pe{HubID}_{name}`)
              can be retrieved through the
              [event definitions API](https://developers.hubspot.com/docs/reference/api/analytics-and-events/custom-events/custom-event-definitions#get-%2Fevents%2Fv3%2Fevent-definitions)
              or in
              [HubSpot's UI](https://knowledge.hubspot.com/reports/create-custom-behavioral-events-with-the-code-wizard#find-internal-name).

          properties: The event properties to update. Takes the format of key-value pairs (property
              internal name and property value). Learn more about
              [HubSpot's default event properties](https://developers.hubspot.com/docs/guides/api/analytics-and-events/custom-events/custom-event-definitions#hubspot-s-default-event-properties).

          email: The visitor's email address. Used for associating the event data with a CRM
              record.

          object_id: The ID of the record for which the event occurred (e.g., contact ID or visitor
              ID).

          occurred_at: The time when this event occurred. If this isn't set, the current time will be
              used.

          utk: The visitor's usertoken. Used for associating the event data with a CRM record.

          uuid: Include a universally unique identifier to assign a unique ID to the event
              occurrence. Can be useful for matching data between HubSpot and other external
              systems.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/events/custom/2026-03/send",
            body=await async_maybe_transform(
                {
                    "event_name": event_name,
                    "properties": properties,
                    "email": email,
                    "object_id": object_id,
                    "occurred_at": occurred_at,
                    "utk": utk,
                    "uuid": uuid,
                },
                send_send_event_params.SendSendEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_event_batch(
        self,
        *,
        inputs: Iterable[BehavioralEventHTTPCompletionRequestParam],
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
        return await self._post(
            "/events/custom/2026-03/send/batch",
            body=await async_maybe_transform({"inputs": inputs}, send_send_event_batch_params.SendSendEventBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_event_definition(
        self,
        event_name: str,
        *,
        description: str | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBehavioralEventTypeDefinition:
        """
        Args:
          description: A description of the event that will be shown as help text in HubSpot.

          label: Human readable label for the event. Used in HubSpot UI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return await self._patch(
            path_template("/events/custom/2026-03/event-definitions/{event_name}", event_name=event_name),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "label": label,
                },
                send_update_event_definition_params.SendUpdateEventDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    async def update_event_definition_property(
        self,
        property_name: str,
        *,
        event_name: str,
        description: str | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Args:
          description: A description of the property that will be shown as help text in HubSpot.

          label: Human readable label for the property. Used in HubSpot UI

          options: A list of available options for the property if it is an enumeration. NOTE: This
              field is only applicable for enumerated properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return await self._patch(
            path_template(
                "/events/custom/2026-03/event-definitions/{event_name}/property/{property_name}",
                event_name=event_name,
                property_name=property_name,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "label": label,
                    "options": options,
                },
                send_update_event_definition_property_params.SendUpdateEventDefinitionPropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )


class SendResourceWithRawResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.create_event_definition = to_raw_response_wrapper(
            send.create_event_definition,
        )
        self.create_event_definition_property = to_raw_response_wrapper(
            send.create_event_definition_property,
        )
        self.delete_event_definition = to_raw_response_wrapper(
            send.delete_event_definition,
        )
        self.delete_event_definition_property = to_raw_response_wrapper(
            send.delete_event_definition_property,
        )
        self.get_event_definition = to_raw_response_wrapper(
            send.get_event_definition,
        )
        self.list_event_definitions = to_raw_response_wrapper(
            send.list_event_definitions,
        )
        self.send_event = to_raw_response_wrapper(
            send.send_event,
        )
        self.send_event_batch = to_raw_response_wrapper(
            send.send_event_batch,
        )
        self.update_event_definition = to_raw_response_wrapper(
            send.update_event_definition,
        )
        self.update_event_definition_property = to_raw_response_wrapper(
            send.update_event_definition_property,
        )


class AsyncSendResourceWithRawResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.create_event_definition = async_to_raw_response_wrapper(
            send.create_event_definition,
        )
        self.create_event_definition_property = async_to_raw_response_wrapper(
            send.create_event_definition_property,
        )
        self.delete_event_definition = async_to_raw_response_wrapper(
            send.delete_event_definition,
        )
        self.delete_event_definition_property = async_to_raw_response_wrapper(
            send.delete_event_definition_property,
        )
        self.get_event_definition = async_to_raw_response_wrapper(
            send.get_event_definition,
        )
        self.list_event_definitions = async_to_raw_response_wrapper(
            send.list_event_definitions,
        )
        self.send_event = async_to_raw_response_wrapper(
            send.send_event,
        )
        self.send_event_batch = async_to_raw_response_wrapper(
            send.send_event_batch,
        )
        self.update_event_definition = async_to_raw_response_wrapper(
            send.update_event_definition,
        )
        self.update_event_definition_property = async_to_raw_response_wrapper(
            send.update_event_definition_property,
        )


class SendResourceWithStreamingResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.create_event_definition = to_streamed_response_wrapper(
            send.create_event_definition,
        )
        self.create_event_definition_property = to_streamed_response_wrapper(
            send.create_event_definition_property,
        )
        self.delete_event_definition = to_streamed_response_wrapper(
            send.delete_event_definition,
        )
        self.delete_event_definition_property = to_streamed_response_wrapper(
            send.delete_event_definition_property,
        )
        self.get_event_definition = to_streamed_response_wrapper(
            send.get_event_definition,
        )
        self.list_event_definitions = to_streamed_response_wrapper(
            send.list_event_definitions,
        )
        self.send_event = to_streamed_response_wrapper(
            send.send_event,
        )
        self.send_event_batch = to_streamed_response_wrapper(
            send.send_event_batch,
        )
        self.update_event_definition = to_streamed_response_wrapper(
            send.update_event_definition,
        )
        self.update_event_definition_property = to_streamed_response_wrapper(
            send.update_event_definition_property,
        )


class AsyncSendResourceWithStreamingResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.create_event_definition = async_to_streamed_response_wrapper(
            send.create_event_definition,
        )
        self.create_event_definition_property = async_to_streamed_response_wrapper(
            send.create_event_definition_property,
        )
        self.delete_event_definition = async_to_streamed_response_wrapper(
            send.delete_event_definition,
        )
        self.delete_event_definition_property = async_to_streamed_response_wrapper(
            send.delete_event_definition_property,
        )
        self.get_event_definition = async_to_streamed_response_wrapper(
            send.get_event_definition,
        )
        self.list_event_definitions = async_to_streamed_response_wrapper(
            send.list_event_definitions,
        )
        self.send_event = async_to_streamed_response_wrapper(
            send.send_event,
        )
        self.send_event_batch = async_to_streamed_response_wrapper(
            send.send_event_batch,
        )
        self.update_event_definition = async_to_streamed_response_wrapper(
            send.update_event_definition,
        )
        self.update_event_definition_property = async_to_streamed_response_wrapper(
            send.update_event_definition_property,
        )
