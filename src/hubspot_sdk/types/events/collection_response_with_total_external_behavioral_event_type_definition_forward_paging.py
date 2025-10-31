# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalExternalBehavioralEventTypeDefinitionForwardPaging"]


class CollectionResponseWithTotalExternalBehavioralEventTypeDefinitionForwardPaging(BaseModel):
    results: List["ExternalBehavioralEventTypeDefinition"]

    total: int

    paging: Optional[ForwardPaging] = None


from .external_behavioral_event_type_definition import ExternalBehavioralEventTypeDefinition
