# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSpendItem"]


class PublicSpendItem(BaseModel):
    id: str
    """The unique identifier for the spend item, represented as a string."""

    amount: float
    """The monetary amount of the spend item, represented as a number."""

    created_at: int = FieldInfo(alias="createdAt")
    """A Unix timestamp in milliseconds indicating when the spend item was created."""

    name: str
    """The name of the spend item, represented as a string."""

    order: int
    """An integer that specifies the order of the spend item."""

    updated_at: int = FieldInfo(alias="updatedAt")
    """
    A Unix timestamp in milliseconds indicating when the spend item was last
    updated.
    """

    description: Optional[str] = None
    """A brief description of the spend item, represented as a string."""
