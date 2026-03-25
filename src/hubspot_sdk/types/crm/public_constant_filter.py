# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicConstantFilter"]


class PublicConstantFilter(BaseModel):
    filter_type: Literal["CONSTANT"] = FieldInfo(alias="filterType")
    """Specifies the type of filter, which is (CONSTANT)."""

    should_accept: bool = FieldInfo(alias="shouldAccept")
    """Indicates whether the filter should accept the condition."""

    source: Optional[str] = None
    """Defines the source of the constant filter."""
