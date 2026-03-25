# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicMonthReference"]


class PublicMonthReference(BaseModel):
    day: int
    """The day component of the month reference."""

    reference_type: Literal["MONTH"] = FieldInfo(alias="referenceType")
    """Indicates the type of reference, (MONTH)."""

    hour: Optional[int] = None
    """The hour component of the month reference."""

    millisecond: Optional[int] = None
    """The millisecond component of the month reference."""

    minute: Optional[int] = None
    """The minute component of the month reference."""

    second: Optional[int] = None
    """The second component of the month reference."""
