# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PropertyValue"]


class PropertyValue(TypedDict, total=False):
    """
    Represents a single custom property of a marketing event, storing its name, value, metadata (like source, timestamp, and sensitivity), and related audit information for tracking changes.
    """

    data_sensitivity: Required[Annotated[Literal["high", "none", "standard"], PropertyInfo(alias="dataSensitivity")]]
    """
    The sensitivity level of the property, such as "non_sensitive", "sensitive", and
    "highly_sensitive".
    """

    is_encrypted: Required[Annotated[bool, PropertyInfo(alias="isEncrypted")]]
    """Whether the property value is encrypted."""

    is_large_value: Required[Annotated[bool, PropertyInfo(alias="isLargeValue")]]
    """Indicates if the value exceeds normal size limits."""

    name: Required[str]
    """The unique property name."""

    persistence_timestamp: Required[Annotated[int, PropertyInfo(alias="persistenceTimestamp")]]
    """When the value was persisted to database, in epoch milliseconds."""

    request_id: Required[Annotated[str, PropertyInfo(alias="requestId")]]
    """A unique ID associated with this request."""

    selected_by_user: Required[Annotated[bool, PropertyInfo(alias="selectedByUser")]]
    """Whether the value was selected by a user."""

    selected_by_user_timestamp: Required[Annotated[int, PropertyInfo(alias="selectedByUserTimestamp")]]
    """The timestamp when the value was selected by a user, if applicable."""

    source: Required[
        Literal[
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
    ]
    """The origin of the property value, such as "IMPORT" or "API"."""

    source_id: Required[Annotated[str, PropertyInfo(alias="sourceId")]]
    """The ID of the property source indicating where it was created."""

    source_label: Required[Annotated[str, PropertyInfo(alias="sourceLabel")]]
    """A human-readable label."""

    source_metadata: Required[Annotated[str, PropertyInfo(alias="sourceMetadata")]]
    """Metadata providing additional context about the source."""

    source_upstream_deployable: Required[Annotated[str, PropertyInfo(alias="sourceUpstreamDeployable")]]

    source_vid: Required[Annotated[Iterable[int], PropertyInfo(alias="sourceVid")]]
    """The unique identifier associated with the source."""

    timestamp: Required[int]
    """When the value was set, as a 64-bit integer."""

    unit: Required[str]
    """The unit of measurement or context for the value."""

    updated_by_user_id: Required[Annotated[int, PropertyInfo(alias="updatedByUserId")]]
    """The ID of the user who updated the property."""

    use_timestamp_as_persistence_timestamp: Required[
        Annotated[bool, PropertyInfo(alias="useTimestampAsPersistenceTimestamp")]
    ]
    """
    Flag indicating whether to use the timestamp field as the persistence timestamp.
    """

    value: Required[str]
    """The property value."""
