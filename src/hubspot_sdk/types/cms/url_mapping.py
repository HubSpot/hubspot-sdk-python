# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["URLMapping"]


class URLMapping(BaseModel):
    id: str
    """The unique ID of this URL redirect."""

    destination: str
    """
    The destination URL, where the target URL should be redirected if it matches the
    `routePrefix`.
    """

    is_match_full_url: bool = FieldInfo(alias="isMatchFullUrl")
    """Whether the `routePrefix` should match on the entire URL, including the domain."""

    is_match_query_string: bool = FieldInfo(alias="isMatchQueryString")
    """
    Whether the `routePrefix` should match on the entire URL path, including the
    query string.
    """

    is_only_after_not_found: bool = FieldInfo(alias="isOnlyAfterNotFound")
    """
    Whether the URL redirect mapping should apply only if a live page on the URL
    isn't found. If False, the URL redirect mapping will take precedence over any
    existing page.
    """

    is_pattern: bool = FieldInfo(alias="isPattern")
    """Whether the `routePrefix` should match based on pattern."""

    is_protocol_agnostic: bool = FieldInfo(alias="isProtocolAgnostic")
    """Whether the `routePrefix` should match both HTTP and HTTPS protocols."""

    is_trailing_slash_optional: bool = FieldInfo(alias="isTrailingSlashOptional")
    """Whether a trailing slash will be ignored."""

    precedence: int
    """Used to prioritize URL redirection.

    If a given URL matches more than one redirect, the one with the **lower**
    precedence will be used.
    """

    redirect_style: int = FieldInfo(alias="redirectStyle")
    """The type of redirect to create.

    Options include: 301 (permanent), 302 (temporary), or 305 (proxy). Find more
    details
    [here](https://knowledge.hubspot.com/cos-general/how-to-redirect-a-hubspot-page).
    """

    route_prefix: str = FieldInfo(alias="routePrefix")
    """The target incoming URL, path, or pattern to match for redirection."""

    created: Optional[datetime] = None

    updated: Optional[datetime] = None
