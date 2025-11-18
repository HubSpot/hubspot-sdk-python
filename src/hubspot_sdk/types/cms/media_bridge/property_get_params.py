# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PropertyGetParams"]


class PropertyGetParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    archived: bool
    """Whether to return only results that have been archived."""

    properties: str
    """Limit the response to only include the specified properties."""
