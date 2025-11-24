# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SiteSearchGetIndexedDataParams"]


class SiteSearchGetIndexedDataParams(TypedDict, total=False):
    type: Literal["BLOG_POST", "KNOWLEDGE_ARTICLE", "LANDING_PAGE", "LISTING_PAGE", "SITE_PAGE"]
    """The type of document.

    Can be one of `SITE_PAGE`, `BLOG_POST`, or `KNOWLEDGE_ARTICLE`.
    """
