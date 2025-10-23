# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SideOrCornerParam"]


class SideOrCornerParam(TypedDict, total=False):
    horizontal_side: Required[Annotated[str, PropertyInfo(alias="horizontalSide")]]

    vertical_side: Required[Annotated[str, PropertyInfo(alias="verticalSide")]]
