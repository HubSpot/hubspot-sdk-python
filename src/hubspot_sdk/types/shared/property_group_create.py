# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyGroupCreate"]


class PropertyGroupCreate(BaseModel):
    label: str

    name: str

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)
