# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicNowReference"]


class PublicNowReference(BaseModel):
    reference_type: Literal["NOW"] = FieldInfo(alias="referenceType")
    """Indicates the type of reference (NOW)."""

    hour: Optional[int] = None
    """The hour component of the current time reference."""

    millisecond: Optional[int] = None
    """The millisecond component of the current time reference."""

    minute: Optional[int] = None
    """The minute component of the current time reference."""

    second: Optional[int] = None
    """The second component of the current time reference."""
