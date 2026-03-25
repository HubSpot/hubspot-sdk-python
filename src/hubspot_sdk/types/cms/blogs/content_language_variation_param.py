# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..public_access_rule_param import PublicAccessRuleParam

__all__ = ["ContentLanguageVariationParam"]


class ContentLanguageVariationParam(TypedDict, total=False):
    id: Required[int]
    """The unique ID of the content language variation."""

    archived_in_dashboard: Required[Annotated[bool, PropertyInfo(alias="archivedInDashboard")]]
    """
    If True, the variant will not show up in your dashboard, although the post could
    still be live.
    """

    author_name: Required[Annotated[str, PropertyInfo(alias="authorName")]]
    """The name of the user who last published the blog post.

    For posts that haven't been published yet, this property will reflect the user
    who initially created the draft.
    """

    campaign: Required[str]
    """The GUID of the marketing campaign this page is a part of."""

    campaign_name: Required[Annotated[str, PropertyInfo(alias="campaignName")]]
    """Name of the associated marketing campaign."""

    created: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp (ISO8601 format) when this Blog Post was created."""

    name: Required[str]
    """The internal name of the content language variation."""

    password: Required[str]
    """Set this to create a password protected page.

    Entering the password will be required to view the page.
    """

    public_access_rules: Required[Annotated[Iterable[PublicAccessRuleParam], PropertyInfo(alias="publicAccessRules")]]

    public_access_rules_enabled: Required[Annotated[bool, PropertyInfo(alias="publicAccessRulesEnabled")]]
    """Boolean to determine whether or not to respect publicAccessRules."""

    publish_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="publishDate", format="iso8601")]]
    """The date (ISO8601 format) the page is to be published at."""

    slug: Required[str]
    """The path of the this page.

    This field is appended to the domain to construct the url of this page.
    """

    state: Required[str]
    """An ENUM describing the current state of this page.

    Maximum string length: 25
    """

    updated: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp (ISO8601 format) when this Blog Post was updated."""

    tag_ids: Annotated[Iterable[int], PropertyInfo(alias="tagIds")]
