# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PagesContentLanguageVariation"]


class PagesContentLanguageVariation(BaseModel):
    id: int

    archived_in_dashboard: bool = FieldInfo(alias="archivedInDashboard")

    author_name: str = FieldInfo(alias="authorName")

    campaign: str

    created: datetime

    name: str

    password: str

    public_access_rules: List[object] = FieldInfo(alias="publicAccessRules")

    public_access_rules_enabled: bool = FieldInfo(alias="publicAccessRulesEnabled")

    publish_date: datetime = FieldInfo(alias="publishDate")

    slug: str

    state: str

    updated: datetime

    tag_ids: Optional[List[int]] = FieldInfo(alias="tagIds", default=None)
