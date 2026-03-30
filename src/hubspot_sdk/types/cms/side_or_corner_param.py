# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SideOrCornerParam"]


class SideOrCornerParam(TypedDict, total=False):
    horizontal_side: Required[Annotated[Literal["CENTER", "LEFT", "RIGHT"], PropertyInfo(alias="horizontalSide")]]
    """Specifies the horizontal side of an element."""

    vertical_side: Required[Annotated[Literal["BOTTOM", "MIDDLE", "TOP"], PropertyInfo(alias="verticalSide")]]
    """Specifies the vertical side of an element."""
