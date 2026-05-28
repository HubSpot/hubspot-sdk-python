# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.crm import property_get_params, property_list_params, property_create_params, property_update_params
from ...._base_client import make_request_options
from ....types.shared.property import Property
from ....types.shared_params.option_input import OptionInput
from ....types.crm.collection_response_property_no_paging import CollectionResponsePropertyNoPaging

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return PropertiesResourceWithStreamingResponse(self)

    def create(
        self,
        object_type: str,
        *,
        field_type: Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ],
        group_name: str,
        label: str,
        name: str,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"],
        calculation_formula: str | Omit = omit,
        currency_property_name: str | Omit = omit,
        data_sensitivity: Literal["highly_sensitive", "non_sensitive", "sensitive"] | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        external_options: bool | Omit = omit,
        form_field: bool | Omit = omit,
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        number_display_hint: Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"]
        | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        referenced_object_type: str | Omit = omit,
        show_currency_symbol: bool | Omit = omit,
        text_display_hint: Literal[
            "domain_name",
            "email",
            "ip_address",
            "multi_line",
            "phone_number",
            "physical_address",
            "postal_code",
            "unformatted_single_line",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Create and return a copy of a new property for the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            path_template("/crm/properties/2026-03/{object_type}", object_type=object_type),
            body=maybe_transform(
                {
                    "field_type": field_type,
                    "group_name": group_name,
                    "label": label,
                    "name": name,
                    "type": type,
                    "calculation_formula": calculation_formula,
                    "currency_property_name": currency_property_name,
                    "data_sensitivity": data_sensitivity,
                    "description": description,
                    "display_order": display_order,
                    "external_options": external_options,
                    "form_field": form_field,
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "number_display_hint": number_display_hint,
                    "options": options,
                    "referenced_object_type": referenced_object_type,
                    "show_currency_symbol": show_currency_symbol,
                    "text_display_hint": text_display_hint,
                },
                property_create_params.PropertyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    def update(
        self,
        property_name: str,
        *,
        object_type: str,
        calculation_formula: str | Omit = omit,
        currency_property_name: str | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        field_type: Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ]
        | Omit = omit,
        form_field: bool | Omit = omit,
        group_name: str | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        number_display_hint: Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"]
        | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        show_currency_symbol: bool | Omit = omit,
        text_display_hint: Literal[
            "domain_name",
            "email",
            "ip_address",
            "multi_line",
            "phone_number",
            "physical_address",
            "postal_code",
            "unformatted_single_line",
        ]
        | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """Perform a partial update of a property identified by { propertyName }.

        Provided
        fields will be overwritten.

        Args:
          calculation_formula: Represents a formula that is used to compute a calculated property.

          description: A description of the property that will be shown as help text in HubSpot.

          display_order: Properties are displayed in order starting with the lowest positive integer
              value. Values of -1 will cause the Property to be displayed after any positive
              values.

          field_type: Controls how the property appears in HubSpot.

          form_field: Whether or not the property can be used in a HubSpot form.

          group_name: The name of the property group the property belongs to.

          hidden: If true, the property won't be visible and can't be used in HubSpot.

          label: A human-readable property label that will be shown in HubSpot.

          options: A list of valid options for the property.

          type: The data type of the property.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return self._patch(
            path_template(
                "/crm/properties/2026-03/{object_type}/{property_name}",
                object_type=object_type,
                property_name=property_name,
            ),
            body=maybe_transform(
                {
                    "calculation_formula": calculation_formula,
                    "currency_property_name": currency_property_name,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "form_field": form_field,
                    "group_name": group_name,
                    "hidden": hidden,
                    "label": label,
                    "number_display_hint": number_display_hint,
                    "options": options,
                    "show_currency_symbol": show_currency_symbol,
                    "text_display_hint": text_display_hint,
                    "type": type,
                },
                property_update_params.PropertyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    def list(
        self,
        object_type: str,
        *,
        archived: bool | Omit = omit,
        data_sensitivity: Literal["highly_sensitive", "non_sensitive", "sensitive"] | Omit = omit,
        locale: str | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyNoPaging:
        """
        Read all existing properties for the specified object type and HubSpot account.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            path_template("/crm/properties/2026-03/{object_type}", object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "data_sensitivity": data_sensitivity,
                        "locale": locale,
                        "properties": properties,
                    },
                    property_list_params.PropertyListParams,
                ),
            ),
            cast_to=CollectionResponsePropertyNoPaging,
        )

    def delete(
        self,
        property_name: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move a property identified by {propertyName} to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/crm/properties/2026-03/{object_type}/{property_name}",
                object_type=object_type,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        property_name: str,
        *,
        object_type: str,
        archived: bool | Omit = omit,
        data_sensitivity: Literal["highly_sensitive", "non_sensitive", "sensitive"] | Omit = omit,
        locale: str | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Read a property identified by {propertyName}.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return self._get(
            path_template(
                "/crm/properties/2026-03/{object_type}/{property_name}",
                object_type=object_type,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "data_sensitivity": data_sensitivity,
                        "locale": locale,
                        "properties": properties,
                    },
                    property_get_params.PropertyGetParams,
                ),
            ),
            cast_to=Property,
        )


class AsyncPropertiesResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPropertiesResourceWithStreamingResponse(self)

    async def create(
        self,
        object_type: str,
        *,
        field_type: Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ],
        group_name: str,
        label: str,
        name: str,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"],
        calculation_formula: str | Omit = omit,
        currency_property_name: str | Omit = omit,
        data_sensitivity: Literal["highly_sensitive", "non_sensitive", "sensitive"] | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        external_options: bool | Omit = omit,
        form_field: bool | Omit = omit,
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        number_display_hint: Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"]
        | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        referenced_object_type: str | Omit = omit,
        show_currency_symbol: bool | Omit = omit,
        text_display_hint: Literal[
            "domain_name",
            "email",
            "ip_address",
            "multi_line",
            "phone_number",
            "physical_address",
            "postal_code",
            "unformatted_single_line",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Create and return a copy of a new property for the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            path_template("/crm/properties/2026-03/{object_type}", object_type=object_type),
            body=await async_maybe_transform(
                {
                    "field_type": field_type,
                    "group_name": group_name,
                    "label": label,
                    "name": name,
                    "type": type,
                    "calculation_formula": calculation_formula,
                    "currency_property_name": currency_property_name,
                    "data_sensitivity": data_sensitivity,
                    "description": description,
                    "display_order": display_order,
                    "external_options": external_options,
                    "form_field": form_field,
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "number_display_hint": number_display_hint,
                    "options": options,
                    "referenced_object_type": referenced_object_type,
                    "show_currency_symbol": show_currency_symbol,
                    "text_display_hint": text_display_hint,
                },
                property_create_params.PropertyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    async def update(
        self,
        property_name: str,
        *,
        object_type: str,
        calculation_formula: str | Omit = omit,
        currency_property_name: str | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        field_type: Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ]
        | Omit = omit,
        form_field: bool | Omit = omit,
        group_name: str | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        number_display_hint: Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"]
        | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        show_currency_symbol: bool | Omit = omit,
        text_display_hint: Literal[
            "domain_name",
            "email",
            "ip_address",
            "multi_line",
            "phone_number",
            "physical_address",
            "postal_code",
            "unformatted_single_line",
        ]
        | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """Perform a partial update of a property identified by { propertyName }.

        Provided
        fields will be overwritten.

        Args:
          calculation_formula: Represents a formula that is used to compute a calculated property.

          description: A description of the property that will be shown as help text in HubSpot.

          display_order: Properties are displayed in order starting with the lowest positive integer
              value. Values of -1 will cause the Property to be displayed after any positive
              values.

          field_type: Controls how the property appears in HubSpot.

          form_field: Whether or not the property can be used in a HubSpot form.

          group_name: The name of the property group the property belongs to.

          hidden: If true, the property won't be visible and can't be used in HubSpot.

          label: A human-readable property label that will be shown in HubSpot.

          options: A list of valid options for the property.

          type: The data type of the property.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return await self._patch(
            path_template(
                "/crm/properties/2026-03/{object_type}/{property_name}",
                object_type=object_type,
                property_name=property_name,
            ),
            body=await async_maybe_transform(
                {
                    "calculation_formula": calculation_formula,
                    "currency_property_name": currency_property_name,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "form_field": form_field,
                    "group_name": group_name,
                    "hidden": hidden,
                    "label": label,
                    "number_display_hint": number_display_hint,
                    "options": options,
                    "show_currency_symbol": show_currency_symbol,
                    "text_display_hint": text_display_hint,
                    "type": type,
                },
                property_update_params.PropertyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    async def list(
        self,
        object_type: str,
        *,
        archived: bool | Omit = omit,
        data_sensitivity: Literal["highly_sensitive", "non_sensitive", "sensitive"] | Omit = omit,
        locale: str | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyNoPaging:
        """
        Read all existing properties for the specified object type and HubSpot account.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            path_template("/crm/properties/2026-03/{object_type}", object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "data_sensitivity": data_sensitivity,
                        "locale": locale,
                        "properties": properties,
                    },
                    property_list_params.PropertyListParams,
                ),
            ),
            cast_to=CollectionResponsePropertyNoPaging,
        )

    async def delete(
        self,
        property_name: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move a property identified by {propertyName} to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/crm/properties/2026-03/{object_type}/{property_name}",
                object_type=object_type,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        property_name: str,
        *,
        object_type: str,
        archived: bool | Omit = omit,
        data_sensitivity: Literal["highly_sensitive", "non_sensitive", "sensitive"] | Omit = omit,
        locale: str | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Read a property identified by {propertyName}.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return await self._get(
            path_template(
                "/crm/properties/2026-03/{object_type}/{property_name}",
                object_type=object_type,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "data_sensitivity": data_sensitivity,
                        "locale": locale,
                        "properties": properties,
                    },
                    property_get_params.PropertyGetParams,
                ),
            ),
            cast_to=Property,
        )


class PropertiesResourceWithRawResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.create = to_raw_response_wrapper(
            properties.create,
        )
        self.update = to_raw_response_wrapper(
            properties.update,
        )
        self.list = to_raw_response_wrapper(
            properties.list,
        )
        self.delete = to_raw_response_wrapper(
            properties.delete,
        )
        self.get = to_raw_response_wrapper(
            properties.get,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._properties.batch)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._properties.groups)


class AsyncPropertiesResourceWithRawResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.create = async_to_raw_response_wrapper(
            properties.create,
        )
        self.update = async_to_raw_response_wrapper(
            properties.update,
        )
        self.list = async_to_raw_response_wrapper(
            properties.list,
        )
        self.delete = async_to_raw_response_wrapper(
            properties.delete,
        )
        self.get = async_to_raw_response_wrapper(
            properties.get,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._properties.batch)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._properties.groups)


class PropertiesResourceWithStreamingResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.create = to_streamed_response_wrapper(
            properties.create,
        )
        self.update = to_streamed_response_wrapper(
            properties.update,
        )
        self.list = to_streamed_response_wrapper(
            properties.list,
        )
        self.delete = to_streamed_response_wrapper(
            properties.delete,
        )
        self.get = to_streamed_response_wrapper(
            properties.get,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._properties.batch)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._properties.groups)


class AsyncPropertiesResourceWithStreamingResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.create = async_to_streamed_response_wrapper(
            properties.create,
        )
        self.update = async_to_streamed_response_wrapper(
            properties.update,
        )
        self.list = async_to_streamed_response_wrapper(
            properties.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            properties.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            properties.get,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._properties.batch)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._properties.groups)
