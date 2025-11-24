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
        "CALCULATED",
        "CENTRAL_EXCHANGE_RATES",
        "CHATSPOT",
        "CLONE_OBJECTS",
        "COMMUNICATOR",
        "COMPANIES",
        "COMPANY_FAMILIES",
        "COMPANY_INSIGHTS",
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
        "DATASET",
        "DEALS",
        "DEFAULT",
        "DELETE_OBJECTS",
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
        "MEETINGS",
        "MERGE_COMPANIES",
        "MERGE_CONTACTS",
        "MERGE_OBJECTS",
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
        "PROPERTY_RESTORE",
        "PROPERTY_SETTINGS",
        "PROSPECTING_AGENT",
        "QUOTAS",
        "QUOTES",
        "RECYCLING_BIN",
        "RESTORE_OBJECTS",
        "SALES",
        "SALES_MESSAGES",
        "SALESFORCE",
        "SEQUENCES",
        "SETTINGS",
        "SIDEKICK",
        "SIGNALS",
        "SLACK_INTEGRATION",
        "SOCIAL",
        "SUCCESS",
        "TALLY",
        "TASK",
        "UNKNOWN",
        "WAL_INCREMENTAL",
        "WORKFLOW_CONTACT_DELETE_ACTION",
        "WORKFLOWS",
    ]

    hs_engagement_source_id: str

    hs_meeting_end_time: datetime

    hs_meeting_outcome: str

    hs_meeting_start_time: datetime

    hs_meeting_title: str

    hs_timestamp: datetime

    hs_activity_type: Optional[str] = None

    hs_attachment_ids: Optional[List[str]] = None

    hs_attendee_owner_ids: Optional[List[str]] = None

    hs_include_description_in_reminder: Optional[str] = None

    hs_internal_meeting_notes: Optional[str] = None

    hs_meeting_body: Optional[str] = None

    hs_meeting_external_url: Optional[str] = None

    hs_meeting_location: Optional[str] = None

    hs_meeting_location_type: Optional[Literal["ADDRESS", "CUSTOM", "PHONE"]] = None

    hs_unique_id: Optional[str] = None

    hubspot_owner_id: Optional[str] = None
