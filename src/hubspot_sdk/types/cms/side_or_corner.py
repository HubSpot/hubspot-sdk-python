# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SideOrCorner"]


class SideOrCorner(BaseModel):
    horizontal_side: str = FieldInfo(alias="horizontalSide")

    vertical_side: str = FieldInfo(alias="verticalSide")
