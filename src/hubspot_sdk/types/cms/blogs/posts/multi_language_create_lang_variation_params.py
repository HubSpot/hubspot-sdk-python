# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["MultiLanguageCreateLangVariationParams"]


class MultiLanguageCreateLangVariationParams(TypedDict, total=False):
    id: Required[str]
    """ID of blog post to clone."""

    language: str
    """Target language of new variant."""

    use_published: Annotated[bool, PropertyInfo(alias="usePublished")]
