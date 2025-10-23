# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .card_actions import CardActions
from .card_display_body import CardDisplayBody
from .card_audit_response import CardAuditResponse
from .public_card_fetch_body import PublicCardFetchBody

__all__ = ["PublicCardResponse"]


class PublicCardResponse(BaseModel):
    id: str

    actions: CardActions
    """Configuration for custom user actions on cards."""

    audit_history: List[CardAuditResponse] = FieldInfo(alias="auditHistory")

    display: CardDisplayBody
    """Configuration for displayed info on a card"""

    fetch: PublicCardFetchBody

    title: str

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
