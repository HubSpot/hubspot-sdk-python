# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PostCreateLangVariationParams"]


class PostCreateLangVariationParams(TypedDict, total=False):
    id: Required[str]
    """ID of blog post to clone."""

    language: str
    """Target language of new variant."""
