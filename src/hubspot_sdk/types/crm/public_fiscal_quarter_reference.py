# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicFiscalQuarterReference"]


class PublicFiscalQuarterReference(BaseModel):
    day: int
    """The day component of the fiscal quarter reference."""

    month: int
    """The month component of the fiscal quarter reference."""

    reference_type: Literal["FISCAL_QUARTER"] = FieldInfo(alias="referenceType")
    """Indicates the type of reference (FISCAL_QUARTER)."""

    hour: Optional[int] = None
    """The hour component of the fiscal quarter reference."""

    millisecond: Optional[int] = None
    """The millisecond component of the fiscal quarter reference."""

    minute: Optional[int] = None
    """The minute component of the fiscal quarter reference."""

    second: Optional[int] = None
    """The second component of the fiscal quarter reference."""
