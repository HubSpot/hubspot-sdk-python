# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSpendItem"]


class PublicSpendItem(BaseModel):
    id: str

    amount: float

    created_at: int = FieldInfo(alias="createdAt")

    name: str

    order: int

    updated_at: int = FieldInfo(alias="updatedAt")

    description: Optional[str] = None
