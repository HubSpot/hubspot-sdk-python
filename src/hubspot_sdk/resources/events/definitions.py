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
    definition_list_params,
    definition_send_params,
    definition_create_params,
    definition_update_params,
    definition_send_batch_params,
    definition_create_property_params,
    definition_update_property_params,
)
from ...types.shared.property import Property
from ...types.shared_params.option_input import OptionInput
from ...types.events.external_behavioral_event_type_definition import ExternalBehavioralEventTypeDefinition
from ...types.events.behavioral_event_http_completion_request_param import BehavioralEventHTTPCompletionRequestParam
from ...types.events.external_behavioral_event_property_create_param import ExternalBehavioralEventPropertyCreateParam
from ...types.events.external_object_resolution_mapping_request_param import ExternalObjectResolutionMappingRequestParam

__all__ = ["DefinitionsResource", "AsyncDefinitionsResource"]


class DefinitionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return DefinitionsResourceWithStreamingResponse(self)

    def create(
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
        """Args:
          label: Human readable label for the event.

        Used in HubSpot UI

          property_definitions: List of custom properties on event

          description: A description of the event that will be shown as help text in HubSpot.

          name: Internal event name, which must be used when referencing the event from this
              event definitions API. If a name is not supplied, one will be generated based on
              the label. The `name` value will also be used to automatically generate a
              `fullyQualifiedName` for the event definition, which you'll use when sending
              event completions to this event.

          primary_object: The object type to associate this event to. Can be one of CONTACT, COMPANY,
              DEAL, TICKET. If no primaryObject is supplied, we will default to associating
              the event to CONTACT objects.

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
                definition_create_params.DefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    def update(
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
                definition_update_params.DefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    def list(
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
                    definition_list_params.DefinitionListParams,
                ),
            ),
            model=ExternalBehavioralEventTypeDefinition,
        )

    def delete(
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

    def create_property(
        self,
        event_name: str,
        *,
        label: str,
        type: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
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
                definition_create_property_params.DefinitionCreatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    def delete_property(
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

    def get(
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

    def send(
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
        """
        Args:
          event_name: Internal name of the event-type to trigger

          properties: Map of properties for the event in the format property internal name - property
              value

          email: Email of visitor

          object_id: The object id that this event occurred on. Could be a contact id or a visitor
              id.

          occurred_at: The time when this event occurred (if any). If this isn't set, the current time
              will be used

          utk: User token

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
                definition_send_params.DefinitionSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_batch(
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
            body=maybe_transform({"inputs": inputs}, definition_send_batch_params.DefinitionSendBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_property(
        self,
        property_name: str,
        *,
        event_name: str,
        description: str | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
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
                definition_update_property_params.DefinitionUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )


class AsyncDefinitionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDefinitionsResourceWithStreamingResponse(self)

    async def create(
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
        """Args:
          label: Human readable label for the event.

        Used in HubSpot UI

          property_definitions: List of custom properties on event

          description: A description of the event that will be shown as help text in HubSpot.

          name: Internal event name, which must be used when referencing the event from this
              event definitions API. If a name is not supplied, one will be generated based on
              the label. The `name` value will also be used to automatically generate a
              `fullyQualifiedName` for the event definition, which you'll use when sending
              event completions to this event.

          primary_object: The object type to associate this event to. Can be one of CONTACT, COMPANY,
              DEAL, TICKET. If no primaryObject is supplied, we will default to associating
              the event to CONTACT objects.

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
                definition_create_params.DefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    async def update(
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
                definition_update_params.DefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBehavioralEventTypeDefinition,
        )

    def list(
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
                    definition_list_params.DefinitionListParams,
                ),
            ),
            model=ExternalBehavioralEventTypeDefinition,
        )

    async def delete(
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

    async def create_property(
        self,
        event_name: str,
        *,
        label: str,
        type: str,
        description: str | Omit = omit,
        name: str | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
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
                definition_create_property_params.DefinitionCreatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    async def delete_property(
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

    async def get(
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

    async def send(
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
        """
        Args:
          event_name: Internal name of the event-type to trigger

          properties: Map of properties for the event in the format property internal name - property
              value

          email: Email of visitor

          object_id: The object id that this event occurred on. Could be a contact id or a visitor
              id.

          occurred_at: The time when this event occurred (if any). If this isn't set, the current time
              will be used

          utk: User token

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
                definition_send_params.DefinitionSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_batch(
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
            body=await async_maybe_transform(
                {"inputs": inputs}, definition_send_batch_params.DefinitionSendBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_property(
        self,
        property_name: str,
        *,
        event_name: str,
        description: str | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
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
                definition_update_property_params.DefinitionUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )


class DefinitionsResourceWithRawResponse:
    def __init__(self, definitions: DefinitionsResource) -> None:
        self._definitions = definitions

        self.create = to_raw_response_wrapper(
            definitions.create,
        )
        self.update = to_raw_response_wrapper(
            definitions.update,
        )
        self.list = to_raw_response_wrapper(
            definitions.list,
        )
        self.delete = to_raw_response_wrapper(
            definitions.delete,
        )
        self.create_property = to_raw_response_wrapper(
            definitions.create_property,
        )
        self.delete_property = to_raw_response_wrapper(
            definitions.delete_property,
        )
        self.get = to_raw_response_wrapper(
            definitions.get,
        )
        self.send = to_raw_response_wrapper(
            definitions.send,
        )
        self.send_batch = to_raw_response_wrapper(
            definitions.send_batch,
        )
        self.update_property = to_raw_response_wrapper(
            definitions.update_property,
        )


class AsyncDefinitionsResourceWithRawResponse:
    def __init__(self, definitions: AsyncDefinitionsResource) -> None:
        self._definitions = definitions

        self.create = async_to_raw_response_wrapper(
            definitions.create,
        )
        self.update = async_to_raw_response_wrapper(
            definitions.update,
        )
        self.list = async_to_raw_response_wrapper(
            definitions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            definitions.delete,
        )
        self.create_property = async_to_raw_response_wrapper(
            definitions.create_property,
        )
        self.delete_property = async_to_raw_response_wrapper(
            definitions.delete_property,
        )
        self.get = async_to_raw_response_wrapper(
            definitions.get,
        )
        self.send = async_to_raw_response_wrapper(
            definitions.send,
        )
        self.send_batch = async_to_raw_response_wrapper(
            definitions.send_batch,
        )
        self.update_property = async_to_raw_response_wrapper(
            definitions.update_property,
        )


class DefinitionsResourceWithStreamingResponse:
    def __init__(self, definitions: DefinitionsResource) -> None:
        self._definitions = definitions

        self.create = to_streamed_response_wrapper(
            definitions.create,
        )
        self.update = to_streamed_response_wrapper(
            definitions.update,
        )
        self.list = to_streamed_response_wrapper(
            definitions.list,
        )
        self.delete = to_streamed_response_wrapper(
            definitions.delete,
        )
        self.create_property = to_streamed_response_wrapper(
            definitions.create_property,
        )
        self.delete_property = to_streamed_response_wrapper(
            definitions.delete_property,
        )
        self.get = to_streamed_response_wrapper(
            definitions.get,
        )
        self.send = to_streamed_response_wrapper(
            definitions.send,
        )
        self.send_batch = to_streamed_response_wrapper(
            definitions.send_batch,
        )
        self.update_property = to_streamed_response_wrapper(
            definitions.update_property,
        )


class AsyncDefinitionsResourceWithStreamingResponse:
    def __init__(self, definitions: AsyncDefinitionsResource) -> None:
        self._definitions = definitions

        self.create = async_to_streamed_response_wrapper(
            definitions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            definitions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            definitions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            definitions.delete,
        )
        self.create_property = async_to_streamed_response_wrapper(
            definitions.create_property,
        )
        self.delete_property = async_to_streamed_response_wrapper(
            definitions.delete_property,
        )
        self.get = async_to_streamed_response_wrapper(
            definitions.get,
        )
        self.send = async_to_streamed_response_wrapper(
            definitions.send,
        )
        self.send_batch = async_to_streamed_response_wrapper(
            definitions.send_batch,
        )
        self.update_property = async_to_streamed_response_wrapper(
            definitions.update_property,
        )
