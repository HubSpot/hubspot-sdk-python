# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.events import (
    event_definition_list_params,
    event_definition_create_params,
    event_definition_update_params,
    event_definition_create_property_params,
    event_definition_update_property_params,
)
from ...types.shared.property import Property
from ...types.shared_params.option_input import OptionInput
from ...types.events.event_definition_get_response import EventDefinitionGetResponse
from ...types.events.event_definition_list_response import EventDefinitionListResponse
from ...types.events.event_definition_create_response import EventDefinitionCreateResponse
from ...types.events.event_definition_update_response import EventDefinitionUpdateResponse

__all__ = ["EventDefinitionsResource", "AsyncEventDefinitionsResource"]


class EventDefinitionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EventDefinitionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        label: str,
        property_definitions: Iterable[event_definition_create_params.PropertyDefinition],
        description: str | Omit = omit,
        name: str | Omit = omit,
        primary_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDefinitionCreateResponse:
        """
        Create a custom event definition.

        Args:
          label: Human readable label for the event. Used in HubSpot UI

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
            "/events/v3/event-definitions",
            body=maybe_transform(
                {
                    "label": label,
                    "property_definitions": property_definitions,
                    "description": description,
                    "name": name,
                    "primary_object": primary_object,
                },
                event_definition_create_params.EventDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDefinitionCreateResponse,
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
    ) -> EventDefinitionUpdateResponse:
        """
        Update a specific custom event definition by name.

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
            f"/events/v3/event-definitions/{event_name}",
            body=maybe_transform(
                {
                    "description": description,
                    "label": label,
                },
                event_definition_update_params.EventDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDefinitionUpdateResponse,
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
    ) -> SyncPage[EventDefinitionListResponse]:
        """
        Retrieve existing custom event definitions.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          search_string: Characters in the event name that the user is searching for. This search is a
              naive “contains” search, no fuzzy matching is done.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/v3/event-definitions",
            page=SyncPage[EventDefinitionListResponse],
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
                    event_definition_list_params.EventDefinitionListParams,
                ),
            ),
            model=EventDefinitionListResponse,
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
        Delete a custom event definition by name.

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
            f"/events/v3/event-definitions/{event_name}",
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
        """
        Create a new property for an existing event definition.

        Args:
          label: Human readable label for the property. Used in HubSpot UI

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
            f"/events/v3/event-definitions/{event_name}/property",
            body=maybe_transform(
                {
                    "label": label,
                    "type": type,
                    "description": description,
                    "name": name,
                    "options": options,
                },
                event_definition_create_property_params.EventDefinitionCreatePropertyParams,
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
        Delete an existing property from a custom event definition.

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
            f"/events/v3/event-definitions/{event_name}/property/{property_name}",
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
    ) -> EventDefinitionGetResponse:
        """
        Fetch a single custom event definition by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return self._get(
            f"/events/v3/event-definitions/{event_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDefinitionGetResponse,
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
        Update an existing property in a custom event definition.

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
            f"/events/v3/event-definitions/{event_name}/property/{property_name}",
            body=maybe_transform(
                {
                    "description": description,
                    "label": label,
                    "options": options,
                },
                event_definition_update_property_params.EventDefinitionUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )


class AsyncEventDefinitionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEventDefinitionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        label: str,
        property_definitions: Iterable[event_definition_create_params.PropertyDefinition],
        description: str | Omit = omit,
        name: str | Omit = omit,
        primary_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDefinitionCreateResponse:
        """
        Create a custom event definition.

        Args:
          label: Human readable label for the event. Used in HubSpot UI

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
            "/events/v3/event-definitions",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "property_definitions": property_definitions,
                    "description": description,
                    "name": name,
                    "primary_object": primary_object,
                },
                event_definition_create_params.EventDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDefinitionCreateResponse,
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
    ) -> EventDefinitionUpdateResponse:
        """
        Update a specific custom event definition by name.

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
            f"/events/v3/event-definitions/{event_name}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "label": label,
                },
                event_definition_update_params.EventDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDefinitionUpdateResponse,
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
    ) -> AsyncPaginator[EventDefinitionListResponse, AsyncPage[EventDefinitionListResponse]]:
        """
        Retrieve existing custom event definitions.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          search_string: Characters in the event name that the user is searching for. This search is a
              naive “contains” search, no fuzzy matching is done.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/v3/event-definitions",
            page=AsyncPage[EventDefinitionListResponse],
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
                    event_definition_list_params.EventDefinitionListParams,
                ),
            ),
            model=EventDefinitionListResponse,
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
        Delete a custom event definition by name.

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
            f"/events/v3/event-definitions/{event_name}",
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
        """
        Create a new property for an existing event definition.

        Args:
          label: Human readable label for the property. Used in HubSpot UI

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
            f"/events/v3/event-definitions/{event_name}/property",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "type": type,
                    "description": description,
                    "name": name,
                    "options": options,
                },
                event_definition_create_property_params.EventDefinitionCreatePropertyParams,
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
        Delete an existing property from a custom event definition.

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
            f"/events/v3/event-definitions/{event_name}/property/{property_name}",
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
    ) -> EventDefinitionGetResponse:
        """
        Fetch a single custom event definition by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_name:
            raise ValueError(f"Expected a non-empty value for `event_name` but received {event_name!r}")
        return await self._get(
            f"/events/v3/event-definitions/{event_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDefinitionGetResponse,
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
        Update an existing property in a custom event definition.

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
            f"/events/v3/event-definitions/{event_name}/property/{property_name}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "label": label,
                    "options": options,
                },
                event_definition_update_property_params.EventDefinitionUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )


