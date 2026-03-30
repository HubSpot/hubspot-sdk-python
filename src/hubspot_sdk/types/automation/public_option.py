# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicOption"]


class PublicOption(BaseModel):
    label: str
    """A user-friendly label that identifies the option."""

    value: str
    """The actual value of the option."""

    description: Optional[str] = None
    """A description of the option."""

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)
    """The position of the option relative to others in the list."""
