# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalGuestSettings"]


class ExternalGuestSettings(BaseModel):
    can_add_guests: bool = FieldInfo(alias="canAddGuests")
    """Indicates whether guests can be added to the meeting."""

    max_guest_count: int = FieldInfo(alias="maxGuestCount")
    """The maximum number of guests that can be added to the meeting."""
