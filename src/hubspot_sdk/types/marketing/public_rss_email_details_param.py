# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRssEmailDetailsParam"]


class PublicRssEmailDetailsParam(TypedDict, total=False):
    blog_email_type: Annotated[str, PropertyInfo(alias="blogEmailType")]

    blog_image_max_width: Annotated[int, PropertyInfo(alias="blogImageMaxWidth")]

    blog_layout: Annotated[str, PropertyInfo(alias="blogLayout")]

    hubspot_blog_id: Annotated[str, PropertyInfo(alias="hubspotBlogId")]

    max_entries: Annotated[int, PropertyInfo(alias="maxEntries")]

    rss_entry_template: Annotated[str, PropertyInfo(alias="rssEntryTemplate")]

    timing: Dict[str, object]

    url: str

    use_headline_as_subject: Annotated[bool, PropertyInfo(alias="useHeadlineAsSubject")]
