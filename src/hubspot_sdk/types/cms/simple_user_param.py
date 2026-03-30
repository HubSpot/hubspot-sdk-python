# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SimpleUserParam"]


class SimpleUserParam(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the user."""

    email: Required[str]
    """The email address of the user."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The first name of the user."""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """The last name of the user."""
