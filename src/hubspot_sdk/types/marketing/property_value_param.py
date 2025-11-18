# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PropertyValueParam"]


class PropertyValueParam(TypedDict, total=False):
    data_sensitivity: Required[Annotated[Literal["none", "standard", "high"], PropertyInfo(alias="dataSensitivity")]]
    """
    The sensitivity level of the property, such as "non_sensitive", "sensitive", and
    "highly_sensitive".
    """

    is_encrypted: Required[Annotated[bool, PropertyInfo(alias="isEncrypted")]]
    """Whether the property value is encrypted."""

    is_large_value: Required[Annotated[bool, PropertyInfo(alias="isLargeValue")]]

    name: Required[str]
    """Name of custom property"""

    persistence_timestamp: Required[Annotated[int, PropertyInfo(alias="persistenceTimestamp")]]

    request_id: Required[Annotated[str, PropertyInfo(alias="requestId")]]
    """A unique ID associated with this request."""

    selected_by_user: Required[Annotated[bool, PropertyInfo(alias="selectedByUser")]]
    """Whether the value was selected by a user."""

    selected_by_user_timestamp: Required[Annotated[int, PropertyInfo(alias="selectedByUserTimestamp")]]
    """The timestamp when the value was selected by a user, if applicable."""

    source: Required[
        Literal[
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
        ]
    ]
    """The origin of the property value, such as "IMPORT" or "API"."""

    source_id: Required[Annotated[str, PropertyInfo(alias="sourceId")]]
    """The ID of the property source indicating where it was created."""

    source_label: Required[Annotated[str, PropertyInfo(alias="sourceLabel")]]
    """A human-readable label."""

    source_metadata: Required[Annotated[str, PropertyInfo(alias="sourceMetadata")]]
    """Source metadata encoded as a base64 string. For example: `ZXhhbXBsZSBzdHJpbmc=`"""

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

    value: Required[str]
    """Custom property value"""
