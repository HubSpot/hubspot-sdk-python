# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["MultiLanguageCreateLanguageVariationParams"]


class MultiLanguageCreateLanguageVariationParams(TypedDict, total=False):
    id: Required[str]
    """ID of blog to clone."""

    language: str
    """Target language of new variant."""

    primary_language: Annotated[str, PropertyInfo(alias="primaryLanguage")]
    """Language of primary blog to clone."""

    slug: str
    """Path to this blog."""
