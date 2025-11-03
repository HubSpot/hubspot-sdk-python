# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AutomationActionsOption"]


class AutomationActionsOption(BaseModel):
    description: str
    """A description of the option."""

    display_order: int = FieldInfo(alias="displayOrder")
    """The position of the item relative to others in the list."""

    double_data: float = FieldInfo(alias="doubleData")

    hidden: bool
    """Whether the option is displayed in HubSpot's UI."""

    label: str
    """A user-friendly label that identifies the option."""

    read_only: bool = FieldInfo(alias="readOnly")
    """Whether the option is read-only."""

    value: str
    """The actual value of the option."""
