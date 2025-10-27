# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AppListPortalsParams"]


class AppListPortalsParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    limit: int
    """The maximum number of results to return in a single request."""

    start_portal_id: Annotated[int, PropertyInfo(alias="startPortalId")]
    """The initial account ID for listing, enabling pagination."""
