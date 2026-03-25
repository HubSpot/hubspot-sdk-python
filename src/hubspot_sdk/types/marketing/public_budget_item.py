# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicBudgetItem"]


class PublicBudgetItem(BaseModel):
    id: str
    """The unique identifier for the budget item."""

    amount: float
    """The monetary amount allocated for the budget item."""

    created_at: int = FieldInfo(alias="createdAt")
    """The timestamp when the budget item was created."""

    name: str
    """The name of the budget item."""

    order: int
    """The order of the budget item, indicating its sequence based on creation date."""

    updated_at: int = FieldInfo(alias="updatedAt")
    """The timestamp when the budget item was last updated."""

    description: Optional[str] = None
    """A description of the budget item."""
