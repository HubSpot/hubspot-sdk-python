# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExternalCalendarMeetingEventResponseProperties"]


class ExternalCalendarMeetingEventResponseProperties(BaseModel):
    hs_engagement_source: Literal[
        "ACADEMY",
        "ACCEPTANCE_TEST",
        "ACTIVITY_AUTO_ASSOCIATE",
        "ACTIVITY_LOG_REVERT",
        "ADS",
        "AI_GROUP",
        "ANALYTICS",
        "API",
        "APPROVALS",
        "ASSISTS",
        "ASSOCIATIONS",
        "AUTO_ASSOCIATE_BY_DOMAIN",
        "AUTOMATION_JOURNEY",
        "AUTOMATION_PLATFORM",
        "AVATARS_SERVICE",
        "BATCH_UPDATE",
        "BCC_TO_CRM",
        "BEHAVIORAL_EVENTS",
        "BET_ASSIGNMENT",
        "BET_CRM_CONNECTOR",
        "BIDEN",
        "BILLING",
        "BOT",
        "BREEZE_AGENT",
        "CALCULATED",
        "CENTRAL_EXCHANGE_RATES",
        "CHATSPOT",
        "CLONE_OBJECTS",
        "COMMUNICATOR",
        "COMPANIES",
        "COMPANY_FAMILIES",
        "COMPANY_INSIGHTS",
        "CONNECTED_ACCOUNT",
        "CONTACTS",
        "CONTACTS_WEB",
        "CONTENT_MEMBERSHIP",
        "CONVERSATIONAL_ENRICHMENT",
        "CONVERSATIONS",
        "CRM_PROCESSES_PLATFORM",
        "CRM_UI",
        "CRM_UI_BULK_ACTION",
        "CUSTOMER_AGENT",
        "DATA_ENRICHMENT",
        "DATA_QUALITY",
        "DATASET",
        "DEALS",
        "DEFAULT",
        "DELETE_OBJECTS",
        "DI_WRITE_TO_CRM",
        "EMAIL",
        "EMAIL_INBOX_IMPORT",
        "EMAIL_INTEGRATION",
        "ENGAGEMENTS",
        "EXTENSION",
        "FILE_MANAGER",
        "FLYWHEEL_PRODUCT_DATA_SYNC",
        "FORECASTING",
        "FORM",
        "FORWARD_TO_CRM",
        "GMAIL_INTEGRATION",
        "GOALS",
        "HEISENBERG",
        "HELP_DESK",
        "HELP_DESK_AI",
        "IMPORT",
        "INTEGRATION",
        "INTEGRATIONS_PLATFORM",
        "INTEGRATIONS_SYNC",
        "INTENT",
        "INTERNAL_PROCESSING",
        "LEADIN",
        "LEGAL_BASIS_REMEDIATION",
        "MARKET_SOURCING",
        "MARKETPLACE",
        "MARKETS",
        "MEETINGS",
        "MERGE_COMPANIES",
        "MERGE_CONTACTS",
        "MERGE_OBJECTS",
        "MERGE_REVERT_OBJECTS",
        "MICROAPPS",
        "MIGRATION",
        "MOBILE_ANDROID",
        "MOBILE_IOS",
        "PAYMENTS",
        "PIPELINE_SETTINGS",
        "PLAYBOOKS",
        "PORTAL_OBJECT_SYNC",
        "PORTAL_USER_ASSOCIATOR",
        "PRESENTATIONS",
        "PRIMARY_AUTOMATION",
        "PROPERTY_DEFAULT_VALUE",
        "PROPERTY_RESTORE",
        "PROPERTY_SETTINGS",
        "PROSPECTING_AGENT",
        "QUOTAS",
        "QUOTES",
        "RECYCLING_BIN",
        "RESTORE_OBJECTS",
        "REVENUE_PLATFORM",
        "SALES",
        "SALES_MESSAGES",
        "SALESFORCE",
        "SEQUENCES",
        "SETTINGS",
        "SIDEKICK",
        "SIGNALS",
        "SLACK_INTEGRATION",
        "SMART_DATA_CAPTURE",
        "SOCIAL",
        "SUCCESS",
        "TALLY",
        "TASK",
        "UNKNOWN",
        "WAL_INCREMENTAL",
        "WORK_UI",
        "WORKFLOW_CONTACT_DELETE_ACTION",
        "WORKFLOWS",
    ]
    """The source of the engagement, will always be `MEETINGS`."""

    hs_engagement_source_id: str
    """The ID associated with the process created the engagement.

    Should always be empty when creating meeting events through this API.
    """

    hs_meeting_end_time: datetime
    """The end time of the meeting in ISO 8601 format."""

    hs_meeting_outcome: str
    """The outcome of the meeting.

    Acceptable default values are: SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW,
    CANCELED. This property can be changed to include additional custom values.
    """

    hs_meeting_start_time: datetime
    """The start time of the meeting in ISO 8601 format."""

    hs_meeting_title: str
    """The title of the meeting and calendar event."""

    hs_timestamp: datetime
    """The time that the meeting should start in ISO 8601 format.

    This value should be the same as `hs_meeting_start_time`.
    """

    hs_activity_type: Optional[str] = None
    """The activity type of the meeting.

    Acceptable values are based on portal defined call and meeting types.
    """

    hs_attachment_ids: Optional[List[str]] = None

    hs_attendee_owner_ids: Optional[List[str]] = None

    hs_include_description_in_reminder: Optional[str] = None
    """Whether to include the meeting description in the reminder."""

    hs_internal_meeting_notes: Optional[str] = None
    """Internal notes related to the meeting."""

    hs_meeting_body: Optional[str] = None
    """The description of the meeting and calendar event."""

    hs_meeting_external_url: Optional[str] = None
    """The calendar event URL for the meeting."""

    hs_meeting_location: Optional[str] = None
    """
    The physical address, virtual location, or phone number where the meeting will
    take place.
    """

    hs_meeting_location_type: Optional[Literal["ADDRESS", "CUSTOM", "PHONE"]] = None
    """The type of location for the meeting.

    Acceptable values are: ADDRESS, CUSTOM, PHONE.
    """

    hs_unique_id: Optional[str] = None
    """The unique ID of the created calendar event."""

    hubspot_owner_id: Optional[str] = None
    """The owner ID of the HubSpot user hosting the meeting."""
