# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SitePageCreateLanguageVariationParams"]


class SitePageCreateLanguageVariationParams(TypedDict, total=False):
    id: Required[str]
    """ID of content to clone."""

    language: str
    """Target language of new variant."""

    primary_language: Annotated[str, PropertyInfo(alias="primaryLanguage")]
    """Language of primary content to clone."""
