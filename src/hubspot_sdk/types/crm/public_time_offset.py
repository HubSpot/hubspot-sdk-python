# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTimeOffset"]


class PublicTimeOffset(BaseModel):
    amount: int
    """The numerical value representing the quantity of the time offset."""

    offset_direction: str = FieldInfo(alias="offsetDirection")
    """Indicates the direction of the time offset, such as forward or backward."""

    time_unit: str = FieldInfo(alias="timeUnit")
    """Specifies the unit of time for the offset, such as days, hours, or minutes."""
