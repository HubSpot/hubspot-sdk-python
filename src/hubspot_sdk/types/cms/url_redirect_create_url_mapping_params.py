# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["URLRedirectCreateURLMappingParams"]


class URLRedirectCreateURLMappingParams(TypedDict, total=False):
    id: Required[str]
    """The unique ID of this URL redirect."""

    created: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date and time when the URL mapping was initially created."""

    destination: Required[str]
    """
    The destination URL, where the target URL should be redirected if it matches the
    `routePrefix`.
    """

    is_match_full_url: Required[Annotated[bool, PropertyInfo(alias="isMatchFullUrl")]]
    """Whether the `routePrefix` should match on the entire URL, including the domain."""

    is_match_query_string: Required[Annotated[bool, PropertyInfo(alias="isMatchQueryString")]]
    """
    Whether the `routePrefix` should match on the entire URL path, including the
    query string.
    """

    is_only_after_not_found: Required[Annotated[bool, PropertyInfo(alias="isOnlyAfterNotFound")]]
    """
    Whether the URL redirect mapping should apply only if a live page on the URL
    isn't found. If False, the URL redirect mapping will take precedence over any
    existing page.
    """

    is_pattern: Required[Annotated[bool, PropertyInfo(alias="isPattern")]]
    """Whether the `routePrefix` should match based on pattern."""

    is_protocol_agnostic: Required[Annotated[bool, PropertyInfo(alias="isProtocolAgnostic")]]
    """Whether the `routePrefix` should match both HTTP and HTTPS protocols."""

    is_trailing_slash_optional: Required[Annotated[bool, PropertyInfo(alias="isTrailingSlashOptional")]]
    """Whether a trailing slash will be ignored."""

    precedence: Required[int]
    """Used to prioritize URL redirection.

    If a given URL matches more than one redirect, the one with the **lower**
    precedence will be used.
    """

    redirect_style: Required[Annotated[int, PropertyInfo(alias="redirectStyle")]]
    """The type of redirect to create.

    Options include: 301 (permanent), 302 (temporary), or 305 (proxy). Find more
    details
    [here](https://knowledge.hubspot.com/cos-general/how-to-redirect-a-hubspot-page).
    """

    route_prefix: Required[Annotated[str, PropertyInfo(alias="routePrefix")]]
    """The target incoming URL, path, or pattern to match for redirection."""

    updated: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date and time when the URL mapping was last modified."""
