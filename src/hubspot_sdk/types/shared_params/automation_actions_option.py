# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AutomationActionsOption"]


class AutomationActionsOption(TypedDict, total=False):
    """A HubSpot property option"""

    description: Required[str]
    """A description of the option."""

    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]
    """The position of the item relative to others in the list."""

    double_data: Required[Annotated[float, PropertyInfo(alias="doubleData")]]
    """A numerical value associated with the option."""

    hidden: Required[bool]
    """Whether the option is displayed in HubSpot's UI."""

    label: Required[str]
    """A user-friendly label that identifies the option."""

    read_only: Required[Annotated[bool, PropertyInfo(alias="readOnly")]]
    """Whether the option is read-only."""

    value: Required[str]
    """The actual value of the option."""
