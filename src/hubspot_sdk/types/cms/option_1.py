# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Option1"]


class Option1(BaseModel):
    hidden: bool

    label: str

    value: str

    description: Optional[str] = None

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)
