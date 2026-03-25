# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TagCreateLangVariationParams"]


class TagCreateLangVariationParams(TypedDict, total=False):
    id: Required[str]
    """ID of the object to be cloned."""

    name: Required[str]
    """Name of newly cloned blog tag."""

    language: str
    """Target language of new variant."""

    primary_language: Annotated[str, PropertyInfo(alias="primaryLanguage")]
    """Language of primary blog tag to clone."""
