# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicOptionParam"]


class PublicOptionParam(TypedDict, total=False):
    label: Required[str]
    """A user-friendly label that identifies the option."""

    value: Required[str]
    """The actual value of the option."""

    description: str
    """A description of the option."""

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """The position of the option relative to others in the list."""
