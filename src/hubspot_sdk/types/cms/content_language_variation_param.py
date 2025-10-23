# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_access_rule_param import PublicAccessRuleParam

__all__ = ["ContentLanguageVariationParam"]


class ContentLanguageVariationParam(TypedDict, total=False):
    id: Required[int]

    archived_in_dashboard: Required[Annotated[bool, PropertyInfo(alias="archivedInDashboard")]]

    author_name: Required[Annotated[str, PropertyInfo(alias="authorName")]]

    campaign: Required[str]

    created: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    name: Required[str]

    password: Required[str]

    public_access_rules: Required[Annotated[Iterable[PublicAccessRuleParam], PropertyInfo(alias="publicAccessRules")]]

    public_access_rules_enabled: Required[Annotated[bool, PropertyInfo(alias="publicAccessRulesEnabled")]]

    publish_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="publishDate", format="iso8601")]]

    slug: Required[str]

    state: Required[str]

    updated: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    tag_ids: Annotated[Iterable[int], PropertyInfo(alias="tagIds")]
