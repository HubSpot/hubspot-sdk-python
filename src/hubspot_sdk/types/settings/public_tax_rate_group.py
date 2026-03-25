# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTaxRateGroup"]


class PublicTaxRateGroup(BaseModel):
    id: str
    """The unique identifier for the tax rate."""

    active: bool
    """Indicates whether the tax rate group is currently active."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the tax rate was created."""

    label: str
    """The display label for the tax rate."""

    name: str
    """The name of the tax rate."""

    percentage_rate: float = FieldInfo(alias="percentageRate")
    """The percentage rate applied."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the tax rate was last updated."""
