# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .external_unified_event import ExternalUnifiedEvent
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponseExternalUnifiedEvent"]


class CollectionResponseExternalUnifiedEvent(BaseModel):
    results: List[ExternalUnifiedEvent]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
