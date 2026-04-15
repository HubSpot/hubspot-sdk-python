# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["URLMappingCreateParams"]


class URLMappingCreateParams(TypedDict, total=False):
    id: Required[int]
    """The unique identifier for the URL mapping, represented as a 64-bit integer."""

    cdn_purge_embargo_time: Required[Annotated[int, PropertyInfo(alias="cdnPurgeEmbargoTime")]]
    """
    A Unix timestamp in milliseconds indicating the embargo time for CDN purge
    related to the URL mapping.
    """

    content_group_id: Required[Annotated[int, PropertyInfo(alias="contentGroupId")]]
    """
    A 64-bit integer representing the content group associated with the URL mapping.
    """

    cos_object_type: Required[
        Annotated[
            Literal[
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
            PropertyInfo(alias="cosObjectType"),
        ]
    ]
    """A string representing the type of content object associated with the URL
    mapping.

    Valid values include various content types such as 'CONTENT', 'LAYOUT', 'FILE',
    etc.
    """

    created: Required[int]
    """A Unix timestamp in milliseconds indicating when the URL mapping was created."""

    created_by_id: Required[Annotated[int, PropertyInfo(alias="createdById")]]
    """The identifier of the user who created the URL mapping."""

    deleted_at: Required[Annotated[int, PropertyInfo(alias="deletedAt")]]
    """A Unix timestamp in milliseconds indicating when the URL mapping was deleted."""

    destination: Required[str]
    """The destination URL to which the routePrefix is redirected."""

    internally_created: Required[Annotated[bool, PropertyInfo(alias="internallyCreated")]]
    """A boolean indicating if the URL mapping was created internally by the system."""

    is_active: Required[Annotated[bool, PropertyInfo(alias="isActive")]]
    """A boolean indicating if the URL mapping is currently active."""

    is_match_full_url: Required[Annotated[bool, PropertyInfo(alias="isMatchFullUrl")]]
    """A boolean indicating if the full URL should be matched."""

    is_match_query_string: Required[Annotated[bool, PropertyInfo(alias="isMatchQueryString")]]
    """A boolean indicating if the query string should be matched."""

    is_only_after_not_found: Required[Annotated[bool, PropertyInfo(alias="isOnlyAfterNotFound")]]
    """
    A boolean indicating if the mapping should only be applied after a 404 Not Found
    response.
    """

    is_pattern: Required[Annotated[bool, PropertyInfo(alias="isPattern")]]
    """A boolean indicating if the routePrefix is a pattern."""

    is_protocol_agnostic: Required[Annotated[bool, PropertyInfo(alias="isProtocolAgnostic")]]
    """
    A boolean indicating if the mapping should ignore the URL protocol (http/https).
    """

    is_regex: Required[Annotated[bool, PropertyInfo(alias="isRegex")]]
    """
    A boolean indicating if the routePrefix should be treated as a regular
    expression.
    """

    is_trailing_slash_optional: Required[Annotated[bool, PropertyInfo(alias="isTrailingSlashOptional")]]
    """A boolean indicating if the trailing slash in the URL is optional."""

    label: Required[str]
    """A label for the URL mapping."""

    last_used_at: Required[Annotated[int, PropertyInfo(alias="lastUsedAt")]]

    name: Required[str]
    """The name of the URL mapping."""

    note: Required[str]
    """A string containing notes about the URL mapping."""

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]
    """The identifier for the HubSpot portal associated with this URL mapping."""

    precedence: Required[int]
    """
    An integer representing the precedence of the URL mapping, used to determine
    order of evaluation.
    """

    redirect_style: Required[Annotated[int, PropertyInfo(alias="redirectStyle")]]
    """An integer representing the style of redirection used."""

    route_prefix: Required[Annotated[str, PropertyInfo(alias="routePrefix")]]
    """The prefix of the URL path that is being mapped."""

    updated: Required[int]
    """
    A Unix timestamp in milliseconds indicating when the URL mapping was last
    updated.
    """

    updated_by_id: Required[Annotated[int, PropertyInfo(alias="updatedById")]]
    """The identifier of the user who last updated the URL mapping."""
