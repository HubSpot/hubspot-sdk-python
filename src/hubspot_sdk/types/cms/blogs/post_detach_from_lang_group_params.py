# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PostDetachFromLangGroupParams"]


class PostDetachFromLangGroupParams(TypedDict, total=False):
    id: Required[str]
    """ID of the object to remove from a multi-language group."""
