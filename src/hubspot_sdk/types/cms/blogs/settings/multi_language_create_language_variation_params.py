# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["MultiLanguageCreateLanguageVariationParams"]


class MultiLanguageCreateLanguageVariationParams(TypedDict, total=False):
    id: Required[str]

    language: str

    primary_language: Annotated[str, PropertyInfo(alias="primaryLanguage")]

    slug: str
