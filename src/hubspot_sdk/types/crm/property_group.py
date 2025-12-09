# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyGroup"]


class PropertyGroup(BaseModel):
    """An ID for a group of properties"""

    archived: bool

    display_order: int = FieldInfo(alias="displayOrder")
    """
    Property groups are displayed in order starting with the lowest positive integer
    value. Values of -1 will cause the property group to be displayed after any
    positive values.
    """

    label: str
    """A human-readable label that will be shown in HubSpot."""

    name: str
    """
    The internal property group name, which must be used when referencing the
    property group via the API.
    """
