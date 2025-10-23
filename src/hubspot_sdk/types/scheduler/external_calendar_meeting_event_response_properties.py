# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExternalCalendarMeetingEventResponseProperties"]


class ExternalCalendarMeetingEventResponseProperties(BaseModel):
    hs_engagement_source: Literal[
        "UNKNOWN",
        "IMPORT",
        "API",
        "FORM",
        "ANALYTICS",
        "MIGRATION",
        "SALESFORCE",
        "INTEGRATION",
        "CONTACTS_WEB",
        "WAL_INCREMENTAL",
        "TASK",
        "EMAIL",
        "WORKFLOWS",
        "CALCULATED",
        "SOCIAL",
        "BATCH_UPDATE",
        "SIGNALS",
        "BIDEN",
        "DEFAULT",
        "COMPANIES",
        "DEALS",
        "ASSISTS",
        "PRESENTATIONS",
        "TALLY",
        "SIDEKICK",
        "CRM_UI",
        "MERGE_CONTACTS",
        "PORTAL_USER_ASSOCIATOR",
        "INTEGRATIONS_PLATFORM",
        "BCC_TO_CRM",
        "FORWARD_TO_CRM",
        "ENGAGEMENTS",
        "SALES",
        "HEISENBERG",
        "LEADIN",
        "GMAIL_INTEGRATION",
        "ACADEMY",
        "SALES_MESSAGES",
        "AVATARS_SERVICE",
        "MERGE_COMPANIES",
        "SEQUENCES",
        "COMPANY_FAMILIES",
        "MOBILE_IOS",
        "MOBILE_ANDROID",
        "CONTACTS",
        "ASSOCIATIONS",
        "EXTENSION",
        "SUCCESS",
        "BOT",
        "INTEGRATIONS_SYNC",
        "AUTOMATION_PLATFORM",
        "CONVERSATIONS",
        "EMAIL_INTEGRATION",
        "CONTENT_MEMBERSHIP",
        "QUOTES",
        "BET_ASSIGNMENT",
        "QUOTAS",
        "BET_CRM_CONNECTOR",
        "MEETINGS",
        "MERGE_OBJECTS",
        "RECYCLING_BIN",
        "ADS",
        "AI_GROUP",
        "COMMUNICATOR",
        "SETTINGS",
        "PROPERTY_SETTINGS",
        "PIPELINE_SETTINGS",
        "COMPANY_INSIGHTS",
        "BEHAVIORAL_EVENTS",
        "PAYMENTS",
        "GOALS",
        "PORTAL_OBJECT_SYNC",
        "APPROVALS",
        "FILE_MANAGER",
        "MARKETPLACE",
        "INTERNAL_PROCESSING",
        "FORECASTING",
        "SLACK_INTEGRATION",
        "CRM_UI_BULK_ACTION",
        "WORKFLOW_CONTACT_DELETE_ACTION",
        "ACCEPTANCE_TEST",
        "PLAYBOOKS",
        "CHATSPOT",
        "FLYWHEEL_PRODUCT_DATA_SYNC",
        "HELP_DESK",
        "BILLING",
        "DATA_ENRICHMENT",
        "AUTOMATION_JOURNEY",
        "MICROAPPS",
        "INTENT",
        "PROSPECTING_AGENT",
        "CENTRAL_EXCHANGE_RATES",
        "HELP_DESK_AI",
        "CONVERSATIONAL_ENRICHMENT",
        "CRM_PROCESSES_PLATFORM",
        "CLONE_OBJECTS",
        "MARKET_SOURCING",
        "DATASET",
        "PROPERTY_RESTORE",
        "EMAIL_INBOX_IMPORT",
        "CUSTOMER_AGENT",
        "LEGAL_BASIS_REMEDIATION",
        "AUTO_ASSOCIATE_BY_DOMAIN",
        "ACTIVITY_AUTO_ASSOCIATE",
        "PRIMARY_AUTOMATION",
        "DELETE_OBJECTS",
        "RESTORE_OBJECTS",
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

    hs_meeting_location_type: Optional[Literal["PHONE", "ADDRESS", "CUSTOM"]] = None

    hs_unique_id: Optional[str] = None

    hubspot_owner_id: Optional[str] = None
