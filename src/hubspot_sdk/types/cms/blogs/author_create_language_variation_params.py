# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .blog_author_param import BlogAuthorParam

__all__ = ["AuthorCreateLanguageVariationParams"]


class AuthorCreateLanguageVariationParams(TypedDict, total=False):
    id: Required[str]
    """ID of the object to be cloned."""

    blog_author: Required[Annotated[BlogAuthorParam, PropertyInfo(alias="blogAuthor")]]
    """Model definition for a Blog Author."""

    language: str
    """Language of newly cloned object."""

    primary_language: Annotated[str, PropertyInfo(alias="primaryLanguage")]
    """Primary language in multi-language group."""
