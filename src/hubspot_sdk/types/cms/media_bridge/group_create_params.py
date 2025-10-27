# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    label: Required[str]

    name: Required[str]

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
