# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PropertyListParams"]


class PropertyListParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    archived: bool
    """Whether to return only results that have been archived."""

    properties: str
    """Filter the response to the specified properties."""
