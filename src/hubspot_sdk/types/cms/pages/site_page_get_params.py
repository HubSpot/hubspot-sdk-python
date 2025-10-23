# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SitePageGetParams"]


class SitePageGetParams(TypedDict, total=False):
    archived: bool
    """Specifies whether to return deleted Site Pages. Defaults to `false`."""

    property: str
