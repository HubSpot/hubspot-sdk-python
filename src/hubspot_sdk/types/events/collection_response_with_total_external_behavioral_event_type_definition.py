# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging

__all__ = ["CollectionResponseWithTotalExternalBehavioralEventTypeDefinition"]


class CollectionResponseWithTotalExternalBehavioralEventTypeDefinition(BaseModel):
    results: List["ExternalBehavioralEventTypeDefinition"]

    total: int

    paging: Optional[Paging] = None


from .external_behavioral_event_type_definition import ExternalBehavioralEventTypeDefinition
