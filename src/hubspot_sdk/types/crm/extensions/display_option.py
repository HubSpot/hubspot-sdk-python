# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DisplayOption"]


class DisplayOption(BaseModel):
    """Option definition for STATUS dataTypes."""

    label: str
    """The text that will be displayed to users for this option."""

    name: str
    """JSON-friendly unique name for option."""

    type: Literal["DANGER", "DEFAULT", "INFO", "SUCCESS", "WARNING"]
    """The type of status."""
