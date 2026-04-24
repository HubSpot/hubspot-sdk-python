# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.crm import (
    object_schema_get_params,
    object_schema_list_params,
    object_schema_create_params,
    object_schema_delete_params,
    object_schema_update_params,
    object_schema_create_association_params,
)
from ...._base_client import make_request_options
from ....types.crm.object_schema import ObjectSchema
from ....types.shared.base_association_definition import BaseAssociationDefinition
from ....types.shared.base_object_type_definition import BaseObjectTypeDefinition
from ....types.crm.object_type_property_create_param import ObjectTypePropertyCreateParam
from ....types.shared_params.object_type_definition_labels import ObjectTypeDefinitionLabels
from ....types.crm.collection_response_object_schema_no_paging import CollectionResponseObjectSchemaNoPaging

__all__ = ["ObjectSchemasResource", "AsyncObjectSchemasResource"]


class ObjectSchemasResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObjectSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ObjectSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return ObjectSchemasResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allows_sensitive_properties: bool,
        associated_objects: SequenceNotStr[str],
        labels: ObjectTypeDefinitionLabels,
        name: str,
        properties: Iterable[ObjectTypePropertyCreateParam],
        required_properties: SequenceNotStr[str],
        searchable_properties: SequenceNotStr[str],
        secondary_display_properties: SequenceNotStr[str],
        description: str | Omit = omit,
        primary_display_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Create a new custom object schema by defining its properties and associations.

        Args:
          allows_sensitive_properties: Determines if the object type can include properties that are marked as
              sensitive.

          associated_objects: Associations defined for this object type.

          name: A unique name for this object. For internal use only.

          properties: Properties defined for this object type.

          required_properties: The names of properties that should be **required** when creating an object of
              this type.

          searchable_properties: Names of properties that will be indexed for this object type in by HubSpot's
              product search.

          secondary_display_properties: The names of secondary properties for this object. These will be displayed as
              secondary on the HubSpot record page for this object type.

          description: A brief explanation of the object type.

          primary_display_property: The name of the primary property for this object. This will be displayed as
              primary on the HubSpot record page for this object type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm-object-schemas/2026-03/schemas",
            body=maybe_transform(
                {
                    "allows_sensitive_properties": allows_sensitive_properties,
                    "associated_objects": associated_objects,
                    "labels": labels,
                    "name": name,
                    "properties": properties,
                    "required_properties": required_properties,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                    "description": description,
                    "primary_display_property": primary_display_property,
                },
                object_schema_create_params.ObjectSchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectSchema,
        )

    def update(
        self,
        object_type: str,
        *,
        clear_description: bool,
        allows_sensitive_properties: bool | Omit = omit,
        description: str | Omit = omit,
        labels: ObjectTypeDefinitionLabels | Omit = omit,
        primary_display_property: str | Omit = omit,
        required_properties: SequenceNotStr[str] | Omit = omit,
        restorable: bool | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseObjectTypeDefinition:
        """
        Update attributes of a custom object schema, such as properties and labels,
        using the object type ID or fully qualified name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._patch(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}", object_type=object_type),
            body=maybe_transform(
                {
                    "clear_description": clear_description,
                    "allows_sensitive_properties": allows_sensitive_properties,
                    "description": description,
                    "labels": labels,
                    "primary_display_property": primary_display_property,
                    "required_properties": required_properties,
                    "restorable": restorable,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                object_schema_update_params.ObjectSchemaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseObjectTypeDefinition,
        )

    def list(
        self,
        *,
        archived: bool | Omit = omit,
        include_association_definitions: bool | Omit = omit,
        include_audit_metadata: bool | Omit = omit,
        include_property_definitions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectSchemaNoPaging:
        """
        Retrieve all custom object schemas, with options to include property
        definitions, association definitions, and audit metadata.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm-object-schemas/2026-03/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "include_association_definitions": include_association_definitions,
                        "include_audit_metadata": include_audit_metadata,
                        "include_property_definitions": include_property_definitions,
                    },
                    object_schema_list_params.ObjectSchemaListParams,
                ),
            ),
            cast_to=CollectionResponseObjectSchemaNoPaging,
        )

    def delete(
        self,
        object_type: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a custom object schema from the account using its object type ID or fully
        qualified name.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}", object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, object_schema_delete_params.ObjectSchemaDeleteParams),
            ),
            cast_to=NoneType,
        )

    def create_association(
        self,
        object_type: str,
        *,
        from_object_type_id: str,
        to_object_type_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseAssociationDefinition:
        """
        Create a new association between the specified object type and another object
        type. This operation requires the definition of the association attributes, such
        as the primary and target object type IDs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}/associations", object_type=object_type),
            body=maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                object_schema_create_association_params.ObjectSchemaCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseAssociationDefinition,
        )

    def delete_association(
        self,
        association_identifier: str,
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
        Remove an association between two object types identified by the association
        identifier and object type. This operation is irreversible and will permanently
        delete the specified association.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not association_identifier:
            raise ValueError(
                f"Expected a non-empty value for `association_identifier` but received {association_identifier!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/crm-object-schemas/2026-03/schemas/{object_type}/associations/{association_identifier}",
                object_type=object_type,
                association_identifier=association_identifier,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        object_type: str,
        *,
        include_association_definitions: bool | Omit = omit,
        include_audit_metadata: bool | Omit = omit,
        include_property_definitions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Retrieve details of a custom object schema, including its properties and
        associations, using the object type ID or fully qualified name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}", object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_association_definitions": include_association_definitions,
                        "include_audit_metadata": include_audit_metadata,
                        "include_property_definitions": include_property_definitions,
                    },
                    object_schema_get_params.ObjectSchemaGetParams,
                ),
            ),
            cast_to=ObjectSchema,
        )


class AsyncObjectSchemasResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObjectSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncObjectSchemasResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allows_sensitive_properties: bool,
        associated_objects: SequenceNotStr[str],
        labels: ObjectTypeDefinitionLabels,
        name: str,
        properties: Iterable[ObjectTypePropertyCreateParam],
        required_properties: SequenceNotStr[str],
        searchable_properties: SequenceNotStr[str],
        secondary_display_properties: SequenceNotStr[str],
        description: str | Omit = omit,
        primary_display_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Create a new custom object schema by defining its properties and associations.

        Args:
          allows_sensitive_properties: Determines if the object type can include properties that are marked as
              sensitive.

          associated_objects: Associations defined for this object type.

          name: A unique name for this object. For internal use only.

          properties: Properties defined for this object type.

          required_properties: The names of properties that should be **required** when creating an object of
              this type.

          searchable_properties: Names of properties that will be indexed for this object type in by HubSpot's
              product search.

          secondary_display_properties: The names of secondary properties for this object. These will be displayed as
              secondary on the HubSpot record page for this object type.

          description: A brief explanation of the object type.

          primary_display_property: The name of the primary property for this object. This will be displayed as
              primary on the HubSpot record page for this object type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm-object-schemas/2026-03/schemas",
            body=await async_maybe_transform(
                {
                    "allows_sensitive_properties": allows_sensitive_properties,
                    "associated_objects": associated_objects,
                    "labels": labels,
                    "name": name,
                    "properties": properties,
                    "required_properties": required_properties,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                    "description": description,
                    "primary_display_property": primary_display_property,
                },
                object_schema_create_params.ObjectSchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectSchema,
        )

    async def update(
        self,
        object_type: str,
        *,
        clear_description: bool,
        allows_sensitive_properties: bool | Omit = omit,
        description: str | Omit = omit,
        labels: ObjectTypeDefinitionLabels | Omit = omit,
        primary_display_property: str | Omit = omit,
        required_properties: SequenceNotStr[str] | Omit = omit,
        restorable: bool | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseObjectTypeDefinition:
        """
        Update attributes of a custom object schema, such as properties and labels,
        using the object type ID or fully qualified name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._patch(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}", object_type=object_type),
            body=await async_maybe_transform(
                {
                    "clear_description": clear_description,
                    "allows_sensitive_properties": allows_sensitive_properties,
                    "description": description,
                    "labels": labels,
                    "primary_display_property": primary_display_property,
                    "required_properties": required_properties,
                    "restorable": restorable,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                object_schema_update_params.ObjectSchemaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseObjectTypeDefinition,
        )

    async def list(
        self,
        *,
        archived: bool | Omit = omit,
        include_association_definitions: bool | Omit = omit,
        include_audit_metadata: bool | Omit = omit,
        include_property_definitions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectSchemaNoPaging:
        """
        Retrieve all custom object schemas, with options to include property
        definitions, association definitions, and audit metadata.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm-object-schemas/2026-03/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "include_association_definitions": include_association_definitions,
                        "include_audit_metadata": include_audit_metadata,
                        "include_property_definitions": include_property_definitions,
                    },
                    object_schema_list_params.ObjectSchemaListParams,
                ),
            ),
            cast_to=CollectionResponseObjectSchemaNoPaging,
        )

    async def delete(
        self,
        object_type: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a custom object schema from the account using its object type ID or fully
        qualified name.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}", object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, object_schema_delete_params.ObjectSchemaDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def create_association(
        self,
        object_type: str,
        *,
        from_object_type_id: str,
        to_object_type_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseAssociationDefinition:
        """
        Create a new association between the specified object type and another object
        type. This operation requires the definition of the association attributes, such
        as the primary and target object type IDs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}/associations", object_type=object_type),
            body=await async_maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                object_schema_create_association_params.ObjectSchemaCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseAssociationDefinition,
        )

    async def delete_association(
        self,
        association_identifier: str,
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
        Remove an association between two object types identified by the association
        identifier and object type. This operation is irreversible and will permanently
        delete the specified association.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not association_identifier:
            raise ValueError(
                f"Expected a non-empty value for `association_identifier` but received {association_identifier!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/crm-object-schemas/2026-03/schemas/{object_type}/associations/{association_identifier}",
                object_type=object_type,
                association_identifier=association_identifier,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        object_type: str,
        *,
        include_association_definitions: bool | Omit = omit,
        include_audit_metadata: bool | Omit = omit,
        include_property_definitions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Retrieve details of a custom object schema, including its properties and
        associations, using the object type ID or fully qualified name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            path_template("/crm-object-schemas/2026-03/schemas/{object_type}", object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_association_definitions": include_association_definitions,
                        "include_audit_metadata": include_audit_metadata,
                        "include_property_definitions": include_property_definitions,
                    },
                    object_schema_get_params.ObjectSchemaGetParams,
                ),
            ),
            cast_to=ObjectSchema,
        )


