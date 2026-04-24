# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, List, Iterable
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
from ....types.cms import (
    media_bridge_get_property_params,
    media_bridge_list_schemas_params,
    media_bridge_update_schema_params,
    media_bridge_create_property_params,
    media_bridge_list_properties_params,
    media_bridge_update_property_params,
    media_bridge_update_settings_params,
    media_bridge_register_app_name_params,
    media_bridge_create_association_params,
    media_bridge_create_object_type_params,
    media_bridge_list_oembed_domains_params,
    media_bridge_create_oembed_domain_params,
    media_bridge_delete_oembed_domain_params,
    media_bridge_update_oembed_domain_params,
    media_bridge_create_property_group_params,
    media_bridge_update_property_group_params,
    media_bridge_create_media_played_event_params,
    media_bridge_create_attention_span_event_params,
    media_bridge_list_object_types_by_media_type_params,
    media_bridge_update_event_visibility_settings_params,
    media_bridge_create_media_played_percent_event_params,
)
from ...._base_client import make_request_options
from ....types.cms.object_schema import ObjectSchema
from ....types.cms.endpoints_param import EndpointsParam
from ....types.shared.property_group import PropertyGroup
from ....types.cms.media_played_event import MediaPlayedEvent
from ....types.cms.attention_span_event import AttentionSpanEvent
from ....types.cms.media_bridge_property import MediaBridgeProperty
from ....types.shared_params.option_input import OptionInput
from ....types.cms.event_visibility_change import EventVisibilityChange
from ....types.cms.event_visibility_response import EventVisibilityResponse
from ....types.shared.association_definition import AssociationDefinition
from ....types.shared.object_type_definition import ObjectTypeDefinition
from ....types.cms.object_definition_response import ObjectDefinitionResponse
from ....types.cms.media_played_percentage_event import MediaPlayedPercentageEvent
from ....types.cms.integrator_o_embed_domain_model import IntegratorOEmbedDomainModel
from ....types.cms.o_embed_domains_collection_response import OEmbedDomainsCollectionResponse
from ....types.cms.attention_span_calculated_values_param import AttentionSpanCalculatedValuesParam
from ....types.cms.collection_response_property_no_paging import CollectionResponsePropertyNoPaging
from ....types.shared_params.object_type_definition_labels import ObjectTypeDefinitionLabels
from ....types.cms.bulk_integrator_object_creation_response import BulkIntegratorObjectCreationResponse
from ....types.cms.collection_response_object_schema_no_paging import CollectionResponseObjectSchemaNoPaging
from ....types.cms.media_bridge_provider_registration_response import MediaBridgeProviderRegistrationResponse
from ....types.shared.collection_response_property_group_no_paging import CollectionResponsePropertyGroupNoPaging

__all__ = ["MediaBridgeResource", "AsyncMediaBridgeResource"]


class MediaBridgeResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> MediaBridgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MediaBridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaBridgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return MediaBridgeResourceWithStreamingResponse(self)

    def create_association(
        self,
        object_type: str,
        *,
        app_id: int,
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
        Create a new association definition for the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}/associations",
                app_id=app_id,
                object_type=object_type,
            ),
            body=maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                media_bridge_create_association_params.MediaBridgeCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationDefinition,
        )

    def create_attention_span_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        raw_data_map: Dict[str, int],
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        derived_values: AttentionSpanCalculatedValuesParam | Omit = omit,
        external_id: str | Omit = omit,
        external_play_context: Literal["EMAIL", "EXTERNAL_PAGE"] | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        raw_data_string: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttentionSpanEvent:
        """
        Create an event containing the viewers attention span details for the media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media-bridge/2026-03/events/attention-span",
            body=maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "raw_data_map": raw_data_map,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "derived_values": derived_values,
                    "external_id": external_id,
                    "external_play_context": external_play_context,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                    "raw_data_string": raw_data_string,
                },
                media_bridge_create_attention_span_event_params.MediaBridgeCreateAttentionSpanEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttentionSpanEvent,
        )

    def create_media_played_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        session_id: str,
        state: Literal["STARTED", "VIEWED"],
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        external_play_context: Literal["EMAIL", "EXTERNAL_PAGE"] | Omit = omit,
        iframe_url: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedEvent:
        """
        Create an event for when a user begins playing a piece of media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media-bridge/2026-03/events/media-played",
            body=maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "session_id": session_id,
                    "state": state,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "external_play_context": external_play_context,
                    "iframe_url": iframe_url,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                media_bridge_create_media_played_event_params.MediaBridgeCreateMediaPlayedEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedEvent,
        )

    def create_media_played_percent_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        played_percent: int,
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        external_play_context: Literal["EMAIL", "EXTERNAL_PAGE"] | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedPercentageEvent:
        """
        Create an event representing a user reaching quarterly milestones in a piece of
        media they're viewing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media-bridge/2026-03/events/media-played-percent",
            body=maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "played_percent": played_percent,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "external_play_context": external_play_context,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                media_bridge_create_media_played_percent_event_params.MediaBridgeCreateMediaPlayedPercentEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedPercentageEvent,
        )

    def create_object_type(
        self,
        app_id: int,
        *,
        media_types: List[Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkIntegratorObjectCreationResponse:
        """
        Create a new media object type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/object-definitions", app_id=app_id),
            body=maybe_transform(
                {"media_types": media_types}, media_bridge_create_object_type_params.MediaBridgeCreateObjectTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIntegratorObjectCreationResponse,
        )

    def create_oembed_domain(
        self,
        app_id: int,
        *,
        endpoints: EndpointsParam,
        portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorOEmbedDomainModel:
        """
        Set up a new oEmbed domain for your media bridge app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/oembed-domains", app_id=app_id),
            body=maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                media_bridge_create_oembed_domain_params.MediaBridgeCreateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )

    def create_property(
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProperty:
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
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}", app_id=app_id, object_type=object_type
            ),
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
                },
                media_bridge_create_property_params.MediaBridgeCreatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProperty,
        )

    def create_property_group(
        self,
        object_type: str,
        *,
        app_id: int,
        label: str,
        name: str,
        display_order: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyGroup:
        """
        Create a new property group for the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups", app_id=app_id, object_type=object_type
            ),
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "display_order": display_order,
                },
                media_bridge_create_property_group_params.MediaBridgeCreatePropertyGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyGroup,
        )

    def create_video_association_definition(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssociationDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/video-association-definition", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationDefinition,
        )

    def delete_association(
        self,
        association_id: str,
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
        Delete an existing association definition for an object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not association_id:
            raise ValueError(f"Expected a non-empty value for `association_id` but received {association_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}/associations/{association_id}",
                app_id=app_id,
                object_type=object_type,
                association_id=association_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_oembed_domain(
        self,
        app_id: int,
        *,
        id: int | Omit = omit,
        domain_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing oEmbed domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/media-bridge/2026-03/{app_id}/settings/oembed-domains", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "domain_portal_id": domain_portal_id,
                    },
                    media_bridge_delete_oembed_domain_params.MediaBridgeDeleteOembedDomainParams,
                ),
            ),
            cast_to=NoneType,
        )

    def delete_property(
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
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/{property_name}",
                app_id=app_id,
                object_type=object_type,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_property_group(
        self,
        group_name: str,
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
        Delete an existing property group by name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not group_name:
            raise ValueError(f"Expected a non-empty value for `group_name` but received {group_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups/{group_name}",
                app_id=app_id,
                object_type=object_type,
                group_name=group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_event_visibility_settings(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVisibilityResponse:
        """
        Get the visibility settings for media bridge events for your apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/media-bridge/2026-03/{app_id}/settings/event-visibility", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVisibilityResponse,
        )

    def get_oembed_domain(
        self,
        o_embed_domain_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorOEmbedDomainModel:
        """
        Get the details for an existing oEmbed domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not o_embed_domain_id:
            raise ValueError(f"Expected a non-empty value for `o_embed_domain_id` but received {o_embed_domain_id!r}")
        return self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
                app_id=app_id,
                o_embed_domain_id=o_embed_domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )

    def get_property(
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
    ) -> MediaBridgeProperty:
        """
        Get the details for an existing property by name.

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
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/{property_name}",
                app_id=app_id,
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
                        "properties": properties,
                    },
                    media_bridge_get_property_params.MediaBridgeGetPropertyParams,
                ),
            ),
            cast_to=MediaBridgeProperty,
        )

    def get_property_group(
        self,
        group_name: str,
        *,
        app_id: int,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyGroup:
        """
        Get the details of an existing property group by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not group_name:
            raise ValueError(f"Expected a non-empty value for `group_name` but received {group_name!r}")
        return self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups/{group_name}",
                app_id=app_id,
                object_type=object_type,
                group_name=group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyGroup,
        )

    def get_schema(
        self,
        object_type: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Get the schema for a specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}", app_id=app_id, object_type=object_type
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectSchema,
        )

    def list_object_types_by_media_type(
        self,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        *,
        app_id: int,
        include_full_definition: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDefinitionResponse:
        """
        Get the existing objects types that belong to the specified media type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_type:
            raise ValueError(f"Expected a non-empty value for `media_type` but received {media_type!r}")
        return self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/settings/object-definitions/{media_type}",
                app_id=app_id,
                media_type=media_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_full_definition": include_full_definition},
                    media_bridge_list_object_types_by_media_type_params.MediaBridgeListObjectTypesByMediaTypeParams,
                ),
            ),
            cast_to=ObjectDefinitionResponse,
        )

    def list_oembed_domains(
        self,
        app_id: int,
        *,
        domain_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OEmbedDomainsCollectionResponse:
        """
        Get the details for existing oEmbed domains for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/media-bridge/2026-03/{app_id}/settings/oembed-domains", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain_portal_id": domain_portal_id},
                    media_bridge_list_oembed_domains_params.MediaBridgeListOembedDomainsParams,
                ),
            ),
            cast_to=OEmbedDomainsCollectionResponse,
        )

    def list_properties(
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}", app_id=app_id, object_type=object_type
            ),
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
                    media_bridge_list_properties_params.MediaBridgeListPropertiesParams,
                ),
            ),
            cast_to=CollectionResponsePropertyNoPaging,
        )

    def list_property_groups(
        self,
        object_type: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyGroupNoPaging:
        """
        Get the property groups for a specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups", app_id=app_id, object_type=object_type
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePropertyGroupNoPaging,
        )

    def list_schemas(
        self,
        app_id: int,
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
        Get the schemas for all object types.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/media-bridge/2026-03/{app_id}/schemas", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, media_bridge_list_schemas_params.MediaBridgeListSchemasParams
                ),
            ),
            cast_to=CollectionResponseObjectSchemaNoPaging,
        )

    @typing_extensions.deprecated("deprecated")
    def register_app_name(
        self,
        app_id: int,
        *,
        updated_at: int,
        allow_import_on_disconnect: bool | Omit = omit,
        module_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProviderRegistrationResponse:
        """
        Register the name that your app will display when a user is selecting media
        bridge items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/register", app_id=app_id),
            body=maybe_transform(
                {
                    "updated_at": updated_at,
                    "allow_import_on_disconnect": allow_import_on_disconnect,
                    "module_name": module_name,
                    "name": name,
                },
                media_bridge_register_app_name_params.MediaBridgeRegisterAppNameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProviderRegistrationResponse,
        )

    def update_event_visibility_settings(
        self,
        app_id: int,
        *,
        event_type: Literal["ALL", "ATTENTION_SPAN", "MEDIA_PLAYS", "MEDIA_PLAYS_PERCENT"],
        updated_at: int,
        show_in_reporting: bool | Omit = omit,
        show_in_timeline: bool | Omit = omit,
        show_in_workflows: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVisibilityChange:
        """
        Set the visibility settings for media bridge events created by your app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/media-bridge/2026-03/{app_id}/settings/event-visibility", app_id=app_id),
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "updated_at": updated_at,
                    "show_in_reporting": show_in_reporting,
                    "show_in_timeline": show_in_timeline,
                    "show_in_workflows": show_in_workflows,
                },
                media_bridge_update_event_visibility_settings_params.MediaBridgeUpdateEventVisibilitySettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVisibilityChange,
        )

    def update_oembed_domain(
        self,
        o_embed_domain_id: str,
        *,
        app_id: int,
        endpoints: EndpointsParam,
        portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorOEmbedDomainModel:
        """
        Update an existing oEmbed domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not o_embed_domain_id:
            raise ValueError(f"Expected a non-empty value for `o_embed_domain_id` but received {o_embed_domain_id!r}")
        return self._patch(
            path_template(
                "/media-bridge/2026-03/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
                app_id=app_id,
                o_embed_domain_id=o_embed_domain_id,
            ),
            body=maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                media_bridge_update_oembed_domain_params.MediaBridgeUpdateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )

    def update_property(
        self,
        property_name: str,
        *,
        app_id: int,
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
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        number_display_hint: Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"]
        | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        show_currency_symbol: bool | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProperty:
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
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/{property_name}",
                app_id=app_id,
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
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "label": label,
                    "number_display_hint": number_display_hint,
                    "options": options,
                    "show_currency_symbol": show_currency_symbol,
                    "type": type,
                },
                media_bridge_update_property_params.MediaBridgeUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProperty,
        )

    def update_property_group(
        self,
        group_name: str,
        *,
        app_id: int,
        object_type: str,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyGroup:
        """
        Update an existing property group by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not group_name:
            raise ValueError(f"Expected a non-empty value for `group_name` but received {group_name!r}")
        return self._patch(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups/{group_name}",
                app_id=app_id,
                object_type=object_type,
                group_name=group_name,
            ),
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                },
                media_bridge_update_property_group_params.MediaBridgeUpdatePropertyGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyGroup,
        )

    def update_schema(
        self,
        object_type: str,
        *,
        app_id: int,
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
    ) -> ObjectTypeDefinition:
        """
        Update the schema for an existing object type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._patch(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}", app_id=app_id, object_type=object_type
            ),
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
                media_bridge_update_schema_params.MediaBridgeUpdateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTypeDefinition,
        )

    def update_settings(
        self,
        app_id: int,
        *,
        updated_at: int,
        allow_import_on_disconnect: bool | Omit = omit,
        module_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProviderRegistrationResponse:
        """
        Update the name that your app will display when a user is selecting media bridge
        items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            path_template("/media-bridge/2026-03/{app_id}/settings", app_id=app_id),
            body=maybe_transform(
                {
                    "updated_at": updated_at,
                    "allow_import_on_disconnect": allow_import_on_disconnect,
                    "module_name": module_name,
                    "name": name,
                },
                media_bridge_update_settings_params.MediaBridgeUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProviderRegistrationResponse,
        )


class AsyncMediaBridgeResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMediaBridgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaBridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaBridgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMediaBridgeResourceWithStreamingResponse(self)

    async def create_association(
        self,
        object_type: str,
        *,
        app_id: int,
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
        Create a new association definition for the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}/associations",
                app_id=app_id,
                object_type=object_type,
            ),
            body=await async_maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                media_bridge_create_association_params.MediaBridgeCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationDefinition,
        )

    async def create_attention_span_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        raw_data_map: Dict[str, int],
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        derived_values: AttentionSpanCalculatedValuesParam | Omit = omit,
        external_id: str | Omit = omit,
        external_play_context: Literal["EMAIL", "EXTERNAL_PAGE"] | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        raw_data_string: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttentionSpanEvent:
        """
        Create an event containing the viewers attention span details for the media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media-bridge/2026-03/events/attention-span",
            body=await async_maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "raw_data_map": raw_data_map,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "derived_values": derived_values,
                    "external_id": external_id,
                    "external_play_context": external_play_context,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                    "raw_data_string": raw_data_string,
                },
                media_bridge_create_attention_span_event_params.MediaBridgeCreateAttentionSpanEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttentionSpanEvent,
        )

    async def create_media_played_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        session_id: str,
        state: Literal["STARTED", "VIEWED"],
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        external_play_context: Literal["EMAIL", "EXTERNAL_PAGE"] | Omit = omit,
        iframe_url: str | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedEvent:
        """
        Create an event for when a user begins playing a piece of media.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media-bridge/2026-03/events/media-played",
            body=await async_maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "session_id": session_id,
                    "state": state,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "external_play_context": external_play_context,
                    "iframe_url": iframe_url,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                media_bridge_create_media_played_event_params.MediaBridgeCreateMediaPlayedEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedEvent,
        )

    async def create_media_played_percent_event(
        self,
        *,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        occurred_timestamp: int,
        played_percent: int,
        session_id: str,
        _hsenc: str | Omit = omit,
        contact_id: int | Omit = omit,
        contact_utk: str | Omit = omit,
        external_id: str | Omit = omit,
        external_play_context: Literal["EMAIL", "EXTERNAL_PAGE"] | Omit = omit,
        media_bridge_id: int | Omit = omit,
        media_name: str | Omit = omit,
        media_url: str | Omit = omit,
        page_id: int | Omit = omit,
        page_name: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaPlayedPercentageEvent:
        """
        Create an event representing a user reaching quarterly milestones in a piece of
        media they're viewing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media-bridge/2026-03/events/media-played-percent",
            body=await async_maybe_transform(
                {
                    "media_type": media_type,
                    "occurred_timestamp": occurred_timestamp,
                    "played_percent": played_percent,
                    "session_id": session_id,
                    "_hsenc": _hsenc,
                    "contact_id": contact_id,
                    "contact_utk": contact_utk,
                    "external_id": external_id,
                    "external_play_context": external_play_context,
                    "media_bridge_id": media_bridge_id,
                    "media_name": media_name,
                    "media_url": media_url,
                    "page_id": page_id,
                    "page_name": page_name,
                    "page_url": page_url,
                },
                media_bridge_create_media_played_percent_event_params.MediaBridgeCreateMediaPlayedPercentEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaPlayedPercentageEvent,
        )

    async def create_object_type(
        self,
        app_id: int,
        *,
        media_types: List[Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkIntegratorObjectCreationResponse:
        """
        Create a new media object type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/object-definitions", app_id=app_id),
            body=await async_maybe_transform(
                {"media_types": media_types}, media_bridge_create_object_type_params.MediaBridgeCreateObjectTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIntegratorObjectCreationResponse,
        )

    async def create_oembed_domain(
        self,
        app_id: int,
        *,
        endpoints: EndpointsParam,
        portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorOEmbedDomainModel:
        """
        Set up a new oEmbed domain for your media bridge app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/oembed-domains", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                media_bridge_create_oembed_domain_params.MediaBridgeCreateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )

    async def create_property(
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProperty:
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
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}", app_id=app_id, object_type=object_type
            ),
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
                },
                media_bridge_create_property_params.MediaBridgeCreatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProperty,
        )

    async def create_property_group(
        self,
        object_type: str,
        *,
        app_id: int,
        label: str,
        name: str,
        display_order: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyGroup:
        """
        Create a new property group for the specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups", app_id=app_id, object_type=object_type
            ),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "display_order": display_order,
                },
                media_bridge_create_property_group_params.MediaBridgeCreatePropertyGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyGroup,
        )

    async def create_video_association_definition(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssociationDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/video-association-definition", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationDefinition,
        )

    async def delete_association(
        self,
        association_id: str,
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
        Delete an existing association definition for an object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not association_id:
            raise ValueError(f"Expected a non-empty value for `association_id` but received {association_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}/associations/{association_id}",
                app_id=app_id,
                object_type=object_type,
                association_id=association_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_oembed_domain(
        self,
        app_id: int,
        *,
        id: int | Omit = omit,
        domain_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing oEmbed domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/media-bridge/2026-03/{app_id}/settings/oembed-domains", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "domain_portal_id": domain_portal_id,
                    },
                    media_bridge_delete_oembed_domain_params.MediaBridgeDeleteOembedDomainParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_property(
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
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/{property_name}",
                app_id=app_id,
                object_type=object_type,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_property_group(
        self,
        group_name: str,
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
        Delete an existing property group by name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not group_name:
            raise ValueError(f"Expected a non-empty value for `group_name` but received {group_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups/{group_name}",
                app_id=app_id,
                object_type=object_type,
                group_name=group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_event_visibility_settings(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVisibilityResponse:
        """
        Get the visibility settings for media bridge events for your apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/media-bridge/2026-03/{app_id}/settings/event-visibility", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVisibilityResponse,
        )

    async def get_oembed_domain(
        self,
        o_embed_domain_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorOEmbedDomainModel:
        """
        Get the details for an existing oEmbed domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not o_embed_domain_id:
            raise ValueError(f"Expected a non-empty value for `o_embed_domain_id` but received {o_embed_domain_id!r}")
        return await self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
                app_id=app_id,
                o_embed_domain_id=o_embed_domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )

    async def get_property(
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
    ) -> MediaBridgeProperty:
        """
        Get the details for an existing property by name.

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
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/{property_name}",
                app_id=app_id,
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
                        "properties": properties,
                    },
                    media_bridge_get_property_params.MediaBridgeGetPropertyParams,
                ),
            ),
            cast_to=MediaBridgeProperty,
        )

    async def get_property_group(
        self,
        group_name: str,
        *,
        app_id: int,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyGroup:
        """
        Get the details of an existing property group by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not group_name:
            raise ValueError(f"Expected a non-empty value for `group_name` but received {group_name!r}")
        return await self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups/{group_name}",
                app_id=app_id,
                object_type=object_type,
                group_name=group_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyGroup,
        )

    async def get_schema(
        self,
        object_type: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectSchema:
        """
        Get the schema for a specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}", app_id=app_id, object_type=object_type
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectSchema,
        )

    async def list_object_types_by_media_type(
        self,
        media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"],
        *,
        app_id: int,
        include_full_definition: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDefinitionResponse:
        """
        Get the existing objects types that belong to the specified media type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_type:
            raise ValueError(f"Expected a non-empty value for `media_type` but received {media_type!r}")
        return await self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/settings/object-definitions/{media_type}",
                app_id=app_id,
                media_type=media_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_full_definition": include_full_definition},
                    media_bridge_list_object_types_by_media_type_params.MediaBridgeListObjectTypesByMediaTypeParams,
                ),
            ),
            cast_to=ObjectDefinitionResponse,
        )

    async def list_oembed_domains(
        self,
        app_id: int,
        *,
        domain_portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OEmbedDomainsCollectionResponse:
        """
        Get the details for existing oEmbed domains for your app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/media-bridge/2026-03/{app_id}/settings/oembed-domains", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"domain_portal_id": domain_portal_id},
                    media_bridge_list_oembed_domains_params.MediaBridgeListOembedDomainsParams,
                ),
            ),
            cast_to=OEmbedDomainsCollectionResponse,
        )

    async def list_properties(
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}", app_id=app_id, object_type=object_type
            ),
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
                    media_bridge_list_properties_params.MediaBridgeListPropertiesParams,
                ),
            ),
            cast_to=CollectionResponsePropertyNoPaging,
        )

    async def list_property_groups(
        self,
        object_type: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyGroupNoPaging:
        """
        Get the property groups for a specified object type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups", app_id=app_id, object_type=object_type
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePropertyGroupNoPaging,
        )

    async def list_schemas(
        self,
        app_id: int,
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
        Get the schemas for all object types.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/media-bridge/2026-03/{app_id}/schemas", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, media_bridge_list_schemas_params.MediaBridgeListSchemasParams
                ),
            ),
            cast_to=CollectionResponseObjectSchemaNoPaging,
        )

    @typing_extensions.deprecated("deprecated")
    async def register_app_name(
        self,
        app_id: int,
        *,
        updated_at: int,
        allow_import_on_disconnect: bool | Omit = omit,
        module_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProviderRegistrationResponse:
        """
        Register the name that your app will display when a user is selecting media
        bridge items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/media-bridge/2026-03/{app_id}/settings/register", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "updated_at": updated_at,
                    "allow_import_on_disconnect": allow_import_on_disconnect,
                    "module_name": module_name,
                    "name": name,
                },
                media_bridge_register_app_name_params.MediaBridgeRegisterAppNameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProviderRegistrationResponse,
        )

    async def update_event_visibility_settings(
        self,
        app_id: int,
        *,
        event_type: Literal["ALL", "ATTENTION_SPAN", "MEDIA_PLAYS", "MEDIA_PLAYS_PERCENT"],
        updated_at: int,
        show_in_reporting: bool | Omit = omit,
        show_in_timeline: bool | Omit = omit,
        show_in_workflows: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVisibilityChange:
        """
        Set the visibility settings for media bridge events created by your app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/media-bridge/2026-03/{app_id}/settings/event-visibility", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "updated_at": updated_at,
                    "show_in_reporting": show_in_reporting,
                    "show_in_timeline": show_in_timeline,
                    "show_in_workflows": show_in_workflows,
                },
                media_bridge_update_event_visibility_settings_params.MediaBridgeUpdateEventVisibilitySettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVisibilityChange,
        )

    async def update_oembed_domain(
        self,
        o_embed_domain_id: str,
        *,
        app_id: int,
        endpoints: EndpointsParam,
        portal_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorOEmbedDomainModel:
        """
        Update an existing oEmbed domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not o_embed_domain_id:
            raise ValueError(f"Expected a non-empty value for `o_embed_domain_id` but received {o_embed_domain_id!r}")
        return await self._patch(
            path_template(
                "/media-bridge/2026-03/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
                app_id=app_id,
                o_embed_domain_id=o_embed_domain_id,
            ),
            body=await async_maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                media_bridge_update_oembed_domain_params.MediaBridgeUpdateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )

    async def update_property(
        self,
        property_name: str,
        *,
        app_id: int,
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
        has_unique_value: bool | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        number_display_hint: Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"]
        | Omit = omit,
        options: Iterable[OptionInput] | Omit = omit,
        show_currency_symbol: bool | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProperty:
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
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/{property_name}",
                app_id=app_id,
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
                    "has_unique_value": has_unique_value,
                    "hidden": hidden,
                    "label": label,
                    "number_display_hint": number_display_hint,
                    "options": options,
                    "show_currency_symbol": show_currency_symbol,
                    "type": type,
                },
                media_bridge_update_property_params.MediaBridgeUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProperty,
        )

    async def update_property_group(
        self,
        group_name: str,
        *,
        app_id: int,
        object_type: str,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyGroup:
        """
        Update an existing property group by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not group_name:
            raise ValueError(f"Expected a non-empty value for `group_name` but received {group_name!r}")
        return await self._patch(
            path_template(
                "/media-bridge/2026-03/{app_id}/properties/{object_type}/groups/{group_name}",
                app_id=app_id,
                object_type=object_type,
                group_name=group_name,
            ),
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                },
                media_bridge_update_property_group_params.MediaBridgeUpdatePropertyGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyGroup,
        )

    async def update_schema(
        self,
        object_type: str,
        *,
        app_id: int,
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
    ) -> ObjectTypeDefinition:
        """
        Update the schema for an existing object type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._patch(
            path_template(
                "/media-bridge/2026-03/{app_id}/schemas/{object_type}", app_id=app_id, object_type=object_type
            ),
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
                media_bridge_update_schema_params.MediaBridgeUpdateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectTypeDefinition,
        )

    async def update_settings(
        self,
        app_id: int,
        *,
        updated_at: int,
        allow_import_on_disconnect: bool | Omit = omit,
        module_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaBridgeProviderRegistrationResponse:
        """
        Update the name that your app will display when a user is selecting media bridge
        items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            path_template("/media-bridge/2026-03/{app_id}/settings", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "updated_at": updated_at,
                    "allow_import_on_disconnect": allow_import_on_disconnect,
                    "module_name": module_name,
                    "name": name,
                },
                media_bridge_update_settings_params.MediaBridgeUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProviderRegistrationResponse,
        )


class MediaBridgeResourceWithRawResponse:
    def __init__(self, media_bridge: MediaBridgeResource) -> None:
        self._media_bridge = media_bridge

        self.create_association = to_raw_response_wrapper(
            media_bridge.create_association,
        )
        self.create_attention_span_event = to_raw_response_wrapper(
            media_bridge.create_attention_span_event,
        )
        self.create_media_played_event = to_raw_response_wrapper(
            media_bridge.create_media_played_event,
        )
        self.create_media_played_percent_event = to_raw_response_wrapper(
            media_bridge.create_media_played_percent_event,
        )
        self.create_object_type = to_raw_response_wrapper(
            media_bridge.create_object_type,
        )
        self.create_oembed_domain = to_raw_response_wrapper(
            media_bridge.create_oembed_domain,
        )
        self.create_property = to_raw_response_wrapper(
            media_bridge.create_property,
        )
        self.create_property_group = to_raw_response_wrapper(
            media_bridge.create_property_group,
        )
        self.create_video_association_definition = to_raw_response_wrapper(
            media_bridge.create_video_association_definition,
        )
        self.delete_association = to_raw_response_wrapper(
            media_bridge.delete_association,
        )
        self.delete_oembed_domain = to_raw_response_wrapper(
            media_bridge.delete_oembed_domain,
        )
        self.delete_property = to_raw_response_wrapper(
            media_bridge.delete_property,
        )
        self.delete_property_group = to_raw_response_wrapper(
            media_bridge.delete_property_group,
        )
        self.get_event_visibility_settings = to_raw_response_wrapper(
            media_bridge.get_event_visibility_settings,
        )
        self.get_oembed_domain = to_raw_response_wrapper(
            media_bridge.get_oembed_domain,
        )
        self.get_property = to_raw_response_wrapper(
            media_bridge.get_property,
        )
        self.get_property_group = to_raw_response_wrapper(
            media_bridge.get_property_group,
        )
        self.get_schema = to_raw_response_wrapper(
            media_bridge.get_schema,
        )
        self.list_object_types_by_media_type = to_raw_response_wrapper(
            media_bridge.list_object_types_by_media_type,
        )
        self.list_oembed_domains = to_raw_response_wrapper(
            media_bridge.list_oembed_domains,
        )
        self.list_properties = to_raw_response_wrapper(
            media_bridge.list_properties,
        )
        self.list_property_groups = to_raw_response_wrapper(
            media_bridge.list_property_groups,
        )
        self.list_schemas = to_raw_response_wrapper(
            media_bridge.list_schemas,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                media_bridge.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_event_visibility_settings = to_raw_response_wrapper(
            media_bridge.update_event_visibility_settings,
        )
        self.update_oembed_domain = to_raw_response_wrapper(
            media_bridge.update_oembed_domain,
        )
        self.update_property = to_raw_response_wrapper(
            media_bridge.update_property,
        )
        self.update_property_group = to_raw_response_wrapper(
            media_bridge.update_property_group,
        )
        self.update_schema = to_raw_response_wrapper(
            media_bridge.update_schema,
        )
        self.update_settings = to_raw_response_wrapper(
            media_bridge.update_settings,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._media_bridge.batch)


class AsyncMediaBridgeResourceWithRawResponse:
    def __init__(self, media_bridge: AsyncMediaBridgeResource) -> None:
        self._media_bridge = media_bridge

        self.create_association = async_to_raw_response_wrapper(
            media_bridge.create_association,
        )
        self.create_attention_span_event = async_to_raw_response_wrapper(
            media_bridge.create_attention_span_event,
        )
        self.create_media_played_event = async_to_raw_response_wrapper(
            media_bridge.create_media_played_event,
        )
        self.create_media_played_percent_event = async_to_raw_response_wrapper(
            media_bridge.create_media_played_percent_event,
        )
        self.create_object_type = async_to_raw_response_wrapper(
            media_bridge.create_object_type,
        )
        self.create_oembed_domain = async_to_raw_response_wrapper(
            media_bridge.create_oembed_domain,
        )
        self.create_property = async_to_raw_response_wrapper(
            media_bridge.create_property,
        )
        self.create_property_group = async_to_raw_response_wrapper(
            media_bridge.create_property_group,
        )
        self.create_video_association_definition = async_to_raw_response_wrapper(
            media_bridge.create_video_association_definition,
        )
        self.delete_association = async_to_raw_response_wrapper(
            media_bridge.delete_association,
        )
        self.delete_oembed_domain = async_to_raw_response_wrapper(
            media_bridge.delete_oembed_domain,
        )
        self.delete_property = async_to_raw_response_wrapper(
            media_bridge.delete_property,
        )
        self.delete_property_group = async_to_raw_response_wrapper(
            media_bridge.delete_property_group,
        )
        self.get_event_visibility_settings = async_to_raw_response_wrapper(
            media_bridge.get_event_visibility_settings,
        )
        self.get_oembed_domain = async_to_raw_response_wrapper(
            media_bridge.get_oembed_domain,
        )
        self.get_property = async_to_raw_response_wrapper(
            media_bridge.get_property,
        )
        self.get_property_group = async_to_raw_response_wrapper(
            media_bridge.get_property_group,
        )
        self.get_schema = async_to_raw_response_wrapper(
            media_bridge.get_schema,
        )
        self.list_object_types_by_media_type = async_to_raw_response_wrapper(
            media_bridge.list_object_types_by_media_type,
        )
        self.list_oembed_domains = async_to_raw_response_wrapper(
            media_bridge.list_oembed_domains,
        )
        self.list_properties = async_to_raw_response_wrapper(
            media_bridge.list_properties,
        )
        self.list_property_groups = async_to_raw_response_wrapper(
            media_bridge.list_property_groups,
        )
        self.list_schemas = async_to_raw_response_wrapper(
            media_bridge.list_schemas,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                media_bridge.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_event_visibility_settings = async_to_raw_response_wrapper(
            media_bridge.update_event_visibility_settings,
        )
        self.update_oembed_domain = async_to_raw_response_wrapper(
            media_bridge.update_oembed_domain,
        )
        self.update_property = async_to_raw_response_wrapper(
            media_bridge.update_property,
        )
        self.update_property_group = async_to_raw_response_wrapper(
            media_bridge.update_property_group,
        )
        self.update_schema = async_to_raw_response_wrapper(
            media_bridge.update_schema,
        )
        self.update_settings = async_to_raw_response_wrapper(
            media_bridge.update_settings,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._media_bridge.batch)


class MediaBridgeResourceWithStreamingResponse:
    def __init__(self, media_bridge: MediaBridgeResource) -> None:
        self._media_bridge = media_bridge

        self.create_association = to_streamed_response_wrapper(
            media_bridge.create_association,
        )
        self.create_attention_span_event = to_streamed_response_wrapper(
            media_bridge.create_attention_span_event,
        )
        self.create_media_played_event = to_streamed_response_wrapper(
            media_bridge.create_media_played_event,
        )
        self.create_media_played_percent_event = to_streamed_response_wrapper(
            media_bridge.create_media_played_percent_event,
        )
        self.create_object_type = to_streamed_response_wrapper(
            media_bridge.create_object_type,
        )
        self.create_oembed_domain = to_streamed_response_wrapper(
            media_bridge.create_oembed_domain,
        )
        self.create_property = to_streamed_response_wrapper(
            media_bridge.create_property,
        )
        self.create_property_group = to_streamed_response_wrapper(
            media_bridge.create_property_group,
        )
        self.create_video_association_definition = to_streamed_response_wrapper(
            media_bridge.create_video_association_definition,
        )
        self.delete_association = to_streamed_response_wrapper(
            media_bridge.delete_association,
        )
        self.delete_oembed_domain = to_streamed_response_wrapper(
            media_bridge.delete_oembed_domain,
        )
        self.delete_property = to_streamed_response_wrapper(
            media_bridge.delete_property,
        )
        self.delete_property_group = to_streamed_response_wrapper(
            media_bridge.delete_property_group,
        )
        self.get_event_visibility_settings = to_streamed_response_wrapper(
            media_bridge.get_event_visibility_settings,
        )
        self.get_oembed_domain = to_streamed_response_wrapper(
            media_bridge.get_oembed_domain,
        )
        self.get_property = to_streamed_response_wrapper(
            media_bridge.get_property,
        )
        self.get_property_group = to_streamed_response_wrapper(
            media_bridge.get_property_group,
        )
        self.get_schema = to_streamed_response_wrapper(
            media_bridge.get_schema,
        )
        self.list_object_types_by_media_type = to_streamed_response_wrapper(
            media_bridge.list_object_types_by_media_type,
        )
        self.list_oembed_domains = to_streamed_response_wrapper(
            media_bridge.list_oembed_domains,
        )
        self.list_properties = to_streamed_response_wrapper(
            media_bridge.list_properties,
        )
        self.list_property_groups = to_streamed_response_wrapper(
            media_bridge.list_property_groups,
        )
        self.list_schemas = to_streamed_response_wrapper(
            media_bridge.list_schemas,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                media_bridge.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_event_visibility_settings = to_streamed_response_wrapper(
            media_bridge.update_event_visibility_settings,
        )
        self.update_oembed_domain = to_streamed_response_wrapper(
            media_bridge.update_oembed_domain,
        )
        self.update_property = to_streamed_response_wrapper(
            media_bridge.update_property,
        )
        self.update_property_group = to_streamed_response_wrapper(
            media_bridge.update_property_group,
        )
        self.update_schema = to_streamed_response_wrapper(
            media_bridge.update_schema,
        )
        self.update_settings = to_streamed_response_wrapper(
            media_bridge.update_settings,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._media_bridge.batch)


class AsyncMediaBridgeResourceWithStreamingResponse:
    def __init__(self, media_bridge: AsyncMediaBridgeResource) -> None:
        self._media_bridge = media_bridge

        self.create_association = async_to_streamed_response_wrapper(
            media_bridge.create_association,
        )
        self.create_attention_span_event = async_to_streamed_response_wrapper(
            media_bridge.create_attention_span_event,
        )
        self.create_media_played_event = async_to_streamed_response_wrapper(
            media_bridge.create_media_played_event,
        )
        self.create_media_played_percent_event = async_to_streamed_response_wrapper(
            media_bridge.create_media_played_percent_event,
        )
        self.create_object_type = async_to_streamed_response_wrapper(
            media_bridge.create_object_type,
        )
        self.create_oembed_domain = async_to_streamed_response_wrapper(
            media_bridge.create_oembed_domain,
        )
        self.create_property = async_to_streamed_response_wrapper(
            media_bridge.create_property,
        )
        self.create_property_group = async_to_streamed_response_wrapper(
            media_bridge.create_property_group,
        )
        self.create_video_association_definition = async_to_streamed_response_wrapper(
            media_bridge.create_video_association_definition,
        )
        self.delete_association = async_to_streamed_response_wrapper(
            media_bridge.delete_association,
        )
        self.delete_oembed_domain = async_to_streamed_response_wrapper(
            media_bridge.delete_oembed_domain,
        )
        self.delete_property = async_to_streamed_response_wrapper(
            media_bridge.delete_property,
        )
        self.delete_property_group = async_to_streamed_response_wrapper(
            media_bridge.delete_property_group,
        )
        self.get_event_visibility_settings = async_to_streamed_response_wrapper(
            media_bridge.get_event_visibility_settings,
        )
        self.get_oembed_domain = async_to_streamed_response_wrapper(
            media_bridge.get_oembed_domain,
        )
        self.get_property = async_to_streamed_response_wrapper(
            media_bridge.get_property,
        )
        self.get_property_group = async_to_streamed_response_wrapper(
            media_bridge.get_property_group,
        )
        self.get_schema = async_to_streamed_response_wrapper(
            media_bridge.get_schema,
        )
        self.list_object_types_by_media_type = async_to_streamed_response_wrapper(
            media_bridge.list_object_types_by_media_type,
        )
        self.list_oembed_domains = async_to_streamed_response_wrapper(
            media_bridge.list_oembed_domains,
        )
        self.list_properties = async_to_streamed_response_wrapper(
            media_bridge.list_properties,
        )
        self.list_property_groups = async_to_streamed_response_wrapper(
            media_bridge.list_property_groups,
        )
        self.list_schemas = async_to_streamed_response_wrapper(
            media_bridge.list_schemas,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                media_bridge.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_event_visibility_settings = async_to_streamed_response_wrapper(
            media_bridge.update_event_visibility_settings,
        )
        self.update_oembed_domain = async_to_streamed_response_wrapper(
            media_bridge.update_oembed_domain,
        )
        self.update_property = async_to_streamed_response_wrapper(
            media_bridge.update_property,
        )
        self.update_property_group = async_to_streamed_response_wrapper(
            media_bridge.update_property_group,
        )
        self.update_schema = async_to_streamed_response_wrapper(
            media_bridge.update_schema,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            media_bridge.update_settings,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._media_bridge.batch)
