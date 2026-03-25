# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .error_detail import ErrorDetail

__all__ = ["StandardError"]


class StandardError(BaseModel):
    """Ye olde error"""

    category: str
    """Error category."""

    context: Dict[str, List[str]]
    """Error context."""

    errors: List[ErrorDetail]
    """List of error details."""

    links: Dict[str, str]
    """Error links."""

    message: str
    """Error message."""

    status: str
    """Error status."""

    id: Optional[str] = None
    """Error ID."""

    sub_category: Optional[object] = FieldInfo(alias="subCategory", default=None)
    """Error subcategory."""
