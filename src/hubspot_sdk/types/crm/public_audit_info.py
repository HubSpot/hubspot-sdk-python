# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAuditInfo"]


class PublicAuditInfo(BaseModel):
    action: str
    """The action performed that triggered the audit event."""

    identifier: str
    """A unique string identifier for the audit event."""

    portal_id: int = FieldInfo(alias="portalId")
    """The unique identifier for the HubSpot portal where the audit event occurred."""

    from_user_id: Optional[int] = FieldInfo(alias="fromUserId", default=None)
    """The ID of the user who initiated the audit event."""

    message: Optional[str] = None
    """A descriptive message related to the audit event."""

    raw_object: Optional[object] = FieldInfo(alias="rawObject", default=None)
    """An object containing the raw data associated with the audit event."""

    timestamp: Optional[datetime] = None
    """The date and time when the audit event took place."""
