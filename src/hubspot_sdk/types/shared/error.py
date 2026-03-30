# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .error_detail import ErrorDetail

__all__ = ["Error"]


class Error(BaseModel):
    category: str
    """The error category"""

    correlation_id: str = FieldInfo(alias="correlationId")
    """A unique identifier for the request.

    Include this value with any error reports or support tickets
    """

    message: str
    """
    A human readable message describing the error along with remediation steps where
    appropriate
    """

    context: Optional[Dict[str, List[str]]] = None
    """Context about the error condition"""

    errors: Optional[List[ErrorDetail]] = None
    """further information about the error"""

    links: Optional[Dict[str, str]] = None
    """
    A map of link names to associated URIs containing documentation about the error
    or recommended remediation steps
    """

    sub_category: Optional[str] = FieldInfo(alias="subCategory", default=None)
    """A specific category that contains more specific detail about the error"""