class ObjectSchemasResourceWithRawResponse:
    def __init__(self, object_schemas: ObjectSchemasResource) -> None:
        self._object_schemas = object_schemas

        self.create = to_raw_response_wrapper(
            object_schemas.create,
        )
        self.update = to_raw_response_wrapper(
            object_schemas.update,
        )
        self.list = to_raw_response_wrapper(
            object_schemas.list,
        )
        self.delete = to_raw_response_wrapper(
            object_schemas.delete,
        )
        self.create_association = to_raw_response_wrapper(
            object_schemas.create_association,
        )
        self.delete_association = to_raw_response_wrapper(
            object_schemas.delete_association,
        )
        self.get = to_raw_response_wrapper(
            object_schemas.get,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._object_schemas.batch)


class AsyncObjectSchemasResourceWithRawResponse:
    def __init__(self, object_schemas: AsyncObjectSchemasResource) -> None:
        self._object_schemas = object_schemas

        self.create = async_to_raw_response_wrapper(
            object_schemas.create,
        )
        self.update = async_to_raw_response_wrapper(
            object_schemas.update,
        )
        self.list = async_to_raw_response_wrapper(
            object_schemas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            object_schemas.delete,
        )
        self.create_association = async_to_raw_response_wrapper(
            object_schemas.create_association,
        )
        self.delete_association = async_to_raw_response_wrapper(
            object_schemas.delete_association,
        )
        self.get = async_to_raw_response_wrapper(
            object_schemas.get,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._object_schemas.batch)


