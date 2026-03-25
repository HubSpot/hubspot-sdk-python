# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicYearReference"]


class PublicYearReference(BaseModel):
    day: int
    """The day component of the year reference."""

    month: int
    """The month component of the year reference."""

    reference_type: Literal["YEAR"] = FieldInfo(alias="referenceType")
    """Indicates the type of reference (YEAR)."""

    hour: Optional[int] = None
    """The hour component of the year reference."""

    millisecond: Optional[int] = None
    """The millisecond component of the year reference."""

    minute: Optional[int] = None
    """The minute component of the year reference."""

    second: Optional[int] = None
    """The second component of the year reference."""
