# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .hydrated_critical_action import HydratedCriticalAction

__all__ = ["CollectionResponseHydratedCriticalActionForwardPaging"]


class CollectionResponseHydratedCriticalActionForwardPaging(BaseModel):
    results: List[HydratedCriticalAction]

    paging: Optional[ForwardPaging] = None