class ObjectSchemasResourceWithStreamingResponse:
    def __init__(self, object_schemas: ObjectSchemasResource) -> None:
        self._object_schemas = object_schemas

        self.create = to_streamed_response_wrapper(
            object_schemas.create,
        )
        self.update = to_streamed_response_wrapper(
            object_schemas.update,
        )
        self.list = to_streamed_response_wrapper(
            object_schemas.list,
        )
        self.delete = to_streamed_response_wrapper(
            object_schemas.delete,
        )
        self.create_association = to_streamed_response_wrapper(
            object_schemas.create_association,
        )
        self.delete_association = to_streamed_response_wrapper(
            object_schemas.delete_association,
        )
        self.get = to_streamed_response_wrapper(
            object_schemas.get,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._object_schemas.batch)


class AsyncObjectSchemasResourceWithStreamingResponse:
    def __init__(self, object_schemas: AsyncObjectSchemasResource) -> None:
        self._object_schemas = object_schemas

        self.create = async_to_streamed_response_wrapper(
            object_schemas.create,
        )
        self.update = async_to_streamed_response_wrapper(
            object_schemas.update,
        )
        self.list = async_to_streamed_response_wrapper(
            object_schemas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            object_schemas.delete,
        )
        self.create_association = async_to_streamed_response_wrapper(
            object_schemas.create_association,
        )
        self.delete_association = async_to_streamed_response_wrapper(
            object_schemas.delete_association,
        )
        self.get = async_to_streamed_response_wrapper(
            object_schemas.get,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._object_schemas.batch)
