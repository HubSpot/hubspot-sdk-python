# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List
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
from ....types.cms.media_bridge import (
    integrator_setting_update_app_name_params,
    integrator_setting_register_app_name_params,
    integrator_setting_list_oembed_domains_params,
    integrator_setting_create_oembed_domain_params,
    integrator_setting_delete_oembed_domain_params,
    integrator_setting_update_oembed_domain_params,
    integrator_setting_create_object_definition_params,
    integrator_setting_update_event_visibility_settings_params,
    integrator_setting_get_object_definitions_by_media_type_params,
)
from ....types.cms.endpoints_param import EndpointsParam
from ....types.cms.event_visibility_change import EventVisibilityChange
from ....types.cms.event_visibility_response import EventVisibilityResponse
from ....types.cms.object_definition_response import ObjectDefinitionResponse
from ....types.cms.integrator_o_embed_domain_model import IntegratorOEmbedDomainModel
from ....types.cms.o_embed_domains_collection_response import OEmbedDomainsCollectionResponse
from ....types.cms.bulk_integrator_object_creation_response import BulkIntegratorObjectCreationResponse
from ....types.cms.media_bridge_provider_registration_response import MediaBridgeProviderRegistrationResponse

__all__ = ["IntegratorSettingsResource", "AsyncIntegratorSettingsResource"]


class IntegratorSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegratorSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return IntegratorSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegratorSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return IntegratorSettingsResourceWithStreamingResponse(self)

    def create_object_definition(
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
            f"/media-bridge/v1/{app_id}/settings/object-definitions",
            body=maybe_transform(
                {"media_types": media_types},
                integrator_setting_create_object_definition_params.IntegratorSettingCreateObjectDefinitionParams,
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
            f"/media-bridge/v1/{app_id}/settings/oembed-domains",
            body=maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                integrator_setting_create_oembed_domain_params.IntegratorSettingCreateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
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
          id: The ID of the oEmbed to delete.

          domain_portal_id: Filter response by Hub ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/media-bridge/v1/{app_id}/settings/oembed-domains",
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
                    integrator_setting_delete_oembed_domain_params.IntegratorSettingDeleteOembedDomainParams,
                ),
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
            f"/media-bridge/v1/{app_id}/settings/event-visibility",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVisibilityResponse,
        )

    def get_object_definitions_by_media_type(
        self,
        media_type: Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"],
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
          include_full_definition: Include the full definition in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_type:
            raise ValueError(f"Expected a non-empty value for `media_type` but received {media_type!r}")
        return self._get(
            f"/media-bridge/v1/{app_id}/settings/object-definitions/{media_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_full_definition": include_full_definition},
                    integrator_setting_get_object_definitions_by_media_type_params.IntegratorSettingGetObjectDefinitionsByMediaTypeParams,
                ),
            ),
            cast_to=ObjectDefinitionResponse,
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
            f"/media-bridge/v1/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
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
          domain_portal_id: Filter response by Hub ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/media-bridge/v1/{app_id}/settings/oembed-domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain_portal_id": domain_portal_id},
                    integrator_setting_list_oembed_domains_params.IntegratorSettingListOembedDomainsParams,
                ),
            ),
            cast_to=OEmbedDomainsCollectionResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def register_app_name(
        self,
        app_id: int,
        *,
        updated_at: int,
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
            f"/media-bridge/v1/{app_id}/settings/register",
            body=maybe_transform(
                {
                    "updated_at": updated_at,
                    "name": name,
                },
                integrator_setting_register_app_name_params.IntegratorSettingRegisterAppNameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProviderRegistrationResponse,
        )

    def update_app_name(
        self,
        app_id: int,
        *,
        updated_at: int,
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
            f"/media-bridge/v1/{app_id}/settings",
            body=maybe_transform(
                {
                    "updated_at": updated_at,
                    "name": name,
                },
                integrator_setting_update_app_name_params.IntegratorSettingUpdateAppNameParams,
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
        event_type: Literal["ALL", "MEDIA_PLAYS", "MEDIA_PLAYS_PERCENT", "ATTENTION_SPAN"],
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
            f"/media-bridge/v1/{app_id}/settings/event-visibility",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "updated_at": updated_at,
                    "show_in_reporting": show_in_reporting,
                    "show_in_timeline": show_in_timeline,
                    "show_in_workflows": show_in_workflows,
                },
                integrator_setting_update_event_visibility_settings_params.IntegratorSettingUpdateEventVisibilitySettingsParams,
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
            f"/media-bridge/v1/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
            body=maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                integrator_setting_update_oembed_domain_params.IntegratorSettingUpdateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )


class AsyncIntegratorSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegratorSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegratorSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegratorSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncIntegratorSettingsResourceWithStreamingResponse(self)

    async def create_object_definition(
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
            f"/media-bridge/v1/{app_id}/settings/object-definitions",
            body=await async_maybe_transform(
                {"media_types": media_types},
                integrator_setting_create_object_definition_params.IntegratorSettingCreateObjectDefinitionParams,
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
            f"/media-bridge/v1/{app_id}/settings/oembed-domains",
            body=await async_maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                integrator_setting_create_oembed_domain_params.IntegratorSettingCreateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
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
          id: The ID of the oEmbed to delete.

          domain_portal_id: Filter response by Hub ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/media-bridge/v1/{app_id}/settings/oembed-domains",
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
                    integrator_setting_delete_oembed_domain_params.IntegratorSettingDeleteOembedDomainParams,
                ),
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
            f"/media-bridge/v1/{app_id}/settings/event-visibility",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVisibilityResponse,
        )

    async def get_object_definitions_by_media_type(
        self,
        media_type: Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"],
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
          include_full_definition: Include the full definition in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_type:
            raise ValueError(f"Expected a non-empty value for `media_type` but received {media_type!r}")
        return await self._get(
            f"/media-bridge/v1/{app_id}/settings/object-definitions/{media_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_full_definition": include_full_definition},
                    integrator_setting_get_object_definitions_by_media_type_params.IntegratorSettingGetObjectDefinitionsByMediaTypeParams,
                ),
            ),
            cast_to=ObjectDefinitionResponse,
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
            f"/media-bridge/v1/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
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
          domain_portal_id: Filter response by Hub ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/media-bridge/v1/{app_id}/settings/oembed-domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"domain_portal_id": domain_portal_id},
                    integrator_setting_list_oembed_domains_params.IntegratorSettingListOembedDomainsParams,
                ),
            ),
            cast_to=OEmbedDomainsCollectionResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def register_app_name(
        self,
        app_id: int,
        *,
        updated_at: int,
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
            f"/media-bridge/v1/{app_id}/settings/register",
            body=await async_maybe_transform(
                {
                    "updated_at": updated_at,
                    "name": name,
                },
                integrator_setting_register_app_name_params.IntegratorSettingRegisterAppNameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaBridgeProviderRegistrationResponse,
        )

    async def update_app_name(
        self,
        app_id: int,
        *,
        updated_at: int,
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
            f"/media-bridge/v1/{app_id}/settings",
            body=await async_maybe_transform(
                {
                    "updated_at": updated_at,
                    "name": name,
                },
                integrator_setting_update_app_name_params.IntegratorSettingUpdateAppNameParams,
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
        event_type: Literal["ALL", "MEDIA_PLAYS", "MEDIA_PLAYS_PERCENT", "ATTENTION_SPAN"],
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
            f"/media-bridge/v1/{app_id}/settings/event-visibility",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "updated_at": updated_at,
                    "show_in_reporting": show_in_reporting,
                    "show_in_timeline": show_in_timeline,
                    "show_in_workflows": show_in_workflows,
                },
                integrator_setting_update_event_visibility_settings_params.IntegratorSettingUpdateEventVisibilitySettingsParams,
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
            f"/media-bridge/v1/{app_id}/settings/oembed-domains/{o_embed_domain_id}",
            body=await async_maybe_transform(
                {
                    "endpoints": endpoints,
                    "portal_id": portal_id,
                },
                integrator_setting_update_oembed_domain_params.IntegratorSettingUpdateOembedDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorOEmbedDomainModel,
        )


class IntegratorSettingsResourceWithRawResponse:
    def __init__(self, integrator_settings: IntegratorSettingsResource) -> None:
        self._integrator_settings = integrator_settings

        self.create_object_definition = to_raw_response_wrapper(
            integrator_settings.create_object_definition,
        )
        self.create_oembed_domain = to_raw_response_wrapper(
            integrator_settings.create_oembed_domain,
        )
        self.delete_oembed_domain = to_raw_response_wrapper(
            integrator_settings.delete_oembed_domain,
        )
        self.get_event_visibility_settings = to_raw_response_wrapper(
            integrator_settings.get_event_visibility_settings,
        )
        self.get_object_definitions_by_media_type = to_raw_response_wrapper(
            integrator_settings.get_object_definitions_by_media_type,
        )
        self.get_oembed_domain = to_raw_response_wrapper(
            integrator_settings.get_oembed_domain,
        )
        self.list_oembed_domains = to_raw_response_wrapper(
            integrator_settings.list_oembed_domains,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                integrator_settings.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_app_name = to_raw_response_wrapper(
            integrator_settings.update_app_name,
        )
        self.update_event_visibility_settings = to_raw_response_wrapper(
            integrator_settings.update_event_visibility_settings,
        )
        self.update_oembed_domain = to_raw_response_wrapper(
            integrator_settings.update_oembed_domain,
        )


class AsyncIntegratorSettingsResourceWithRawResponse:
    def __init__(self, integrator_settings: AsyncIntegratorSettingsResource) -> None:
        self._integrator_settings = integrator_settings

        self.create_object_definition = async_to_raw_response_wrapper(
            integrator_settings.create_object_definition,
        )
        self.create_oembed_domain = async_to_raw_response_wrapper(
            integrator_settings.create_oembed_domain,
        )
        self.delete_oembed_domain = async_to_raw_response_wrapper(
            integrator_settings.delete_oembed_domain,
        )
        self.get_event_visibility_settings = async_to_raw_response_wrapper(
            integrator_settings.get_event_visibility_settings,
        )
        self.get_object_definitions_by_media_type = async_to_raw_response_wrapper(
            integrator_settings.get_object_definitions_by_media_type,
        )
        self.get_oembed_domain = async_to_raw_response_wrapper(
            integrator_settings.get_oembed_domain,
        )
        self.list_oembed_domains = async_to_raw_response_wrapper(
            integrator_settings.list_oembed_domains,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                integrator_settings.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_app_name = async_to_raw_response_wrapper(
            integrator_settings.update_app_name,
        )
        self.update_event_visibility_settings = async_to_raw_response_wrapper(
            integrator_settings.update_event_visibility_settings,
        )
        self.update_oembed_domain = async_to_raw_response_wrapper(
            integrator_settings.update_oembed_domain,
        )


class IntegratorSettingsResourceWithStreamingResponse:
    def __init__(self, integrator_settings: IntegratorSettingsResource) -> None:
        self._integrator_settings = integrator_settings

        self.create_object_definition = to_streamed_response_wrapper(
            integrator_settings.create_object_definition,
        )
        self.create_oembed_domain = to_streamed_response_wrapper(
            integrator_settings.create_oembed_domain,
        )
        self.delete_oembed_domain = to_streamed_response_wrapper(
            integrator_settings.delete_oembed_domain,
        )
        self.get_event_visibility_settings = to_streamed_response_wrapper(
            integrator_settings.get_event_visibility_settings,
        )
        self.get_object_definitions_by_media_type = to_streamed_response_wrapper(
            integrator_settings.get_object_definitions_by_media_type,
        )
        self.get_oembed_domain = to_streamed_response_wrapper(
            integrator_settings.get_oembed_domain,
        )
        self.list_oembed_domains = to_streamed_response_wrapper(
            integrator_settings.list_oembed_domains,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                integrator_settings.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_app_name = to_streamed_response_wrapper(
            integrator_settings.update_app_name,
        )
        self.update_event_visibility_settings = to_streamed_response_wrapper(
            integrator_settings.update_event_visibility_settings,
        )
        self.update_oembed_domain = to_streamed_response_wrapper(
            integrator_settings.update_oembed_domain,
        )


class AsyncIntegratorSettingsResourceWithStreamingResponse:
    def __init__(self, integrator_settings: AsyncIntegratorSettingsResource) -> None:
        self._integrator_settings = integrator_settings

        self.create_object_definition = async_to_streamed_response_wrapper(
            integrator_settings.create_object_definition,
        )
        self.create_oembed_domain = async_to_streamed_response_wrapper(
            integrator_settings.create_oembed_domain,
        )
        self.delete_oembed_domain = async_to_streamed_response_wrapper(
            integrator_settings.delete_oembed_domain,
        )
        self.get_event_visibility_settings = async_to_streamed_response_wrapper(
            integrator_settings.get_event_visibility_settings,
        )
        self.get_object_definitions_by_media_type = async_to_streamed_response_wrapper(
            integrator_settings.get_object_definitions_by_media_type,
        )
        self.get_oembed_domain = async_to_streamed_response_wrapper(
            integrator_settings.get_oembed_domain,
        )
        self.list_oembed_domains = async_to_streamed_response_wrapper(
            integrator_settings.list_oembed_domains,
        )
        self.register_app_name = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                integrator_settings.register_app_name,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update_app_name = async_to_streamed_response_wrapper(
            integrator_settings.update_app_name,
        )
        self.update_event_visibility_settings = async_to_streamed_response_wrapper(
            integrator_settings.update_event_visibility_settings,
        )
        self.update_oembed_domain = async_to_streamed_response_wrapper(
            integrator_settings.update_oembed_domain,
        )
