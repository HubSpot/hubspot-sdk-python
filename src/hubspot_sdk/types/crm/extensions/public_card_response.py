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
    """The unique id of the card."""

    actions: CardActions

    audit_history: List[CardAuditResponse] = FieldInfo(alias="auditHistory")
    """
    A list of actions performed on the card, including creation, deletion, and
    updates.
    """

    display: CardDisplayBody

    fetch: PublicCardFetchBody

    title: str
    """The top-level title for this card, displayed to users in the CRM UI."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time when the card was created."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time when the card was last updated."""
