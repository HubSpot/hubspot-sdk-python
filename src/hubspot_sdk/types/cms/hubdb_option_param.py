# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .simple_user_param import SimpleUserParam

__all__ = ["HubdbOptionParam"]


class HubdbOptionParam(TypedDict, total=False):
    """A HubSpot property option"""

    id: Required[str]
    """The unique ID of the option."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]]
    """The timestamp when the option was created, in ISO 8601 format."""

    label: Required[str]
    """A user-friendly label that identifies the option."""

    name: Required[str]
    """An internal name assigned to the option, distinct from the label."""

    order: Required[int]
    """The order in which the option appears, represented as an integer."""

    type: Required[str]
    """Indicates the category or data type of the option (e.g., string, number)."""

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]]
    """The timestamp when the option was last updated, in ISO 8601 format."""

    created_by: Annotated[SimpleUserParam, PropertyInfo(alias="createdBy")]

    created_by_user_id: Annotated[int, PropertyInfo(alias="createdByUserId")]
    """The ID of the user who created the option."""

    updated_by: Annotated[SimpleUserParam, PropertyInfo(alias="updatedBy")]

    updated_by_user_id: Annotated[int, PropertyInfo(alias="updatedByUserId")]
    """The ID of the user who last updated the option."""
