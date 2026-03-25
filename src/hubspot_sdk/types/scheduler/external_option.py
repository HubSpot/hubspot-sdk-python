# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalOption"]


class ExternalOption(BaseModel):
    description: str
    """A brief description of the option."""

    display_order: int = FieldInfo(alias="displayOrder")
    """The order in which the option should be displayed."""

    double_data: float = FieldInfo(alias="doubleData")
    """Deprecated property. Will always be 0."""

    hidden: bool
    """Whether the option should be hidden from the user."""

    label: str
    """The text label for the option."""

    read_only: bool = FieldInfo(alias="readOnly")
    """Whether the option is read-only."""

    value: str
    """The value associated with the option."""
