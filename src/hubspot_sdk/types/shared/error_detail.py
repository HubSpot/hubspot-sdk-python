# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ErrorDetail"]


class ErrorDetail(BaseModel):
    message: str
    """
    A human readable message describing the error along with remediation steps where
    appropriate
    """

    code: Optional[str] = None
    """The status code associated with the error detail"""

    context: Optional[Dict[str, List[str]]] = None
    """Context about the error condition"""

    in_: Optional[str] = FieldInfo(alias="in", default=None)
    """The name of the field or parameter in which the error was found."""

    sub_category: Optional[str] = FieldInfo(alias="subCategory", default=None)
    """A specific category that contains more specific detail about the error"""
