# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..marketing.paging import Paging
from .external_unified_event import ExternalUnifiedEvent

__all__ = ["CollectionResponseExternalUnifiedEvent"]


class CollectionResponseExternalUnifiedEvent(BaseModel):
    results: List[ExternalUnifiedEvent]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
