# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .participation_breakdown import ParticipationBreakdown

__all__ = ["CollectionResponseWithTotalParticipationBreakdownForwardPaging"]


class CollectionResponseWithTotalParticipationBreakdownForwardPaging(BaseModel):
    results: List[ParticipationBreakdown]

    total: int

    paging: Optional[ForwardPaging] = None
