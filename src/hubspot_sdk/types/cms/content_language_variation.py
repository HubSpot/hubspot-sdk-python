# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContentLanguageVariation"]


class ContentLanguageVariation(BaseModel):
    id: int
    """ID of object to set as primary in multi-language group."""

    archived_in_dashboard: bool = FieldInfo(alias="archivedInDashboard")
    """
    If True, the variant will not show up in your dashboard, although the post could
    still be live.
    """

    author_name: str = FieldInfo(alias="authorName")
    """The name of the user who last published the blog post.

    For posts that haven't been published yet, this property will reflect the user
    who initially created the draft.
    """

    campaign: str
    """The GUID of the marketing campaign this page is a part of."""

    campaign_name: str = FieldInfo(alias="campaignName")
    """Name of the associated marketing campaign."""

    created: datetime
    """The timestamp (ISO8601 format) when this Blog Post was created."""

    name: str
    """The internal name of the content language variation."""

    password: str
    """Set this to create a password protected page.

    Entering the password will be required to view the page.
    """

    public_access_rules: List[object] = FieldInfo(alias="publicAccessRules")

    public_access_rules_enabled: bool = FieldInfo(alias="publicAccessRulesEnabled")
    """Boolean to determine whether or not to respect publicAccessRules."""

    publish_date: datetime = FieldInfo(alias="publishDate")
    """The date (ISO8601 format) the page is to be published at."""

    slug: str
    """The path of the this page.

    This field is appended to the domain to construct the url of this page.
    """

    state: str
    """An ENUM describing the current state of this page.

    Maximum string length: 25
    """

    updated: datetime
    """The timestamp (ISO8601 format) when this Blog Post was updated."""

    tag_ids: Optional[List[int]] = FieldInfo(alias="tagIds", default=None)
