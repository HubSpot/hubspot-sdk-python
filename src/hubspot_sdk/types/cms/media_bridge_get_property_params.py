# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MediaBridgeGetPropertyParams"]


class MediaBridgeGetPropertyParams(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    archived: bool
    """Whether to return only results that have been archived."""

    properties: str
