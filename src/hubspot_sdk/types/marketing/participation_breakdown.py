# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .participation_properties import ParticipationProperties
from .participation_associations import ParticipationAssociations

__all__ = ["ParticipationBreakdown"]


class ParticipationBreakdown(BaseModel):
    id: str
    """The internal ID of the target marketing event"""

    associations: ParticipationAssociations

    created_at: datetime = FieldInfo(alias="createdAt")
    """The creation time and date of the target marketing event"""

    properties: ParticipationProperties
