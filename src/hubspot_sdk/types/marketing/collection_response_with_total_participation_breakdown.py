# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .participation_breakdown import ParticipationBreakdown

__all__ = ["CollectionResponseWithTotalParticipationBreakdown"]


class CollectionResponseWithTotalParticipationBreakdown(BaseModel):
    results: List[ParticipationBreakdown]

    total: int

    paging: Optional[Paging] = None
