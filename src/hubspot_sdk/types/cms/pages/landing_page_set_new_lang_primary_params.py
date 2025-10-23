# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LandingPageSetNewLangPrimaryParams"]


class LandingPageSetNewLangPrimaryParams(TypedDict, total=False):
    id: Required[str]
    """ID of object to set as primary in multi-language group."""
