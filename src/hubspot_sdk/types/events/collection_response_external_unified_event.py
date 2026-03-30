# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .external_unified_event import ExternalUnifiedEvent

__all__ = ["CollectionResponseExternalUnifiedEvent"]


class CollectionResponseExternalUnifiedEvent(BaseModel):
    results: List[ExternalUnifiedEvent]
    """
    An array of ExternalUnifiedEvent objects, each representing an individual event
    with its associated details.
    """

    paging: Optional[Paging] = None
