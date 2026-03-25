# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTodayReference"]


class PublicTodayReference(BaseModel):
    reference_type: Literal["TODAY"] = FieldInfo(alias="referenceType")
    """Indicates the type of reference (TODAY)."""

    hour: Optional[int] = None
    """The hour component of the current day reference."""

    millisecond: Optional[int] = None
    """The millisecond component of the current day reference."""

    minute: Optional[int] = None
    """The minute component of the current day reference."""

    second: Optional[int] = None
    """The second component of the current day reference."""
