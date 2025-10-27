# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRssEmailDetails"]


class PublicRssEmailDetails(BaseModel):
    blog_email_type: Optional[str] = FieldInfo(alias="blogEmailType", default=None)

    blog_image_max_width: Optional[int] = FieldInfo(alias="blogImageMaxWidth", default=None)

    blog_layout: Optional[str] = FieldInfo(alias="blogLayout", default=None)

    hubspot_blog_id: Optional[str] = FieldInfo(alias="hubspotBlogId", default=None)

    max_entries: Optional[int] = FieldInfo(alias="maxEntries", default=None)

    rss_entry_template: Optional[str] = FieldInfo(alias="rssEntryTemplate", default=None)

    timing: Optional[Dict[str, object]] = None

    url: Optional[str] = None

    use_headline_as_subject: Optional[bool] = FieldInfo(alias="useHeadlineAsSubject", default=None)
