# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

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
from ...._base_client import make_request_options
from ....types.shared.property import Property
from ....types.cms.media_bridge import (
    property_get_params,
    property_list_params,
    property_create_params,
    property_update_params,
    property_get_batch_params,
    property_create_batch_params,
    property_delete_batch_params,
)
from ....types.shared_params.option_input import OptionInput
from ....types.shared_params.property_name import PropertyName
from ....types.shared_params.property_create import PropertyCreate
from ....types.shared.batch_response_property import BatchResponseProperty
from ....types.cms.collection_response_property_no_paging import CollectionResponsePropertyNoPaging

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PropertiesResourceWithStreamingResponse(self)

    def create(
        self,
        object_type: str,
        *,
        app_id: int,
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
        data_sensitivity: Literal["non_sensitive", "sensitive", "highly_sensitive"] | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        external_options: bool | Omit = omit,
        form_field: bool | Omit = omit,
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        referenced_object_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Create a new property for the specified media type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}",
            body=maybe_transform(
                {
                    "field_type": field_type,
                    "group_name": group_name,
                    "label": label,
                    "name": name,
                    "type": type,
                    "calculation_formula": calculation_formula,
                    "data_sensitivity": data_sensitivity,
                    "description": description,
                    "display_order": display_order,
                    "external_options": external_options,
                    "form_field": form_field,
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "options": options,
                    "referenced_object_type": referenced_object_type,
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
        app_id: int,
        object_type: str,
        calculation_formula: str | Omit = omit,
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
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Update an existing property for an object type.

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
        return self._patch(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/{property_name}",
            body=maybe_transform(
                {
                    "calculation_formula": calculation_formula,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "form_field": form_field,
                    "group_name": group_name,
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "label": label,
                    "options": options,
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
        app_id: int,
        archived: bool | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyNoPaging:
        """
        Get the existing properties defined for a media object type.

        Args:
          archived: Whether to return only results that have been archived.

          properties: Filter the response to the specified properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            f"/media-bridge/v1/{app_id}/properties/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
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
        app_id: int,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing property for an object type.

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
            f"/media-bridge/v1/{app_id}/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_batch(
        self,
        object_type: str,
        *,
        app_id: int,
        inputs: Iterable[PropertyCreate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseProperty:
        """
        Create a batch of properties of the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/batch/create",
            body=maybe_transform({"inputs": inputs}, property_create_batch_params.PropertyCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseProperty,
        )

    def delete_batch(
        self,
        object_type: str,
        *,
        app_id: int,
        inputs: Iterable[PropertyName],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a batch of existing properties for the specified types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/batch/archive",
            body=maybe_transform({"inputs": inputs}, property_delete_batch_params.PropertyDeleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        property_name: str,
        *,
        app_id: int,
        object_type: str,
        archived: bool | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Get the details for an existing property by name.

        Args:
          archived: Whether to return only results that have been archived.

          properties: Limit the response to only include the specified properties.

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
            f"/media-bridge/v1/{app_id}/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "properties": properties,
                    },
                    property_get_params.PropertyGetParams,
                ),
            ),
            cast_to=Property,
        )

    def get_batch(
        self,
        object_type: str,
        *,
        app_id: int,
        archived: bool,
        data_sensitivity: Literal["non_sensitive", "sensitive", "highly_sensitive"],
        inputs: Iterable[PropertyName],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseProperty:
        """
        Get the details for a batch of properties for a specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/batch/read",
            body=maybe_transform(
                {
                    "archived": archived,
                    "data_sensitivity": data_sensitivity,
                    "inputs": inputs,
                },
                property_get_batch_params.PropertyGetBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseProperty,
        )


class AsyncPropertiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPropertiesResourceWithStreamingResponse(self)

    async def create(
        self,
        object_type: str,
        *,
        app_id: int,
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
        data_sensitivity: Literal["non_sensitive", "sensitive", "highly_sensitive"] | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        external_options: bool | Omit = omit,
        form_field: bool | Omit = omit,
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        referenced_object_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Create a new property for the specified media type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}",
            body=await async_maybe_transform(
                {
                    "field_type": field_type,
                    "group_name": group_name,
                    "label": label,
                    "name": name,
                    "type": type,
                    "calculation_formula": calculation_formula,
                    "data_sensitivity": data_sensitivity,
                    "description": description,
                    "display_order": display_order,
                    "external_options": external_options,
                    "form_field": form_field,
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "options": options,
                    "referenced_object_type": referenced_object_type,
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
        app_id: int,
        object_type: str,
        calculation_formula: str | Omit = omit,
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
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Update an existing property for an object type.

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
        return await self._patch(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/{property_name}",
            body=await async_maybe_transform(
                {
                    "calculation_formula": calculation_formula,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "form_field": form_field,
                    "group_name": group_name,
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "label": label,
                    "options": options,
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
        app_id: int,
        archived: bool | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyNoPaging:
        """
        Get the existing properties defined for a media object type.

        Args:
          archived: Whether to return only results that have been archived.

          properties: Filter the response to the specified properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            f"/media-bridge/v1/{app_id}/properties/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
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
        app_id: int,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing property for an object type.

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
            f"/media-bridge/v1/{app_id}/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_batch(
        self,
        object_type: str,
        *,
        app_id: int,
        inputs: Iterable[PropertyCreate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseProperty:
        """
        Create a batch of properties of the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/batch/create",
            body=await async_maybe_transform(
                {"inputs": inputs}, property_create_batch_params.PropertyCreateBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseProperty,
        )

    async def delete_batch(
        self,
        object_type: str,
        *,
        app_id: int,
        inputs: Iterable[PropertyName],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a batch of existing properties for the specified types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/batch/archive",
            body=await async_maybe_transform(
                {"inputs": inputs}, property_delete_batch_params.PropertyDeleteBatchParams
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
        app_id: int,
        object_type: str,
        archived: bool | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Get the details for an existing property by name.

        Args:
          archived: Whether to return only results that have been archived.

          properties: Limit the response to only include the specified properties.

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
            f"/media-bridge/v1/{app_id}/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "properties": properties,
                    },
                    property_get_params.PropertyGetParams,
                ),
            ),
            cast_to=Property,
        )

    async def get_batch(
        self,
        object_type: str,
        *,
        app_id: int,
        archived: bool,
        data_sensitivity: Literal["non_sensitive", "sensitive", "highly_sensitive"],
        inputs: Iterable[PropertyName],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseProperty:
        """
        Get the details for a batch of properties for a specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/media-bridge/v1/{app_id}/properties/{object_type}/batch/read",
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "data_sensitivity": data_sensitivity,
                    "inputs": inputs,
                },
                property_get_batch_params.PropertyGetBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseProperty,
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
        self.create_batch = to_raw_response_wrapper(
            properties.create_batch,
        )
        self.delete_batch = to_raw_response_wrapper(
            properties.delete_batch,
        )
        self.get = to_raw_response_wrapper(
            properties.get,
        )
        self.get_batch = to_raw_response_wrapper(
            properties.get_batch,
        )


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
        self.create_batch = async_to_raw_response_wrapper(
            properties.create_batch,
        )
        self.delete_batch = async_to_raw_response_wrapper(
            properties.delete_batch,
        )
        self.get = async_to_raw_response_wrapper(
            properties.get,
        )
        self.get_batch = async_to_raw_response_wrapper(
            properties.get_batch,
        )


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
        self.create_batch = to_streamed_response_wrapper(
            properties.create_batch,
        )
        self.delete_batch = to_streamed_response_wrapper(
            properties.delete_batch,
        )
        self.get = to_streamed_response_wrapper(
            properties.get,
        )
        self.get_batch = to_streamed_response_wrapper(
            properties.get_batch,
        )


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
        self.create_batch = async_to_streamed_response_wrapper(
            properties.create_batch,
        )
        self.delete_batch = async_to_streamed_response_wrapper(
            properties.delete_batch,
        )
        self.get = async_to_streamed_response_wrapper(
            properties.get,
        )
        self.get_batch = async_to_streamed_response_wrapper(
            properties.get_batch,
        )
