# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SideOrCorner"]


class SideOrCorner(BaseModel):
    horizontal_side: Literal["CENTER", "LEFT", "RIGHT"] = FieldInfo(alias="horizontalSide")
    """Specifies the horizontal side of an element."""

    vertical_side: Literal["BOTTOM", "MIDDLE", "TOP"] = FieldInfo(alias="verticalSide")
    """Specifies the vertical side of an element."""