class EventDefinitionsResourceWithRawResponse:
    def __init__(self, event_definitions: EventDefinitionsResource) -> None:
        self._event_definitions = event_definitions

        self.create = to_raw_response_wrapper(
            event_definitions.create,
        )
        self.update = to_raw_response_wrapper(
            event_definitions.update,
        )
        self.list = to_raw_response_wrapper(
            event_definitions.list,
        )
        self.delete = to_raw_response_wrapper(
            event_definitions.delete,
        )
        self.create_property = to_raw_response_wrapper(
            event_definitions.create_property,
        )
        self.delete_property = to_raw_response_wrapper(
            event_definitions.delete_property,
        )
        self.get = to_raw_response_wrapper(
            event_definitions.get,
        )
        self.update_property = to_raw_response_wrapper(
            event_definitions.update_property,
        )


class AsyncEventDefinitionsResourceWithRawResponse:
    def __init__(self, event_definitions: AsyncEventDefinitionsResource) -> None:
        self._event_definitions = event_definitions

        self.create = async_to_raw_response_wrapper(
            event_definitions.create,
        )
        self.update = async_to_raw_response_wrapper(
            event_definitions.update,
        )
        self.list = async_to_raw_response_wrapper(
            event_definitions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            event_definitions.delete,
        )
        self.create_property = async_to_raw_response_wrapper(
            event_definitions.create_property,
        )
        self.delete_property = async_to_raw_response_wrapper(
            event_definitions.delete_property,
        )
        self.get = async_to_raw_response_wrapper(
            event_definitions.get,
        )
        self.update_property = async_to_raw_response_wrapper(
            event_definitions.update_property,
        )


class EventDefinitionsResourceWithStreamingResponse:
    def __init__(self, event_definitions: EventDefinitionsResource) -> None:
        self._event_definitions = event_definitions

        self.create = to_streamed_response_wrapper(
            event_definitions.create,
        )
        self.update = to_streamed_response_wrapper(
            event_definitions.update,
        )
        self.list = to_streamed_response_wrapper(
            event_definitions.list,
        )
        self.delete = to_streamed_response_wrapper(
            event_definitions.delete,
        )
        self.create_property = to_streamed_response_wrapper(
            event_definitions.create_property,
        )
        self.delete_property = to_streamed_response_wrapper(
            event_definitions.delete_property,
        )
        self.get = to_streamed_response_wrapper(
            event_definitions.get,
        )
        self.update_property = to_streamed_response_wrapper(
            event_definitions.update_property,
        )


class AsyncEventDefinitionsResourceWithStreamingResponse:
    def __init__(self, event_definitions: AsyncEventDefinitionsResource) -> None:
        self._event_definitions = event_definitions

        self.create = async_to_streamed_response_wrapper(
            event_definitions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            event_definitions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            event_definitions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            event_definitions.delete,
        )
        self.create_property = async_to_streamed_response_wrapper(
            event_definitions.create_property,
        )
        self.delete_property = async_to_streamed_response_wrapper(
            event_definitions.delete_property,
        )
        self.get = async_to_streamed_response_wrapper(
            event_definitions.get,
        )
        self.update_property = async_to_streamed_response_wrapper(
            event_definitions.update_property,
        )
