# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .event_id_view import EventIDView

__all__ = ["EmailSendStatusView"]


class EmailSendStatusView(BaseModel):
    """Describes the status of an email send request."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
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
            "ADDRESS_LIST_BOMBED",
            "ADDRESS_ONLY_ACCEPTED_ON_PROD",
            "ADDRESS_OPTED_OUT",
            "BLOCKED_ADDRESS",
            "BLOCKED_DOMAIN",
            "CAMPAIGN_CANCELLED",
            "CANCELLED_ABUSE",
            "CORRUPT_INPUT",
            "EMAIL_DISABLED",
            "EMAIL_UNCONFIRMED",
            "GDPR_DOI_ENABLED",
            "GRAYMAIL_SUPPRESSED",
            "HUBL_LIMIT_EXCEEDED",
            "IDEMPOTENT_FAIL",
            "IDEMPOTENT_IGNORE",
            "INVALID_FROM_ADDRESS",
            "INVALID_TO_ADDRESS",
            "LOW_CONTACT_QUALITY_SCORE",
            "MISSING_CONTENT",
            "MISSING_REQUIRED_PARAMETER",
            "MISSING_TEMPLATE_PROPERTIES",
            "MTA_IGNORE",
            "NON_MARKETABLE_CONTACT",
            "PORTAL_AUTHENTICATION_FAILURE",
            "PORTAL_EXPIRED",
            "PORTAL_MISSING_MARKETING_SCOPE",
            "PORTAL_NOT_AUTHORIZED_FOR_APPLICATION",
            "PORTAL_OVER_LIMIT",
            "PORTAL_SUSPENDED",
            "PREVIOUS_SPAM",
            "PREVIOUSLY_BOUNCED",
            "PREVIOUSLY_UNSUBSCRIBED_BRAND",
            "PREVIOUSLY_UNSUBSCRIBED_BUSINESS_UNIT",
            "PREVIOUSLY_UNSUBSCRIBED_MESSAGE",
            "PREVIOUSLY_UNSUBSCRIBED_PORTAL",
            "QUARANTINED_ADDRESS",
            "QUEUED",
            "RECIPIENT_FATIGUE_SUPPRESSED",
            "SENT",
            "TEMPLATE_RENDER_EXCEPTION",
            "THROTTLED",
            "TOO_MANY_RECIPIENTS",
            "UNCONFIGURED_SENDING_DOMAIN",
            "UNDELIVERABLE",
            "VALIDATION_FAILED",
        ]
    ] = FieldInfo(alias="sendResult", default=None)
    """Result of the send."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """Time when the send began processing."""
