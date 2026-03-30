# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .margin import Margin
from .padding import Padding
from ..._models import BaseModel

__all__ = ["BreakpointStyles"]


class BreakpointStyles(BaseModel):
    hidden: bool
    """Boolean indicating if the breakpoint is visible."""

    margin: Margin

    padding: Padding
