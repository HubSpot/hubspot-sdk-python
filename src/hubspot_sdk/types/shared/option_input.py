# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OptionInput"]


class OptionInput(BaseModel):
    display_order: int = FieldInfo(alias="displayOrder")
    """Options are shown in order starting with the lowest positive integer value.

    Values of -1 will cause the option to be displayed after any positive values.
    """

    hidden: bool
    """Hidden options won't be shown in HubSpot."""

    label: str
    """A human-readable option label that will be shown in HubSpot."""

    value: str
    """
    The internal value of the option, which must be used when setting the property
    value through the API.
    """

    description: Optional[str] = None
    """A description of the option."""
