# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ...types.cms import url_mapping_create_params
from ..._base_client import make_request_options

__all__ = ["URLMappingsResource", "AsyncURLMappingsResource"]


class URLMappingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return URLMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return URLMappingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: int,
        cdn_purge_embargo_time: int,
        content_group_id: int,
        cos_object_type: Literal[
            "ACCESS_GROUP_MEMBERSHIP",
            "APP_PAGE",
            "BLOCK",
            "BLOG",
            "BLOG_AUTHOR",
            "BRAND_BUSINESS_UNIT",
            "BRAND_SETTINGS",
            "CONTACT_MEMBERSHIP",
            "CONTENT",
            "CONTENT_EMBED",
            "CONTENT_FOLDER",
            "CONTENT_GROUP",
            "CRM_OBJECT",
            "CRM_OBJECT_TYPE",
            "CUSTOM_WIDGET",
            "CUSTOMER_PORTAL",
            "DATA_QUERY",
            "DESIGN_FOLDER",
            "DOMAIN",
            "DOMAIN_SETTINGS",
            "EMAIL_ADDRESS",
            "EXTENSION_RESOURCE",
            "FILE",
            "FOLDER",
            "FOLLOW_ME",
            "FORM",
            "GLOBAL_CONTENT",
            "HUBDB_TABLE",
            "HUBDB_TABLE_ROW",
            "IMAGE",
            "JS_PROJECT_COMPONENT",
            "KNOWLEDGE_BASE",
            "KNOWLEDGE_CATEGORY",
            "KNOWLEDGE_CATEGORY_TRANSLATION",
            "KNOWLEDGE_HOMEPAGE_CATEGORY",
            "LAYOUT",
            "LAYOUT_SECTION",
            "LIST_MEMBERSHIP",
            "MARKETPLACE_LISTING",
            "PASSWORD_PROTECTED",
            "PAYMENT",
            "PERSONALIZATION_TOKEN",
            "PLACEMENT",
            "PROJECT",
            "QUOTE_TEMPLATE",
            "RAW_ASSET",
            "REDIRECT_URL",
            "SECTION",
            "SERVERLESS_FUNCTION",
            "SITE_MAP",
            "SITE_MENU",
            "SITE_SETTINGS",
            "SUBSCRIPTIONS_SETTINGS",
            "TAG",
            "THEME",
            "THEME_SETTINGS",
            "UNRESTRICTED_ACCESS",
            "URL_MAPPING",
            "VIDEO_PLAYER",
            "WIDGET",
            "WORKFLOW",
        ],
        created: int,
        created_by_id: int,
        deleted_at: int,
        destination: str,
        internally_created: bool,
        is_active: bool,
        is_match_full_url: bool,
        is_match_query_string: bool,
        is_only_after_not_found: bool,
        is_pattern: bool,
        is_protocol_agnostic: bool,
        is_regex: bool,
        is_trailing_slash_optional: bool,
        label: str,
        last_used_at: int,
        name: str,
        note: str,
        portal_id: int,
        precedence: int,
        redirect_style: int,
        route_prefix: str,
        updated: int,
        updated_by_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Create a new URL mapping in your HubSpot account.

        This endpoint allows you to
        define URL redirections and mappings, which can be useful for managing site
        navigation and SEO. The request body must include all required properties of the
        UrlMapping schema.

        Args:
          id: The unique identifier for the URL mapping, represented as a 64-bit integer.

          cdn_purge_embargo_time: A Unix timestamp in milliseconds indicating the embargo time for CDN purge
              related to the URL mapping.

          content_group_id: A 64-bit integer representing the content group associated with the URL mapping.

          cos_object_type: A string representing the type of content object associated with the URL
              mapping. Valid values include various content types such as 'CONTENT', 'LAYOUT',
              'FILE', etc.

          created: A Unix timestamp in milliseconds indicating when the URL mapping was created.

          created_by_id: The identifier of the user who created the URL mapping.

          deleted_at: A Unix timestamp in milliseconds indicating when the URL mapping was deleted.

          destination: The destination URL to which the routePrefix is redirected.

          internally_created: A boolean indicating if the URL mapping was created internally by the system.

          is_active: A boolean indicating if the URL mapping is currently active.

          is_match_full_url: A boolean indicating if the full URL should be matched.

          is_match_query_string: A boolean indicating if the query string should be matched.

          is_only_after_not_found: A boolean indicating if the mapping should only be applied after a 404 Not Found
              response.

          is_pattern: A boolean indicating if the routePrefix is a pattern.

          is_protocol_agnostic: A boolean indicating if the mapping should ignore the URL protocol (http/https).

          is_regex: A boolean indicating if the routePrefix should be treated as a regular
              expression.

          is_trailing_slash_optional: A boolean indicating if the trailing slash in the URL is optional.

          label: A label for the URL mapping.

          name: The name of the URL mapping.

          note: A string containing notes about the URL mapping.

          portal_id: The identifier for the HubSpot portal associated with this URL mapping.

          precedence: An integer representing the precedence of the URL mapping, used to determine
              order of evaluation.

          redirect_style: An integer representing the style of redirection used.

          route_prefix: The prefix of the URL path that is being mapped.

          updated: A Unix timestamp in milliseconds indicating when the URL mapping was last
              updated.

          updated_by_id: The identifier of the user who last updated the URL mapping.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/url-mappings/2026-03/url-mappings",
            body=maybe_transform(
                {
                    "id": id,
                    "cdn_purge_embargo_time": cdn_purge_embargo_time,
                    "content_group_id": content_group_id,
                    "cos_object_type": cos_object_type,
                    "created": created,
                    "created_by_id": created_by_id,
                    "deleted_at": deleted_at,
                    "destination": destination,
                    "internally_created": internally_created,
                    "is_active": is_active,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_regex": is_regex,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "label": label,
                    "last_used_at": last_used_at,
                    "name": name,
                    "note": note,
                    "portal_id": portal_id,
                    "precedence": precedence,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                },
                url_mapping_create_params.URLMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Retrieve a list of URL mappings from the HubSpot account.

        This endpoint provides
        access to URL mapping configurations, which can be used to manage and redirect
        URLs within the HubSpot CMS. It is useful for understanding how URLs are
        structured and redirected in your content management setup.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/url-mappings/2026-03/url-mappings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific URL mapping in your HubSpot account using its unique
        identifier. This operation will remove the URL mapping permanently, and it
        requires appropriate write and delete permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Retrieve a specific URL mapping by its unique identifier.

        This endpoint is
        useful for obtaining details about a particular URL mapping configuration within
        your HubSpot account. It requires the ID of the URL mapping as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncURLMappingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncURLMappingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: int,
        cdn_purge_embargo_time: int,
        content_group_id: int,
        cos_object_type: Literal[
            "ACCESS_GROUP_MEMBERSHIP",
            "APP_PAGE",
            "BLOCK",
            "BLOG",
            "BLOG_AUTHOR",
            "BRAND_BUSINESS_UNIT",
            "BRAND_SETTINGS",
            "CONTACT_MEMBERSHIP",
            "CONTENT",
            "CONTENT_EMBED",
            "CONTENT_FOLDER",
            "CONTENT_GROUP",
            "CRM_OBJECT",
            "CRM_OBJECT_TYPE",
            "CUSTOM_WIDGET",
            "CUSTOMER_PORTAL",
            "DATA_QUERY",
            "DESIGN_FOLDER",
            "DOMAIN",
            "DOMAIN_SETTINGS",
            "EMAIL_ADDRESS",
            "EXTENSION_RESOURCE",
            "FILE",
            "FOLDER",
            "FOLLOW_ME",
            "FORM",
            "GLOBAL_CONTENT",
            "HUBDB_TABLE",
            "HUBDB_TABLE_ROW",
            "IMAGE",
            "JS_PROJECT_COMPONENT",
            "KNOWLEDGE_BASE",
            "KNOWLEDGE_CATEGORY",
            "KNOWLEDGE_CATEGORY_TRANSLATION",
            "KNOWLEDGE_HOMEPAGE_CATEGORY",
            "LAYOUT",
            "LAYOUT_SECTION",
            "LIST_MEMBERSHIP",
            "MARKETPLACE_LISTING",
            "PASSWORD_PROTECTED",
            "PAYMENT",
            "PERSONALIZATION_TOKEN",
            "PLACEMENT",
            "PROJECT",
            "QUOTE_TEMPLATE",
            "RAW_ASSET",
            "REDIRECT_URL",
            "SECTION",
            "SERVERLESS_FUNCTION",
            "SITE_MAP",
            "SITE_MENU",
            "SITE_SETTINGS",
            "SUBSCRIPTIONS_SETTINGS",
            "TAG",
            "THEME",
            "THEME_SETTINGS",
            "UNRESTRICTED_ACCESS",
            "URL_MAPPING",
            "VIDEO_PLAYER",
            "WIDGET",
            "WORKFLOW",
        ],
        created: int,
        created_by_id: int,
        deleted_at: int,
        destination: str,
        internally_created: bool,
        is_active: bool,
        is_match_full_url: bool,
        is_match_query_string: bool,
        is_only_after_not_found: bool,
        is_pattern: bool,
        is_protocol_agnostic: bool,
        is_regex: bool,
        is_trailing_slash_optional: bool,
        label: str,
        last_used_at: int,
        name: str,
        note: str,
        portal_id: int,
        precedence: int,
        redirect_style: int,
        route_prefix: str,
        updated: int,
        updated_by_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Create a new URL mapping in your HubSpot account.

        This endpoint allows you to
        define URL redirections and mappings, which can be useful for managing site
        navigation and SEO. The request body must include all required properties of the
        UrlMapping schema.

        Args:
          id: The unique identifier for the URL mapping, represented as a 64-bit integer.

          cdn_purge_embargo_time: A Unix timestamp in milliseconds indicating the embargo time for CDN purge
              related to the URL mapping.

          content_group_id: A 64-bit integer representing the content group associated with the URL mapping.

          cos_object_type: A string representing the type of content object associated with the URL
              mapping. Valid values include various content types such as 'CONTENT', 'LAYOUT',
              'FILE', etc.

          created: A Unix timestamp in milliseconds indicating when the URL mapping was created.

          created_by_id: The identifier of the user who created the URL mapping.

          deleted_at: A Unix timestamp in milliseconds indicating when the URL mapping was deleted.

          destination: The destination URL to which the routePrefix is redirected.

          internally_created: A boolean indicating if the URL mapping was created internally by the system.

          is_active: A boolean indicating if the URL mapping is currently active.

          is_match_full_url: A boolean indicating if the full URL should be matched.

          is_match_query_string: A boolean indicating if the query string should be matched.

          is_only_after_not_found: A boolean indicating if the mapping should only be applied after a 404 Not Found
              response.

          is_pattern: A boolean indicating if the routePrefix is a pattern.

          is_protocol_agnostic: A boolean indicating if the mapping should ignore the URL protocol (http/https).

          is_regex: A boolean indicating if the routePrefix should be treated as a regular
              expression.

          is_trailing_slash_optional: A boolean indicating if the trailing slash in the URL is optional.

          label: A label for the URL mapping.

          name: The name of the URL mapping.

          note: A string containing notes about the URL mapping.

          portal_id: The identifier for the HubSpot portal associated with this URL mapping.

          precedence: An integer representing the precedence of the URL mapping, used to determine
              order of evaluation.

          redirect_style: An integer representing the style of redirection used.

          route_prefix: The prefix of the URL path that is being mapped.

          updated: A Unix timestamp in milliseconds indicating when the URL mapping was last
              updated.

          updated_by_id: The identifier of the user who last updated the URL mapping.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/url-mappings/2026-03/url-mappings",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "cdn_purge_embargo_time": cdn_purge_embargo_time,
                    "content_group_id": content_group_id,
                    "cos_object_type": cos_object_type,
                    "created": created,
                    "created_by_id": created_by_id,
                    "deleted_at": deleted_at,
                    "destination": destination,
                    "internally_created": internally_created,
                    "is_active": is_active,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_regex": is_regex,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "label": label,
                    "last_used_at": last_used_at,
                    "name": name,
                    "note": note,
                    "portal_id": portal_id,
                    "precedence": precedence,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                },
                url_mapping_create_params.URLMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Retrieve a list of URL mappings from the HubSpot account.

        This endpoint provides
        access to URL mapping configurations, which can be used to manage and redirect
        URLs within the HubSpot CMS. It is useful for understanding how URLs are
        structured and redirected in your content management setup.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/url-mappings/2026-03/url-mappings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific URL mapping in your HubSpot account using its unique
        identifier. This operation will remove the URL mapping permanently, and it
        requires appropriate write and delete permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Retrieve a specific URL mapping by its unique identifier.

        This endpoint is
        useful for obtaining details about a particular URL mapping configuration within
        your HubSpot account. It requires the ID of the URL mapping as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/url-mappings/2026-03/url-mappings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class URLMappingsResourceWithRawResponse:
    def __init__(self, url_mappings: URLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = to_custom_raw_response_wrapper(
            url_mappings.create,
            BinaryAPIResponse,
        )
        self.list = to_custom_raw_response_wrapper(
            url_mappings.list,
            BinaryAPIResponse,
        )
        self.delete = to_raw_response_wrapper(
            url_mappings.delete,
        )
        self.get = to_custom_raw_response_wrapper(
            url_mappings.get,
            BinaryAPIResponse,
        )


class AsyncURLMappingsResourceWithRawResponse:
    def __init__(self, url_mappings: AsyncURLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = async_to_custom_raw_response_wrapper(
            url_mappings.create,
            AsyncBinaryAPIResponse,
        )
        self.list = async_to_custom_raw_response_wrapper(
            url_mappings.list,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_raw_response_wrapper(
            url_mappings.delete,
        )
        self.get = async_to_custom_raw_response_wrapper(
            url_mappings.get,
            AsyncBinaryAPIResponse,
        )


class URLMappingsResourceWithStreamingResponse:
    def __init__(self, url_mappings: URLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = to_custom_streamed_response_wrapper(
            url_mappings.create,
            StreamedBinaryAPIResponse,
        )
        self.list = to_custom_streamed_response_wrapper(
            url_mappings.list,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_streamed_response_wrapper(
            url_mappings.delete,
        )
        self.get = to_custom_streamed_response_wrapper(
            url_mappings.get,
            StreamedBinaryAPIResponse,
        )


class AsyncURLMappingsResourceWithStreamingResponse:
    def __init__(self, url_mappings: AsyncURLMappingsResource) -> None:
        self._url_mappings = url_mappings

        self.create = async_to_custom_streamed_response_wrapper(
            url_mappings.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list = async_to_custom_streamed_response_wrapper(
            url_mappings.list,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_streamed_response_wrapper(
            url_mappings.delete,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            url_mappings.get,
            AsyncStreamedBinaryAPIResponse,
        )
