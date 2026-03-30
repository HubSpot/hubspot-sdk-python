# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContactIDParam"]


class ContactIDParam(TypedDict, total=False):
    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]
    """The ID of the portal associated with the contact."""

    email: str
    """The email address of the contact."""

    vid: int
    """The unique identifier for the contact."""
