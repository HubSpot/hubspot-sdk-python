# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LandingPageGetParams"]


class LandingPageGetParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived."""

    property: str
    """A specific property of the landing page to include in the response."""
