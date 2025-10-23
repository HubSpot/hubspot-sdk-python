# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LandingPageGetParams"]


class LandingPageGetParams(TypedDict, total=False):
    archived: bool
    """Specifies whether to return deleted Landing Pages. Defaults to `false`."""

    property: str
