# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_link_availability_for_duration import ExternalLinkAvailabilityForDuration

__all__ = ["ExternalLinkAvailability"]


class ExternalLinkAvailability(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more available meeting times beyond the returned set."""

    link_availability_by_duration: Dict[str, ExternalLinkAvailabilityForDuration] = FieldInfo(
        alias="linkAvailabilityByDuration"
    )
    """Available booking slots for the meeting, grouped by the duration."""
