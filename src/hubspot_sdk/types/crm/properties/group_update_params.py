# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """
    Property groups are displayed in order starting with the lowest positive integer
    value. Values of -1 will cause the property group to be displayed after any
    positive values.
    """

    label: str
    """A human-readable label that will be shown in HubSpot."""
