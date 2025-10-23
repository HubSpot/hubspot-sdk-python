# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuthorAttachToLangGroupParams"]


class AuthorAttachToLangGroupParams(TypedDict, total=False):
    id: Required[str]
    """ID of the object to add to a multi-language group."""

    language: Required[str]
    """Designated language of the object to add to a multi-language group."""

    primary_id: Required[Annotated[str, PropertyInfo(alias="primaryId")]]
    """ID of primary language object in multi-language group."""

    primary_language: Annotated[str, PropertyInfo(alias="primaryLanguage")]
    """Primary language of the multi-language group."""
