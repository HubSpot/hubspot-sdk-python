# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicQuarterReference"]


class PublicQuarterReference(BaseModel):
    day: int
    """The day component of the quarter reference."""

    month: int
    """The month component of the quarter reference."""

    reference_type: Literal["QUARTER"] = FieldInfo(alias="referenceType")
    """Indicates the type of reference (QUARTER)."""

    hour: Optional[int] = None
    """The hour component of the quarter reference."""

    millisecond: Optional[int] = None
    """The millisecond component of the quarter reference."""

    minute: Optional[int] = None
    """The minute component of the quarter reference."""

    second: Optional[int] = None
    """The second component of the quarter reference."""
