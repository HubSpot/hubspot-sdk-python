# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.crm.objects import (
    schema_list_params,
    schema_create_params,
    schema_delete_params,
    schema_update_params,
    schema_create_association_params,
)
from ....types.crm.objects.object_schema import ObjectSchema
from ....types.crm.objects.association_definition import AssociationDefinition
from ....types.crm.objects.object_type_definition import ObjectTypeDefinition
from ....types.crm.objects.object_type_property_create_param import ObjectTypePropertyCreateParam
from ....types.crm.objects.object_type_definition_labels_param import ObjectTypeDefinitionLabelsParam
from ....types.crm.objects.collection_response_object_schema_no_paging import CollectionResponseObjectSchemaNoPaging

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SchemasResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        associated_objects: SequenceNotStr[str],
        labels: ObjectTypeDefinitionLabelsParam,
        name: str,
        properties: Iterable[ObjectTypePropertyCreateParam],
        required_properties: SequenceNotStr[str],
        description: str | Omit = omit,
        primary_display_property: str | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """Define a new object schema, along with custom properties and associations.

        The
        entire object schema, including its object type ID, properties, and associations
        will be returned in the response.

        Args:
          associated_objects: Associations defined for this object type.

          labels: Singular and plural labels for the object. Used in CRM display.

          name: A unique name for this object. For internal use only.

          properties: Properties defined for this object type.

          required_properties: The names of properties that should be **required** when creating an object of
              this type.

          primary_display_property: The name of the primary property for this object. This will be displayed as
              primary on the HubSpot record page for this object type.

          searchable_properties: Names of properties that will be indexed for this object type in by HubSpot's
              product search.

          secondary_display_properties: The names of secondary properties for this object. These will be displayed as
              secondary on the HubSpot record page for this object type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm-object-schemas/v3/schemas",
            body=maybe_transform(
                {
                    "associated_objects": associated_objects,
                    "labels": labels,
                    "name": name,
                    "properties": properties,
                    "required_properties": required_properties,
                    "description": description,
                    "primary_display_property": primary_display_property,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_create_params.SchemaCreateParams,
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
        clear_description: bool | Omit = omit,
        description: str | Omit = omit,
        labels: ObjectTypeDefinitionLabelsParam | Omit = omit,
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
    ) -> ObjectTypeDefinition:
        """
        Update the details for an existing object schema.

        Args:
          labels: Singular and plural labels for the object. Used in CRM display.

          primary_display_property: The name of the primary property for this object. This will be displayed as
              primary on the HubSpot record page for this object type.

          required_properties: The names of properties that should be **required** when creating an object of
              this type.

          searchable_properties: Names of properties that will be indexed for this object type in by HubSpot's
              product search.

          secondary_display_properties: The names of secondary properties for this object. These will be displayed as
              secondary on the HubSpot record page for this object type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._patch(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            body=maybe_transform(
                {
                    "clear_description": clear_description,
                    "description": description,
                    "labels": labels,
                    "primary_display_property": primary_display_property,
                    "required_properties": required_properties,
                    "restorable": restorable,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_update_params.SchemaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTypeDefinition,
        )

    def list(
        self,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectSchemaNoPaging:
        """
        Returns all object schemas that have been defined for your account.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm-object-schemas/v3/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, schema_list_params.SchemaListParams),
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
        """Deletes a schema.

        Any existing records of this schema must be deleted **first**.
        Otherwise this call will fail.

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
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, schema_delete_params.SchemaDeleteParams),
            ),
            cast_to=NoneType,
        )

    def archive_association(
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
        Removes an existing association from a schema.

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
            f"/crm-object-schemas/v3/schemas/{object_type}/associations/{association_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
    ) -> AssociationDefinition:
        """
        Defines a new association between the primary schema's object type and other
        object types.

        Args:
          from_object_type_id: ID of the primary object type to link from.

          to_object_type_id: ID of the target object type to link to.

          name: A unique name for this association.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/crm-object-schemas/v3/schemas/{object_type}/associations",
            body=maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                schema_create_association_params.SchemaCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationDefinition,
        )

    def read(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Returns an existing object schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectSchema,
        )


class AsyncSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSchemasResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        associated_objects: SequenceNotStr[str],
        labels: ObjectTypeDefinitionLabelsParam,
        name: str,
        properties: Iterable[ObjectTypePropertyCreateParam],
        required_properties: SequenceNotStr[str],
        description: str | Omit = omit,
        primary_display_property: str | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """Define a new object schema, along with custom properties and associations.

        The
        entire object schema, including its object type ID, properties, and associations
        will be returned in the response.

        Args:
          associated_objects: Associations defined for this object type.

          labels: Singular and plural labels for the object. Used in CRM display.

          name: A unique name for this object. For internal use only.

          properties: Properties defined for this object type.

          required_properties: The names of properties that should be **required** when creating an object of
              this type.

          primary_display_property: The name of the primary property for this object. This will be displayed as
              primary on the HubSpot record page for this object type.

          searchable_properties: Names of properties that will be indexed for this object type in by HubSpot's
              product search.

          secondary_display_properties: The names of secondary properties for this object. These will be displayed as
              secondary on the HubSpot record page for this object type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm-object-schemas/v3/schemas",
            body=await async_maybe_transform(
                {
                    "associated_objects": associated_objects,
                    "labels": labels,
                    "name": name,
                    "properties": properties,
                    "required_properties": required_properties,
                    "description": description,
                    "primary_display_property": primary_display_property,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_create_params.SchemaCreateParams,
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
        clear_description: bool | Omit = omit,
        description: str | Omit = omit,
        labels: ObjectTypeDefinitionLabelsParam | Omit = omit,
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
    ) -> ObjectTypeDefinition:
        """
        Update the details for an existing object schema.

        Args:
          labels: Singular and plural labels for the object. Used in CRM display.

          primary_display_property: The name of the primary property for this object. This will be displayed as
              primary on the HubSpot record page for this object type.

          required_properties: The names of properties that should be **required** when creating an object of
              this type.

          searchable_properties: Names of properties that will be indexed for this object type in by HubSpot's
              product search.

          secondary_display_properties: The names of secondary properties for this object. These will be displayed as
              secondary on the HubSpot record page for this object type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._patch(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            body=await async_maybe_transform(
                {
                    "clear_description": clear_description,
                    "description": description,
                    "labels": labels,
                    "primary_display_property": primary_display_property,
                    "required_properties": required_properties,
                    "restorable": restorable,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_update_params.SchemaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTypeDefinition,
        )

    async def list(
        self,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectSchemaNoPaging:
        """
        Returns all object schemas that have been defined for your account.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm-object-schemas/v3/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, schema_list_params.SchemaListParams),
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
        """Deletes a schema.

        Any existing records of this schema must be deleted **first**.
        Otherwise this call will fail.

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
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, schema_delete_params.SchemaDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def archive_association(
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
        Removes an existing association from a schema.

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
            f"/crm-object-schemas/v3/schemas/{object_type}/associations/{association_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
    ) -> AssociationDefinition:
        """
        Defines a new association between the primary schema's object type and other
        object types.

        Args:
          from_object_type_id: ID of the primary object type to link from.

          to_object_type_id: ID of the target object type to link to.

          name: A unique name for this association.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/crm-object-schemas/v3/schemas/{object_type}/associations",
            body=await async_maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                schema_create_association_params.SchemaCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationDefinition,
        )

    async def read(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Returns an existing object schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectSchema,
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_raw_response_wrapper(
            schemas.create,
        )
        self.update = to_raw_response_wrapper(
            schemas.update,
        )
        self.list = to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = to_raw_response_wrapper(
            schemas.delete,
        )
        self.archive_association = to_raw_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = to_raw_response_wrapper(
            schemas.create_association,
        )
        self.read = to_raw_response_wrapper(
            schemas.read,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_raw_response_wrapper(
            schemas.create,
        )
        self.update = async_to_raw_response_wrapper(
            schemas.update,
        )
        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schemas.delete,
        )
        self.archive_association = async_to_raw_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = async_to_raw_response_wrapper(
            schemas.create_association,
        )
        self.read = async_to_raw_response_wrapper(
            schemas.read,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_streamed_response_wrapper(
            schemas.create,
        )
        self.update = to_streamed_response_wrapper(
            schemas.update,
        )
        self.list = to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = to_streamed_response_wrapper(
            schemas.delete,
        )
        self.archive_association = to_streamed_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = to_streamed_response_wrapper(
            schemas.create_association,
        )
        self.read = to_streamed_response_wrapper(
            schemas.read,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_streamed_response_wrapper(
            schemas.create,
        )
        self.update = async_to_streamed_response_wrapper(
            schemas.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schemas.delete,
        )
        self.archive_association = async_to_streamed_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = async_to_streamed_response_wrapper(
            schemas.create_association,
        )
        self.read = async_to_streamed_response_wrapper(
            schemas.read,
        )
