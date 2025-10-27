# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .event_id_view import EventIDView

__all__ = ["EmailSendStatusView"]


class EmailSendStatusView(BaseModel):
    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """Status of the send request."""

    status_id: str = FieldInfo(alias="statusId")
    """Identifier used to query the status of the send."""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Time when the send was completed."""

    event_id: Optional[EventIDView] = FieldInfo(alias="eventId", default=None)
    """The ID of a send event."""

    message: Optional[str] = None

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Time when the send was requested."""

    send_result: Optional[
        Literal[
            "SENT",
            "IDEMPOTENT_IGNORE",
            "QUEUED",
            "IDEMPOTENT_FAIL",
            "THROTTLED",
            "EMAIL_DISABLED",
            "PORTAL_SUSPENDED",
            "INVALID_TO_ADDRESS",
            "BLOCKED_DOMAIN",
            "PREVIOUSLY_BOUNCED",
            "EMAIL_UNCONFIRMED",
            "PREVIOUS_SPAM",
            "PREVIOUSLY_UNSUBSCRIBED_MESSAGE",
            "PREVIOUSLY_UNSUBSCRIBED_PORTAL",
            "INVALID_FROM_ADDRESS",
            "CAMPAIGN_CANCELLED",
            "VALIDATION_FAILED",
            "MTA_IGNORE",
            "BLOCKED_ADDRESS",
            "PORTAL_OVER_LIMIT",
            "PORTAL_EXPIRED",
            "PORTAL_MISSING_MARKETING_SCOPE",
            "MISSING_TEMPLATE_PROPERTIES",
            "MISSING_REQUIRED_PARAMETER",
            "PORTAL_AUTHENTICATION_FAILURE",
            "MISSING_CONTENT",
            "CORRUPT_INPUT",
            "TEMPLATE_RENDER_EXCEPTION",
            "GRAYMAIL_SUPPRESSED",
            "UNCONFIGURED_SENDING_DOMAIN",
            "UNDELIVERABLE",
            "CANCELLED_ABUSE",
            "QUARANTINED_ADDRESS",
            "ADDRESS_ONLY_ACCEPTED_ON_PROD",
            "PORTAL_NOT_AUTHORIZED_FOR_APPLICATION",
            "ADDRESS_LIST_BOMBED",
            "ADDRESS_OPTED_OUT",
            "RECIPIENT_FATIGUE_SUPPRESSED",
            "TOO_MANY_RECIPIENTS",
            "PREVIOUSLY_UNSUBSCRIBED_BRAND",
            "NON_MARKETABLE_CONTACT",
            "PREVIOUSLY_UNSUBSCRIBED_BUSINESS_UNIT",
            "GDPR_DOI_ENABLED",
            "HUBL_LIMIT_EXCEEDED",
            "LOW_CONTACT_QUALITY_SCORE",
        ]
    ] = FieldInfo(alias="sendResult", default=None)
    """Result of the send."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """Time when the send began processing."""
