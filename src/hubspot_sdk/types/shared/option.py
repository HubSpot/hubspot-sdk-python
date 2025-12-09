# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Option"]


class Option(BaseModel):
    """The options available when a property is an enumeration"""

    hidden: bool
    """Hidden options will not be displayed in HubSpot."""

    label: str
    """A human-readable option label that will be shown in HubSpot."""

    value: str
    """
    The internal value of the option, which must be used when setting the property
    value through the API.
    """

    description: Optional[str] = None
    """A description of the option."""

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)
    """Options are displayed in order starting with the lowest positive integer value.

    Values of -1 will cause the option to be displayed after any positive values.
    """
