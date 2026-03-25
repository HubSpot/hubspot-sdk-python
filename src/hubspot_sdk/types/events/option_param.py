# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OptionParam"]


class OptionParam(TypedDict, total=False):
    """A HubSpot property option"""

    hidden: Required[bool]
    """Whether the option is displayed in HubSpot's UI."""

    label: Required[str]
    """A user-friendly label that identifies the option."""

    value: Required[str]
    """The actual value of the option."""

    description: str
    """A description of the option."""

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """The position of the item relative to others in the list."""
