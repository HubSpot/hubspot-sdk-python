# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.error_detail import ErrorDetail

__all__ = ["StandardError1"]


class StandardError1(BaseModel):
    category: str
    """The main category of the error."""

    context: Dict[str, List[str]]
    """Additional context-specific information related to the error."""

    errors: List[ErrorDetail]
    """The detailed error objects."""

    links: Dict[str, str]
    """URLs linking to documentation or resources associated with the error."""

    message: str
    """A human-readable string describing the error and possible remediation steps."""

    status: str
    """The HTTP status code associated with the error."""

    id: Optional[str] = None
    """A unique ID for the error instance."""

    sub_category: Optional[object] = FieldInfo(alias="subCategory", default=None)
    """A more specific error category within each main category."""
