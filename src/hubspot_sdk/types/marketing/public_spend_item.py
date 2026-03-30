# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSpendItem"]


class PublicSpendItem(BaseModel):
    id: str
    """Unique identifier for the spend item."""

    amount: float
    """The monetary value associated with the spend item."""

    created_at: int = FieldInfo(alias="createdAt")
    """The timestamp indicating when the spend item was created."""

    name: str
    """The name assigned to the spend item."""

    order: int
    """The sequence order of the spend item, where 0 is the oldest."""

    updated_at: int = FieldInfo(alias="updatedAt")
    """The timestamp indicating when the spend item was last updated."""

    description: Optional[str] = None
    """A detailed explanation or notes about the spend item."""
